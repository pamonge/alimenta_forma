from rest_framework import serializers
from .models import UserType, Profile, Offer, Announcement, Content, Course, Registration, Attendance, Mark

class UserTypeSerializer (serializers.ModelSerializer):
  class Meta:
    model = UserType
    fields = '__all__'

class ProfileSerializer (serializers.ModelSerializer):
  class Meta:
    model = Profile
    fields = '__all__'

class OfferSerializer (serializers.ModelSerializer):
  class Meta:
    model = Offer
    fields = '__all__'

class AnnouncementSerializer (serializers.ModelSerializer):
  class Meta:
    model = Announcement
    fields = '__all__'

class ContentSerializer (serializers.ModelSerializer):
  class Meta:
    model = Content
    fields = '__all__'

class CourseSerializer (serializers.ModelSerializer):
  class Meta:
    model = Course
    fields = '__all__'

class RegistrationSerializer (serializers.ModelSerializer):
  class Meta:
    model = Registration
    fields = '__all__'

class AttendanceSerializer (serializers.ModelSerializer):
  class Meta:
    model = Attendance
    fields = '__all__'

class MarkSerializer (serializers.ModelSerializer):
  class Meta:
    model = Mark
    fields = '__all__'