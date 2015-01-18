import urllib
import json

#List Git users

def git_users():
    list = []
    url = urllib.urlopen('https://api.github.com/users').read()
    info = json.loads(url)
    print 'User counts:', len(info)
    for line in info:
        a = str(line['login'])
        list.append(a)
    return sorted(list)

#List users's repos
      
def git_user_repos(user):
    repos = []
    u = 'https://api.github.com/users/%s/repos' % (user)
    url = urllib.urlopen(u).read()
    info = json.loads(url)
    print 'User repos counts:', len(info)
    for line in info:
        a = str(line['name'])
        repos.append(a)
    return sorted(repos)

#List user's stats by repo additions deletions total commits by week

def git_user_repo_stats():
    for i in git_users():    
        print i    
    print
    user = raw_input('Enter User Name:') 
    print
    for i in git_user_repos(user):    
        print i        
    print
    repo = raw_input('''Enter User's Repo Name:''') 
    print
    list = []
    u1 = 'https://api.github.com/repos/%s/%s/stats/contributors' % (user,repo)
    url1 = urllib.urlopen(u1).read()
    info1 = json.loads(url1)
    for line in info1:
        a = line['author']
        list.append(str(a[u'login']))
        for w in line['weeks']:
            lst = []
            if w['c'] !=0:
                lst.append(w['w'])
                lst.append(w['c'])
                lst.append(w['a'])
                lst.append(w['d'])
                list.append(lst)
    return list

#List user's stats by repo total commits, weekly commits, daily commits for last year

def git_user_repo_stats_weekly_per_year():
    for i in git_users():    
        print i    
    print
    user = raw_input('Enter User Name:') 
    print
    for i in git_user_repos(user):    
        print i        
    print
    repo = raw_input('''Enter User's Repo Name:''') 
    print
    last_y = []
    u2 = 'https://api.github.com/repos/%s/%s/stats/commit_activity' % (user,repo)
    url2 = urllib.urlopen(u2).read()
    info2 = json.loads(url2)
    for line in info2:
        last = []
        if line['total'] != 0:
            last.append(line['week'])
            last.append(line['total'])
            last.append(line['days'])
            last_y.append(last)
    return last_y

#Print list user's stats by repo total commits, weekly commits, daily commits for last year

def print_git_user_activity_per_year():
    for i in git_user_repo_stats_weekly_per_year():
        for k in i:
            print 'Week', i[0]
            print 'Total commits per week', i[1]
            print 'Days', i[2]

#Print list user's stats by repo additions deletions total commits by week

def print_git_user_repo_stats():
    for i in git_user_repo_stats():
        if type(i) == str:
            print
            print 'Author:', i
            print
        else:
            print 'Week', i[0]
            print 'Total commits per week', i[1]
            print 'Additions', i[2]
            print 'Deletions', i[3]
    
#Print list user's stats by repo total commits, weekly commits, daily commits for last year per week

def print_git_user_repo_stats_per_year():
    for i in git_users():    
        print i    
    print
    user = raw_input('Enter User Name:') 
    print
    for i in git_user_repos(user):    
        print i        
    print
    repo = raw_input('''Enter User's Repo Name:''') 
    print
    list = []
    last_y = []
    u1 = 'https://api.github.com/repos/%s/%s/stats/contributors' % (user,repo)
    u2 = 'https://api.github.com/repos/%s/%s/stats/commit_activity' % (user,repo)
    url1 = urllib.urlopen(u1).read()
    url2 = urllib.urlopen(u2).read()
    info1 = json.loads(url1)
    info2 = json.loads(url2)
    for line in info1:
        a = line['author']
        list.append(str(a[u'login']))
        for w in line['weeks']:
            lst = []
            if w['c'] !=0:
                lst.append(w['w'])
                lst.append(w['c'])
                lst.append(w['a'])
                lst.append(w['d'])
                list.append(lst)
    for line in info2:
        last = []
        if line['total'] != 0:
            last.append(line['week'])
            last.append(line['total'])
            last.append(line['days'])
            last_y.append(last)
    for i in list:
        if type(i) == str:
            print
            print 'Author:', i
            print
        
        for k in last_y:
            #for t in k:
            if k[0] == i[0]:
                print 'Week', k[0]
                print 'Total commits per week', k[1]
                print 'Days', k[2]
                print 'Additions per week', i[2]
                print 'Deletions per week', i[3]


#print_git_user_repo_stats_per_year()