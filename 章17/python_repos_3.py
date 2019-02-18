import sys
import pygal
import requests
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

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
    url='https://api.github.com/search/repositories?q=language:java&sort=stars'
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
    draw_repos(repo_dicts)


def repo_whole(repo_dicts,num=100):
    i=1
    for repo_dict in repo_dicts[:num]:
        print(i)
        i+=1
        repo_list(repo_dict)


def draw_repos(dict_repos):
    names,plot_dicts=[],[]
    for dict_repo in dict_repos:
        names.append(dict_repo['name'])
        
        plot_dict={'value':dict_repo['stargazers_count'],
                   'label':dict_repo['description'],
                   'xlink':dict_repo['html_url'],
                   }
        plot_dicts.append(plot_dict)

    my_style=LS('#336699',base_style=LCS)
    
    my_config=pygal.Config()
    my_config.x_label_rotation=45
    my_config.show_legend=False
    my_config.title_font_size=24
    my_config.label_font_size=14
    my_config.major_label_font_size=18
    my_config.truncate_label=15
    my_config.show_y_guides= False
    my_config.width=1000
    
    
    chart= pygal.Bar(my_config,style=my_style)
    chart.title='Most-Starred Python Projects on Github'
    chart.x_labels =names

    chart.add('',plot_dicts)
    chart.render_to_file('python_repos_java.svg')












main()
