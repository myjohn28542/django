
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from .models import User


class RegisterAPI(viewsets.GenericViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):

        data = request.data
        print(data)
        user = User.objects.create(
            email=data['email'],
            password=data['password']
        )
        # user.save()
        return Response({}, status=status.HTTP_201_CREATED)
        # data = request.data
        # user = User.objects.create(data)
        # return Response(data=user, status=201)












