# Generated by Django 2.2.28 on 2024-08-02 20:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('reciever', models.CharField(max_length=256)),
                ('due_date', models.IntegerField()),
                ('period_type', models.CharField(max_length=128)),
                ('period_covered', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='household',
            name='lead_resident',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='household',
            name='max_residents',
            field=models.IntegerField(default=100),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, upload_to='profile_images')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Resident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('household', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Household')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=256)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Bill')),
                ('household', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Household')),
            ],
        ),
        migrations.AddField(
            model_name='bill',
            name='household',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Household'),
        ),
    ]
