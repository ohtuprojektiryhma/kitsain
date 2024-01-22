from django.http import JsonResponse
from rest_framework import viewsets, permissions
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from backend.backend.models import Recipe
from django.contrib.auth.models import Group, User
from backend.backend.serializers import (
    RecipeSerializer,
    UserSerializer,
    GroupSerializer,
    IngredientsSerializer,
    StepsSerializer,
)
from services.recipe_service import RecipeService


class RecipeViewSet(viewsets.ModelViewSet):
    """
    API endoint that allows recipes to be viewed or edited.
    """

    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticated]


@csrf_exempt
@require_POST
def recipe_generator(request):
    data = request.POST
    print(data)
    serializer = IngredientsSerializer(data=data["ingredients"])

    if serializer.is_valid():
        ingredients = serializer.validated_data["ingredients"]

        recipe = RecipeService().get_recipe(ingredients, data["recipe_type"])

        return recipe

    return JsonResponse({"error": "Invalid ingredients data"}, status=400)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
