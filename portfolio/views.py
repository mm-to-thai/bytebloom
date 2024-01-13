from django.shortcuts import render
from . import models
from . import serializers
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ReadOnlyModelViewSet

# Create your views here.
class HeaderViewSet(ReadOnlyModelViewSet):
    queryset = models.Header.objects.all()
    serializer_class = serializers.HeaderSerializer

class ServiceViewSet(ReadOnlyModelViewSet):
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializer

class ProfessionalBackgroundViewSet(ReadOnlyModelViewSet):
    queryset = models.ProfessionalBackground.objects.prefetch_related('services').all()
    serializer_class = serializers.ProfessionalBackgroundSerializer

class SkillViewSet(ReadOnlyModelViewSet):
    queryset = models.Skill.objects.all()
    serializer_class = serializers.SkillSerializer

class ProjectViewSet(ReadOnlyModelViewSet):
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer
    pagination_class = PageNumberPagination

class BlogViewSet(ReadOnlyModelViewSet):
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer
    pagination_class = PageNumberPagination

class ExperienceViewSet(ReadOnlyModelViewSet):
    queryset = models.Experience.objects.all()
    serializer_class = serializers.ExperienceSerializer

class CompleteProjectViewSet(ReadOnlyModelViewSet):
    queryset = models.CompleteProject.objects.all()
    serializer_class = serializers.CompleteProjectSerializer

class HappyCustomerViewSet(ReadOnlyModelViewSet):
    queryset = models.HappyCustomer.objects.all()
    serializer_class = serializers.HappyCustomerSerializer

class AboutMeViewSet(ReadOnlyModelViewSet):
    queryset = models.AboutMe.objects.select_related('experience')\
    .select_related('complete_project').select_related('happy_customer').all()
    serializer_class = serializers.AboutMeSerializer