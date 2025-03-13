# Generated by Django 5.1.6 on 2025-03-12 14:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Hobby",
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
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Result",
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
                ("marks", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="Subject",
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
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Student",
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
                ("name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=50)),
                (
                    "image",
                    models.ImageField(
                        blank=True, default="def.png", upload_to="images/"
                    ),
                ),
                ("mother_name", models.CharField(max_length=50)),
                ("father_name", models.CharField(max_length=50)),
                (
                    "religion",
                    models.CharField(
                        choices=[
                            ("Islam", "Islam"),
                            ("Hindu", "Hindu"),
                            ("Christian", "Christian"),
                            ("Buddho", "Buddho"),
                            ("Atheist", "Atheist"),
                            ("Others", "Others"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("Male", "Male"),
                            ("Female", "Female"),
                            ("Others", "Ohters"),
                        ],
                        max_length=10,
                    ),
                ),
                ("date_of_birth", models.DateField()),
                ("roll", models.IntegerField()),
                ("city", models.CharField(max_length=100)),
                ("is_Bangladeshi", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("age", models.PositiveIntegerField()),
                (
                    "hobby",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="student_management_app.hobby",
                    ),
                ),
                ("result", models.ManyToManyField(to="student_management_app.result")),
                (
                    "subject",
                    models.ManyToManyField(to="student_management_app.subject"),
                ),
            ],
        ),
        migrations.AddField(
            model_name="result",
            name="subject",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="student_management_app.subject",
            ),
        ),
    ]
