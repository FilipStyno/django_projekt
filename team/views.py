
from django.shortcuts import render, get_object_or_404
from .models import Person, Player, Trainer, Injury

def home(request):
    total_players = Player.objects.count()
    total_trainers = Trainer.objects.count()
    injuries = Injury.objects.select_related('player__person').order_by('-date_of_injury')[:5]  # 5 latest injuries
    last_update = Injury.objects.order_by('-date_of_injury').first()
    context = {
        'total_players': total_players,
        'total_trainers': total_trainers,
        'injuries': injuries,
        'last_update': last_update.date_of_injury if last_update else None,
    }
    return render(request, 'team/home.html', context)
def player_list(request):
    keepers = Player.objects.filter(position='gk').select_related('person').order_by('person__surname')
    defenders = Player.objects.filter(position='df').select_related('person').order_by('person__surname')
    midfielders = Player.objects.filter(position='mf').select_related('person').order_by('person__surname')
    forwards = Player.objects.filter(position='fw').select_related('person').order_by('person__surname')
    return render(request, 'team/player_list.html', {
        'keepers': keepers,
        'defenders': defenders,
        'midfielders': midfielders,
        'forwards': forwards,
    })

def trainer_list(request):
    trainers = Trainer.objects.select_related('person').all()
    return render(request, 'team/trainer_list.html', {'trainers': trainers})

def person_detail(request, pk):
    person = get_object_or_404(Person, pk=pk)
    # Try to get linked Player or Trainer
    try:
        player = person.player
    except Player.DoesNotExist:
        player = None
    try:
        trainer = person.trainer
    except Trainer.DoesNotExist:
        trainer = None
    # Injuries (if a player)
    injuries = player.injuries.all() if player else []
    context = {
        "person": person,
        "player": player,
        "trainer": trainer,
        "injuries": injuries,
    }
    return render(request, 'team/person_detail.html', context)