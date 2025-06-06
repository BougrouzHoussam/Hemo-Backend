
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

# Create your models here.

class FixEmail(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(username = username)
        except UserModel.DoesNotExist:
            try:
                user = UserModel.objects.get(email = username)
            except UserModel.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
                UserModel().set_password(password)
            else:
                if user.check_password(password) and self.user_can_authenticate(user):
                    return user
    
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
            UserModel().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
    
