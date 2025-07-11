# Generated by Django 5.2.4 on 2025-07-10 11:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('equipment', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ShooterProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shooting_class', models.CharField(choices=[('Springer', 'Springer'), ('PCP overall', 'PCP overall')], max_length=50)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('pellets', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='equipment.pellets')),
                ('rifle', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='equipment.rifle')),
                ('scope', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='equipment.scope')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
