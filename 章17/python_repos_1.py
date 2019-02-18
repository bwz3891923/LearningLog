import sys
import requests

def repo_list(x):
    print("Selected information about first repository,")
    print('Name:',x['name'])
    print('Owner:',x['owner']['login'])
    print('Stars:',x['stargazers_count'])
    print('Repository:',x['html_url'])
    print('Created:',x['created_at'])
    print('Updared:',x['updated_at'])


    try:
        print('Description:',x['description'])

    except UnicodeEncodeError:
        non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
        x['description']=x['description'].translate(non_bmp_map)
        print('Description:',x['description'])
        print("********This descroption has the error of 'UCS-2'*******\n")

    else:
        print('\n\n')



def main():  
    url='https://api.github.com/search/repositories?q=language:python&sort=stars'
    r=requests.get(url)
    print("Status code:",r.status_code)

    response_dict=r.json()
    print(response_dict.keys())
    print("Total repositories:",response_dict['total_count'])

    repo_dicts = response_dict['items']
    print("Repositories returned:",len(repo_dicts))

    repo_dict=repo_dicts[0]
    print("\nKeys:",len(repo_dict))
    for key in sorted(repo_dict.keys()):
        print(key)

    repo_whole(repo_dicts)


def repo_whole(repo_dicts,num=100):
    i=1
    for repo_dict in repo_dicts[:num]:
        print(i)
        i+=1
        repo_list(repo_dict)











main()
