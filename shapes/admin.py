from django.contrib import admin

# Register your models here.
from .models import Profile, FacebookSession, FacebookSessionError, Collection,Collection_Individual, User_Collection

admin.site.register(Profile)
admin.site.register(FacebookSession)
admin.site.register(FacebookSessionError)
admin.site.register(Collection)
admin.site.register(Collection_Individual)
admin.site.register(User_Collection)
