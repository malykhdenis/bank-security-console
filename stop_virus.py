import argparse
import datetime
import os
import django
from django.shortcuts import get_object_or_404
from tabulate import tabulate

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from datacenter.models import Passcard, Visit


def get_virus_passcards(name, date):
    """Create table with passcards, which contacted with virus."""
    patient = get_object_or_404(Passcard, owner_name=name)
    first_date = datetime.date.fromisoformat(date) - datetime.timedelta(7)
    danger_visits = (
        Visit.objects.filter(passcard=patient)
        .filter(entered_at__date__gte=first_date)
        .filter(entered_at__date__lte=date)
    )
    result = []
    for danger_visit in danger_visits:
        possible_virus_visits = (
            Visit.objects.exclude(passcard=patient)
            .filter(entered_at__gte=danger_visit.entered_at)
            .filter(entered_at__lte=danger_visit.leaved_at)
            .select_related('passcard')
        )
        for possible_virus_visit in possible_virus_visits:
            result.append(
                [possible_virus_visit.entered_at.date(),
                 possible_virus_visit.passcard.owner_name]
            )
    headers = ["date", "name"]
    print(tabulate(result, headers, tablefmt='psql'))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Create table with passcards, which contacted with virus.'
    )
    parser.add_argument('-p', '--patient', help="patient's name")
    parser.add_argument('-d', '--date', help='date of illness')
    args = parser.parse_args()
    get_virus_passcards(args.patient, args.date)
