from django.contrib import admin
from .models import Finch,FeedingFinch, Toy

# Register your models here.
admin.site.register(Finch)
admin.site.register(FeedingFinch)
admin.site.register(Toy)