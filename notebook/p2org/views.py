from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class AccountView(LoginRequiredMixin, TemplateView):
    template_name = 'p2org/account.html'
