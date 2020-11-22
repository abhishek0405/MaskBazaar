from rest_framework import serializers
from .models import Product
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    image=serializers.ImageField(max_length=None,required=True,allow_empty_file=False)
    class Meta:
        model=Product
        fields=('name','description','image','price','category')
