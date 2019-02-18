import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS
from operator import itemgetter

def main():
    url='https://hacker-news.firebaseio.com/v0/topstories.json'
    r=requests.get(url)
    print("Status code:",r.status_code)
    code_return(r)


def code_return(r):
    submission_ids=r.json()
    submission_dicts=[]
    for submission_id in submission_ids[:50]:
        url=('https://hacker-news.firebaseio.com/v0/item/'+
             str(submission_id)+'.json')
        
        submission_r=requests.get(url)
        print(submission_r.status_code)
        response_dict=submission_r.json()

        submission_dict={
            'title':response_dict['title'],
            'link':'https://news.ycombinator.com/item?id='+str(submission_id),
            'comments':response_dict.get('descendants',0),
            }
        submission_dicts.append(submission_dict)
        submission_dicts=sorted(submission_dicts,key=itemgetter('comments'),
                                reverse=True)

    print_of(submission_dicts)
    draw_picture(submission_dicts)

def print_of(xes):
    for x in xes:        
        print("\nTitle:",x['title'])
        print("Discussion:",x['link'])
        print("Comments:",x['comments'])


def draw_picture(datas):
    plot_dicts=[{'value':data['comments'],
                'label':data['title'],
                'xlink':data['link']}
               for data in datas]
  
    my_style=LS('#336699',base_style=LCS)
    chart=pygal.Bar(style=my_style,x_labelsize=45,show_legend=False)
    chart.title='Sorted Article of Hacker'
    chart.add('',plot_dicts)
    chart.render_to_file('Hacker.svg')
    



        



main()
