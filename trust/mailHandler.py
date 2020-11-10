from django.core.mail import send_mail
import environ

env = environ.Env()
# reading .env file
environ.Env.read_env()

# Volunteer

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

# Regular Donator

def sendMailToRegularDonator(fname, amount, send_to):
    subject = "Regarding Donation in The Travancore Charitable Trust"
    message = "Hello "+fname+"! \n\nWe have successfully received your donation request.\nWe are glad that you have decided to help some innocent and poor souls. \n\n Thank You for your graet contibution.\n\nWe have received Amount: "+str(amount)+" from you.\n\nRegards\n-The Travancore Trust"
    send_mail(
        subject,
        message,
        env("EMAIL"),
        [send_to],
        fail_silently = False,
    )

def sendMailToTravancoreRegularDonation(fname, lname, email, gender, contact, occupation, city, zipcode, type):
    if type == "Money":
        message = "The amount of "+amount+" has been received on our website regarding Donation by:\n\nFirst Name: "+fname+"\nLast Name: "+lname+"\nEmail Id: "+email+"\nGender: "+gender+"\nPhone Number: "+contact+"\nOccupation: "+occupation+"\nCity: "+city+"\nZipcode: "+zipcode+"\nType: "+type+"\nAmount: "+amount+"\nRegards"
        subject = "A amount has been received on Travancore Charitable Trust"
        send_mail(
            subject,
            message,
            env("EMAIL"),
            ['parmarnaitik0909@gmail.com'],
            fail_silently = False,

        )

    else:
        message = "We have received a donation of Type: "+type+"\n\nFirst Name: "+fname+"\nLast Name: "+lname+"\nEmail Id: "+email+"\nGender: "+gender+"\nPhone Number: "+contact+"\nOccupation: "+occupation+"\nCity: "+city+"\nZipcode: "+zipcode+"\nType: "+type+"\n\nRegards"
        subject = "A amount has been received on Travancore Charitable Trust"
        send_mail(
            subject,
            message,
            env("EMAIL"),
            ['parmarnaitik0909@gmail.com'],
            fail_silently = False,

        )



# Anonymous Donator


def sendMailToTravancoreIrregularDonation(zipcode, amount, type):
    if type == "Money":

        message = "The amount of "+amount+" has been received on our website regarding Donation by:\n\nName: "+name+"\nEmail Id: "+email+"\nPhone Number: "+phone+"\n\n\nRegards"
        subject = "A amount has been received on Travancore Charitable Trust"
        send_mail(
            subject,
            message,
            env("EMAIL"),
            ['parmarnaitik0909@gmail.com'],
            fail_silently = False,

        )

    else:
        message = "We have received a donation of Type: "+type+"\nZipcode: "+zipcode+"\n\nRegards"
        subject = "A amount has been received on Travancore Charitable Trust"
        send_mail(
            subject,
            message,
            env("EMAIL"),
            ['parmarnaitik0909@gmail.com'],
            fail_silently = False,
        )




    # Contact

def sendMailToContactPerson(name, send_to):
    subject = "Thanks for contacting us"
    message = "Hello "+name+"! \n\nWe have successfully received your message.\n\nWe will get back to you as soon as possible.\n\nRegards\n-The Travancore Charitable Trust"
    try:
        send_mail(
            subject,
            message,
            env("EMAIL"),
            [send_to],
            fail_silently = False,
        )
    except:
        print("EMAIL NOT SENT")


def sendMailToTravancoreContact(name, email, message):
    message = "A new message has been received on our website:\n\nName: "+name+"\nEmail Id: "+email+"\nMessage: "+message+"\n\n\nRegards"
    subject = "A message has been received on Travancore Charitable Trust"
    send_mail(
        subject,
        message,
        env("EMAIL"),
        ['parmarnaitik0909@gmail.com'],
        fail_silently = False,

    )
