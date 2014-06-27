from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView


urlpatterns = patterns('',
    # Examples:
    url(r'^home/$', 'film.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^films/$', 'film.views.FilmAll', name='films'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rooms/$', 'room.views.RoomAll', name='allRooms'),
    url(r'^films/(?P<filmtitle>.*)/$', 'film.views.DescriptionFilm'),
    (r'^$', TemplateView.as_view(template_name="base.html")),
    url(r'^room/(?P<roomnumber>.*)/$', 'room.views.InformationRoom'),
    url(r'^user/$', 'user.views.UserRegiteration', name='register'),
    #url(r'^thankYouRegister/$', 'user.views.thankYouRegister', name='thankYouRegister'),
    url(r'^signUp/$', 'signUp.views.home', name='signUp'),
    url(r'^thankYou/$', 'signUp.views.thankYou', name='thankYou'),
)
