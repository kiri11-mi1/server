from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.UserView.as_view({'post': 'registration'})),
    path('login/', views.UserView.as_view({'post': 'login'})),
    path('delete/', views.UserView.as_view({'delete': 'delete'})),
    path('book/', views.BookView.as_view({
                'post': 'add',
                'get': 'get',
                'put': 'update',
                'delete': 'delete',
    })),

]