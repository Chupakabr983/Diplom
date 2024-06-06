from django.db import models
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

