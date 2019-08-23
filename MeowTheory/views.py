from django.shortcuts import render

# Create your views here.
from MeowTheory.models import *
from django.core.cache import cache
import json, datetime, decimal
from django.http import JsonResponse, HttpResponse
from django.views import View
from django.db.models import Avg, Sum, Q
from django.db import connection
from MT.settings import MEDIA_URL

class GetUserDetail(View):

    def dispatch(self, request, *args, **kwargs):
        obj = super().dispatch(request, *args, **kwargs)
        return obj

    def get(self,request):

        user_obj=User.objects.filter(id=1).first()
        level_obj=Level.objects.filter(experience__lte=user_obj.experience).order_by("-experience").first()
        print(user_obj.avatar)
        return JsonResponse({"data":{"username":user_obj.username,"level":level_obj.name,"user_avatar":MEDIA_URL+str(user_obj.avatar),"level_img":MEDIA_URL+str(level_obj.img)}})