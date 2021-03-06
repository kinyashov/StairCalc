# Generated by Django 2.0.3 on 2018-05-03 08:35

from django.db import migrations, models
import django.db.models.deletion
import stair.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название ограждения/балюстрады')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Цена ограждения/балюстрады')),
            ],
            options={
                'verbose_name': 'Тип ограждения',
                'verbose_name_plural': 'Типы ограждений',
            },
        ),
        migrations.CreateModel(
            name='Height',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min', models.PositiveIntegerField(default=0, verbose_name='минимальное значение')),
                ('slider', stair.fields.SliderField(verbose_name='')),
                ('max', models.PositiveIntegerField(default=10000, verbose_name='максимальное значение')),
                ('step', models.PositiveSmallIntegerField(default=5, verbose_name='шаг диапазона')),
            ],
            options={
                'verbose_name': 'Высота лестницы',
                'verbose_name_plural': 'Высота лестницы',
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название материала')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Цена метериала')),
            ],
            options={
                'verbose_name': 'Материал',
                'verbose_name_plural': 'Материалы',
            },
        ),
        migrations.CreateModel(
            name='MinWidthStep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min', models.PositiveIntegerField(default=0, verbose_name='минимальное значение')),
                ('slider', stair.fields.SliderField(verbose_name='')),
                ('max', models.PositiveIntegerField(default=10000, verbose_name='максимальное значение')),
                ('step', models.PositiveSmallIntegerField(default=5, verbose_name='шаг диапазона')),
            ],
            options={
                'verbose_name': 'Минимальная ширина ступени',
                'verbose_name_plural': 'Минимальная ширина ступени',
            },
        ),
        migrations.CreateModel(
            name='MinWidthTopStep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min', models.PositiveIntegerField(default=0, verbose_name='минимальное значение')),
                ('slider', stair.fields.SliderField(verbose_name='')),
                ('max', models.PositiveIntegerField(default=10000, verbose_name='максимальное значение')),
                ('step', models.PositiveSmallIntegerField(default=5, verbose_name='шаг диапазона')),
            ],
            options={
                'verbose_name': 'Минимальная ширина верхней ступени',
                'verbose_name_plural': 'Минимальная ширина верхней ступени',
            },
        ),
        migrations.CreateModel(
            name='Stair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название лестницы')),
                ('material_stair', models.ManyToManyField(blank=True, to='stair.Material', verbose_name='Доступные материалы')),
            ],
            options={
                'verbose_name': 'Лестница',
                'verbose_name_plural': 'Лестницы',
            },
        ),
        migrations.CreateModel(
            name='Tint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название отделки/тонировки')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Цена отделки/тонировки')),
            ],
            options={
                'verbose_name': 'Окраска/тонировка',
                'verbose_name_plural': 'Окраска/тонировка',
            },
        ),
        migrations.CreateModel(
            name='TrackSupport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название пристенного профиля')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Цена пристенного профиля')),
            ],
            options={
                'verbose_name': 'Пристенный профиль',
                'verbose_name_plural': 'Пристенные профили',
            },
        ),
        migrations.CreateModel(
            name='Turn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название поворота')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Цена поворота')),
            ],
            options={
                'verbose_name': 'Тип поворота',
                'verbose_name_plural': 'Типы поворотов',
            },
        ),
        migrations.CreateModel(
            name='WidthMarsh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min', models.PositiveIntegerField(default=0, verbose_name='минимальное значение')),
                ('slider', stair.fields.SliderField(verbose_name='')),
                ('max', models.PositiveIntegerField(default=10000, verbose_name='максимальное значение')),
                ('step', models.PositiveSmallIntegerField(default=5, verbose_name='шаг диапазона')),
                ('stair', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='stair.Stair')),
            ],
            options={
                'verbose_name': 'Ширина марша',
                'verbose_name_plural': 'Ширина марша',
            },
        ),
        migrations.AddField(
            model_name='stair',
            name='tint',
            field=models.ManyToManyField(blank=True, to='stair.Tint', verbose_name='Варианты отделки'),
        ),
        migrations.AddField(
            model_name='stair',
            name='type_fence',
            field=models.ManyToManyField(blank=True, to='stair.Fence', verbose_name='Варианты ограждений'),
        ),
        migrations.AddField(
            model_name='stair',
            name='type_track_support',
            field=models.ManyToManyField(blank=True, to='stair.TrackSupport', verbose_name='Варианты пристенного профиля'),
        ),
        migrations.AddField(
            model_name='stair',
            name='type_turn',
            field=models.ManyToManyField(blank=True, to='stair.Turn', verbose_name='Варианты поворота'),
        ),
        migrations.AddField(
            model_name='minwidthtopstep',
            name='stair',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='stair.Stair'),
        ),
        migrations.AddField(
            model_name='minwidthstep',
            name='stair',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='stair.Stair'),
        ),
        migrations.AddField(
            model_name='height',
            name='stair',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='stair.Stair'),
        ),
    ]
