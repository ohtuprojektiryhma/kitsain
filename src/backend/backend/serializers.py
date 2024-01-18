from django.contrib.auth.models import Group, User
from rest_framework import serializers
from backend.backend.models import Recipe, Ingredients, Steps


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = ['ingredient']

class StepsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Steps
        fields = ['step']


class RecipeSerializer(serializers.Serializer):
    ingredients = IngredientsSerializer(many=True)
    steps = StepsSerializer(many=True)

    class Meta:
        model = Recipe
        fields = ['id', 'steps, ingredients, name']