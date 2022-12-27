from rest_framework import serializers


from .models import Customer, Category, Add, AddPic


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class AddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Add
        fields = '__all__'


class AddPicSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddPic
        fields = '__all__'