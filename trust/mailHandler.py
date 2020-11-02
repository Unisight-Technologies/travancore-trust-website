from django.core.mail import send_mail
import environ

env = environ.Env()
# reading .env file
environ.Env.read_env()


def sendMailToVolunteer(name, send_to):
    subject = "Regarding form submission for volunteering in The Travancore Charitable Trust"
    message = "Hello "+name+"! \n\nWe have successfully received all your details of volunteerform.\n\n\We are glad that you are ready to work with our Trust.\n\nWe will get back to you as soon as possible.\n\nRegards\n-The Travancore Trust"
    send_mail(
        subject,
        message,
        env("EMAIL"),
        [send_to],
        fail_silently = False,
    )

def sendMailToDonater(name, amount, send_to):
    subject = "Regarding Donation in The Travancore Charitable Trust"
    message = "Hello "+name+"! \n\nWe have successfully received your donation.\nWe are glad that you have decided to help some innocent and poor souls. \n\n Thank You for your graet contibution.\n\nWe have received "+amount+" from you.\n\nRegards\n-The Travancore Trust"
    send_mail(
        subject,
        message,
        env("EMAIL"),
        [send_to],
        fail_silently = False,
    )

def sendMailToContactPerson(name, email, message):
    subject = "Regarding contact details sent to us"
    message = "Hello "+name+"! \n\nWe have successfully received your details.\n\nName: "+name+"\nEmail Id: "+email+"\nMessage: "+message+"\n\.\n\nWe will get back to you as soon as possible.\n\nRegards\n-The Travancore Charitable Trust"
    send_mail(
        subject,
        message,
        env("EMAIL"),
        [send_to],
        fail_silently = False,
    )


def sendMailToTravancoreVolunteer(name, email, contact):
    message = "The following details has been received on our website regarding Volunteer Form Submission:\n\nName: "+name+"\nEmail Id: "+email+"\Contact: "+contact+"\n\nRegards"
    subject = "A Volunteer Form has been received on Travancore Charitable Trust"
    send_mail(
        subject,
        message,
        env("EMAIL"),
        ['parmarnaitik0909@gmail.com'],
        fail_silently = False,

    )


def sendMailToTravancoreDonation(name, email, contact, amount):
    message = "The amount of "+amount+" has been received on our website regarding Donation by:\n\nName: "+name+"\nEmail Id: "+email+"\nPhone Number: "+phone+"\n\n\nRegards"
    subject = "A amount has been received on Travancore Charitable Trust"
    send_mail(
        subject,
        message,
        env("EMAIL"),
        ['parmarnaitik0909@gmail.com'],
        fail_silently = False,

    )


def sendMailToTravancoreContact(name, email, message):
    message = "The message "+message+" has been received on our website:\n\nName: "+name+"\nEmail Id: "+email+"\nMessage: "+message+"\n\n\nRegards"
    subject = "A message has been received on Travancore Charitable Trust"
    send_mail(
        subject,
        message,
        env("EMAIL"),
        ['parmarnaitik0909@gmail.com'],
        fail_silently = False,

    )
