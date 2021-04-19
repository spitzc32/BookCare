from app.accounts.models import Account, AccountAddress
from rest_framework import serializers, fields


class AccountSerializer(serializers.ModelSerializer):
    address = serializers.SerializerMethodField()

    class Meta:
        model = Account
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
            'preferred_name',
            'profile_picture',
            'longitude',
            'latitude',
            'is_active',
            'is_staff',
            'address',
        )

    def get_address(self, obj):
        address_qs = AccountAddress.objects.filter(
            account=obj.id,
            is_active=True,
        )

        serializer = AccountAddressSerializer(data=address_qs, many=True)
        serializer.is_valid()
        return serializer.data


class AccountAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = AccountAddress
        fields = (
            'number_bulding',
            'street',
            'area',
            'zipcode',
            'province',
            'country',
        )
