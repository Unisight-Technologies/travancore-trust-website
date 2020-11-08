from django.contrib import admin

# Register your models here.
from .models import Volunteer, Contact, Regulardonation, Anonymousdonation, Visitors

admin.site.register(Volunteer)
admin.site.register(Contact)
admin.site.register(Regulardonation)
admin.site.register(Anonymousdonation)
admin.site.register(Visitors)
