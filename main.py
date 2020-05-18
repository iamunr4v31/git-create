from helper import createRepo, createFolder, gitInit, gitAdd, gitCommit, gitPush, gitRemote, openCode
import argparse

USAGE = '''
            usage: git create [-h] [--help] [-private P] [-name Name]

            required arguments:
            -n N, --name N            Set the name of the repository.


            optional arguments:
            -h, --help                Show this help message and exit
            -p P, --private P         Set repository to private if set to True. By default the repository is set to public.
            -d D, --description D     Set description


'''
def initParser():
    parser = argparse.ArgumentParser(prog='git create')
    parser.add_argument('-n','--name', required=True, nargs=1, help='Set the name of the repository.')
    parser.add_argument('-p','--private', nargs='?', default=False, type=bool, help='Set repository to private if set to True. By default the repository is set to public.')
    parser.add_argument('-hi','--has-issues', nargs='?',type=bool, default=True, help='Has issues?.')
    parser.add_argument('-d', '--description', nargs='?',type=str, default='', help='Set description.')
    args = parser.parse_args()
    return args

def main():
    args = initParser()
    ret = createFolder(args.name)
    # if 'Folder exists' in ret:
    #     print(ret)
    #     exit()
    ret_url = createRepo(args.name[0], description=args.description, private=args.private, has_issues=args.has_issues)
    gitInit()
    gitAdd()
    gitCommit()
    gitRemote(ret_url)
    gitPush()
    openCode()

    # print(args)

if __name__ == "__main__":
    main()
    


    