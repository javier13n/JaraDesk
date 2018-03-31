from django.contrib import admin
from apps.desk.models import Profile
from apps.desk.models import Category
from apps.desk.models import Subcategory
from apps.desk.models import Ticket
from apps.desk.models import TicketActivity
from apps.desk.models import TicketState
from apps.desk.models import TicketType

# Register your models here.

admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Ticket)
admin.site.register(TicketActivity)
admin.site.register(TicketState)
admin.site.register(TicketType)
