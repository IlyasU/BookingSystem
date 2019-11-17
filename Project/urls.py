from django.conf.urls import include, url
from django.contrib import admin

from django.conf.urls.static import static
from django.conf import settings


from polls.views import MyRegisterFormView

urlpatterns = [
    url(r'^$', include('polls.urls')), #this line added
    url(r'^MainPage/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'signUp/', MyRegisterFormView.as_view(), name="register"),

] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)