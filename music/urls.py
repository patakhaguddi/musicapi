from django.conf.urls import url


from .views import ListSongsView, LoginView, RegisterUsersView, SongsDetailView

urlpatterns = [
    url(r'^songs/', ListSongsView.as_view(), name = "all-songs"),
    url(r'^auth/login/', LoginView.as_view(), name="auth-login"),
    url(r'^auth/register/', RegisterUsersView.as_view(), name="auth-register"),
    url(r'^songs/<int:pk>', SongsDetailView.as_view(), name="songs-detail")

]