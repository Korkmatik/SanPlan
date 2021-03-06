from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .controllers import EventController


class IndexView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request,
                      'events/index.html',
                      {
                          'event': EventController.get_events(),
                          'home': True,
                      })


class EventsView(LoginRequiredMixin, View):

    def get(self, request, id):
        event = EventController.get_event_by_id(id)
        return render(request,
                      'events/detail.html',
                      {
                          'event': event,
                          'from': event.get_from_date_time(),
                          'to': event.get_to_date_time(),
                          'address': event.get_address(),
                      })
