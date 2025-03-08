from rest_framework.serializers import ModelSerializer
from .models import *

class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = (
            'id', 'username', 'password', 'email', 'phone_number', 'birthdate','first_name', 'last_name', 'date_joined', 'role'
        )

        extra_kwargs = {
            'password': {
                'write_only': True
            },
            'username': {
                'read_only': True,
            },
            'phone_number': {
                'required': True,
            },
            'date_joined': {
                'read_only': True
            },
            'role': {
                'default': 'Regular',
            }
        }

    def create(self, validated_data):
        return Account.objects.create_user(**validated_data)


