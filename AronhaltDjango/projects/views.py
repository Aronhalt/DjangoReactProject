from django.shortcuts import render, get_object_or_404
from models import Project
from rest_framework import generics
from serializers import ProjectSerializer
# Create your views here.

def index(request):
	return render(request, 'projects/index.html')
class projectDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Project.objects.all()
	serializer_class = ProjectSerializer
def detail(request,project_id):
	project = get_object_or_404(Project,pk = project_id)
	return render(request, 'projects/detail.html', {'project':project})

