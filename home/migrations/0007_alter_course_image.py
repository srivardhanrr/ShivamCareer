# Generated by Django 4.2.1 on 2023-06-03 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_course_image_alter_blog_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='courses/image/'),
        ),
    ]
