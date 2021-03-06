# Generated by Django 2.2 on 2019-04-18 08:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Crust',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Dinner_Platter_toppings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Extra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=2, help_text='Price in US$', max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Pasta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('price', models.DecimalField(decimal_places=2, help_text='Price in US$', max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, help_text='Price in US$', max_digits=4)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='crust', to='orders.Crust')),
            ],
        ),
        migrations.CreateModel(
            name='Salads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('price', models.DecimalField(decimal_places=2, help_text='Price in US$', max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Subs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, help_text='Price in US$', max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Subs_topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Topping_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Toppings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Subs_with_add_on',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Add_on', models.ManyToManyField(blank=True, to='orders.Extra')),
                ('Basket', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Basket')),
                ('Subs', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Subs')),
            ],
        ),
        migrations.AddField(
            model_name='subs',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Subs_topping'),
        ),
        migrations.AddField(
            model_name='subs',
            name='quantity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Size'),
        ),
        migrations.CreateModel(
            name='Pizza_with_toppings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Basket', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Basket')),
                ('Pizza', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Pizza')),
                ('Toppings', models.ManyToManyField(blank=True, to='orders.Toppings')),
            ],
        ),
        migrations.AddField(
            model_name='pizza',
            name='quantity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quantity', to='orders.Size'),
        ),
        migrations.AddField(
            model_name='pizza',
            name='toppings',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='toppings', to='orders.Topping_type'),
        ),
        migrations.CreateModel(
            name='Dinner_Platter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, help_text='Price in US$', max_digits=4)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Dinner_Platter_toppings')),
                ('quantity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Size')),
            ],
        ),
        migrations.AddField(
            model_name='basket',
            name='Dinner_Platter',
            field=models.ManyToManyField(blank=True, to='orders.Dinner_Platter'),
        ),
        migrations.AddField(
            model_name='basket',
            name='Pasta',
            field=models.ManyToManyField(blank=True, to='orders.Pasta'),
        ),
        migrations.AddField(
            model_name='basket',
            name='Pizza',
            field=models.ManyToManyField(blank=True, through='orders.Pizza_with_toppings', to='orders.Pizza'),
        ),
        migrations.AddField(
            model_name='basket',
            name='Salads',
            field=models.ManyToManyField(blank=True, to='orders.Salads'),
        ),
        migrations.AddField(
            model_name='basket',
            name='Subs',
            field=models.ManyToManyField(blank=True, through='orders.Subs_with_add_on', to='orders.Subs'),
        ),
        migrations.AddField(
            model_name='basket',
            name='User',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
