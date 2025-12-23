from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.
from django.views import View
from .mixin import mixinreponse

class viewers(mixinreponse,View):
    def get(self,request):
        return HttpResponse("hello everyone" ,self.mixinreponse)
    
    