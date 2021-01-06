from django.urls import path
from .views import postImage, profilePage, homePage
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('upload_img/', postImage.as_view(), name='postImage'),
    path('profile_page/', profilePage.as_view(), name='profilePage'),
    path('', homePage.as_view(), name='home'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
