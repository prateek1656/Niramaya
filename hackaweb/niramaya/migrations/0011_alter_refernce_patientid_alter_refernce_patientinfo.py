# Generated by Django 4.0.1 on 2022-02-13 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('niramaya', '0010_alter_refernce_patientinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='refernce',
            name='patientID',
            field=models.CharField(default='default', max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='refernce',
            name='patientInfo',
            field=models.FileField(upload_to='documents/'),
        ),
    ]
