# Generated by Django 5.1.2 on 2024-11-02 14:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("follows", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=150)),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="email address"
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("is_staff", models.BooleanField(default=False)),
                ("is_superuser", models.BooleanField(default=False)),
                ("is_approved", models.BooleanField(default=False)),
                ("bio", models.TextField(blank=True, max_length=160)),
                (
                    "profile_image",
                    models.ImageField(blank=True, null=True, upload_to="profiles/"),
                ),
                (
                    "followers",
                    models.ManyToManyField(
                        related_name="following",
                        through="follows.Follow",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True, related_name="customuser_groups", to="auth.group"
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        related_name="customuser_permissions",
                        to="auth.permission",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
