from .models import Event


class EventController:

    @staticmethod
    def get_events():
        return Event.objects.all()

    @staticmethod
    def get_event_by_id(id):
        return Event.objects.get(id=id)

    @staticmethod
    def get_adresse_by_event_id(id):
        return Event.objects.get(id=id).get_address()
