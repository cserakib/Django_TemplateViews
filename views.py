from django.views.generic import TemplateView

class Home_View(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['name'] = "Md Rakibul Islam"
        context['Country']= "Bangladesh"
        list = [1,2,3,4,5,6]
        context['list'] = list
        return context

class About_View(TemplateView):
    template_name = 'about.html'