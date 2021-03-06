# Generated by Django 3.0.6 on 2020-07-25 00:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allergen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Snack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qrcode', models.BigIntegerField(null=True)),
                ('description', models.CharField(max_length=600, null=True)),
                ('name', models.CharField(max_length=64, null=True)),
                ('origName', models.CharField(max_length=64, null=True)),
                ('origCountry', models.CharField(max_length=64, null=True)),
                ('whereToBuy', models.CharField(max_length=800, null=True)),
                ('calories', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200, null=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('password', models.CharField(max_length=48, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='View',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('ofitem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.Snack')),
                ('viewBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.User')),
            ],
        ),
        migrations.CreateModel(
            name='SnackCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ctg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.Category')),
                ('snack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.Snack')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=500)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('ofitem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.Snack')),
                ('ratedby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.User')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('ofitem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.Snack')),
                ('ratedby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.User')),
            ],
        ),
        migrations.CreateModel(
            name='CollectionEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.Collection')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.Snack')),
            ],
        ),
        migrations.AddField(
            model_name='collection',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.User'),
        ),
        migrations.CreateModel(
            name='AllergyProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hasit', models.BooleanField()),
                ('confirmed', models.BooleanField()),
                ('allergen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.Allergen')),
                ('snack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.Snack')),
            ],
        ),
    ]
