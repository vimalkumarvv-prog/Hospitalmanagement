# Generated by Django 5.1.4 on 2025-01-25 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0025_alter_appointment_appointmentdate_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='appointment',
            unique_together={('doctorId', 'appointmentDate', 'appointmentTime')},
        ),
    ]
