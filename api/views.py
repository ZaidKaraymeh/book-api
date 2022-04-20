from django.shortcuts import render
import json
# Create your views here.

def set_order(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        data = json.loads(body_unicode)