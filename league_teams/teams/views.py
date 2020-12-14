from django.shortcuts import render
from .models import Club
from random import sample

# Create your views here.
def index(request):
    clubs = Club.objects.all()
    if clubs.count() != 0:
        clubs.delete()
    
    super_qualifiers = {
        'Striking Sharpshooters': 'Delhi',
        'Blue Bombers': 'Haryana',
        'Blue Geckos': 'Madhya Pradesh',
        'Midnight Miners': 'Uttar Pradesh',
        'Alpha Blockers': 'Rajasthan',
        'Tornado Geckos': 'Punjab',
        'Muffin Racers': 'Maharashtra',
        'Black & White Gangstaz': 'Andra Pradesh',
    }
    
    qualifiers = {
        'Rhino Hurricanes': 'Uttar Pradesh',
        'Midnight Stars': 'J&K',
        'Rocky Assassins': 'Delhi',
        'Skull Fireballs': 'Goa',
        'Spirit Blockers': 'Andra Pradesh',
        'Wind Kamikaze Pilots': 'Kerala',
        'Retro Chuckers': 'Uttarakhand',
        'Venomous Cyborgs': 'West Bengal',
        'Quicksilver Ninjas': 'Sikkim',
        'Retro Heroes': 'Haryana',
        'Lions': 'Punjab',
        'Raging Spanners': 'Himachal Pradesh',
        'Poison Spiders': 'Odisha',
        'Black Bullets': 'Uttar Pradesh',
        'Thunder Commandos': 'Uttar Pradesh',
        'Venomous Sharks': 'Haryana',
        'Killer Stars': 'Nagaland',
        'Knockout Busters': 'Madhya Pradesh',
        'Real Madrid': 'Delhi',
        'Demolition Piledrivers': 'Rajasthan',
        'Flying Xpress': 'Delhi',
        'Silver Wasps': 'Uttarakhand',
        'The Showstoppers': 'Delhi',
        'Wolfsburg': 'Haryana',
    }

    for k, v in super_qualifiers.items():
        club = Club(name=k, state=v, is_super_qualifier=True)
        club.save()
    
    for k, v in qualifiers.items():
        club = Club(name=k, state=v)
        club.save()
    
    return render(request, 'teams/index.html', {'clubs': Club.objects.all()})

def teams(request):
    clubs = Club.objects.all()
    if clubs.count() == 0:
        super_qualifiers = {
            'Striking Sharpshooters': 'Delhi',
            'Blue Bombers': 'Haryana',
            'Blue Geckos': 'Madhya Pradesh',
            'Midnight Miners': 'Uttar Pradesh',
            'Alpha Blockers': 'Rajasthan',
            'Tornado Geckos': 'Punjab',
            'Muffin Racers': 'Maharashtra',
            'Black & White Gangstaz': 'Andra Pradesh',
        }
        
        qualifiers = {
            'Rhino Hurricanes': 'Uttar Pradesh',
            'Midnight Stars': 'J&K',
            'Rocky Assassins': 'Delhi',
            'Skull Fireballs': 'Goa',
            'Spirit Blockers': 'Andra Pradesh',
            'Wind Kamikaze Pilots': 'Kerala',
            'Retro Chuckers': 'Uttarakhand',
            'Venomous Cyborgs': 'West Bengal',
            'Quicksilver Ninjas': 'Sikkim',
            'Retro Heroes': 'Haryana',
            'Lions': 'Punjab',
            'Raging Spanners': 'Himachal Pradesh',
            'Poison Spiders': 'Odisha',
            'Black Bullets': 'Uttar Pradesh',
            'Thunder Commandos': 'Uttar Pradesh',
            'Venomous Sharks': 'Haryana',
            'Killer Stars': 'Nagaland',
            'Knockout Busters': 'Madhya Pradesh',
            'Real Madrid': 'Delhi',
            'Demolition Piledrivers': 'Rajasthan',
            'Flying Xpress': 'Delhi',
            'Silver Wasps': 'Uttarakhand',
            'The Showstoppers': 'Delhi',
            'Wolfsburg': 'Haryana',
        }

        for k, v in super_qualifiers.items():
            club = Club(name=k, state=v, is_super_qualifier=True)
            club.save()
        
        for k, v in qualifiers.items():
            club = Club(name=k, state=v)
            club.save()

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