from django.contrib import admin

from django.contrib import admin
from .models import Person

from django.contrib import admin
from .models import Person, Player, Trainer, Injury

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'role', 'date_of_birth')
    search_fields = ('name', 'surname')
    list_filter = ('role',)
    # You can add more customizations here if you like

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('person', 'position', 'dress_number', 'nationality', 'goals', 'assists')
    search_fields = ('person__name', 'person__surname', 'nationality')
    list_filter = ('position',)

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('person', 'team_role')
    search_fields = ('person__name', 'person__surname')
    list_filter = ('team_role',)

@admin.register(Injury)
class InjuryAdmin(admin.ModelAdmin):
    list_display = ('player', 'type_of_injury', 'date_of_injury', 'expected_return_date')
    search_fields = ('type_of_injury',)
    list_filter = ('date_of_injury',)