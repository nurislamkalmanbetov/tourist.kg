# Generated by Django 3.2.9 on 2022-04-07 15:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tours', '0002_auto_20220331_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regulartour',
            name='status',
            field=models.CharField(choices=[('waiting', 'Идет набор'), ('start', 'Начался'), ('completed', 'Завершен'), ('rejected', 'Отменен')], default='waiting', max_length=10, verbose_name='Статус'),
        ),
        migrations.CreateModel(
            name='TourBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_count', models.PositiveSmallIntegerField(verbose_name='Места')),
                ('mobile', models.CharField(max_length=10, verbose_name='Номер телефона')),
                ('status', models.CharField(choices=[('new', 'Новый'), ('confirmed', 'Подтвержден'), ('finished', 'Завершен'), ('rejected', 'Отменен')], default='new', max_length=9, verbose_name='Статус')),
                ('is_paid', models.BooleanField(default=False, verbose_name='Оплачено')),
                ('notice', models.CharField(blank=True, max_length=255, null=True, verbose_name='Доп. Инфо')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('regulat_tour', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tours.regulartour')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Бронирование',
                'verbose_name_plural': 'Бронирования',
                'ordering': ['-created'],
            },
        ),
    ]
