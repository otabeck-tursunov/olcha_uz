# Generated by Django 5.1.6 on 2025-03-04 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='role',
            field=models.CharField(choices=[('Regular', 'Regular'), ('Admin', 'Admin'), ('Superuser', 'Superuser')], default='Regular', max_length=50),
        ),
    ]
