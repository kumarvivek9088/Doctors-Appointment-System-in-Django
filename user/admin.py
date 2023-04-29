from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Doctor,Patient,User,Blog, Appointment
# Register your models here.
admin.site.register(Doctor)
admin.site.register(User,UserAdmin)
admin.site.register(Patient)
admin.site.register(Blog)
admin.site.register(Appointment)

