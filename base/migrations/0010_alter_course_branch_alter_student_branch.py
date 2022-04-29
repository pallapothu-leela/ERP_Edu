# Generated by Django 4.0.3 on 2022-04-29 22:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_rename_u_id_lecturer_e_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.branch'),
        ),
        migrations.AlterField(
            model_name='student',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.branch'),
        ),
    ]
