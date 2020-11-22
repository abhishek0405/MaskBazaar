from django.shortcuts import render
from rest_framework import viewsets
from  rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from .models import CustomUser
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login,logout
import re
import random
# Create your views here.
@csrf_exempt  # to allow certain security things
def signin(request):
    if not request.method =='POST':
        return JsonResponse({'error':'Send Post request with valid params'})
    #validating the userid and pass
    username = request.POST['email']
    password = request.POST['password']

    #if not re.match("\b[\w\.-]+@[\w\.-]+\.\w{2,4}\b",username):
        #return JsonResponse({'error ':'Enter Valid Email'})

    if len(password)<3:
        return JsonResponse({'error':"Atleast 5 letters in pass"})

    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(email=username)

        if user.check_password(password):
            usr_dict = UserModel.objects.filter(email=username).values().first()
            usr_dict.pop('password') #we might use this in frontend hence popping it out.

            if user.session_token!='0': #0 is default value of token
                user.session_token='0' #if not logged in earlier this done so now next block excecuted.
                user.save()
                return JsonResponse({'error':'prev session exists'})

            token = generate_session_token()
            user.session_token = token
            user.save()
            login(request,user)# inbuilt method
            return JsonResponse({'token':token,'user':usr_dict})#we popped off password hence can pass here

        else:
            return  JsonResponse({'error':'Invalid pass'})



    except UserModel.DoesNotExist:
        return JsonResponse({'error':'Invalid Email'})

def signout(request,id):

    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(pk=id)
        user.session_token='0'
        user.save()
    except UserModel.DoesNotExist:
        return JsonResponse({'error':'Invalid userID'})
    logout(request)
    return JsonResponse({'success':'Logout Success'})

def generate_session_token(length=10): #aim is to generate 10 letter long string
    letterchoices = [chr(i) for i in range(97,123)] +[str(i) for i in range(10)] #list of all letters and numbers
    return ''.join(random.SystemRandom().choice(letterchoices) for _ in range(length))#returns 10 random letters from the list

class UserViewSet(viewsets.ModelViewSet): #standard code to refer
    permission_classes_by_action = {'create':[AllowAny]}

    queryset = CustomUser.objects.all().order_by(('id'))
    serializer_class = UserSerializer

    def get_permissions(self):  #this is done so that someone doesnt become superuser by modifying post
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]