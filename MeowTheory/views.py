# Create your views here.
from django.http import JsonResponse
from django.views import View

from MT.settings import MEDIA_URL
from MeowTheory.models import *


class GetUserDetail(View):

    def dispatch(self, request, *args, **kwargs):
        obj = super().dispatch(request, *args, **kwargs)
        return obj

    def get(self, request):

        user_obj = User.objects.filter(id=1).first()
        level_obj = Level.objects.filter(experience__lte=user_obj.experience).order_by("-experience").first()
        next_obj = Level.objects.filter(upper_level=level_obj).first()
        if not next_obj:
            big_next = Level.objects.filter().order_by("-experience").first()
            next = "已满级"
            next_img = str(big_next.img)
            next_experience = big_next.experience
            experience=big_next.experience
        else:
            next = next_obj.name
            next_img = str(next_obj.img)
            next_experience = next_obj.experience
            experience=user_obj.experience

        return JsonResponse({"data": {"username": user_obj.username, "level": level_obj.name,
                                      "user_avatar": MEDIA_URL + str(user_obj.avatar),
                                      "level_img": MEDIA_URL + str(level_obj.img),"experience":experience,"next_experience":next_experience,"next":next,"next_img":MEDIA_URL+next_img}})
