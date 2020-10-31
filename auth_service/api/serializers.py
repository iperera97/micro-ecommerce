from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"


class SignupSerializer(UserSerializer):

    class Meta(UserSerializer.Meta):
        read_only_fields = (
            "username", "is_superuser", "is_staff",
            "register_date", "last_update_date"
        )

    def create(self, data):
        return User.objects.create_customer(**data)
