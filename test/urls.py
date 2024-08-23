from django.urls import path
from .views import PessoaFormView

urlpatterns=[path('pessoas/',PessoaFormView.as_view(),name='pessoa')]