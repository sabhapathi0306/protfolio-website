
from django.shortcuts import render
from django.shortcuts import HttpResponse
import requests
import git_projects
import json
# Create your views here.
obj = git_projects.GitRepos()
def index(request):
    lis = []
    lis_non = []
    for i ,j in obj.git().items():
        name = i
        url = j
        new_git = {
            "name":name,
            "url":url
        }
        lis.append(new_git)
    myjson = json.dumps(lis)
    myj = json.loads(myjson)
    for k,l in obj.git_non().items():
        name = k
        url = l
        new_git_non= {
            "name":name,
            "url":url
        }
        lis_non.append(new_git_non)
    myjson_non = json.dumps(lis_non)
    myj_non = json.loads(myjson_non)

    return render(request,'index.html',{'data':myj,'non_data':myj_non})