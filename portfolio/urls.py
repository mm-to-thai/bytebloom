from rest_framework_nested.routers import DefaultRouter
from . import views
from django.urls import path,include

router = DefaultRouter()
router.register('headers',views.HeaderViewSet)
router.register('services',views.ServiceViewSet)
router.register('professional_background',views.ProfessionalBackgroundViewSet)
router.register('skills',views.SkillViewSet)
router.register('projects',views.ProjectViewSet)
router.register('blogs',views.BlogViewSet)
router.register('experience',views.ExperienceViewSet)
router.register('completed_project',views.CompleteProjectViewSet)
router.register('happy_customer',views.HappyCustomerViewSet)
router.register('about_me',views.AboutMeViewSet)

urlpatterns = [
    path('',include(router.urls)),
]