# Generated by Django 5.1.4 on 2024-12-19 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store_pdf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_file', models.FileField(null=True, upload_to='uploads/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
