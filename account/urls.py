from . import views
from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView

app_name = 'account'
urlpatterns = [
    url(r'^password-change/$', PasswordChangeView.as_view(template_name='registration/password_change_form.html'),
        name='password_change'),
    url(r'^password-change/done/$', PasswordChangeDoneView.as_view(
        template_name='registration/password_change_done.html'),
        name='password_change_done'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', LoginView.as_view(template_name='registration/login.html'), name='login'),
    url(r'^logout/$', LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
    # url(r'^logout-then-login/$', 'django.contrib.auth.views.logout_then_login', name='logout_then_login'),
    url(r'^my_page/$', views.self_page, name='account'),
    url(r'^edit/$', views.edit, name='edit'),
    url(r'^add_animal/$', views.register_animal, name='add_animal'),
    url(r'^edit_animal/$', views.animal_edit, name='edit_animal'),
    url(r'^add_shelter/$', views.register_shelter, name='add_shelter'),
    url(r'^edit_shelter/$', views.edit_shelter, name='edit_shelter'),
    url(r'^page/$', views.page, name='page'),
]
