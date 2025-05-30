from rest_framework import viewsets
from .serializer import UserTypeSerializer, ProfileSerializer, OfferSerializer, AnnouncementSerializer, ContentSerializer, CourseSerializer, RegistrationSerializer, AttendanceSerializer, MarkSerializer
from .models import UserType, Profile, Offer, Announcement, Content, Course, Registration, Attendance, Mark

# Create your views here.
class UserTypeViewSet (viewsets.ModelViewSet):
  queryset = UserType.objects.all()
  serializer_class = UserTypeSerializer

class ProfileViewSet (viewsets.ModelViewSet):
  queryset = Profile.objects.all()
  serializer_class = ProfileSerializer

class OfferViewSet (viewsets.ModelViewSet):
  queryset = Offer.objects.all()
  serializer_class = OfferSerializer

class AnnouncementViewSet (viewsets.ModelViewSet):
  queryset = Announcement.objects.all()
  serializer_class = AnnouncementSerializer

class ContentViewSet (viewsets.ModelViewSet):
  queryset = Content.objects.all()
  serializer_class = ContentSerializer

class CourseViewSet (viewsets.ModelViewSet):
  queryset = Course.objects.all()
  serializer_class = CourseSerializer

class RegistrationViewSet (viewsets.ModelViewSet):
  queryset = Registration.objects.all()
  serializer_class = RegistrationSerializer

class AttendanceViewSet (viewsets.ModelViewSet):
  queryset = Attendance.objects.all()
  serializer_class = AttendanceSerializer

class MarkViewSet (viewsets.ModelViewSet):
  queryset = Mark.objects.all()
  serializer_class = MarkSerializer