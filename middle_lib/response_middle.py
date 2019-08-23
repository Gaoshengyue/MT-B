from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse, HttpResponse
class ResponseMiddle(MiddlewareMixin):
    def process_request(self,request):
        pass
    def process_response(self, request,response):
        # print(request)
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "10000"
        response["Access-Control-Allow-Headers"] = "*"
        return response