from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, AllowAny
from rest_framework.generics import *

from accounts.permissions import IsAdminAccount
from .serializers import *


class CategoryListCreateAPIView(ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def get_permissions(self):
        if self.request.method not in SAFE_METHODS:
            return [IsAdminAccount()]
        return [AllowAny()]


class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def get_permissions(self):
        if self.request.method not in SAFE_METHODS:
            return [IsAdminAccount()]
        return [AllowAny()]
