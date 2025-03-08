from django.db import models
from django.contrib.auth.models import User, AbstractUser


class Account(AbstractUser):
    phone_number = models.CharField(max_length=13, unique=True)
    birthdate = models.DateField(blank=True, null=True)
    role = models.CharField(
        max_length=50,
        choices=[
            ('Regular', 'Regular'),
            ('Admin', 'Admin'),
            ('Superuser', 'Superuser'),
        ],
        default='Regular',
    )

    def __str__(self):
        return self.username


class Indentification(models.Model):
    pass_front = models.ImageField()
    pass_back = models.ImageField()
    with_pass = models.ImageField()
    card_number = models.CharField(max_length=16)
    expiration_date = models.CharField(max_length=5)
    card_phone_number = models.CharField(max_length=13)

    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.account.user.username


class Seller(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
