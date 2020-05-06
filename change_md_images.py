from bs4 import BeautifulSoup
from markdown2 import markdown
import sys
import requests
import shutil
from markdownify import markdownify as md
from github import Github
from datetime import datetime
from git import Repo
import json
def download_image(image,g):
    r = requests.get(image["src"], stream=True)
    periods = image["src"].count(".")
    print("images/"+image["src"].replace("/","_").replace(":","_").replace(".","_",periods-1))
    repo = g.get_user().get_repo("images-for-md")
    remote_file_name = "images/"+ datetime.now().strftime("%c%f").replace(" ","_").replace(":","_")+image["src"].split("/")[-1]  # have the image
    repo.create_file(remote_file_name,"jpg",r.content,branch="master")
    return "https://juno-day.github.io/images-for-md/"+remote_file_name

def find_and_change_images(markdown_file):
    html = BeautifulSoup(markdown(markdown_file), "html.parser")
    images = html.find_all("img")
    print(images)
    number=0
    with open("../gitcreds.json","r") as f:
        data = json.load(f)
    g = Github(data["git_cred"]) #{ "git_cred": "" }
    for image in images:
        new_image = download_image(image,g)
        html.find_all("img")[number]["src"] = new_image
        number+=1
    return html

def open_file_to_html(file):
    with open(file,"r") as f:
        markdown_from_file = f.read()
        return markdown_from_file

    

try:
    print(sys.argv)
    file = sys.argv[1]
except:
    file = "./test.md"
markdowntxt = open_file_to_html(file)
new_html_file = find_and_change_images(markdowntxt)
print(new_html_file.find_all("img"))
with open(sys.argv[1],"w+") as f:
    print(md(new_html_file))
    f.write(md(new_html_file))