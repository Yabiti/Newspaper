from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import( ArticleListView,
                    DetailListView,
                    DeleteListView,
                    UpdateListView,
                    HomePageView
)

urlpatterns = [
        path('', HomePageView.as_view(), name='home'),
    path("<int:pk>/edit/", UpdateListView.as_view(), name="edit"),
    path("<int:pk>/", DetailListView.as_view(), name="detail"),
    path("<int:pk>/delete/", DeleteListView.as_view(), name="delete"),
    path("", ArticleListView.as_view(), name="list")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
