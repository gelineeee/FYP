from django.urls import path

from accounts_api import views


urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view())
]