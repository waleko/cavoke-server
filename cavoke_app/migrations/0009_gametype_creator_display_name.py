# Generated by Django 2.2.4 on 2019-08-22 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cavoke_app', '0008_auto_20190720_1844'),
    ]

    operations = [
        migrations.AddField(
            model_name='gametype',
            name='creator_display_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
