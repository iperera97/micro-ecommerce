from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, email, password, **kwargs):
        """ create new user
        Args:
            email (str)
            password (str)
        Raises:
            if user creation data invalid error will be throw
        Returns:
            object: user instance if successfully created otherwise throw error
        """
        is_active = kwargs.get("status") or True
        user = self.model(
            email=self.normalize_email(email),
            username=kwargs.get("username"),
            is_active=is_active,
            is_superuser=kwargs.get("is_superuser", False),
            is_staff=kwargs.get("is_staff", False),
        )

        user.set_password(password)
        user.full_clean()
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, username, **kwargs):
        data = {
            **kwargs,
            "username": username,
            "is_superuser": True,
            "is_staff": True
        }
        return self.create_user(email, password, **data)

    def create_staff_user(self, email, password, username, **kwargs):
        data = {
            **kwargs,
            "username": username,
            "is_superuser": False,
            "is_staff": True
        }
        return self.create_user(email, password, **data)

    def create_customer(self, email, password, **kwargs):
        data = {
            **kwargs,
            "is_superuser": False,
            "is_staff": False
        }
        return self.create_user(email, password, **data)
