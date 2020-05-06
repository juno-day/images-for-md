from bs4 import BeautifulSoup
from markdown2 import markdown
import sys
import requests
import shutil
from markdownify import markdownify as md
from github import Github
from git import Repo

def download_image(image,github):
    r = requests.get(image["src"], stream=True)
    periods = image["src"].count(".")
    print("/Users/shorya/Dropbox/programming_shorya/python_code/md-to-img"+image["src"].replace("/","_").replace(":","_").replace(".","_",periods-1))
    with open("/Users/shorya/Dropbox/programming_shorya/python_code/md-to-img"+image["src"].replace("/","_").replace(":","_").replace(".","_",periods-1), 'wb+') as f:
        f.write(r.content)
    repo_dir = 'md-to-img'
    repo = Repo(repo_dir)
    file_list = [
    "/Users/shorya/Dropbox/programming_shorya/python_code/md-to-img"+image["src"].replace("/","_").replace(":","_").replace(".","_",periods-1)
    ]
    commit_message = 'Add simple regression analysis'
    repo.index.add(file_list)
    repo.index.commit(commit_message)
    origin = repo.remote('origin')
    origin.push()
    return "/Users/shorya/Dropbox/programming_shorya/python_code/md-to-img"+image["src"].replace("/","_").replace(":","_").replace(".","_",periods-1)

def find_and_change_images(markdown_file):
    html = BeautifulSoup(markdown(markdown_file), "html.parser")
    images = html.find_all("img")
    print(images)
    number=0
    g = Github("63b4e41dee5ad3735ffa34faba078b9c41854f6b")
    for image in images:
        new_image = download_image(image,g)
        html.find_all("img")[number]["src"] = new_image
        number+=1
    return html

def open_file_to_html(file):
    with open(file,"r") as f:
        markdown_from_file = f.read()
        return markdown_from_file

if
    
# 63b4e41dee5ad3735ffa34faba078b9c41854f6b
print(sys.argv)
file = sys.argv[1]

markdowntxt = open_file_to_html(file)
new_html_file = find_and_change_images(markdowntxt)
print(new_html_file.find_all("img"))
with open("/Users/shorya/Dropbox/programming_shorya/python_code/md-to-imgoutput_"+sys.argv[1],"w+") as f:
    print(md(new_html_file))
    f.write(md(new_html_file))