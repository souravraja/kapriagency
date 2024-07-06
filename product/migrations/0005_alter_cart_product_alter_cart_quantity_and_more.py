# Generated by Django 4.2.13 on 2024-07-06 05:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("product", "0004_orderplaced"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cart",
            name="Product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="product.product"
            ),
        ),
        migrations.AlterField(
            model_name="cart",
            name="quantity",
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name="cart",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
