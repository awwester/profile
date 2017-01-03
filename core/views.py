from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView
from django.views.decorators.csrf import csrf_exempt

from braces.views import StaffuserRequiredMixin, JsonRequestResponseMixin, \
                         CsrfExemptMixin


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


class DashboardHomeListView(StaffuserRequiredMixin, ListView):
    model = Article
    template_name = 'dashboard_home.html'


class SendContactView(CsrfExemptMixin, JsonRequestResponseMixin, View):
    require_json = True

    def clean_field(self, field_name):
        field = self.request_json[field_name]

        if not len(field):
            raise KeyError

        return field

    def post(self, request, *args, **kwargs):
        try:
            email = self.clean_field("email")
            first_name = self.clean_field("first_name")
            last_name = self.clean_field("last_name")
            message = self.clean_field("message")
        except KeyError:
            error_dict = {"message": "you must include all fields in the contact request"}
            return self.render_bad_request_response(error_dict)

        subject = "[www.adamwester.me] message from %s %s" % (first_name, last_name)
        message = message + "\n\n%s" % email

        send_mail(subject, message, "awwester@gmail.com", ["awwester@gmail.com"], fail_silently=True)
        return self.render_json_response({"message": "Your contact email has been sent."})


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
