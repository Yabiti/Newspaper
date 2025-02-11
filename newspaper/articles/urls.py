from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import( ArticleListView,
                    DetailListView,
                    DeleteListView,
                    UpdateListView
)

urlpatterns = [
    path("<int:pk>/edit", UpdateListView.as_view(), name="article_edit"),
    path("<int:pk>/", DetailListView.as_view(), name="article_detail"),
    path("<int:pk>/delete/", DeleteListView.as_view(), name="article_delete"),
    path("", ArticleListView.as_view(), name="list")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
