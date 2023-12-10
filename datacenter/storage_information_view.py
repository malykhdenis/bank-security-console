from django.shortcuts import render

from datacenter.models import Visit


def storage_information_view(request):
    active_visits = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits = []
    for visit in active_visits:
        non_closed_visits.append(
            {
                'who_entered': visit.passcard.owner_name,
                'entered_at': visit.entered_at,
                'duration': format_duration(visit.get_duration()),
                'is_strange': visit.is_visit_long(),
            }
        )
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)


def format_duration(duration):
    """Convert to timedelta objects to hours, minutes, seconds."""
    days, seconds = duration.days, duration.seconds
    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = (seconds % 60)
    return f'{hours}:{minutes}:{seconds}'
