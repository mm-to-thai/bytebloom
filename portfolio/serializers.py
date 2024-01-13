from rest_framework import serializers
from . import models

class HeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Header
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Service
        fields = '__all__'

class ProfessionalBackgroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProfessionalBackground
        fields = ['id','image','services']
    services = ServiceSerializer(many=True)

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Skill
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields = '__all__'
    
class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Blog
        fields = '__all__'

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Experience
        fields = '__all__'
    
class CompleteProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CompleteProject
        fields = '__all__'
    
class HappyCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HappyCustomer
        fields = '__all__'

class AboutMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AboutMe
        fields = ['id','name','title','desc','image','experience','complete_project','happy_customer']
    experience = ExperienceSerializer()
    complete_project = CompleteProjectSerializer()
    happy_customer = HappyCustomerSerializer()