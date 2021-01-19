from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.UserView.as_view({'post': 'registration'})),
    path('login/', views.UserView.as_view({'post': 'login'})),

]