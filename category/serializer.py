from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'created_at', 'updated_at')

    def create(self, validated_data):
        # if name already exists, then return error message
        if Category.objects.filter(name=validated_data['name']).exists():
            raise serializers.ValidationError({'This Category already exists'})
        return Category.objects.create(**validated_data)
