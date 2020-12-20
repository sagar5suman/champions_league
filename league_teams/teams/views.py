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
    
    clubs = set()
    
    for k, v in qualifiers.items():
        club = Club(name=k, state=v.get('state'), is_super_qualifier=v.get('is_super_qualifier'))
        club.save()
        clubs.add(club)

    return clubs

# Create your views here.
def index(request):
    clubs = Club.objects.filter(group='Unknown')
    if clubs.count() != 32:
        clubs.delete()
        clubs = create_models_and_save_data_in_db()
    return render(request, 'teams/index.html', {'clubs': sample(set(clubs), 32)})

def teams(request):
    clubs = Club.objects.filter(group='Unknown')
    if clubs.count() != 32:
        clubs.delete()
        create_models_and_save_data_in_db()

    super_qualifiers = sample(set(Club.objects.filter(is_super_qualifier=True, group='Unknown')), 8)
    grp = {}
    for i, j in enumerate(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']):
        super_qualifiers[i].group = f'GROUP {j}'
        grp[f'GROUP {j}'] = [super_qualifiers[i]]
        super_qualifiers[i].save()

    qualifiers = sample(set(Club.objects.filter(is_super_qualifier=False, group='Unknown')), 24)
    while qualifiers != []:
        for k, v in grp.items():
            for qualifier in qualifiers:
                if all(qualifier.state != c.state for c in v) and len(v) < 4:
                    qualifier.group = k
                    v.append(qualifier)
                    qualifiers.remove(qualifier)
                    qualifier.save()
                if len(v) == 4:
                    break
    
    list_of_groups = [
        [{'GROUP A': grp.get('GROUP A')}, {'GROUP B': grp.get('GROUP B')}, {'GROUP C': grp.get('GROUP C')}, {'GROUP D': grp.get('GROUP D')}],
        [{'GROUP E': grp.get('GROUP E')}, {'GROUP F': grp.get('GROUP F')}, {'GROUP G': grp.get('GROUP G')}, {'GROUP H': grp.get('GROUP H')}],
    ]
    return render(request, 'teams/teams.html', {'list_of_groups': list_of_groups})