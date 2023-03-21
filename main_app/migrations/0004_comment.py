# Generated by Django 4.1.7 on 2023-03-21 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_report_agency'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=250)),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.report')),
            ],
        ),
    ]
