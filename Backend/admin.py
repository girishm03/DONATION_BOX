from django.contrib import admin
from Backend.models import CategoryDB, WebsiteDB, PersonDB

# Register your models here.

admin.site.register(CategoryDB)
admin.site.register(WebsiteDB)
admin.site.register(PersonDB)
