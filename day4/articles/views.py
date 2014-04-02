from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from django.views.generic.base import TemplateView

from articles.models import Article

# Create your views here.

def articles(request):
  language = 'en-gb'
  session_language = 'en-gb'

  if 'lang' in request.COOKIES:
    language = request.COOKIES['lang']

  if 'lang' in request.session:
    session_language = request.session['lang']

  return render_to_response('articles.html',
                            {'articles': Article.objects.all(),
                             'language': language,
                             'session_language': session_language})
  
def article(request, article_id=1):
  return render_to_response('article.html',
                            {'article': Article.objects.get(id=article_id)})

def language(request, language='en-gb'):
  response = HttpResponse('setting language to %s' % language)
  response.set_cookie('lang', language)

  request.session['lang'] = language

  return response

def hello(request):
  name = "carpedm30"
  return render_to_response('hello.html', {'name': name})

class HelloTemplate(TemplateView):
  template_name = 'hello.html'

  def get_context_date(self, **kwargs):
    context = super(HelloTemplate, self).get_context_date(**kwargs)
    context['name'] = 'carpedm40'

    return context
