"""task1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user.views import signin,doctorsignup,home,patientsignup,signout,upload,blog,filter,myblog,myfilter,viewblog,bookappointment, confirmbooking,bookedappointment
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('home/',home),
    path('signin/',signin),
    path('signup/doctor',doctorsignup),
    path('signup/patient',patientsignup),
    path('signout/',signout),
    path('blog/upload/',upload),
    path('blog/',blog),
    path('blog/filter/<str:fl>',filter),
    path('blog/myblog/',myblog),
    path('blog/myblog/filter/<str:fl>',myfilter),
    path('blog/viewblog/<int:bno>',viewblog),
    path('bookappointment/',bookappointment),
    path('bookappointment/<str:doctor>/',confirmbooking),
    path('bookedappointment/',bookedappointment),
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
