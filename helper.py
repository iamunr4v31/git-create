from github import Github
import subprocess
from cred import username, passw
import os

def execCmd(cmd):
    '''
        Executes any terminal command
    '''
    try:
        result = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        return result
    
    except Exception:
        return 'Could not execute function'


def createRepo(name, description='', private=False, has_issues=True,):
    '''
        Creates a repository in Github
    '''
    
    
    g = Github(username, passw)
    user = g.get_user()
    repo = user.create_repo(name, description=description, private=private, has_issues=has_issues)
    return 'https://github.com/' + repo.full_name

def createFolder(name):

    '''
        Creates the said folder in said directory
    '''
    try:
        # print(os.getcwd())
        os.cd(os.path.abspath(os.path.dirname(__file__)))
        create = execCmd(['mkdir', name])
        out = create.stdout.readline().decode('utf-8').strip()
        if 'cannot create dir' in out:
            raise ZeroDivisionError

    except Exception:
        out = 'Folder exists. Try another name.'

    finally:
        return out

def gitInit():
    try:
        result = execCmd(['git', 'init'])
        out = result.stdout.readline().decode('utf-8').strip()
        print(out)

    except AttributeError:
        print(result)

def gitAdd():
    try:
        os.system('echo > README.md')
        result = execCmd(['git', 'add', '.'])
        out = result.stdout.readline().decode('utf-8').strip()
        print(out)

    except AttributeError:
        print(result)


def gitCommit():
    try:
        result = execCmd(['git', 'commit', '-m', '\"initial commit\"'])
        out = result.stdout.readline().decode('utf-8').strip()
        print(out)

    except AttributeError:
        print(result)

def gitPush():
    try:
        result = execCmd(['git', 'push', '-u', 'origin', 'master'])
        out = result.stdout.readline().decode('utf-8').strip()
        print(out)

    except AttributeError:
        print(result)

def gitRemote(url):
    try:
        result = execCmd(['git', 'remote', 'add', 'origin', url])
        out = result.stdout.readline().decode('utf-8').strip()
        print(out)

    except AttributeError:
        print(result)


def openCode():
    try:
        '''didn't work with subprocess. need to figure out why and reduce the no. of imports'''
        # result = execCmd(['code', '.'])
        # out = result.stdout.readline().decode('utf-8').strip()
        # print(out)
        os.system('code .')

    except Exception:
        pass


# if __name__ == "__main__":
#     print(create_repo('test'))