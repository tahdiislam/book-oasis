from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from core.views import Home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),
    path('book-filter/<slug:category>', Home.as_view(), name='filter_home'),
    path('user/', include('accounts.urls')),
    path('book/', include('books.urls')),
    path('borrow/', include('borrows.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)