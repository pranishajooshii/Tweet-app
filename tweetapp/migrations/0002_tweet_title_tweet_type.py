# Generated by Django 5.2 on 2025-04-05 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweetapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='title',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tweet',
            name='type',
            field=models.CharField(choices=[('education', 'Education'), ('technology', 'Technology'), ('health', 'Health')], default='education', max_length=50),
        ),
    ]
