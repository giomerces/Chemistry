# Generated by Django 3.2.16 on 2022-12-26 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compounds', '0002_auto_20221226_1523'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=250, null=True)),
                ('shipping_cost_by_km', models.DecimalField(decimal_places=8, max_digits=16)),
                ('min_purchase', models.DecimalField(decimal_places=8, max_digits=16)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CompoundStore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('unit_price', models.DecimalField(decimal_places=8, max_digits=16)),
                ('unit', models.CharField(choices=[('g', 'Gramme'), ('Kg', 'Kilo'), ('mL', 'Milliliter'), ('L', 'Liter')], max_length=10)),
                ('available', models.BooleanField(default=True)),
                ('compound', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compounds.compound')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compounds.store')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='compound',
            name='members',
            field=models.ManyToManyField(through='compounds.CompoundStore', to='compounds.Store'),
        ),
    ]
