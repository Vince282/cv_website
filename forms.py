
from django import forms
from .models import Education, WorkExperience, Skills, Projects

# Form for Personal Info
from django import forms
from .models import PersonalInfo

class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        fields = ['name', 'email', 'bio']

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['school', 'degree', 'start_year', 'end_year']


class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = ['company', 'job_title', 'start_date', 'end_date', 'description']


class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = ['skill_name']


class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['project_title', 'description', 'project_url']
