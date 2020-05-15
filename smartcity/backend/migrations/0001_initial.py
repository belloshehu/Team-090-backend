# Generated by Django 3.0.6 on 2020-05-15 16:31

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('document_required', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('continent', models.CharField(choices=[('Africa', 'Africa'), ('Europe', 'Europe'), ('Asia', 'Asia')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LocalGovernmentArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Country')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceProvider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address1', models.CharField(max_length=100)),
                ('address2', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=100)),
                ('service_rendered', models.CharField(max_length=50)),
                ('picture', models.ImageField(max_length=50, upload_to=None)),
                ('description', models.TextField(max_length=200)),
                ('year_of_experience', models.IntegerField()),
                ('year_of_establishement', models.DateField(default=django.utils.timezone.now)),
                ('supporting_document', models.FileField(upload_to='')),
                ('rating', models.FloatField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Country')),
                ('local_government_are', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.LocalGovernmentArea')),
                ('service_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Category')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.State')),
            ],
        ),
        migrations.AddField(
            model_name='localgovernmentarea',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.State'),
        ),
        migrations.AddField(
            model_name='category',
            name='services',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Service'),
        ),
    ]
