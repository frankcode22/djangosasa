# Generated by Django 5.2.1 on 2025-05-24 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Approval_status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_head', models.CharField(max_length=200)),
                ('approval', models.CharField(max_length=200)),
            ],
        ),
    ]
