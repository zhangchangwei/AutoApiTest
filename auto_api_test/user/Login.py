from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, request



class Login(View):
    def post(self, request):
        print(request)