from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from blog.models import Article, Tag


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['tag_list'] = Tag.objects.all()
        context['article_count'] = Article.objects.count()
        context['article_list'] = Article.objects.all()[:2]

        return context


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
