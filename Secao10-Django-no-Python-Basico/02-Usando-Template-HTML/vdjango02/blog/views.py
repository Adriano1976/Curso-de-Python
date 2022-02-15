from django.views.generic import TemplateView


class IndexpageView(TemplateView):
    template_name = 'index.html'


class BlogpageView(TemplateView):
    template_name = 'blog.html'


class HomepageView(TemplateView):
    template_name = 'home.html'


class SobrepageView(TemplateView):
    template_name = 'sobre.html'

