from bootstrap_modal_forms.forms import BSModalForm
from django.db.models import Subquery

from .models import UserLanguage, Language


class NameForm(BSModalForm):
    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        sq = UserLanguage.objects.filter(user_id=1)
        queryset = Language.objects.all().exclude(id__in=Subquery(sq.values('language_id')))
        self.fields['language'].queryset = queryset

    class Meta:
        model = UserLanguage
        fields = ['language']
