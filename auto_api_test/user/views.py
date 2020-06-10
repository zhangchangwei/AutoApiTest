from django.shortcuts import render
from user.models import User
from django.views import View
from django.http import HttpResponse, request



class UserInfo(View):
    def get(self, request):
        return HttpResponse(User.objects.all().values())