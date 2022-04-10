from rest_framework import routers
from .views import StudentViewSet, BookViewSet

router = routers.DefaultRouter()
router.register('book', BookViewSet)
router.register('student', StudentViewSet)

urlpatterns = router.urls