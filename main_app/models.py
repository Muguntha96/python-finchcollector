from django.db import models
from django.urls import reverse

# Create your models here.
class Finch(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()

MEALS = (
  ('B','Breakfast'),
  ('L','Lunch'),
  ('D','Dinner'),
  ('S','Snack')
)
class Feeding(models.Model):
  date_and_time = models.DateTimeField()
  meal = models.CharField(
    max_length=1,
    choices=MEALS,
    default=MEALS[0][0]
    )

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
      return reverse("finch-detail", kwargs={"finch_id": self.id})
  
  def __str__(self):
    return f'{self.get_meal_display()} on {self.date_and_time} ' 