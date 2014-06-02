from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cinema_system.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^films/$', 'film.views.FilmAll'),
    url(r'^admin/', include(admin.site.urls)),
    (r'^fimls/(?P<filmtitle>)/$', 'film.views.DescriptionFilm'),
)
