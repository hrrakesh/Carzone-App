from django.urls import include, path
from . import views



urlpatterns = [
    
    path('inquiry', views.inquiry, name='inquiry'),
    path('other_inquiry', views.other_inquiry, name='other_inquiry'),

]