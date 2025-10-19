from rest_framework import serializers
from .models import Staff

class StaffSerializer(serializers.ModelSerializer):
    # Define password as a write-only field
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = Staff
        fields = ['id', 'number', 'password', 'last_login']
        read_only_fields = ['id', 'last_login']

    def create(self, validated_data):
        # Use the create_user method to handle password hashing
        user = Staff.objects.create_user(
            number=validated_data['number'],
            password=validated_data['password']
        )
        return user

    def update(self, instance, validated_data):
        # Update instance fields
        instance.number = validated_data.get('number', instance.number)

        # Handle password update separately to ensure hashing
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        
        instance.save()
        return instance
