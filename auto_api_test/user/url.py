from django.urls import path
from user.views import UserInfo
from user.Login import Login



urlpatterns = [
    path('list/', UserInfo.as_view()),
    path('login/', Login.as_view())
]
