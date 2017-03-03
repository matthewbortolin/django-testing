from django.shortcuts import render, redirect
from django.http import Http404
from django.core.mail import send_mail
from django.views.generic import TemplateView, UpdateView, View

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

import stripe

from . import models
from . import forms

class HomeView(TemplateView):
    template_name = 'birdie/index.html'

class AdminView(TemplateView):
    template_name = 'birdie/admin.html'
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(AdminView, self).dispatch(request, *args, **kwargs)

class PostUpdateView(UpdateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = 'birdie/update.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        if getattr(request.user, 'first_name', None) == 'Matt':
            raise Http404()
        return super(PostUpdateView, self).post(request, *args, **kwargs)

class PaymentView(View):

    def post(self, request, *args, **kwargs):
        charge = stripe.Charge.create(
            amount = 100,
            currency = 'aud',
            description = '',
            token = request.POST.get('token'),
        ) 
        send_mail(
            'Payment recieved',
            'Charge {} succeded'.format(charge[id]),
            'server@example.com',
            ['admin@example.com',],
        ) 
        return redirect('/')

