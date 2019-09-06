# Generated by Django 2.2.5 on 2019-09-06 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paint', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cv', models.TextField(blank=True, default='')),
                ('statement', models.TextField(blank=True, default='')),
                ('contact_text', models.TextField(blank=True, default='')),
                ('home_repetitive_image', models.ImageField(blank=True, upload_to='')),
            ],
            options={
                'verbose_name_plural': 'Info',
            },
        ),
        migrations.CreateModel(
            name='Technique',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='paint',
            name='technique',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='paint.Technique'),
        ),
    ]