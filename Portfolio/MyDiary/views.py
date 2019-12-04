from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from datetime import datetime
import requests
import json
import pandas as pd
import json
from .models import Business, Review
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

def myAccount(request):
    context = {
        "Name": request.user.first_name + " " + request.user.last_name,
        "Email": request.user.email,
        "Username": request.user.username,
        "Actions": request.user.my_reviews.all(),
    }

    return render(request, "MyDiary/myAccount.html", context)

def sign_up(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        firstName = request.POST["firstName"]
        lastName = request.POST["lastName"]
        user = User.objects.create_user(username, email, password)
        if user is not None:
            user.first_name = firstName
            user.last_name = lastName
            user.save()
            return render(request, "MyDiary/index.html")
        else:
            return render(request, "MyDiary/sign_up.html", {"message": "Invalid input"})
    else:
        return render(request, "MyDiary/sign_up.html", {"message": "Wrong Method"})

def logIn(request):

    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse(index))
        else:
            return render(request, "MyDiary/log_in.html")
    else:
        return render(request, "MyDiary/log_in.html")

def logOut(request):
    logout(request)
    return render(request, "MyDiary/log_in.html", {"message": "Logged out."})


#function to load lattitude and longitude given the name of University
def loadLL(uni):
    df = pd.read_csv("C:/Users/adhik/Downloads/Colleges/final.csv")
    df = df.rename(columns={df.columns[0]: "Institute", df.columns[1]: "latlong"})
    a = dict(zip(df.Institute,df.latlong))
    return a[uni]
# Create your views here.

#function to load list of businesses given the name of university and business type.
def loadApi(university, busiType):
    latlong = loadLL(university);
    #response = requests.get('http://data.fixer.io/api/latest?access_key=0da6ffdfe0a66761abc9bc747582a199')
    #response = requests.get('https://dev.virtualearth.net/REST/v1/LocalSearch/?type=MovieTheaters,KoreanRestaurants&userCircularMapView=44.1636,-93.9994,300&key=AqknOo4_TMZT44ZDjJefyPmkPPTuyLYyg7Gmw9dSBE1RqRMbBl_C0vbxqScnqF7g')
    url = 'https://api.foursquare.com/v2/venues/explore'
    params = dict(
          client_id='GEKN1JRDSVHRCHGQOFAWFAL0JIH43WRT4WNOL1HD4R31I3S4',
          client_secret='C5GQCRI0J2B4GM12Y3QEDRYGDFGKYN2MNQKJLDKG0MMUEUHD',
          v='20180323',
          ll=latlong,
          query=busiType,
          limit=13
    )

    response = requests.get(url=url, params=params)
    #data = json.loads(response.text)

    data = response.json()
    filtered = data['response']['groups'][0]['items']
    businesses = []
    leng = len(filtered)
    for i in range(leng):
        businesses.append(filtered[i]['venue'])

    return businesses

#routing starts from here

def index(request):
    return render(request, 'MyDiary/index.html')

def business(request):
    if request.method == 'POST':
        inst = request.POST["university"]
        type = request.POST["business_type"]
        result = loadApi(inst, type)
        context = {
            "businesses": result,
        }
        return render(request, 'MyDiary/business.html', context)
    else:
        return render(request, 'MyDiary/business.html', {"message": 'Invalid Input'})

def checkBusiness(request):
    business = request.POST["business_obj"]
    #business = business[2:-2]
    business = eval(business)
    id = business['id']
    print("Business: ")
    # {'id': '5862861c24ca6a618f3a6bf0', 'name': 'Daylight Donuts', 'contact': {}, 'location': {'address': '110 Allison Bonnett Memorial Drive', 'lat': 33
    # .452779, 'lng': -86.971295, 'labeledLatLngs': [{'label': 'display', 'lat': 33.452779, 'lng': -86.971295}], 'distance': 6631, 'postalCode': '35023',
    # 'cc': 'US', 'city': 'Hueytown', 'state': 'AL', 'country': 'United States', 'formattedAddress': ['110 Allison Bonnett Memorial Drive', 'Hueytown, AL
    # 35023', 'United States']}, 'categories': [{'id': '4bf58dd8d48988d148941735', 'name': 'Donut Shop', 'pluralName': 'Donut Shops', 'shortName': 'Donuts
    # ', 'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/food/donuts_', 'suffix': '.png'}, 'primary': True}], 'verified': False, 'stats': {'tip
    # Count': 0, 'usersCount': 0, 'checkinsCount': 0, 'visitsCount': 0}, 'beenHere': {'count': 0, 'lastCheckinExpiredAt': 0, 'marked': False, 'unconfirmed
    # Count': 0}, 'photos': {'count': 0, 'groups': []}, 'hereNow': {'count': 0, 'summary': 'Nobody here', 'groups': []}}
    t_name=business['name']
    t_street_address=business['location']['address']
    print(t_name+" with address "+t_street_address)
    t_city=business['location']['city']
    t_state=business['location']['state']
    t_country=business['location']['country']
    t_category=business['categories'][0]['name']
    t_checkId=business['id']
    try:
        result = Business.objects.get(checkId=business['id'])

    except Business.DoesNotExist:
        b = Business(name=t_name, street_address=t_street_address, city=t_city, state=t_state, country=t_country, category=t_category, checkId=t_checkId)
        b.save()
        result = Business.objects.get(checkId=t_checkId)

    all_comments = result.list_reviews.all()
    context = {
        'business': result,
        'reviews': all_comments,
    }

    return render(request, "MyDiary/checkBusiness.html", context)

@login_required(login_url='logIn')
def postComment(request, business_id):
    review = request.POST.get("comment")
    user = request.user;
    try:
        business = Business.objects.get(checkId=business_id)
        info = Review(description=review, reviewer=user, business=business)
        info.save()
    except:
        return render(request, "MyDiary/Error.html", {"message": "Page Not Found"})

    context = {
        'business': business,
        'reviews': business.list_reviews.all(),
    }

    #return render(request, "MyDiary/Success.html", {"message": "Thank you for the submission"})
    return render(request, "MyDiary/checkBusiness.html", {"business": business, "reviews": business.list_reviews.all()})
