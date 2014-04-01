from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.contrib import messages

from .forms import SignUpForm

# Create your views here.

def home(request):
	form = SignUpForm(request.POST or None)
	context = RequestContext(request)

	if form.is_valid():
		# `commit=False`: before save it to database, just keep it in memory
		save_it = form.save(commit=False)
		save_it.save()

		messages.success(request, 'Thank you for joining')
		return HttpResponseRedirect('/thank-you/')

	return render_to_response("signup.html", locals(), context_instance=context)

def thankyou(request):
	context = RequestContext(request)
	return render_to_response("thankyou.html", locals(), context_instance=context)
