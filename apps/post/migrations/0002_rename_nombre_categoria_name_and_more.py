# Generated by Django 5.1.1 on 2024-10-11 21:51

import apps.post.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoria',
            old_name='nombre',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='contenido',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='fecha_creacion',
            new_name='publish_date',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='usuario',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='categoria',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='contenido',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='fecha_publicacion',
            new_name='publish_date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='titulo',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='fecha_actualizacion',
            new_name='update_date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='usuario',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='post',
            name='miniatura',
        ),
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to='post/thumbnail', validators=[apps.post.models.validar_extension]),
        ),
    ]
