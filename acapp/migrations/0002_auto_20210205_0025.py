# Generated by Django 3.1.5 on 2021-02-04 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='portfolio_site',
        ),
        migrations.RemoveField(
            model_name='member',
            name='profile_pic',
        ),
        migrations.AddField(
            model_name='member',
            name='id_card',
            field=models.CharField(default=212132132214, max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='job_title',
            field=models.CharField(default=323224324, max_length=100),
            preserve_default=False,
        ),
    ]
