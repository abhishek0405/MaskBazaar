from rest_framework import routers
from django.urls import path, include
from . import views
router = routers.DefaultRouter()
router.register(r'',views.OrderViewSet) #'' as this invoked only when /api/product so no need to add extra
urlpatterns =[
    path('add/<str:id>/<str:token>',views.add,name='order.add'),
    path('',include(router.urls))#the one defined above
]