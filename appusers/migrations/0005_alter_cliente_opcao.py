# Generated by Django 5.0.3 on 2024-04-08 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appusers', '0004_remove_cliente_phonenumber_alter_cliente_opcao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='opcao',
            field=models.CharField(choices=[('1', 'Diagnóstico'), ('0', 'Serviço'), ('2', 'Compra')], default='0', max_length=11),
        ),
    ]