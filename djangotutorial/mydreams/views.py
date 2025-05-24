from django.shortcuts import render

from django.shortcuts import get_object_or_404,render

from django.template import loader

from .models import MyDream


# Create your views here.
# THIS IS FOR LEEARNING PURPOSES ONLY YOU CAN UNCOMMENT THIS CODE TO SEE THE OUTPUT

from django.http import HttpResponse, Http404
# Create your views here.

def index(request):
    latest_question_list = MyDream.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.dream_title for q in latest_question_list])
    # return HttpResponse("Hello, world. You're at the polls index.")
    return HttpResponse(output)