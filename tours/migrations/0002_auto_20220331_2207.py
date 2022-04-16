# Generated by Django 3.2.9 on 2022-03-31 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='regulartour',
            options={'ordering': ['-start'], 'verbose_name': 'Регуларный тур', 'verbose_name_plural': 'Регуларный туры'},
        ),
        migrations.RemoveField(
            model_name='regulartour',
            name='placec_count',
        ),
        migrations.AddField(
            model_name='regulartour',
            name='places_count',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='Количество мест'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tour',
            name='title',
            field=models.CharField(default=1, max_length=100, verbose_name='Название'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='regulartour',
            name='status',
            field=models.CharField(choices=[('Идет набор', 'waiting'), ('Начался', 'start'), ('Завершен', 'completed'), ('Отменен', 'rejected')], default='waiting', max_length=10, verbose_name='Статус'),
        ),
    ]
