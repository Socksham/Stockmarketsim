# Generated by Django 3.0.6 on 2020-08-07 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200729_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='cashtransactions',
            name='sell',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
