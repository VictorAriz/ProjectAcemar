from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView , LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView



urlpatterns = [

    path('admin/', admin.site.urls),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('users/', include('apps.users.urls', namespace="users")),
    path('quotes/', include('apps.quotes.urls', namespace="quotes")),
    path('accounts/login', LoginView.as_view(), {'template_name': 'index.html'}, name='login'),
    path('accounts/logout', LogoutView.as_view(), name='logout'),
    path('reset/password_reset', PasswordResetView.as_view(),
         {'template_name': 'password_reset_form.html', 'email_template_name': 'password_reset_email.html'},
         name = 'password_reset'),
    path('reset/password_reset_done', PasswordResetDoneView.as_view(),
         {'template_name': 'password_reset_done.html', 'email_template_name': 'password_reset_done.html'},
         name = 'password_reset_done'),
    path('reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', PasswordResetConfirmView.as_view(),
        {'template_name': 'password_reset_confirm.html'},
        name='password_reset_confirm'),
    path('reset/done', PasswordResetCompleteView.as_view(),
        {'template_name': 'password_reset_complete.html'},
        name = 'password_reset_complete'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)






# urlpatterns = [
#     # url(r'^$', include('apps.generalInfo.urls')),
#     url(r'^admin/', admin.site.urls),
#     url(r'^rest-auth/', include('rest_auth.urls')),
#     url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
#     url(r'^users/', include('apps.users.urls', namespace="users")),
#     url(r'^report/', include('apps.report.urls', namespace="report")),
#     # path('report', include('apps.report.urls')),
#     url(r'^accounts/login', login, {'template_name': 'index.html'}, name='login'),
#     url(r'^accounts/logout', logout_then_login, name='logout'),
#     url(r'^reset/password_reset', password_reset,
#         {'template_name': 'password_reset_form.html', 'email_template_name':'password_reset_email.html'},
#         name='password_reset'),
#     url(r'^reset/password_reset_done', password_reset_done,
#         {'template_name': 'password_reset_done.html', 'email_template_name':'password_reset_done.html'},
#         name='password_reset_done'),
#     url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', password_reset_confirm,
#         {'template_name': 'password_reset_confirm.html'},
#         name='password_reset_confirm'),
#     url(r'^reset/done', password_reset_complete,
#         {'template_name': 'password_reset_complete.html'},
#         name='password_reset_complete'),
#   #  url(r'^media/(?P<path>.*)$', static.serve,
#    #                       {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),

#     #url(r'^$', include('apps.generalInfo.urls')),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
