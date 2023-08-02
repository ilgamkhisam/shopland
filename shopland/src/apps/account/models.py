from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from src.apps.product.models import Product



class UserAddress(models.Model):
    street_address = models.CharField("Улица и номер дома", max_length=200, null=True, blank=True)
    city = models.CharField("Город", max_length=100, null=True, blank=True)
    postal_code = models.CharField("Почтовый индекс", max_length=10, null=True, blank=True)
    country = models.CharField("Страна", max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.street_address}, {self.city}, {self.country}"


class User(AbstractUser):
    GENDER_CHOICES = [
        ('M', 'Мужской'),
        ('F', 'Женский'),
        ('O', 'Не указано')
    ]

    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField("Email", unique=True)
    mobile = models.CharField("Номер телефона", max_length=15, null=True, blank=True)
    address = models.OneToOneField(UserAddress, on_delete=models.CASCADE, null=True, blank=True, related_name='users')
    gender = models.CharField("Пол", max_length=2, choices=GENDER_CHOICES, null=True, blank=True)
    birthday = models.DateField("Дата рождения", null=True, blank=True)
    favorite_choice = models.ManyToManyField(Product, related_name="users", blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'