from django.shortcuts import render, get_object_or_404
from .models import Player, Trainer

def player_list(request):
    players = Player.objects.select_related('person').all()
    return render(request, 'team/player_list.html', {'players': players})

def trainer_list(request):
    trainers = Trainer.objects.select_related('person').all()
    return render(request, 'team/trainer_list.html', {'trainers': trainers})