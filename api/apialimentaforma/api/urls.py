from django.urls import path, include
from rest_framework import routers
from .views import UserTypeViewSet, ProfileViewSet, OfferViewSet, AnnouncementViewSet, ContentViewSet, CourseViewSet, RegistrationViewSet, AttendanceViewSet, MarkViewSet

router = routers.DefaultRouter()

router.register (r'usertype', UserTypeViewSet)
router.register (r'profile', ProfileViewSet)
router.register (r'offer', OfferViewSet)
router.register (r'Announcement', AnnouncementViewSet)
router.register (r'content', ContentViewSet)
router.register (r'course', CourseViewSet)
router.register (r'registration', RegistrationViewSet)
router.register (r'attendance', AttendanceViewSet)
router.register (r'mark', MarkViewSet)

urlpatterns = [
    path ('', include(router.urls)),
]


