from django.contrib.auth import get_user_model
from rest_framework import serializers

# region Account Serializer

Account = get_user_model()


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ("email", "username", "password", "first_name", "last_name")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = Account(
                email=validated_data["email"],
                username=validated_data["username"],
                first_name=validated_data["first_name"],
                last_name=validated_data["last_name"]
        )
        user.set_password(validated_data["password"])
        user.save()
        return user

# endregion
