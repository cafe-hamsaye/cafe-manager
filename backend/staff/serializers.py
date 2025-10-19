from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Staff

class StaffSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False, style={'input_type': 'password'})

    class Meta:
        model = Staff
        fields = ('id', 'number', 'password', 'last_login')
        read_only_fields = ('id', 'last_login')

    def create(self, validated_data):
        return Staff.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        instance.number = validated_data.get('number', instance.number)
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        instance.save()
        return instance

# This now mirrors MyTokenObtainPairSerializer exactly
class StaffTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'number'

    default_error_messages = {
        'no_active_account': 'شماره یا رمز عبور اشتباه است'
    }

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims for staff
        token['is_staff_member'] = True
        token['number'] = user.number
        return token
