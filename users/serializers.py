from rest_framework import serializers
from users.models import User
from rest_framework_jwt.settings import api_settings


JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER



class UserRegistrationSerializer(serializers.ModelSerializer):
    # used for serializers.Serializer
    # username = serializers.EmailField(max_length=255, required=True)
    # password = serializers.CharField(max_length=255, required=True)

    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # print(validated_data)
        user = User.objects.create_user(**validated_data)
        payload = JWT_PAYLOAD_HANDLER(user)
        jwt_token = JWT_ENCODE_HANDLER(payload)
        return {'token': jwt_token}