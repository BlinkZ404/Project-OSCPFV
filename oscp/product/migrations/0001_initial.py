# Generated by Django 5.0.4 on 2024-04-24 20:49

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('variant', models.CharField(max_length=20, null=True)),
                ('details', models.TextField(max_length=500, null=True)),
                ('category', models.CharField(choices=[('S', 'Smartphone'), ('C', 'Computer'), ('SW', 'SmartWatch'), ('CA', 'Camera'), ('H', 'Headphone')], max_length=2)),
                ('image', models.ImageField(default='default.jpg', upload_to='static/images')),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('logo', models.ImageField(upload_to='static/images')),
            ],
        ),
        migrations.CreateModel(
            name='MerchantItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('stock', models.CharField(choices=[('In-Stock', 'In-Stock'), ('Pre-Order', 'Pre-Order'), ('Out-of-Stock', 'Out-of-Stock')], default=(('In-Stock', 'In-Stock'), ('Pre-Order', 'Pre-Order'), ('Out-of-Stock', 'Out-of-Stock')), max_length=15)),
                ('shipping', models.CharField(max_length=100, null=True)),
                ('warranty', models.CharField(max_length=100, null=True)),
                ('price', models.IntegerField(null=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.item')),
                ('merchant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.merchant')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('order_date', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('address', models.CharField(max_length=500, null=True)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('payment_info', models.CharField(max_length=20, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Ready to Ship', 'Ready to Ship'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered'), ('Canceled', 'Canceled')], default='Pending', max_length=15)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.merchantitem')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.order')),
            ],
        ),
    ]