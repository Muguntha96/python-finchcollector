from django.forms import ModelForm
from .models import FeedingFinch

class FeedingForm(ModelForm):
  class Meta:
    model = FeedingFinch
    fields = ['date', 'meal']