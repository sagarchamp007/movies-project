# Create your views here.
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from users.serializers import UserRegistrationSerializer
from movies_collection.serializers import CollectionCreateSerializer, CollectionUpdateSerializer
from movies_collection.models import Collection
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.core import serializers
from django.db import transaction
import requests


class MoviesView(CreateAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            movie_api = 'https://demo.credy.in/api/v1/maya/movies'
            username = 'iNd3jDMYRKsN1pjQPMRz2nrq7N99q4Tsp9EY9cM0'
            password = 'Ne5DoTQt7p8qrgkPdtenTK8zd6MorcCR5vXZIJNfJwvfafZfcOs4reyasVYddTyXCz9hcL5FGGIVxw3q02ibnBLhblivqQTp4BIC93LZHj4OppuHQUzwugcYu7TIC5H1' 
            resp = requests.get(movie_api, auth=(username, password))
            response = resp.json()
            status_code = status.HTTP_200_OK
        except Exception as e:
            status_code = status.HTTP_503_SERVICE_UNAVAILABLE
            response = {
                'success': 'false',
                'status code': status_code,
                'message': 'api error',
                'error': str(e)
                }
        return Response(response, status=status_code)



class CollectionView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CollectionCreateSerializer

    
    def post(self, request, c_uuid=None):
        serializer_obj = self.serializer_class(data=request.data)
        serializer_obj.is_valid(raise_exception=True)
        data = serializer_obj.save()
        status_code = status.HTTP_200_OK        
        return Response(data, status=status_code)


    def put(self, request, c_uuid=None):
        try:
            collection = Collection.objects.get(uuid=c_uuid)
        except Collection.DoesNotExist:
            resp = {"is_success": False, "message": "collection not found"}
            return Response(resp, status=status.HTTP_400_BAD_REQUEST)
        serializer_obj = CollectionUpdateSerializer(collection, data=request.data)
        serializer_obj.is_valid(raise_exception=True)
        serializer_obj.save()
        status_code = status.HTTP_200_OK        
        return Response(serializer_obj.data, status=status_code)


    def get(self, request, c_uuid=None):
        try:
            collection = Collection.objects.get(uuid=c_uuid)
        except Collection.DoesNotExist:
            resp = {"is_success": False, "message": "collection not found"}
            return Response(resp, status=status.HTTP_400_BAD_REQUEST)
        s_data = self.serializer_class(collection)
        print(collection.movies)
        status_code = status.HTTP_200_OK        
        return Response(s_data.data, status=status_code)


    def delete(self,  request, c_uuid=None):
        
        try:
            collection = Collection.objects.get(uuid=c_uuid)
        except Collection.DoesNotExist:
            resp = {"is_success": False, "message": "collection not found"}
            return Response(resp, status=status.HTTP_400_BAD_REQUEST)

        collection.movies.clear()
        collection.delete()
        is_deleted = True
        status_code = status.HTTP_200_OK        
        return Response({"is_deleted": is_deleted}, status=status_code)
            


    