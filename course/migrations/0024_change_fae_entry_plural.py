from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0023_misc_tweaks'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='flowaccessexceptionentry',
            options={'verbose_name_plural': 'flow access exception entries'},
        ),
    ]
