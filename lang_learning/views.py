from django.views.generic import ListView, View, FormView
from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import BSModalCreateView
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Language, UserLanguage, UserWord, Word
from .forms import UserLanguageForm, UserWordForm, ChangeUserLanguageForm


class LanguageList(ListView):
    model = Language


class UserInfo(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        user_language_list = UserLanguage.objects.filter(
            user_id=user.id
        )
        context = {
            "user_language_list": user_language_list,
            "user": user
        }
        return render(request, 'lang_learning/user_info.html', context)
        # response.set_cookie('user', user.id)
        # return response


class UserWordCreateModalForm(LoginRequiredMixin, BSModalCreateView):
    template_name = 'lang_learning/add_user_word.html'
    form_class = UserWordForm
    success_message = 'Success: User word was created.'
    success_url = reverse_lazy('lang_learning:user_info')

    def form_valid(self, form):
        user_id = self.request.user.id
        user_language = UserLanguage.active(user_id=user_id)
        form.instance.user_id = user_id
        form.instance.language_id = user_language.language_id
        response = super().form_valid(form)
        if self.object.id:
            UserWord(word_id=self.object.id, user_id=user_id).save()
        return response


class ChangeUserLanguageModalForm(LoginRequiredMixin, FormView):
    template_name = 'lang_learning/change_user_language.html'
    form_class = ChangeUserLanguageForm
    success_url = reverse_lazy('lang_learning:user_info')

    def form_valid(self, form):
        user_id = self.request.user.id
        user_language_id = form.data['user_language']
        ul = UserLanguage.objects.filter(user_id=user_id)
        active_languages = ul.filter(is_active=True)
        if len(active_languages) != 1 or active_languages[0] != user_language_id:
            active_languages.update(is_active=False)
            ul.filter(language=user_language_id).update(is_active=True)
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class UserLanguageCreateModalForm(LoginRequiredMixin, BSModalCreateView):
    template_name = 'lang_learning/add_user_language.html'
    form_class = UserLanguageForm
    success_message = 'Success: User language was created.'
    success_url = reverse_lazy('lang_learning:user_info')

    def form_valid(self, form):
        user_id = self.request.user.id
        form.instance.user_id = user_id
        return super().form_valid(form)


class UserWordList(LoginRequiredMixin, ListView):
    template_name = 'lang_learning/user_word_list.html'
    model = UserWord
    # paginate_by = 10

    def get_queryset(self):
        user_id = self.request.user.id
        user_language = UserLanguage.active(user_id=user_id)
        return UserWord.objects.filter(
            user_id=user_id, word__language__id=user_language.id
        )
