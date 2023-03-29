from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.views import View
from django.contrib.auth.models import User
from .moduls import Task
import json
from django.contrib.auth import authenticate
from base64 import b64decode

def isAuth(auth):
    if auth  is None:
        return False
    token = auth.split(' ')[1]
    auth=b64decode(token).decode()
    username, password = auth.split(':')

    user = authenticate(username=username, password=password)

    if user is not None:
        return user
    return False

def add(request: HttpRequest) -> JsonResponse:
    auth = request.headers.get('Authorization')
    if isAuth(auth):
        if request.method == 'POST':
            body = request.body

            decoded = body.decode()

            data = json.loads(decoded)
            task=data.get("task", False)
            description=data.get("description", False)
            complited=data.get("complited", False)
            result=Task(
                task=task,
                description=description,
                complited=complited,
                student=isAuth(auth)
            )

            result.save()
            return JsonREsponse ({'result':"ok"})


    else:
        return JsonResponse({'message': 'Unauthorized'}, status=401)

