# Generated by Django 3.2.2 on 2021-05-10 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20210510_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Address2',
            field=models.CharField(blank=True, help_text='Address 2', max_length=100, null=True),
        ),
    ]