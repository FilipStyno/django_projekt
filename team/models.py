from django.db import models

class Person(models.Model):
    ROLE_CHOICES = [
        ('player', 'Player'),
        ('trainer', 'Trainer'),
    ]

    name = models.CharField(
        max_length=80,
        verbose_name='First Name',
        help_text='Enter the person\'s first name',
        error_messages={'blank': 'First name is required.'}
    )
    surname = models.CharField(
        max_length=80,
        verbose_name='Surname',
        help_text='Enter the person\'s surname',
        error_messages={'blank': 'Surname is required.'}
    )
    bio = models.TextField(
        verbose_name='Biography',
        help_text="Enter a brief bio or profile of this person",
        blank=True
    )

    date_of_birth = models.DateField(
        verbose_name='Date of Birth',
        help_text='Enter the date of birth (YYYY-MM-DD)',
        null=True, blank=True
    )
    contact = models.CharField(
        max_length=100,
        verbose_name='Contact Info',
        blank=True,
        help_text='Enter phone number or email (optional)'
    )
    picture = models.ImageField(
        upload_to='persons/',
        verbose_name='Photo',
        help_text='Upload a personal photo',
        blank=True, null=True
    )
    role = models.CharField(
        max_length=7,
        choices=ROLE_CHOICES,
        verbose_name='Role',
        help_text='Select if this person is a Player or a Trainer'
    )

    class Meta:
        ordering = ['surname', 'name']
        verbose_name = 'Person'
        verbose_name_plural = 'People'

    def __str__(self):
        return f"{self.name} {self.surname} ({self.get_role_display()})"


class Trainer(models.Model):
    TEAM_ROLE_CHOICES = [
        ('main_coach', 'Main Coach'),
        ('exercise_specialist', 'Exercise Specialist'),
        ('wellness_specialist', 'Wellness Specialist'),
    ]
    person = models.OneToOneField(
        Person,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'trainer'},
        verbose_name='Person',
        help_text='Select the person for this Trainer entry'
    )
    team_role = models.CharField(
        max_length=25,
        choices=TEAM_ROLE_CHOICES,
        verbose_name='Team Role',
        help_text='Select the trainer\'s role in the team'
    )

    class Meta:
        verbose_name = 'Trainer'
        verbose_name_plural = 'Trainers'

    def __str__(self):
        return f"{self.person} - {self.get_team_role_display()}"


class Player(models.Model):
    POSITION_CHOICES = [
        ('gk', 'Goalkeeper'),
        ('df', 'Defender'),
        ('mf', 'Midfielder'),
        ('fw', 'Forward'),
    ]
    person = models.OneToOneField(
        Person,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'player'},
        verbose_name='Person',
        help_text='Select the person for this Player entry'
    )
    position = models.CharField(
        max_length=2,
        choices=POSITION_CHOICES,
        verbose_name='Position',
        help_text='Select the player\'s position'
    )
    dress_number = models.PositiveIntegerField(
        verbose_name='Jersey Number',
        help_text='Enter the jersey number'
    )
    nationality = models.CharField(
        max_length=50,
        verbose_name='Nationality',
        help_text='Enter the player\'s nationality'
    )
    goals = models.PositiveIntegerField(
        verbose_name='Goals Scored',
        default=0,
        help_text='Number of goals scored'
    )
    assists = models.PositiveIntegerField(
        verbose_name='Assists',
        default=0,
        help_text='Number of assists'
    )

    class Meta:
        verbose_name = 'Player'
        verbose_name_plural = 'Players'

    def __str__(self):
        return f"{self.person} - {self.get_position_display()} #{self.dress_number}"


class Injury(models.Model):
    player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        related_name='injuries',
        verbose_name='Player',
        help_text='Select the injured player'
    )
    type_of_injury = models.CharField(
        max_length=100,
        verbose_name='Type of Injury',
        help_text='Describe the injury type'
    )
    date_of_injury = models.DateField(
        verbose_name='Date of Injury',
        help_text='Enter the date the injury occurred'
    )
    expected_return_date = models.DateField(
        verbose_name='Expected Return',
        help_text='Estimated return date',
        blank=True, null=True
    )

    class Meta:
        verbose_name = 'Injury'
        verbose_name_plural = 'Injuries'
        ordering = ['-date_of_injury']

    def __str__(self):
        return f"{self.type_of_injury} ({self.date_of_injury}) - {self.player}"