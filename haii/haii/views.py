from django.views.generic import TemplateView


class TemplateVerify(TemplateView):
    template_name = 'verify-email.html'