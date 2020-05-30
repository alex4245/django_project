from django.urls import path

from . import views

app_name = 'lang_learning'
urlpatterns = [
    path('language_list', views.LanguageList.as_view(), name='language_list'),
    path('user_language_list', views.UserLanguageList.as_view(), name='user_language_list'),  # noqa E501
    path('user_language', views.UserLanguage.as_view(), name='user_language'),
]
