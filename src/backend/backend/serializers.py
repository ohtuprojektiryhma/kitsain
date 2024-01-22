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


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientsSerializer(many=True)
    steps = StepsSerializer(many=True)

    class Meta:
        model = Recipe
        fields = ['id', 'name', 'ingredients', 'steps']

    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredients', [])
        steps_data = validated_data.pop('steps', [])

        # Create the Recipe instance
        recipe = Recipe.objects.create(**validated_data)

        # Create Ingredients instances and associate with the Recipe
        for ingredient_data in ingredients_data:
            Ingredients.objects.create(recipe=recipe, **ingredient_data)

        # Create Steps instances and associate with the Recipe
        for step_data in steps_data:
            Steps.objects.create(recipe=recipe, **step_data)

        return recipe