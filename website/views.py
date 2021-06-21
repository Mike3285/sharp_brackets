from django.shortcuts import render
from django import forms
from django.utils.translation import gettext_lazy as _
# Create your views here.
from django.views.decorators.http import require_GET
from django.http import HttpResponse


@require_GET
def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow: /static/",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")


def render_page(request):

    return render(request, 'pages/index.html')


def about(request):
    return render(request, 'pages/about.html')


def portfolio(request):
    return render(request, 'pages/portfolio.html')


def contacts(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()
    return render(request, 'pages/contacts.html')


class ContactForm(forms.Form):
    name = forms.CharField(label=_('Nome'), max_length=100)
