# Generated by Django 3.2.16 on 2023-12-06 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_subscription_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='comment',
            field=models.CharField(db_index=True, default='', max_length=50),
        ),
    ]
