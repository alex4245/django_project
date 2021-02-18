from bootstrap_modal_forms.forms import BSModalModelForm
from django.db.models import Subquery
from django import forms

from .models import Language, Word, UserLanguage


class UserLanguageForm(BSModalModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user_id = self.request.user.id
        sq = UserLanguage.objects.filter(user_id=user_id)
        queryset = Language.objects.all().exclude(id__in=Subquery(sq.values('language_id')))
        self.fields['language'].queryset = queryset

    class Meta:
        model = UserLanguage
        fields = ['language']


class UserWordForm(BSModalModelForm):

    class Meta:
        model = Word
        fields = ['name']


class ChangeUserLanguageForm(forms.Form):
    # TODO change priority
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['user_language'].queryset = UserLanguage.objects.filter(user_id=self.user.id)

    user_language = forms.ModelChoiceField(
        queryset=None, to_field_name="language"
    )
