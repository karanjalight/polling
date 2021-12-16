# Generated by Django 4.0 on 2021-12-15 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('pollsapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='total_vote',
            field=models.IntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='choice',
            name='vote',
            field=models.IntegerField(default=0, editable=False),
        ),
        migrations.CreateModel(
            name='ControlVote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pollsapp.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
