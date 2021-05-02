from rest_framework import serializers
from movies_collection.models import Collection, Movie, Genre
from django.db import transaction


class GenreSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=115, required=True)


class MovieSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=115, required=True)
    description = serializers.CharField(max_length=500)
    genres = GenreSerializer(many=True)
    uuid = serializers.UUIDField()


class CollectionCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=115, required=True)
    description = serializers.CharField(max_length=500)
    movies =  MovieSerializer(many=True)


    def create(self, validated_data):
        movies_data = validated_data.pop('movies')
        with transaction.atomic():
                collection = Collection.objects.create(**validated_data)
                for m_data in movies_data:
                    genres_data = m_data.pop('genres')
                    movie = Movie.objects.create(**m_data)
                    collection.movies.add(movie)
                    for g_data in genres_data:
                        genre, created = Genre.objects.update_or_create(**g_data)
                        movie.genres.add(genre)
    
        return {'collection_uuid': str(collection.uuid)}



class CollectionUpdateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=115)
    description = serializers.CharField(max_length=500)
    movies =  MovieSerializer(many=True)


    def update(self, instance, validated_data):
        movies_data = validated_data.pop('movies')
        with transaction.atomic():
             collection = instance
             if validated_data['description']:
                collection.description = validated_data['description']
             if validated_data['title']:
                collection.title = validated_data['title']
             collection.save()
             for m_data in movies_data:
                    genres_data = m_data.pop('genres')
                    movie, created = Movie.objects.update_or_create(uuid=m_data['uuid'] ,defaults=m_data)
                    collection.movies.add(movie)
                    for g_data in genres_data:
                        genre, created = Genre.objects.update_or_create(**g_data)
                        movie.genres.add(genre)

        return instance
