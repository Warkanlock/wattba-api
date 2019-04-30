from django.core.management.base import BaseCommand, CommandError

from api.models import Lesson, Subject, User


class Command(BaseCommand):
    help = "Populate the DB with data"
    # TODO: Allow setting locale to fetch country names in right locale
    # https://code.djangoproject.com/ticket/6376

    def handle(self, *args, **options):
        if User.objects.exists():

            Subject.objects.create(name="Math")
            Subject.objects.create(name="Sciences")
            Subject.objects.create(name="Technology")
            Subject.objects.create(name="Humanities")
            Subject.objects.create(name="Art")
            Subject.objects.create(name="Engineering")
            Subject.objects.create(name="Languages")
            Subject.objects.create(name="Health")
            Subject.objects.create(name="Accounting")

            Lesson.objects.create(
                title="Science A",
                content="Some content for Science A",
                author=User.objects.get(pk=1),
                summary="some summary for title A",
                subject=Subject.objects.get(pk=1),
                grade=4,
                tags="these,are,zsdf",
                age_range="10 to 12 yrs",
                language="English",
                translation="Available",
                subject_matter="School and Life",
                activity_type="Some ACTIVITY TYPQ",
                duration="4.37 days",
                supplies="Pens, Markers",
                votes="1431",
                rating="5",
            )

            Lesson.objects.create(
                title="Science B",
                content="Some content for Science A",
                author=User.objects.get(pk=1),
                summary="some summary for title A",
                subject=Subject.objects.get(pk=1),
                grade=4,
                tags="these,are,tags",
                age_range="14 - 16yrs",
                language="English",
                translation="Available",
                subject_matter="School and Life",
                activity_type="Some ACTIVITY TYPQ",
                duration="4.37 days",
                supplies="Pens, pencils and thinking caps",
                votes="2321",
                rating="5",
            )

            Lesson.objects.create(
                title="Science C",
                content="Some content for Science A",
                author=User.objects.get(pk=1),
                summary="some summary for title A",
                subject=Subject.objects.get(pk=1),
                grade=4,
                tags="these,are,tags",
                age_range="18 yrs +",
                language="English",
                translation="Available",
                subject_matter="School and Life",
                activity_type="Some ACTIVITY TYPQ",
                duration="4.234 days",
                supplies="asdfasfd, Cokkies",
                votes="123123",
                rating="5",
            )

            # Country.objects.bulk_create(countries)
            self.stdout.write("Successfully updated %s lessons." % 1)
        else:
            raise CommandError(
                'You have no users in your database.')