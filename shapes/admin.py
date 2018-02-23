from django.contrib import admin

# Register your models here.
from .models import Profile, FacebookSession, FacebookSessionError, Collection,Collection_Individual, User_Collection

admin.site.register(Profile,
                    FacebookSession,
                    FacebookSessionError,
                    Collection,
                    Collection_Individual,
                    User_Collection)
