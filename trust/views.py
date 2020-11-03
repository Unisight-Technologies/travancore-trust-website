from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
# Create your views here.
from . import models
from django.contrib import messages
from . import mailHandler
from django.http import HttpResponseRedirect, HttpResponse
from trust.paytm import PaytmChecksum
from django.views.decorators.csrf import csrf_exempt

MERCHANT_KEY = 'rX0at#Fkd&gd38w6'
MERCHANT_ID = 'FJqxMp75384358553137'


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
        context = {
        'submitted':True
        }
        mailHandler.sendMailToContactPerson(name, email)
        mailHandler.sendMailToTravancoreContact(name, email, message)
    #    messages.success(request, "Your volunteer form details has been successfully submitted. We will get back to you soon.")
        return render(request, 'index.html', context=context)


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
        # messages.success(request, "Your volunteer form details has been successfully submitted. We will get back to you soon.")

        context = {
        'submitted':True
        }
        return render(request, 'index.html', context=context)


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
            # mailHandler.sendMailToRegularDonator(fname, amount, email)
            # mailHandler.sendMailToTravancoreRegularDonation(fname, lname, email, gender, contact, occupation, city, zipcode, type)
            # messages.success(request, "Your volunteer form details has been successfully submitted. We will get back to you soon.")
            request.session['id'] = new_reg_donater.id

            context = {
            'submitted':True
            }

            return HttpResponseRedirect('/payment/')

            # Anonymous Donation
        elif "submit2" in form:
            zipcode = form.get('zipcode')
            type = form.get('type')
            amount = None
            if type == "Money":
                amount = form.get('amount')

            new_anony_donater = models.Anonymousdonation.objects.create(
                        zipcode=zipcode,
                        type=type,
                        amount=amount,

                    )

            mailHandler.sendMailToTravancoreIrregularDonation(zipcode, amount, type)
            # messages.success(request, "Your volunteer form details has been successfully submitted. We will get back to you soon.")

            context = {
            'submitted':True
            }

            return render(request, 'index.html', context=context)


class PaytmView(TemplateView):
    template_name = 'paytm.html'

def payment_view(request):

    current_donator = models.Regulardonation.objects.get(id=request.session['id'])

    param_dict={
                'MID':MERCHANT_ID,
                'ORDER_ID':str(request.session['id']),
                'TXN_AMOUNT':str(current_donator.amount),
                'CUST_ID':current_donator.email,
                'INDUSTRY_TYPE_ID':'Retail',
                'WEBSITE':'WEBSTAGING',
                'CHANNEL_ID':'WEB',
    	        'CALLBACK_URL':'http://127.0.0.1:8000/handle_request/',
            }

    param_dict['CHECKSUMHASH'] = PaytmChecksum.generateSignature(param_dict, MERCHANT_KEY)
    print(param_dict['CHECKSUMHASH'])
    return render(request, 'paytm.html', {'param_dict':param_dict})

@csrf_exempt 
def handle_request(request):
    # import checksum generation utility

    print("HERE")
    paytmChecksum = ""

# Create a Dictionary from the parameters received in POST
# received_data should contains all data received in POST
    form = request.POST
    paytmParams = {}

    for i in form.keys():
        paytmParams[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]
    # Verify checksum
    # Find your Merchant Key in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys
    isValidChecksum = PaytmChecksum.verifySignature(paytmParams, MERCHANT_KEY, checksum)
    if isValidChecksum:
    	if paytmParams['RESPCODE'] == '01':
            pass

    return render(request, 'payment_status.html', {'response':paytmParams})

def after_payment(request):
    if request.method == "POST":
        if request.POST.get('respcode') == '01':
            context={
                'order_id':request.POST.get('order_id'),
                'response':request.POST.get('response'),
                'txn_amount':request.POST.get('txn_amount'),
                'banktxnid':request.POST.get('bankid')
            }
            return render(request, 'payment-complete.html', context)
