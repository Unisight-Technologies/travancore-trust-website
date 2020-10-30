from django.shortcuts import render, redirect
from django.views.generic import View
# Create your views here.


class HomePage(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'index.html')


class AboutPage(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'about.html')


class ContactPage(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'contact.html')

class FundraisPage(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'fundraising.html')


class VolunteerPage(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'volunteer.html')

class ProjectPage(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'project.html')

class EventPage(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'events.html')


class DonatePage(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'donate.html')
