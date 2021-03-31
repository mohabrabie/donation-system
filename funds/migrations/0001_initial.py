# Generated by Django 3.1.7 on 2021-03-30 00:21

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=100)),
                ('is_featured', models.BooleanField(default=False)),
                ('categories', models.ManyToManyField(to='funds.Category')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectPicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('project', models.ForeignKey(on_delete=django.db.models.fields.NOT_PROVIDED, to='funds.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.fields.NOT_PROVIDED, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report', models.CharField(max_length=100)),
                ('project', models.ForeignKey(on_delete=django.db.models.fields.NOT_PROVIDED, to='funds.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.fields.NOT_PROVIDED, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='pictures',
            field=models.ManyToManyField(to='funds.ProjectPicture'),
        ),
        migrations.AddField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(to='funds.Tag'),
        ),
        migrations.AddField(
            model_name='project',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.fields.NOT_PROVIDED, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donation', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('project', models.ForeignKey(on_delete=django.db.models.fields.NOT_PROVIDED, to='funds.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.fields.NOT_PROVIDED, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommentReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report', models.CharField(max_length=100)),
                ('comment', models.ForeignKey(on_delete=django.db.models.fields.NOT_PROVIDED, to='funds.comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.fields.NOT_PROVIDED, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.fields.NOT_PROVIDED, to='funds.project'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.fields.NOT_PROVIDED, to=settings.AUTH_USER_MODEL),
        ),
    ]