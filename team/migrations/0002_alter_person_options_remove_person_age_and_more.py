# Generated by Django 5.2 on 2025-04-30 11:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['surname', 'name'], 'verbose_name': 'Person', 'verbose_name_plural': 'People'},
        ),
        migrations.RemoveField(
            model_name='person',
            name='age',
        ),
        migrations.AddField(
            model_name='person',
            name='contact',
            field=models.CharField(blank=True, help_text='Enter phone number or email (optional)', max_length=100, verbose_name='Contact Info'),
        ),
        migrations.AddField(
            model_name='person',
            name='date_of_birth',
            field=models.DateField(blank=True, help_text='Enter the date of birth (YYYY-MM-DD)', null=True, verbose_name='Date of Birth'),
        ),
        migrations.AddField(
            model_name='person',
            name='picture',
            field=models.ImageField(blank=True, help_text='Upload a personal photo', null=True, upload_to='persons/', verbose_name='Photo'),
        ),
        migrations.AddField(
            model_name='person',
            name='surname',
            field=models.CharField(default='', error_messages={'blank': 'Surname is required.'}, help_text="Enter the person's surname", max_length=80, verbose_name='Surname'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(error_messages={'blank': 'First name is required.'}, help_text="Enter the person's first name", max_length=80, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='person',
            name='role',
            field=models.CharField(choices=[('player', 'Player'), ('trainer', 'Trainer')], help_text='Select if this person is a Player or a Trainer', max_length=7, verbose_name='Role'),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(choices=[('gk', 'Goalkeeper'), ('df', 'Defender'), ('mf', 'Midfielder'), ('fw', 'Forward')], help_text="Select the player's position", max_length=2, verbose_name='Position')),
                ('dress_number', models.PositiveIntegerField(help_text='Enter the jersey number', verbose_name='Jersey Number')),
                ('nationality', models.CharField(help_text="Enter the player's nationality", max_length=50, verbose_name='Nationality')),
                ('goals', models.PositiveIntegerField(default=0, help_text='Number of goals scored', verbose_name='Goals Scored')),
                ('assists', models.PositiveIntegerField(default=0, help_text='Number of assists', verbose_name='Assists')),
                ('yellow_cards', models.PositiveIntegerField(default=0, help_text='Number of yellow cards received', verbose_name='Yellow Cards')),
                ('red_cards', models.PositiveIntegerField(default=0, help_text='Number of red cards received', verbose_name='Red Cards')),
                ('person', models.OneToOneField(help_text='Select the person for this Player entry', limit_choices_to={'role': 'player'}, on_delete=django.db.models.deletion.CASCADE, to='team.person', verbose_name='Person')),
            ],
            options={
                'verbose_name': 'Player',
                'verbose_name_plural': 'Players',
            },
        ),
        migrations.CreateModel(
            name='Injury',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_injury', models.CharField(help_text='Describe the injury type', max_length=100, verbose_name='Type of Injury')),
                ('date_of_injury', models.DateField(help_text='Enter the date the injury occurred', verbose_name='Date of Injury')),
                ('expected_return_date', models.DateField(blank=True, help_text='Estimated return date', null=True, verbose_name='Expected Return')),
                ('player', models.ForeignKey(help_text='Select the injured player', on_delete=django.db.models.deletion.CASCADE, related_name='injuries', to='team.player', verbose_name='Player')),
            ],
            options={
                'verbose_name': 'Injury',
                'verbose_name_plural': 'Injuries',
                'ordering': ['-date_of_injury'],
            },
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_role', models.CharField(choices=[('main_coach', 'Main Coach'), ('exercise_specialist', 'Exercise Specialist'), ('wellness_specialist', 'Wellness Specialist')], help_text="Select the trainer's role in the team", max_length=25, verbose_name='Team Role')),
                ('person', models.OneToOneField(help_text='Select the person for this Trainer entry', limit_choices_to={'role': 'trainer'}, on_delete=django.db.models.deletion.CASCADE, to='team.person', verbose_name='Person')),
            ],
            options={
                'verbose_name': 'Trainer',
                'verbose_name_plural': 'Trainers',
            },
        ),
    ]
