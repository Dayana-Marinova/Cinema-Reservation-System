from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cinema_system.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^films/$', 'film.views.FilmAll'),
    url(r'^admin/', include(admin.site.urls)),
    (r'^rooms/$', 'room.views.RoomAll'),
    (r'^films/(?P<filmtitle>.*)/$', 'film.views.DescriptionFilm'),
    (r'^$', TemplateView.as_view(template_name="base.html")),
    (r'^room/(?P<roomnumber>.*)/$', 'room.views.InformationRoom'),
    (r'^register/$', 'user.views.UserRegiteration'),
)
