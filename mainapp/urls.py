from django.urls import path
from django.views.decorators.cache import cache_page
from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path("", views.MainPageView.as_view(), name="main_page"),

    path("news/", cache_page(60*5)(views.NewsListView.as_view()), name="news"),
    path("news/create", views.NewsCreateView.as_view(), name="news_create"),
    path("news/<int:pk>/update", views.NewsUpdateView.as_view(), name="news_update"),
    path("news/<int:pk>/delete", views.NewsDeleteView.as_view(), name="news_delete"),
    path("news/<int:pk>/detail", views.NewsDetailView.as_view(), name="news_detail"),

    path("courses/",
         cache_page(60*5)(views.CoursesListView.as_view()), name="courses"),
    path("courses/<int:pk>/", views.CoursesDetailView.as_view(),
         name="courses_detail"),
    path(
        "course_feedback/",
        views.CourseFeedbackFormProcessView.as_view(),
        name="course_feedback",
    ),

    path("contacts/", views.ContactsPageView.as_view(), name="contacts"),
    path("doc_site/", views.DocSitePageView.as_view(), name="doc_site"),
    path("log_view/", views.LogView.as_view(), name="log_view"),
    path("log_download/", views.LogDownloadView.as_view(), name="log_download"),
]
