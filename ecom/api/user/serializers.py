from rest_framework import serializers
from django.contrib.auth.hashers import make_password #to hash the pass text
from rest_framework.decorators import authentication_classes,permission_classes
from .models import  CustomUser

class UserSerializer(serializers.HyperlinkedModelSerializer):

    def create(self, validated_data): #create new user
        password = validated_data.pop('password',None) #remove the password from the dictionary passed(this is the data user fills while registering)
        instance = self.Meta.model(**validated_data) #instance created without pass
        if password is not None:
            instance.set_password(password) #hashed version saved
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr,value in validated_data.items():
            if attr == 'password': #handled separately by using set_apssword which does hashing and stuff
                instance.set_password(value)
            else: #this will work for all attri other than pass as pass not stored directly as string hence coded above.Used in built method
                setattr(instance,attr,value)#update attr of instance object with the given value
        instance.save()
        return instance

    class Meta:
        model = CustomUser
        extra_kwargs = {'password':{'write_only':True}}
        fields = ('name','email','password','phone','gender','is_active','is_staff','is_superuser') # the last 3 are from the inherited
                                                                                                    #abstract user class
