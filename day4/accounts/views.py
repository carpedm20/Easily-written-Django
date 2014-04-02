from django.shortcuts import render, RequestContext, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login, authenticate, logout

from .forms import AccountForm, AccountAuthForm

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = AuthenticateForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            # Success
            return redirect('/')
        else:
            # Failure
            return index(request, auth_form=form)
    return redirect('/')

def logout_view(request):
    logout(request)
    return redirect('/')

def join(request):
    form = AccountForm(request.POST or None)
    context = RequestContext(request)
  
    if form.is_valid():
        # `commit=False`: before save it to database, just keep it in memory
        save_it = form.save(commit=False)
        save_it.save()

        messages.success(request, 'Thank you for joining')
        #return HttpResponseRedirect(reverse('articles:all'))
        return render_to_response("join.html", locals(), context_instance=context)

    return render_to_response("join.html", locals(), context_instance=context)
