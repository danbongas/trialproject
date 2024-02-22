from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Recipe
from .serializers import RecipeSerializer
from base.api import serializers




@api_view(['GET', 'POST'])
def getRoutes(request):
    routes = [
        'GET /api/',
        'GET /api/recipes',
        'GET /api/recipes/:id'
    ]
    return Response(routes)



@api_view(['GET'])
def getRecipes(request):
    rooms = Recipe.objects.all()
    serializer = RecipeSerializer(rooms, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getRecipe(request, pk):
    room = Recipe.objects.get(id=pk)
    serializer = RecipeSerializer(room, many=False)
    return Response(serializer.data)