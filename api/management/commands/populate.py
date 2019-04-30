from django.core.management.base import BaseCommand, CommandError

from api.models import Lesson, Subject, User


class Command(BaseCommand):
    help = "Populate the DB with data"
    # TODO: Allow setting locale to fetch country names in right locale
    # https://code.djangoproject.com/ticket/6376

    def handle(self, *args, **options):
        if User.objects.exists():

            Subject.objects.create(name="Science")
            Subject.objects.create(name="Math")
            Subject.objects.create(name="Language")

            Lesson.objects.create(
                title="Science A",
                content="Some content for Science A",
                author=User.objects.get(pk=1),
                summary="some summary for title A",
                subject=Subject.objects.get(pk=1),
                grade=4,
                tags="these,are,tags",
            )

            Lesson.objects.create(
                title="Science B",
                content="Some content for Science A",
                author=User.objects.get(pk=1),
                summary="some summary for title A",
                subject=Subject.objects.get(pk=1),
                grade=4,
                tags="these,are,tags",
            )

            Lesson.objects.create(
                title="Science C",
                content="Some content for Science A",
                author=User.objects.get(pk=1),
                summary="some summary for title A",
                subject=Subject.objects.get(pk=1),
                grade=4,
                tags="these,are,tags",
            )

            # Country.objects.bulk_create(countries)
            self.stdout.write("Successfully updated %s lessons." % 1)
        else:
            raise CommandError(
                'You have no users in your database.')