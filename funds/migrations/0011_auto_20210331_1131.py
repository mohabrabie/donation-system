# Generated by Django 3.1.7 on 2021-03-31 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funds', '0010_auto_20210331_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectpicture',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='funds.project'),
        ),
    ]
