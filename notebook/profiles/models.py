from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import models
from django.contrib.auth.models import AbstractUser


class Company(models.Model):
    name = models.CharField(max_length=255)
    website = models.URLField(null=True)
    phone_number = models.CharField(max_length=12, null=True)
    # address будет отдельной моделью
    # area - отрасль будет отдельной моделью
    # subarea - направление в отрасли (сфера) будет моделью связанной с area


class User(AbstractUser):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    phone_number = models.CharField(max_length=12, null=True)
    position = models.CharField(max_length=255, null=True)
    # address будет отдельной моделью


class BaseRegisterForm(UserCreationForm):
    class BaseRegisterForm(UserCreationForm):
        email = forms.EmailField(label="Email")
        first_name = forms.CharField(label="Имя")
        last_name = forms.CharField(label="Фамилия")

        class Meta:
            model = User
            fields = ("username",
                      "first_name",
                      "last_name",
                      "email",
                      "password1",
                      "password2",)
