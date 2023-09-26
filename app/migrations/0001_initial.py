# Generated by Django 4.2.5 on 2023-09-26 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_food', models.CharField(max_length=40)),
                ('type_of_drinks', models.CharField(max_length=40)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SoftDrinks',
            fields=[
                ('drinks_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.drinks')),
                ('brand', models.CharField(max_length=40)),
                ('color', models.CharField(max_length=40)),
                ('type_of_soft_drinks', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='typeofsoft', to='app.drinks')),
            ],
            options={
                'abstract': False,
            },
            bases=('app.drinks',),
        ),
        migrations.CreateModel(
            name='AlhocolDrinks',
            fields=[
                ('drinks_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.drinks')),
                ('brand', models.CharField(max_length=40)),
                ('color', models.CharField(max_length=40)),
                ('type_of_alhocol_drinks', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='typeofalhocol', to='app.drinks')),
            ],
            options={
                'abstract': False,
            },
            bases=('app.drinks',),
        ),
    ]