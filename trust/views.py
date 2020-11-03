from django.shortcuts import render, redirect
from django.views.generic import View
# Create your views here.
from . import models
from django.contrib import messages
from . import mailHandler


class HomePage(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'index.html')


class AboutPage(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'about.html')


class ContactPage(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'contact.html')

    def post(self, request, *args, **kwargs):
        form = request.POST
        name = form.get('name')
        email = form.get('email')
        message = form.get('message')

        new_contact = models.Contact.objects.create(
                    name = name,
                    email = email,
                    message=message,

                )

        new_contact.save()
        mailHandler.sendMailToContactPerson(name, email)
        mailHandler.sendMailToTravancoreContact(name, email, message)
        # messages.success(request, "Your volunteer form details has been successfully submitted. We will get back to you soon.")
        return render(request, 'index.html')


class FundraisPage(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'fundraising.html')


class VolunteerPage(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'volunteer.html')

    def post(self, request, *args, **kwargs):
        form = request.POST
        name = form.get('name')
        email = form.get('email')
        gender = form.get('gender')
        contact = form.get('contact')
        occupation = form.get('occupation')
        city = form.get('city')
        zipcode = form.get('zipcode')
        reason = form.get('reason')

        new_volunteer = models.Volunteer.objects.create(
                    name=name,
                    email=email,
                    gender=gender,
                    contact=contact,
                    occupation=occupation,
                    city=city,
                    zipcode=zipcode,
                    reason=reason,
                )


        new_volunteer.save()
        mailHandler.sendMailToVolunteer(name, email)
        mailHandler.sendMailToTravancoreVolunteer(name, email, contact)
        messages.success(request, "Your volunteer form details has been successfully submitted. We will get back to you soon.")
        return render(request, 'index.html')


class ProjectPage(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'project.html')

class EventPage(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'events.html')


class DonatePage(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'donate.html')


    def post(self, request, *args, **kwargs):
        form = request.POST
        if "submit1" in form:

            fname = form.get('fname')
            lname = form.get('lname')
            email = form.get('email')
            gender = form.get('gender')
            contact = form.get('contact')
            occupation = form.get('occupation')
            city = form.get('city')
            zipcode = form.get('zipcode')
            type = form.get('type')
            amount = None
            if type == "Money":
                amount = form.get('amount')

            new_reg_donater = models.Regulardonation.objects.create(
                        fname=fname,
                        lname=lname,
                        email=email,
                        gender=gender,
                        contact=contact,
                        occupation=occupation,
                        city=city,
                        zipcode=zipcode,
                        type=type,
                        amount=amount,

                    )

            mailHandler.sendMailToRegularDonator(fname, amount, email)
            mailHandler.sendMailToTravancoreRegularDonation(fname, lname, email, gender, contact, occupation, city, zipcode, type, amount)
            messages.success(request, "Your volunteer form details has been successfully submitted. We will get back to you soon.")
            return render(request, 'index.html')

            # Anonymous Donation
        elif "submit2" in form:
            zipcode = form.get('zipcode')
            type = form.get('type')
            amount = form.get('amount')

            new_anony_donater = models.Anonymousdonation.objects.create(
                        zipcode=zipcode,
                        type=type,
                        amount=amount,

                    )

            mailHandler.sendMailToTravancoreIrregularDonation(zipcode, amount, type)
            messages.success(request, "Your volunteer form details has been successfully submitted. We will get back to you soon.")
            return render(request, 'index.html')
