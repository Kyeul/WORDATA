# Generated by Django 2.2.3 on 2019-10-19 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis_text', '0007_auto_20191019_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataframe',
            name='meaning',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='dataframe',
            name='numbering',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='dataframe',
            name='part_of_speech',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='dataframe',
            name='word',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='dataframe',
            name='word_of_frequency',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='pyeonggawon',
            name='meaning',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='pyeonggawon',
            name='numbering',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='pyeonggawon',
            name='part_of_speech',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='pyeonggawon',
            name='word',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='pyeonggawon',
            name='word_of_frequency',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='suneung',
            name='meaning',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='suneung',
            name='numbering',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='suneung',
            name='part_of_speech',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='suneung',
            name='word',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='suneung',
            name='word_of_frequency',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
