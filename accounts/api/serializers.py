from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_auth.serializers import LoginSerializer

User = get_user_model()


class AccountSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'id', 'usuario', 'nome', 'nome_mae', 'credencial', 'roles', 'password', 'is_staff')
        write_only_fields = ('password',)
        read_only_fields = ('id', )

    def create(self, validated_data):
        user = User(**validated_data)
        # Hash the user's password.
        user.set_password(validated_data['password'])
        user.save()
        return user


class CustomLoginSerializer(LoginSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('usuario', 'password')
