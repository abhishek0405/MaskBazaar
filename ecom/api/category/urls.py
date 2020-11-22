from rest_framework import routers
from django.urls import path, include
from . import views
router = routers.DefaultRouter()
router.register(r'',views.CategoryViewSet) #'' as this invoked only when /api/category so no need to add extra
urlpatterns =[
    path('',include(router.urls))#the one defined above
]