from tours.models import RegularTour


def minus_places_count(pk, count):
    try:
        regular = RegularTour.objects.get(id=pk)
        regular.places_count -= count
        regular.save()
        return True
    except RegularTour.DoesNotExist:
        return False