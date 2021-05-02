# Create your views here.
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from users.serializers import UserRegistrationSerializer


class UserRegistrationView(CreateAPIView):

    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer_obj = self.serializer_class(data=request.data)
        serializer_obj.is_valid(raise_exception=True)
        data = serializer_obj.save()
        status_code = status.HTTP_200_OK
        response = {
            'access_token': data['token']
            }
        
        return Response(response, status=status_code)