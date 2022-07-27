# Machine_learning_bicycle_project
Machine_learning _project of bicycle
Software and account Requirement.

    1.Github Account
    2.Heroku Account
    3.VS Code IDE
    GIT cli
    GIT Documentation

Creating conda environment

conda create -p venv python==3.7 -y

conda activate venv/

OR

conda activate venv

pip install -r requirements.txt

To Add files to git

git add .

OR

git add <file_name>

    Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status

git status

To check all version maintained by git

git log

To create version/commit all changes by git

git commit -m "message"

To send version/changes to github

git push origin main

To check remote url

git remote -v

To setup CI/CD pipeline in heroku we need 3 information

    HEROKU_EMAIL = nimmymathew91@gmail.com
    HEROKU_API_KEY = <9bd90cfb-1110-441d-8b54-5a0f67ce4040>
    HEROKU_APP_NAME = ml-bicycle-project



BUILD DOCKER IMAGE

docker build -t <image_name>:<tagname> .

    Note: Image name for docker must be lowercase

To list docker image

docker images

Run docker image

docker run -p 5000:5000 -e PORT=5000 f8c749e73678

To check running container in docker

docker ps

Tos stop docker conatiner

docker stop <container_id>

python setup.py install

