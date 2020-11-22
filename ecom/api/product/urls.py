from rest_framework import routers
from django.urls import path, include
from . import views
router = routers.DefaultRouter()
router.register(r'',views.ProductViewSet) #'' as this invoked only when /api/product so no need to add extra
urlpatterns =[
    path('',include(router.urls)),#the one defined above
    path('filter/<int:id>/',views.ProductViewSet.filter_bycateg,name='filter.categ')
]