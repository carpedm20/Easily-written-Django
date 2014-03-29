from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

def hello(request, message= 'HeXA'):
    return HttpResponse('Hello, World! Your number is ' + message)

def me(request, name, group, role):
    t = get_template('index.html')

    context = Context({'first': name,
                       'second': group,
                       'third': role,})

    html = t.render(context)
    return HttpResponse(html, mimetype = 'text/html;charset=UTF-8')
