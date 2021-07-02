from django.shortcuts import render
from django import forms
from django.utils.translation import gettext_lazy as _
# Create your views here.
from django.views.decorators.http import require_GET
from django.http import HttpResponse
from django.shortcuts import redirect
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
        form = ContactForm(request.POST)
        if form.is_valid():
            return redirect('thankyou')
    else:
        form = ContactForm()
        context = {'form':form}
        return render(request, 'pages/contacts.html',context=context)


class ContactForm(forms.Form):
    email = forms.EmailField(label=_('Email'), max_length=100, widget=forms.EmailInput(attrs={"class":"form-control border-0 shadow","id":"id_email"}))
    nome = forms.CharField(label=_('Oggetto'), widget=forms.TextInput(attrs={"class":"form-control border-0 shadow","id":"id_nome"}))
    testo = forms.CharField(label=_("Il tuo messaggio"), widget=forms.Textarea(attrs={"class":"form-control border-0 shadow","id":"id_testo"}))
    accettazione = forms.BooleanField(label=_("Accetti i termini e le condizioni sulla privacy"), widget=forms.CheckboxInput(attrs={"class":"form-check border-0 shadow","id":"id_accettazione"}))
