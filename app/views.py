from django.shortcuts import render
from .serailizers import  ApiSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from .models import *


# Create your views here.


def api(request):
	api = Api.objects.get(id=3)
	serailizers =  ApiSerializer(api)
	# json_data = JSONRenderer().render(serailizers.data)
	# return HttpResponse(json_data, content_type='application/json')
	return JsonResponse(serailizers.data)
