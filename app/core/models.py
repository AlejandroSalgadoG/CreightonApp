from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    def _create_user_obj(self, email, password=None, **kwargs):
        if not email:
            raise ValueError("user must have an email address")

        user = self.model(email=self.normalize_email(email), **kwargs)  # create new user object
        user.set_password(password)  # hash password
        return user

    # password is set to none to allow the creation of an unusable user for testing
    # this is the default behavior of the django user model
    def create_user(self, email, password=None, **kwargs):
        user = self._create_user_obj(email, password, **kwargs)
        user.save(using=self._db)  # best practice is to select database (usefull when working with multiple db)
        return user

    def create_superuser(self, email, password):
        user = self._create_user_obj(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"


class Observation(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    date = models.DateField()
    observation = models.CharField(
        max_length=255,
        choices=[
            ("H", "H - flujo abundante"),
            ("M", "M - flujo moderado"),
            ("L", "L - flujo ligero"),
            ("VL", "VL - flujo muy ligero"),
            ("B", "B - sangrado cafe/marron/negro"),
            ("0", "0 - seco"),
            ("2", "2 - humedo sin lubricacion"),
            ("2W", "2W - mojado sin lubricacion"),
            ("4", "4 - brillo sin lubricacion"),
            ("6", "6 - pegajoso (0.5 cm | 1/4 inch)"),
            ("8", "8 - ligoso (1-2 cm | 1/2 - 3/4 inch)"),
            ("10", "10 - elastico (2.5 cm | 1 inch)"),
            ("10DL", "10DL - humedo con lubricacion"),
            ("10SL", "10SL - brillo con lubricacion"),
            ("10WL", "10WL - mojado con lubricacion"),
        ],
    )
    code = models.CharField(
        max_length=255,
        choices=[
            ("B", "B - sangrado cafe/marron/negro"),
            ("C", "C - nublado (blanco)"),
            ("K", "K - transparente"),
            ("L", "L - lubricante"),
            ("P", "P - pastoso (cremoso)"),
            ("R", "R - rojo"),
            ("Y", "Y - amarillo (aun muy palido)"),
        ],
    )
    frequency = models.CharField(
        max_length=255,
        choices=[
            ("x1", "x1 - una vez al dia"),
            ("x2", "x2 - dos veces al dia"),
            ("x3", "x3 - tres veces al dia"),
            ("AD", "AD - a lo largo del dia"),
        ],
    )
