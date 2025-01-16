from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import BasicAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
from .models import *
from .serializers import *

class BaseViewSet(ModelViewSet):
    authentication_classes = [BasicAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = "__all__"
    ordering_fields = "__all__"
    

class UserViewSet(BaseViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ItemViewSet(BaseViewSet):
    queryset = ItemModel.objects.all()
    serializer_class = ItemSerializer
    
    @action(detail=False, methods=['get'])
    def teste(self, request):
        return Response("teste")