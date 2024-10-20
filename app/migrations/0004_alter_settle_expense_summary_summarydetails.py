# Generated by Django 5.1.1 on 2024-10-10 10:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_profiles_profile'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='settle',
            name='expense',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='app.expenseshare'),
        ),
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owes', models.DecimalField(decimal_places=2, max_digits=10)),
                ('owed', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_spent', models.DecimalField(decimal_places=2, max_digits=10)),
                ('on_self', models.DecimalField(decimal_places=2, max_digits=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SummaryDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.BooleanField(default=False)),
                ('paid_for', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paid_for', to=settings.AUTH_USER_MODEL, verbose_name='Paid For')),
                ('payer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payer', to=settings.AUTH_USER_MODEL, verbose_name='Payer')),
            ],
            options={
                'unique_together': {('payer', 'paid_for')},
            },
        ),
    ]
