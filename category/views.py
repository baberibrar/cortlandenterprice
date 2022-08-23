from .models import Category
from .serializer import CategorySerializer
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.


class CategoryList(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
