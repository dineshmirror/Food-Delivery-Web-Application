# Generated by Django 3.0.14 on 2021-09-21 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(null=True, upload_to='menu_images/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='customer.Category')),
            ],
        ),
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('street', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=15, null=True)),
                ('zip_code', models.IntegerField(blank=True, null=True)),
                ('is_paid', models.BooleanField(default=False, null=True)),
                ('is_shipped', models.BooleanField(default=False, null=True)),
                ('items', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='order', to='customer.MenuItem')),
            ],
        ),
    ]
