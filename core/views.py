from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt

from blog.models import Article, Tag
from .models import EmailSubscribe


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['tag_list'] = Tag.objects.all()
        context['article_count'] = Article.objects.filter(public=True).count()
        context['article_list'] = Article.objects.filter(public=True)[:2]

        return context


@csrf_exempt
def contact(request):
    "receive a contact AJAX request and try to send an email"
    if request.method == "POST":
        try:
            send = send_mail('New Message Received from ' + request.POST.get('first_name') + '' + request.POST.get('last_name'),
                request.POST.get('message'), request.POST.get('email'), ['awwester@gmail.com'], fail_silently=False)

            if send == 1:
                return HttpResponse()
            else:
                return HttpResponse(status=400)
        except:
            return HttpResponse(status=400)
    else:
        return HttpResponse('this is only for AJAX Posts')


@csrf_exempt
def email_subscribe(request):
    if request.method == "POST":
        try:
            subscribe = EmailSubscribe(email=request.POST["email"])
            subscribe.save()
            return HttpResponse()
        except Exception as e:
            print(e)
            return HttpResponse(status=400)
    else:
        return HttpResponse(status=405)
