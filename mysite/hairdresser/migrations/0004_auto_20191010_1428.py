# Generated by Django 2.2.1 on 2019-10-10 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hairdresser', '0003_auto_20191010_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hairstyle',
            name='sex',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1),
        ),
    ]
