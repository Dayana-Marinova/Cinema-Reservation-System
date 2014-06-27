from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView


urlpatterns = patterns('',
    # Examples:
    url(r'^home/$', 'film.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^films/$', 'film.views.filmAll', name='films'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rooms/$', 'room.views.roomAll', name='allRooms'),
    url(r'^films/(?P<filmtitle>.*)/$', 'film.views.descriptionFilm'),
    (r'^$', TemplateView.as_view(template_name="base.html")),
    url(r'^room/(?P<roomnumber>.*)/$', 'room.views.informationRoom'),
    url(r'^user/$', 'user.views.userRegiteration', name='register'),
    url(r'^thankYouRegister/$', 'user.views.thankYouRegister', name='thankYouRegister'),
    url(r'^catalog/$', 'catalog.views.catalogAll', name='catalog'),
    url(r'^thankYouReservation/$', 'film.views.descriptionFilm')
)
