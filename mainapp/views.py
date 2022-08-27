from datetime import datetime
from django.http import HttpResponse
from django.views.generic import TemplateView
<<<<<<< HEAD
=======
import json
>>>>>>> lesson_3


class MainPageView(TemplateView):
    template_name = "mainapp/index.html"


class NewsPageView(TemplateView):
    template_name = "mainapp/news.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
<<<<<<< HEAD
        context['news_title'] = 'Громкий новостной заголовок'
        context['news_preview'] = 'Предварительное описание, которое заинтересует каждого'
        context['range'] = range(1, 5)
        context['datetime_obj'] = datetime.now()
=======
        with open('mainapp/templates/hot_news.json', 'r', encoding='utf-8') as f:
            news = json.load(f)
            context['range'] = range(1, len(news)+1)
            context['news'] = news
>>>>>>> lesson_3
        return context


class NewsWithPaginatorView(NewsPageView):
    def get_context_data(self, page, **kwargs):
        context = super().get_context_data(page=page, **kwargs)
        context['page_num'] = page
        return context


class CoursesPageView(TemplateView):
    template_name = "mainapp/courses_list.html"


class ContactsPageView(TemplateView):
    template_name = "mainapp/contacts.html"


class DocSitePageView(TemplateView):
    template_name = "mainapp/doc_site.html"


class LoginPageView(TemplateView):
    template_name = "mainapp/login.html"
