# Generated by Django 2.2.16 on 2020-09-17 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        # this is just here to ensure that feature models correctly refer to identities
        # models as identities. instead of environments.
        # there is still some pain with rolling feature migrations backwards but
        # hopefully this won't be required
        ('features', '0023_auto_20200717_1515')
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.CreateModel(
                    name='Identity',
                    fields=[
                        ('id', models.AutoField(auto_created=True, primary_key=True,
                                                serialize=False, verbose_name='ID')),
                        ('identifier', models.CharField(max_length=2000)),
                        ('created_date', models.DateTimeField(auto_now_add=True,
                                                              verbose_name='DateCreated')),
                        ('environment',
                         models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                           related_name='identities',
                                           to='environments.Environment')),
                    ],
                    options={
                        'verbose_name_plural': 'Identities',
                        'db_table': 'environments_identity',
                        'ordering': ['id'],
                        'unique_together': {('environment', 'identifier')},
                    },
                ),
            ],
            database_operations=[]
        )
    ]
