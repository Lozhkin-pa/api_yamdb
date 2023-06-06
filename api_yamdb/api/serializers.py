from users.models import User, CHOICES
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    role = serializers.ChoiceField(choices=CHOICES, default='user')

    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'role', 'bio'
        )
    
    def validate_username(self, name):
        if name == 'me':
            raise serializers.ValidationError('Имя ME')
        elif name is None or name == "":
            raise serializers.ValidationError('Нет имени')
        return name

    def validate_email(self, email):
        if email is None or email == "":
            raise serializers.ValidationError('Email пуст')
        return email

class RoleSerializer(UserSerializer):
    role = serializers.CharField(read_only=True)


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email',)

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError([
                'Не может быть равно me и содержит только латиницу'])
        return value
    
    def validate(self, data):
        username = data.get('username')
        email = data.get('email')
        if (
            User.objects.filter(username=username).exists()
            and User.objects.get(username=username).email != email
        ):
            raise serializers.ValidationError('Имя уже есть')
        if (
            User.objects.filter(email=email).exists()
            and User.objects.get(email=email).username != username
        ):
            raise serializers.ValidationError('Email уже есть')
        return data

class CreateTokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    confirmation_code = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        confirmation_code = data.get('confirmation_code')
        if username is None:
            raise serializers.ValidationError('Код пуст')
        if confirmation_code is None:
            raise serializers.ValidationError('Код отсутствует')
        return data
