from django.contrib import admin

# Register your models here.
from hello.models import Applicant
from hello.models import Requests

admin.site.register(Applicant)
admin.site.register(Requests)
