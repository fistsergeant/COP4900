from django.urls import path
from . import views

app_name = "xl_calculation"

urlpatterns = [
    path('', views.index, name='index'),
    path('download', views.download, name='download'),
]
