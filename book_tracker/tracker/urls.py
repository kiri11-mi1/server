from django.urls import path
from . import views

urlpatterns = [
    path('user/register/', views.UserView.as_view({'post': 'registration'})),
    path('user/login/', views.UserView.as_view({'post': 'login'})),
    path('user/delete/', views.UserView.as_view({'delete': 'delete'})),
    path('book/', views.BookView.as_view({
                'post': 'add',
                'get': 'get',
                'put': 'update',
                'delete': 'delete',
    })),
]