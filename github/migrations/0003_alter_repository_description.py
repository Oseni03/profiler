# Generated by Django 4.1.1 on 2022-10-23 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("github", "0002_alter_starred_description_alter_starred_language"),
    ]

    operations = [
        migrations.AlterField(
            model_name="repository",
            name="description",
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]