import os
import csv

from django.core.management.base import BaseCommand, CommandError
from django.apps import apps

from api.models import User, Subject


class Command(BaseCommand):
    args = 'Model.csv'
    help = 'Import `Model`.csv into `Model` database.'

    def handle(self, *args, **options):
        # if len(args) != 1:
        #     raise CommandError("Invalid Invocation. See help.")

        csvPath = "/Users/ross/Desktop/wattba/Lesson.csv"
        if not os.path.exists(csvPath):
            raise CommandError("%s doesnt exist." %csvPath)

        model, _ = os.path.splitext(os.path.basename(csvPath))
        Model = apps.get_model("api", model.title())
        if not Model:
            raise CommandError("%s Model doesn't exist'")

        model_fields = [f.name for f in Model._meta.fields]
        fields_name = []

        with open(csvPath, 'rb') as csvFile:
            reader = csv.reader(csvFile, delimiter=',', quotechar="\"")
            fields_name = str(next(reader))
            for i, _ in enumerate(fields_name):
                fields_name[i] = fields_name[i].lower()
                fields_name[i] = fields_name[i].replace(' ', '_')
                if not fields_name[i] in model_fields:
                    raise CommandError("%s field doesn't exists in %s Model" %(fields_name[i], Model))

            for row in reader:
                try:
                    obj = Model()
                    for i, field in enumerate(row):
                        fname = fields_name[i]
                        if fname == "subject":
                            setattr(obj, fname, Subject.objects.filter(name__iexact=field))
                        else:
                            setattr(obj, fname, field)
                    setattr(obj, "author", User.objects.get(pk=1))
                    obj.save()
                except Exception as e:
                    raise CommandError(e)
