from django.db import models
from django.conf import settings

# Create your models here.
class Business(models.Model):
    name = models.CharField(max_length = 200)
    street_address = models.CharField(max_length = 100)
    city = models.CharField(max_length = 50)
    state = models.CharField(max_length = 2)
    country = models.CharField(max_length = 50)
    category = models.CharField(max_length = 30)
    lat = models.FloatField()
    lon = models.FloatField()
    checkId = models.CharField(max_length = 500)

    def __str__(self):
        return f"Name: {self.name} \n Address: {self.street_address}, {self.city}, {self.state}, {self.country} \n Category: {self.category}"

class Review(models.Model):
    #rate = models.IntegerField()
    description = models.CharField(max_length = 1000)
    reviewer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="my_reviews")
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name="list_reviews")


    def __str__(self):
        return f"{self.description} => {self.reviewer.first_name}/5"
