# Generated by Django 3.1.2 on 2021-11-01 19:38

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
            name='Neighbourhood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hood_name', models.CharField(max_length=60)),
                ('hood_location', models.CharField(max_length=60)),
                ('family_size', models.IntegerField()),
                ('pub_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'ordering': ['pub_date'],
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('police_station', models.CharField(blank=True, max_length=60)),
                ('police_no', models.IntegerField(blank=True, verbose_name=10)),
                ('hospital_name', models.CharField(blank=True, max_length=60)),
                ('hospital_no', models.IntegerField(blank=True, verbose_name=10)),
                ('firedpt_name', models.CharField(blank=True, max_length=60)),
                ('firedpt_no', models.IntegerField(blank=True, verbose_name=10)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(null=True)),
                ('profile_photo', models.ImageField(null=True, upload_to='', verbose_name='profile_photo')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('post', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('hood_ref', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='area51.neighbourhood')),
                ('prof_ref', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='area51.profile')),
            ],
            options={
                'ordering': ['pub_date'],
            },
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='prof_ref',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='neighbourhoods', to='area51.profile'),
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biz_name', models.CharField(max_length=60)),
                ('biz_email', models.EmailField(max_length=254)),
                ('biz_description', models.TextField()),
                ('biz_digits', models.IntegerField(null=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('hood_ref', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='businesses', to='area51.neighbourhood')),
            ],
            options={
                'ordering': ['pub_date'],
            },
        ),
    ]
