from django.conf.urls import patterns, include, url
from django.contrib import admin
from article.views import HelloTemplate
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^articles/' , include( 'article.urls')),
    url(r'^hello/$' , 'article.views.hello'),
    url(r'^hello_template/$' , 'article.views.hello_template'),
    url(r'^simple_hello_template/$' , 'article.views.hello_template'),
    url(r'^HelloTemplate/$' , HelloTemplate.as_view()),
    url(r'^article_json/$' , 'article.views.article_json'),
    # Examples:
    # url(r'^$', 'hello_test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'Django_traning_exercise_files.views.login'),
    url(r'^accounts/auth/$', 'Django_traning_exercise_files.views.auth_view'),
    url(r'^accounts/logout/$', 'Django_traning_exercise_files.views.logout'),
    url(r'^accounts/loggedin/$', 'Django_traning_exercise_files.views.loggedin'),
    url(r'^accounts/invalid/$', 'Django_traning_exercise_files.views.invalid_login'),
    url(r'^accounts/register/$', 'Django_traning_exercise_files.views.register_user'),
    url(r'^accounts/register_sucess/$', 'Django_traning_exercise_files.views.register_sucess'),
    ) + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

    