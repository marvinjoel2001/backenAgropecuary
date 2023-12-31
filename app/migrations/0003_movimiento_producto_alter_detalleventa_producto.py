# Generated by Django 4.1.3 on 2023-07-04 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_movimiento_tipo_alter_producto_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='movimiento',
            name='producto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.producto'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='detalleventa',
            name='producto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.producto'),
        ),
    ]
