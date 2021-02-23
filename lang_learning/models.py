from django.db import models
from django.contrib.auth.models import User

from db_utils.model_mixins import Timestampable


class Language(Timestampable, models.Model):
    name = models.CharField(max_length=200)
    shortcut = models.CharField(max_length=20)

    def __str__(self):
        return '%s - %s' % (self.shortcut, self.name)


class UserLanguage(Timestampable, models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    @classmethod
    def active(cls, **kwargs):
        return cls.objects.get(is_active=True, **kwargs)

    class Meta:
        unique_together = ('language', 'user')

    def __str__(self):
        return self.language.name


class Word(Timestampable, models.Model):
    name = models.CharField(max_length=50)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)


class UserWord(Timestampable, models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
