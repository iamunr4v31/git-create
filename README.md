# Git create

## Sweat no more with creation of new projects

A simple effort towards automating git repo creation under the same name as the project folder with an empty README.md

## Before you execute the script:

Update your github credentials in cred.py


**Requirements :**

    1. Python
        1.1 PyGithub

## Create folder as said in createRepo
**Installing createProject**

Install using the given command after cloning, make sure to update the cred.py in the git_create folder before installing

```
python setup.py install
```


**Help Details:**
```
usage: git-create [-h] -n NAME [-p [PRIVATE]] [-hi [HAS_ISSUES]] [-d [DESCRIPTION]]

optional arguments:
  -h, --help            show this help message and exit
  -p [PRIVATE], --private [PRIVATE]
                        Set repository to private if set to True. By default the repository is set to public.
  -hi [HAS_ISSUES], --has-issues [HAS_ISSUES]
                        Has issues?.
  -d [DESCRIPTION], --description [DESCRIPTION]
                        Set description.

required named arguments:
  -n NAME, --name NAME  Set the name of the repository.
```

**Example :**
```
git-create -n test_repo -p True -hi False -d "This is a sample description"
```
