from django.contrib import admin

from .models import Word, Language, UserLanguage

admin.site.register([Word, Language, UserLanguage])
