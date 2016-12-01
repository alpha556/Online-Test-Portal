from django.conf.urls import url
from . import views
from .form import LoginForm
from django.contrib.auth import views as auth_views

app_name = 'exam'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<exam_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<exam_id>[0-9]+)/submit/$', views.submit, name='submit'),
    url(r'register/$', views.UserFormView.as_view(), name='register'),
    url(r'^login/$', auth_views.login, {'template_name': 'exam/login.html', 'authentication_form': LoginForm},
        name='login'),
    url(r'^report/$', views.report, name='report'),
    url(r'^logout/$', auth_views.logout_then_login, name='logout'),
]
