# Generated by Django 3.0.6 on 2020-07-29 19:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200728_2325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchlist',
            name='stocks',
        ),
        migrations.AddField(
            model_name='portfolio',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='watchlist',
            name='stock',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='CashTransactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.CharField(blank=True, max_length=200, null=True)),
                ('price', models.DecimalField(decimal_places=4, max_digits=20)),
                ('amount_of_shares', models.DecimalField(decimal_places=4, max_digits=20)),
                ('price_per_stock', models.DecimalField(decimal_places=4, max_digits=20)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]