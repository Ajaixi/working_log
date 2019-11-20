from django.shortcuts import render
from .models import Project, Opinion, Img
from .forms import ProjectForm, OpinionForm, ImgForm
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    """工作笔记主页"""
    return render(request, 'working_logs/index.html')

@login_required
def projects(request):
    """显示所有工程项目"""
    projects = Project.objects.order_by('date_added')
    context = {'projects': projects}
    return render(request, 'working_logs/projects.html', context)

@login_required
def project(request, project_id):
    """显示工程项目的明细"""
    project = Project.objects.get(id=project_id)
    opinions = project.opinion_set.order_by('date_added')
    context = {'project': project, 'opinions':opinions}
    return render(request, 'working_logs/project.html', context)

@login_required
def new_project(request):
    """添加新项目"""
    if request.method != 'POST':
        form = ProjectForm()
    else:
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('working_logs:projects'))
    context = {'form': form}
    return render(request, 'working_logs/new_project.html', context)

@login_required
def new_opinion(request, project_id):
    """添加意见"""
    project = Project.objects.get(id=project_id)
    if request.method != "POST":
        form = OpinionForm()
    else:
        form = OpinionForm(data=request.POST)
        if form.is_valid():
            new_opinion = form.save(commit=False)
            new_opinion.project = project
            new_opinion.save()
            return HttpResponseRedirect(reverse('working_logs:project', args=[project_id]))
    context = {'project': project, 'form': form}
    return render(request, 'working_logs/new_opinion.html', context)

@login_required
def edit_opinion(request, opinion_id):
    """编辑意见"""
    opinion = Opinion.objects.get(id=opinion_id)
    project = opinion.project
    if request.method != "POST":
        form = OpinionForm(instance=opinion)
    else:
        form = OpinionForm(instance=opinion, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('working_logs:project', args=[project.id]))
    context = {'project': project, 'opinion': opinion, 'form': form}
    return render(request, 'working_logs/edit_opinion.html', context)

@login_required
def delete_project(request, project_id):
    project = Project.objects.get(id=project_id)
    project.delete()
    return HttpResponseRedirect(reverse('working_logs:projects'))


@login_required
def delete_opinion(request, opinion_id):
    opinion = Opinion.objects.get(id=opinion_id)
    project = opinion.project
    opinion.delete()
    return HttpResponseRedirect(reverse('working_logs:project', args=[project.id]))


@login_required
def search(request):
    project_name = request.POST.get('project')
    if request.method != "POST":
        HttpResponseRedirect(reverse('working_logs:index'))
    else:
        try:
            project = Project.objects.get(text=project_name)
        except:
            return HttpResponseRedirect(reverse('working_logs:projects'))
       
        return HttpResponseRedirect(reverse('working_logs:project', args=[project.id]))


def img_upload(request, project_id):
    """
    图片上传
    """
    project = Project.objects.get(id=project_id)
    if request.method != "POST":
        form = ImgForm()
    else:
        files = request.FILES.getlist('img_url')
        if len(files) == 0:
            return HttpResponseRedirect(reverse('working_logs:add_img', args=[project.id]))
        for i in range(len(files)):
            form = ImgForm(request.POST or None, {'img_url':files[i]} or None)
            if form.is_valid():
                new_img = form.save(commit=False)
                new_img.project = project
                print(new_img.img_url.url)
                new_img.save()           
                
        return HttpResponseRedirect(reverse('working_logs:show_img', args=[project.id]))  
        
    context = {'project': project, 'form': form}
    return render(request, 'working_logs/img_upload.html', context)


def img_show(request, project_id):
    """
    图片显示
    """
    project = Project.objects.get(id=project_id)
    imgs = project.img_set.order_by('date_added')
    context = {'project':project, 'imgs':imgs}
    return render(request, 'working_logs/img_show.html', context)
  

def delete_img(request, img_id):
    img = Img.objects.get(id=img_id)
    project = img.project
    img.delete()
    return HttpResponseRedirect(reverse('working_logs:show_img', args=[project.id]))

'''
def img_upload(request, project_id):
    project = Project.objects.get(id=project_id)
    if request.method == 'POST':
        files = request.FILES.getlist('img')
        print(request.FILES)
        print(files)
        
        for f in files:
            print(type(f))
            form = ImgForm(request.POST or None, f or None)
            if form.is_valid():
                new_img = form.save(commit=False)
                new_img.project = project    
                if new_img.img_url:
                    new_img.save()
                else:
                    return HttpResponseRedirect(reverse('working_logs:add_img', args=[project.id]))
        return HttpResponseRedirect(reverse('working_logs:show_img', args=[project.id]))
    context = {'project': project}
    return render(request, 'working_logs/img_upload.html', context)'''