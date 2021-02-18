from django.urls import path

from . import views

app_name = 'lang_learning'

urlpatterns = [
    path('', views.UserInfo.as_view(), name='user_info'),
    path('language_list', views.LanguageList.as_view(), name='language_list'),
    path(
        'user_word_create',
        views.UserWordCreateModalForm.as_view(),
        name='user_word_create'
    ),
    path(
        'change_user_language_modal',
        views.ChangeUserLanguageModalForm.as_view(),
        name='change_user_language_modal'
    ),
    path('user_language_create',
        views.UserLanguageCreateModalForm.as_view(),
        name='user_language_create'
    ),
    path('user_word_list',
        views.UserWordList.as_view(),
        name='user_word_list'
    )
]


