from django.shortcuts import render, render_to_response, RequestContext

# Create your views here.

from .forms import ContactForm

def home(request):
    
    form = ContactForm(request.POST or None)
    #
    #if from.is_valid():
    #    save_it = form.save(commit = False)
    #    save_it.save()
    
    return render_to_response("home.html", locals(), context_instance=RequestContext(request))