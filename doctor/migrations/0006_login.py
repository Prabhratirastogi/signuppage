# Generated by Django 3.2.12 on 2022-04-07 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0005_alter_signup_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('passs1', models.CharField(max_length=50)),
            ],
        ),
    ]
