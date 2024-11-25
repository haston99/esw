from django.contrib import admin
from django.urls import path,include 
from esw import views as landing_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_views.landing_page, name='landing_page'),
]

