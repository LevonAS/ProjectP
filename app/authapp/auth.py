from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


User = get_user_model()


class EmailAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # kwargs = {"email": username}
        # try:
        #     user = User.objects.get(email=username)
        # except User.DoesNotExist:
        #     return None
        # else:
        #     if user.check_password(password) and self.user_can_authenticate(user):
        #         return user

        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
