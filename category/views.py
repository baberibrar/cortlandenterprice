from .models import Category
from .serializer import CategorySerializer
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny


# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return Response({"message": str(e)}, status=400)
        serializer.save()
        response = {
            "message": "Category created successfully",
            "data": serializer.data
        }
        return Response(response, status=status.HTTP_201_CREATED)
