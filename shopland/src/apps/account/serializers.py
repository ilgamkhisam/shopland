
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User
from datetime import date

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        token['username'] = user.username
        return token
    # Кастомный сериалайзер для JWT, добавляет поле "username" в токен для удобства клиентского приложения при аутентификации.


# Сериалайзер для регистрации пользователей с проверкой совпадения паролей и возраста.
class RegisterUserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=255)
    password2 = serializers.CharField(max_length=255)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'birthday',
            'password1',
            'password2',
        )

    # Проверяет, что пароли совпадают, вызывает ошибку, если нет, иначе возвращает валидированные данные
    def validate(self, attrs):
        password1 = attrs.get('password1')
        password2 = attrs.get('password2')
        if password1 != password2:
            raise serializers.ValidationError({"password":"Пароли не совпадают."})
        
        return attrs
    
    # Проверяет дату рождения, чтобы она не была позднее текущей даты и возраст пользователя был не менее 14 лет
    def validate_birthday(self, value):
        if value >= date.today():
            raise serializers.ValidationError({'birthday':'ВЫ рождены слишком рано'})
        
        age = (date.today() - value).days // 365
        if age < 14: 
            raise serializers.ValidationError({'birthday':'Доступ закрыт'})
        return value
    
    # Создает нового пользователя с валидированными данными и устанавливает пароль перед сохранением
    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            birthday = validated_data['birthday']
            
        ) 
        user.set_password(validated_data['password1'])
        user.save()
        return user