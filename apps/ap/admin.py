from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Questions)

admin.site.register(Category)

admin.site.register(Services)

admin.site.register(AboutUs)

admin.site.register(Team)

admin.site.register(Information)

admin.site.register(Contacts)

