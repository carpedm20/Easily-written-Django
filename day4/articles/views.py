from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from django.views.generic.base import TemplateView

from articles.models import Article

# Create your views here.

def articles(request):
  return render_to_response('articles.html',
                            {'articles': Article.objects.all()})
  
def article(request, article_id=1):
  return render_to_response('article.html',
                            {'article': Article.objects.get(id=article_id)})

def hello(request):
  name = "carpedm30"
  return render_to_response('hello.html', {'name': name})

class HelloTemplate(TemplateView):
  template_name = 'hello.html'

  def get_context_date(self, **kwargs):
    context = super(HelloTemplate, self).get_context_date(**kwargs)
    context['name'] = 'carpedm40'

    return context
