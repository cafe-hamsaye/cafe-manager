
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'phone_number', 'password', 'password2')
        extra_kwargs = {
            'password': {'write_only': True},
            'first_name': {'required': True, 'error_messages': {'required': 'لطفا نام خود را وارد کنید', 'blank': 'لطفا نام خود را وارد کنید'}},
            'last_name': {'required': True, 'error_messages': {'required': 'لطفا نام خانوادگی خود را وارد کنید', 'blank': 'لطفا نام خانوادگی خود را وارد کنید'}},
            'phone_number': {'required': True, 'error_messages': {'required': 'لطفا شماره تلفن خود را وارد کنید', 'blank': 'لطفا شماره تلفن خود را وارد کنید'}},
        }

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "رمزهای عبور یکسان نیستند!"})
        return data

    def create(self, validated_data):
        validated_data.pop('password2', None)  # Remove password2 before creating user
        user = User.objects.create_user(**validated_data)
        return user

    def validate_phone_number(self, value):
        if User.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError("کاربری با این شماره تلفن قبلا ثبت‌نام کرده است")
        return value

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    default_error_messages = {
        'no_active_account': 'شماره تلفن یا رمز عبور اشتباه است'
    }

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name

        return token


class AdminLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
