# Generated by Django 4.0.4 on 2022-06-19 00:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_roommember_insession_alter_roommember_uid'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RoomMember',
        ),
    ]
