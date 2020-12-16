from django.shortcuts import render
from .models import Club
from random import sample

def create_models_and_save_data_in_db():
    qualifiers = {
        'Striking Sharpshooters': {'state': 'Delhi', 'is_super_qualifier': True},
        'Blue Bombers': {'state': 'Haryana', 'is_super_qualifier': True},
        'Blue Geckos': {'state': 'Madhya Pradesh', 'is_super_qualifier': True},
        'Midnight Miners': {'state': 'Uttar Pradesh', 'is_super_qualifier': True},
        'Alpha Blockers': {'state': 'Rajasthan', 'is_super_qualifier': True},
        'Tornado Geckos': {'state': 'Punjab', 'is_super_qualifier': True},
        'Muffin Racers': {'state': 'Maharashtra', 'is_super_qualifier': True},
        'Black & White Gangstaz': {'state': 'Andra Pradesh', 'is_super_qualifier': True},
        'Rhino Hurricanes': {'state': 'Uttar Pradesh', 'is_super_qualifier': False},
        'Midnight Stars': {'state': 'J&K', 'is_super_qualifier': False},
        'Rocky Assassins': {'state': 'Delhi', 'is_super_qualifier': False},
        'Skull Fireballs': {'state': 'Goa', 'is_super_qualifier': False},
        'Spirit Blockers': {'state': 'Andra Pradesh', 'is_super_qualifier': False},
        'Wind Kamikaze Pilots': {'state': 'Kerala', 'is_super_qualifier': False},
        'Retro Chuckers': {'state': 'Uttarakhand', 'is_super_qualifier': False},
        'Venomous Cyborgs': {'state': 'West Bengal', 'is_super_qualifier': False},
        'Quicksilver Ninjas': {'state': 'Sikkim', 'is_super_qualifier': False},
        'Retro Heroes': {'state': 'Haryana', 'is_super_qualifier': False},
        'Lions': {'state': 'Punjab', 'is_super_qualifier': False},
        'Raging Spanners': {'state': 'Himachal Pradesh', 'is_super_qualifier': False},
        'Poison Spiders': {'state': 'Odisha', 'is_super_qualifier': False},
        'Black Bullets': {'state': 'Uttar Pradesh', 'is_super_qualifier': False},
        'Thunder Commandos': {'state': 'Uttar Pradesh', 'is_super_qualifier': False},
        'Venomous Sharks': {'state': 'Haryana', 'is_super_qualifier': False},
        'Killer Stars': {'state': 'Nagaland', 'is_super_qualifier': False},
        'Knockout Busters': {'state': 'Madhya Pradesh', 'is_super_qualifier': False},
        'Real Madrid': {'state': 'Delhi', 'is_super_qualifier': False},
        'Demolition Piledrivers': {'state': 'Rajasthan', 'is_super_qualifier': False},
        'Flying Xpress': {'state': 'Delhi', 'is_super_qualifier': False},
        'Silver Wasps': {'state': 'Uttarakhand', 'is_super_qualifier': False},
        'The Showstoppers': {'state': 'Delhi', 'is_super_qualifier': False},
        'Wolfsburg': {'state': 'Haryana', 'is_super_qualifier': False},
    }

    for k, v in qualifiers.items():
        club = Club(name=k, state=v.get('state'), is_super_qualifier=v.get('is_super_qualifier'))
        club.save()

# Create your views here.
def index(request):
    clubs = Club.objects.all()
    if clubs.count() == 0:
        create_models_and_save_data_in_db()

    return render(request, 'teams/index.html', {'clubs': sample(set(Club.objects.all()), 32)})

def teams(request):
    clubs = Club.objects.all()
    if clubs.count() == 0:
        create_models_and_save_data_in_db()

    super_qualifiers = sample(set(Club.objects.filter(is_super_qualifier=True)), 8)
    group_a = [super_qualifiers[0]]
    group_b = [super_qualifiers[1]]
    group_c = [super_qualifiers[2]]
    group_d = [super_qualifiers[3]]
    group_e = [super_qualifiers[4]]
    group_f = [super_qualifiers[5]]
    group_g = [super_qualifiers[6]]
    group_h = [super_qualifiers[7]]

    qualifiers = sample(set(Club.objects.filter(is_super_qualifier=False)), 24)
    while qualifiers != []:
        for group in group_a, group_b, group_c, group_d, group_e, group_f, group_g, group_h:
            for qualifier in qualifiers:
                if all(qualifier.state != c.state for c in group) and len(group) < 4:
                    group.append(qualifier)
                    qualifiers.remove(qualifier)
                if len(group) == 4:
                    break

    list_of_groups = [
        [{'GROUP A': group_a}, {'GROUP B': group_b}, {'GROUP C': group_c}, {'GROUP D': group_d}],
        [{'GROUP E': group_e}, {'GROUP F': group_f}, {'GROUP G': group_g}, {'GROUP H': group_h}],
    ]
    return render(request, 'teams/teams.html', {'list_of_groups': list_of_groups})