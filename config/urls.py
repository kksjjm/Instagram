from django.contrib import admin
from django.urls import path, include
#from rooms import views as room_views 직접 함수로딩 => 이러면 등록해야하는 url이 너무 많아짐
from django.conf.urls.static import static
from django.conf import settings # setting 파일을 불러올 때 

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/rooms/", include("rooms.urls")),
    path("api/v1/categories/", include("categories.urls")),
    path("api/v1/experiences/", include("experiences.urls")),
    path("api/v1/medias/", include("medias.urls")),
    path("api/v1/wishlists/", include("wishlists.urls")),
    path("api/v1/users/", include("users.urls")),
    # path("api/v1/bookings/", include("bookings.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # media root와 url은 다를 수 있음
 