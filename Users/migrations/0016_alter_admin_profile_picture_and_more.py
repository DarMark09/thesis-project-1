# Generated by Django 4.1.5 on 2023-02-21 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Users", "0015_alter_admin_profile_picture_alter_panelusers_group_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="admin",
            name="profile_picture",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="",
                verbose_name="C:\\Users\\Admin\\Desktop\\thesis-project\\media/profile_pictures/",
            ),
        ),
        migrations.AlterField(
            model_name="panel",
            name="profile_picture",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="",
                verbose_name="C:\\Users\\Admin\\Desktop\\thesis-project\\media/profile_pictures/",
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="profile_picture",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="",
                verbose_name="C:\\Users\\Admin\\Desktop\\thesis-project\\media/profile_pictures/",
            ),
        ),
    ]
