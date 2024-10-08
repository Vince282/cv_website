from .models import Education
from .forms import EducationForm
from django.shortcuts import render, redirect
from .models import WorkExperience
from .forms import WorkExperienceForm
from .models import Skills
from .forms import SkillsForm
from .models import Projects
from .forms import ProjectsForm
from django.shortcuts import render, redirect
from .forms import PersonalInfoForm
from .models import PersonalInfo
from django.shortcuts import render
# View for displaying all education entries
def education_list(request):
    education = Education.objects.all()
    return render(request, 'education_list.html', {'education': education})


def add_education(request):
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('education_list')
    else:
        form = EducationForm()
    return render(request, 'add_education.html', {'form': form})


def edit_education(request, education_id):
    education = Education.objects.get(id=education_id)
    if request.method == 'POST':
        form = EducationForm(request.POST, instance=education)
        if form.is_valid():
            form.save()
            return redirect('education_list')
    else:
        form = EducationForm(instance=education)
    return render(request, 'edit_education.html', {'form': form})


def delete_education(request, education_id):
    education = Education.objects.get(id=education_id)
    education.delete()
    return redirect('education_list')

def work_experience_list(request):
    work_experiences = WorkExperience.objects.all()
    return render(request, 'work_experience_list.html', {'work_experiences': work_experiences})


def add_work_experience(request):
    if request.method == 'POST':
        form = WorkExperienceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('work_experience_list')
    else:
        form = WorkExperienceForm()
    return render(request, 'add_work_experience.html', {'form': form})


def edit_work_experience(request, experience_id):
    work_experience = WorkExperience.objects.get(id=experience_id)
    if request.method == 'POST':
        form = WorkExperienceForm(request.POST, instance=work_experience)
        if form.is_valid():
            form.save()
            return redirect('work_experience_list')
    else:
        form = WorkExperienceForm(instance=work_experience)
    return render(request, 'edit_work_experience.html', {'form': form})


def delete_work_experience(request, experience_id):
    work_experience = WorkExperience.objects.get(id=experience_id)
    work_experience.delete()
    return redirect('work_experience_list')

def skills_list(request):
    skills = Skills.objects.all()
    return render(request, 'skills_list.html', {'skills': skills})


def add_skill(request):
    if request.method == 'POST':
        form = SkillsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('skills_list')
    else:
        form = SkillsForm()
    return render(request, 'add_skill.html', {'form': form})

def edit_skill(request, skill_id):
    skill = Skills.objects.get(id=skill_id)
    if request.method == 'POST':
        form = SkillsForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            return redirect('skills_list')
    else:
        form = SkillsForm(instance=skill)
    return render(request, 'edit_skill.html', {'form': form})

def delete_skill(request, skill_id):
    skill = Skills.objects.get(id=skill_id)
    skill.delete()
    return redirect('skills_list')

def projects_list(request):
    projects = Projects.objects.all()
    return render(request, 'projects_list.html', {'projects': projects})


def add_project(request):
    if request.method == 'POST':
        form = ProjectsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects_list')
    else:
        form = ProjectsForm()
    return render(request, 'add_project.html', {'form': form})


def edit_project(request, project_id):
    project = Projects.objects.get(id=project_id)
    if request.method == 'POST':
        form = ProjectsForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects_list')
    else:
        form = ProjectsForm(instance=project)
    return render(request, 'edit_project.html', {'form': form})

# View for deleting a project
def delete_project(request, project_id):
    project = Projects.objects.get(id=project_id)
    project.delete()
    return redirect('projects_list')


def personal_info(request):
    if request.method == 'POST':
        form = PersonalInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('personal_info')  # Redirect after POST
    else:
        form = PersonalInfoForm()

    personal_info_data = PersonalInfo.objects.all()  # Fetch existing data
    return render(request, 'personal_info.html', {'form': form, 'personal_info_data': personal_info_data})


def home(request):
    return render(request, 'home.html')  # Create this template
