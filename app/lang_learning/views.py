from django.views.generic import ListView
from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import BSModalCreateView

from .models import Language, UserLanguage
from .forms import NameForm


class LanguageList(ListView):
    model = Language


class UserLanguageList(ListView):
    template_name = 'lang_learning/user_language_list.html'
    context_object_name = 'user_language_list'
    queryset = UserLanguage.objects.filter(user_id=1).select_related('language')


class UserLanguage(BSModalCreateView):
    template_name = 'lang_learning/user_language.html'
    form_class = NameForm
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('lang_learning:user_language_list')

    def form_valid(self, form):
        form.instance.user_id = 1
        return super().form_valid(form)
