# Generated by Django 2.2.17 on 2021-02-08 14:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('create_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newsId', models.IntegerField(null=True, verbose_name='newsId')),
                ('author', models.CharField(max_length=256, null=True)),
                ('title', models.CharField(max_length=256, null=True)),
                ('description', models.CharField(blank=True, max_length=512, null=True)),
                ('newsImage', models.ImageField(default=False, upload_to='')),
                ('publishedAt', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('create_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('content', models.TextField()),
                ('create_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=20, unique=True)),
                ('stock_code', models.CharField(max_length=20, null=True)),
                ('stock_type', models.CharField(max_length=20, null=True)),
                ('open', models.FloatField(blank=True, null=True)),
                ('high', models.FloatField(blank=True, null=True)),
                ('low', models.FloatField(blank=True, null=True)),
                ('close', models.FloatField(blank=True, null=True)),
                ('adj_close', models.FloatField(blank=True, null=True)),
                ('volume', models.IntegerField(blank=True, null=True)),
                ('before_close', models.FloatField(blank=True, null=True)),
                ('increase', models.FloatField(blank=True, null=True)),
                ('decrease', models.FloatField(blank=True, null=True)),
                ('fluctuation_width', models.FloatField(blank=True, null=True)),
                ('bookmarked', models.BooleanField(default=False)),
                ('chart_image', models.ImageField(default=False, upload_to='')),
                ('last_pattern', models.CharField(blank=True, max_length=50)),
                ('increase_or_decrease', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Stocks',
        ),
        migrations.AddField(
            model_name='user',
            name='mail_alarm_time_hour',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='mail_alarm_time_minute',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='question',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bookmark',
            name='stock',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stock.Stock'),
        ),
        migrations.AddField(
            model_name='bookmark',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Question'),
        ),
    ]
