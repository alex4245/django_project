from django.db import models
from django.contrib.auth.models import User


class Language(models.Model):
    name = models.CharField(max_length=200)
    shortcut = models.CharField(max_length=20)

    def __str__(self):
        return '%s - %s' % (self.shortcut, self.name)


class Word(models.Model):
    name = models.CharField(max_length=50)


class UserWord(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class UserLanguage(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('language', 'user')
