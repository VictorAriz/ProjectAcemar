from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.contrib import messages
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.core.urlresolvers import reverse_lazy
from apps.quotes.forms import quotesForm
from apps.quotes.models import Quotes


# Create your views here.

class quotesCreate(CreateView):
    model = Quotes
    template_name = "quotesForm.html"
    form_class = quotesForm
   # second_form_class = profileForm
    success_url = reverse_lazy('quotes:quotesList')

class quotesDelete(ListView):
    model = Quotes
    template_name = "quotesDelete.html"
    success_url = reverse_lazy('quotes:quotesList')

class quotesEdit(UpdateView):
    model = Quotes
    template_name = "quotesForm.html"
    form_class = quotesForm
    success_url = reverse_lazy('quotes:quotesList')

class quotesList(ListView):
    model = Quotes
    template_name="quotesList.html"

class quotesHome(ListView):
    model = Quotes
    template_name="quotesHome.html"



class quotesDetail(DetailView):
    model = Quotes
    template_name = "quotesDetail.html"
    # form_class = quotesForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print ("pk", self.kwargs['pk'])
        # Quotes.objects.create(
        #     quotes_id = self.kwargs['pk'],
        #     quotes_id = self.request.users.id
        # )
        return context
