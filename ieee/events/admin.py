from django.contrib import admin
from .models import Event, Agenda, Tag, Image

admin.site.site_header = "Club Admin"
admin.site.site_title = "Club Admin Portal"
admin.site.index_title = "Welcome to Club Portal"
admin.site.register(Event)
admin.site.register(Agenda)
admin.site.register(Tag)
admin.site.register(Image)
