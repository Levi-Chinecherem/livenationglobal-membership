# Generated by Django 4.2.4 on 2023-12-27 20:19

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('email_app', '0002_emailinfo_purpose'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailinfo',
            name='message_content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]