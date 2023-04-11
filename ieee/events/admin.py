from django.contrib import admin
from .models import Event, Agenda, Tag, Image

admin.site.site_header = "IEEE Admin"
admin.site.site_title = "IEEE Admin Portal"
admin.site.index_title = "Welcome to IEEE Portal"
admin.site.register(Event)
admin.site.register(Agenda)
admin.site.register(Tag)
admin.site.register(Image)
