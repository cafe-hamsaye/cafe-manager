
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'phone_number', 'password', 'password2', 'is_cafe_staff')
        extra_kwargs = {
            'password': {'write_only': True},
            'first_name': {'required': True, 'error_messages': {'required': 'لطفا نام خود را وارد کنید', 'blank': 'لطفا نام خود را وارد کنید'}},
            'last_name': {'required': True, 'error_messages': {'required': 'لطفا نام خانوادگی خود را وارد کنید', 'blank': 'لطفا نام خانوادگی خود را وارد کنید'}},
            'phone_number': {'required': True, 'error_messages': {'required': 'لطفا شماره تلفن خود را وارد کنید', 'blank': 'لطفا شماره تلفن خود را وارد کنید'}},
            'is_cafe_staff': {'read_only': True}, # Default to read-only
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and request.user and request.user.is_superuser:
            self.fields['is_cafe_staff'].read_only = False

    def validate(self, data):
        # password validation is only for creation
        if 'password' in data and 'password2' in data and data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "رمزهای عبور یکسان نیستند!"})
        return data

    def create(self, validated_data):
        validated_data.pop('password2', None)  # Remove password2 before creating user
        # Ensure is_cafe_staff is not set by non-admins during creation
        if not self.context.get('request').user.is_superuser:
            validated_data['is_cafe_staff'] = False
        user = User.objects.create_user(**validated_data)
        return user

    def validate_phone_number(self, value):
        if User.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError("کاربری با این شماره تلفن قبلا ثبت‌نام کرده است")
        return value

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'phone_number'
    default_error_messages = {
        'no_active_account': 'شماره تلفن یا رمز عبور اشتباه است'
    }

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['is_cafe_staff'] = user.is_cafe_staff

        return token


class AdminTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'username'
    default_error_messages = {
        'no_active_account': 'نام کاربری یا رمز عبور اشتباه است'
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields[self.username_field] = serializers.CharField()
        self.fields['password'] = serializers.CharField(
            style={'input_type': 'password'},
            write_only=True
        )

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['is_admin'] = True
        token['username'] = user.username

        return token
