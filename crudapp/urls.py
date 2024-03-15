from django.urls import path
from . import views
from . import api_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"api/student-view-set", api_views.StudentViewSet, basename="studentviewset")

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("<int:id>/", views.update_student, name="update"),
    path("api/get-student/",api_views.getStudent),
    path("api/post-student/",api_views.postStudent),
    path("api/patch-student/",api_views.patchStudent),
    path("api/student-view/", api_views.StudentVIEW.as_view()),
]

urlpatterns += router.urls