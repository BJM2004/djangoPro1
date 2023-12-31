# Generated by Django 4.2.5 on 2023-09-21 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('adress', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Cursus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('color', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_number', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('birth_date', models.DateField(null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('home_phone_number', models.CharField(max_length=20)),
                ('cellphone_number', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=32)),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Trobinoscoop.faculty')),
                ('friends', models.ManyToManyField(to='Trobinoscoop.person')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(null=True)),
                ('publication_date', models.DateField(null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Trobinoscoop.person')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Trobinoscoop.person')),
                ('year', models.IntegerField(null=True)),
                ('cursus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Trobinoscoop.cursus')),
            ],
            bases=('Trobinoscoop.person',),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Trobinoscoop.person')),
                ('office', models.CharField(max_length=30)),
                ('campus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Trobinoscoop.campus')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Trobinoscoop.job')),
            ],
            bases=('Trobinoscoop.person',),
        ),
    ]
