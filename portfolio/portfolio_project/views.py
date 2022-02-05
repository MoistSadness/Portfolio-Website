from django.shortcuts import render
from portfolio_project.models import Project

# Create your views here.

# Index view to show a snippet of information about each project
def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)

# Detail view to show all the information about the project