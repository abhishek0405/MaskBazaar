from rest_framework import routers
from django.urls import path, include
from . import views
router = routers.DefaultRouter()
router.register(r'',views.UserViewSet) #'' as this invoked only when /api/product so no need to add extra
urlpatterns =[
    path('login/',views.signin,name='signin'),
    path('logout/<int:id>/',views.signout,name='signout'), #as we need id during signout(way function designed)
    path('',include(router.urls)) #sign up
]