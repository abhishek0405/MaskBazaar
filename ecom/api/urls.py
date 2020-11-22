from django.urls import path, include
from rest_framework.authtoken import views
from .views import home#.views means current dir views
urlpatterns = [
    path('', home, name='api.home'),# home is a name of method we will declare in views of respective app
    path('category/',include('api.category.urls')), #route for /api/category defined in the path specified.
    path('product/',include('api.product.urls')),
    path('user/',include('api.user.urls')),
    path('order/',include('api.order.urls')),
    path('payment/',include('api.payment.urls')),
    path('api-token-auth/',views.obtain_auth_token,name='api_token_auth') #if not generating custom token can use this also
]