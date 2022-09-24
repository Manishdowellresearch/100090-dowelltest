from django.http import HttpResponse, JsonResponse 
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt

from dowellfunction.dowellconnection import dowellconnection 
from dowellfunction.dowelleventid import get_event_id
from dowellfunction.population import targeted_population

import os 
import git
import zipfile
from mega import Mega
import time
from datetime import datetime


@csrf_exempt
def index(request):
    return JsonResponse({"name":"manish"})

@csrf_exempt
def repositoryClone(request):
    try:
        repository_name = "test"
        repository_link= "https://github.com/Manishdowellresearch/test.git"
        path="D:\\Dowell\\100090-dowelltest\\git_hub_backup\\file"
        os.chdir(path)
        os.system(f'git clone {repository_link}')
        filename ="post-merge"
        paths=f"D:\\Dowell\\100090-dowelltest\\git_hub_backup\\file\\{repository_name}\\.git\\hooks"
        completepath = os.path.join(paths, filename)
        post_merge = open(completepath, "w")
        line=["!/bin/sh \n","touch /var/www/100045_pythonanywhere_com_wsgi.py \n"]
        post_merge.writelines(line)
        post_merge.close()
        os.chdir(paths)
        os.system("chmod +x post-merge")
        return JsonResponse(
            {
                "status":f"{repository_name} has been clonned .",
                "link":f"http://127.0.0.1:8000/dowell/{repository_name}"
                }
                )
    except:
        return JsonResponse({"status":f"{repository_name} was not clonned ."})

@csrf_exempt
def webhookss(request , repository_name):
    try:
        repo = git.Repo(f'D:\\Dowell\\100090-dowelltest\\git_hub_backup\\file2\\{repository_name}\\.git')
        origin = repo.remotes.origin
        origin.pull()
        def zipdir(path, ziph):
                for root, dirs, files in os.walk(path):
                    for file in files:
                        ziph.write(os.path.join(root, file))
        pathname= f'D:\\Dowell\\100090-dowelltest\\git_hub_backup\\file2\\{repository_name}.zip'
        zipf = zipfile.ZipFile(pathname, 'w', zipfile.ZIP_DEFLATED)
        zipdir(f'.\\file\\{repository_name}', zipf)
        zipf.close()
        time.sleep(2)
        mega = Mega()
        m = mega.login("mdashsharma95@gmail.com", "q1e2r3s4$")
        Folder = m.find(f'github\\{repository_name}')
        m.upload(pathname, Folder[0])
        return JsonResponse({
            "Response":'Updated PythonAnywhere successfully',
            "status":"200"
        })
    except:
        return JsonResponse({
            "Response":'Wrong event type', 
            "status":"400"
        })