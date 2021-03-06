from django.core.management.base import BaseCommand
from rooms.models import Facility


class Command(BaseCommand):

    help = "This command creat facilities"

    """     def add_arguments(self, parser):
        parser.add_argument("--times", help="how many i love you")

        """

    def handle(self, *args, **options):
        facilities = [
            "Private enterance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]
        for f in facilities:
            Facility.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS(f"{len(facilities)} facilities created!"))
