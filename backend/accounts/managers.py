from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    #This is a manager for Account Class
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an phone numbe.")

        if not username:
            raise ValueError("Users must have an Username")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.is_rider = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_rider = False
        user.is_hubmanager = True
        user.is_staff = True
        user.is_superuser=True
        user.save(using=self._db)
        return user