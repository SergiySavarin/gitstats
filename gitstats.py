import urllib
import json
"""This module take statistic data from github.com.  

Data includes names of git users, user's repositories, names commits contributors, 
additions and deletions, total commits by days, weeks and by last year.  

"""

# List Git users.  

def git_users():
    """Form a list of users from github.com.  
    
    Connect to api url and read data.  
    Load data like a json.  
    Print quantity of users.  
    Return sorted list of users names.  
    
    """
    list = []
    url = urllib.urlopen('https://api.github.com/users').read()
    info = json.loads(url)
    print 'User counts:', len(info)
    
    # Creating list of git users.  
    for line in info:
        a = str(line['login'])
        list.append(a)
    return sorted(list)

# List users's repos.  
      
def git_user_repos(user):
    """Form a list of user repos from github.com.  
    
    Connect to api url and read data.  
    Load data like a json.  
    Print quantity of repos.  
    Return sorted list of repos names.  
    
    """
    repos = []
    u = 'https://api.github.com/users/%s/repos' % (user)
    url = urllib.urlopen(u).read()
    info = json.loads(url)
    print 'User repos counts:', len(info)
    
    # Creating list of git user repos.  
    for line in info:
        a = str(line['name'])
        repos.append(a)
    return sorted(repos)

# List user's stats by repo additions deletions total commits by week

def git_user_repo_stats():
    """Form a list of user stats from github.com  by selected repo for all time.  
    
    Print users list.  
    Print selected user repos list.  
    Connect to api url and read statistic data.  
    Load data like a json.  
    Return statistic list selected user's repo.  
    List include contributors names, commit's week, total commits, 
    additions and deletions.  
        
    """
    
    # Printing list of git users.  
    for i in git_users():    
        print i    
    print
    user = raw_input('Enter User Name:') 
    print
    
    # Printing list of git user repos.  
    for i in git_user_repos(user):    
        print i        
    print
    repo = raw_input('''Enter User's Repo Name:''') 
    print
    list = []
    u1 = 'https://api.github.com/repos/%s/%s/stats/contributors' % (user,repo)
    url1 = urllib.urlopen(u1).read()
    info1 = json.loads(url1)
    
    # Creating statistic list of git user's repo.  
    for line in info1:
        a = line['author']
        list.append(str(a[u'login']))        # Adding contributor's name.  
        for w in line['weeks']:
            lst = []
            if w['c'] !=0:
                lst.append(w['w'])           # Adding week number.  
                lst.append(w['c'])           # Adding total commits number.  
                lst.append(w['a'])           # Adding additions number.  
                lst.append(w['d'])           # Adding deletions number.  
                list.append(lst)
    return list

# List user's stats by repo total commits, weekly commits, daily commits for last year

def git_user_repo_stats_weekly_per_year():
    """Form a list of user stats from github.com  by selected repo for last year weekly.  
    
    Print users list.  
    Print selected user repos list.  
    Connect to api url and read statistic data.  
    Load data like a json.  
    Return statistic list selected user's repo.  
    List include commit's week, total commits, quantity commits by day.  
        
    """
    
    # Printing list of git users.  
    for i in git_users():    
        print i    
    print
    user = raw_input('Enter User Name:') 
    print
    
    # Printing list of git user repos.  
    for i in git_user_repos(user):    
        print i        
    print
    repo = raw_input('''Enter User's Repo Name:''') 
    print
    last_y = []
    u2 = 'https://api.github.com/repos/%s/%s/stats/commit_activity' % (user,repo)
    url2 = urllib.urlopen(u2).read()
    info2 = json.loads(url2)
    
    # Creating statistic list of git user's repo.  
    for line in info2:
        last = []
        if line['total'] != 0:
            last.append(line['week'])        # Adding week number.  
            last.append(line['total'])       # Adding total commits number.  
            last.append(line['days'])        # Adding days with total commits by day.  
            last_y.append(last)
    return last_y

# Print list user's stats by repo total commits, 
# weekly commits, daily commits for last year.  

def print_git_user_activity_per_year():
    """Printing a list of user stats from github.com  
    by selected repo for last year weekly.  
    List include commit's week, total commits, 
    quantity commits by day.  
        
    """
    for i in git_user_repo_stats_weekly_per_year():
        for k in i:
            print 'Week', i[0]
            print 'Total commits per week', i[1]
            print 'Days', i[2]

# Print list user's stats by repo additions deletions total commits by week.  

def print_git_user_repo_stats():
    """Printing a list of user stats from github.com  
    by selected repo for last year weekly.  
    List include contributors names, commit's week, 
    total commits, additions and deletions.  
        
    """
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
    
# Print list user's stats by repo total commits, 
# weekly commits, daily commits for last year per week.  

def print_git_user_repo_stats_per_year():
    """Form a list of user stats from github.com  by selected repo for last year weekly.  
    
    Print users list.  
    Print selected user repos list.  
    Connect to api url and read statistic data.  
    Load data like a json.  
    Return statistic list selected user's repo.  
    List include contributors names, commit's week, 
    total commits, quantity commits by day, additions and deletions.  
        
    """
    
    # Printing list of git users.  
    for i in git_users():    
        print i    
    print
    user = raw_input('Enter User Name:') 
    print
    
    # Printing list of git user repos.  
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
    
    # Creating statistic list of git user's repo.  
    for line in info1:
        a = line['author']
        list.append(str(a[u'login']))        # Adding contributor's name.  
        for w in line['weeks']:
            lst = []
            if w['c'] !=0:
                lst.append(w['w'])           # Adding week number.  
                lst.append(w['c'])           # Adding total commits number.  
                lst.append(w['a'])           # Adding additions number.  
                lst.append(w['d'])           # Adding deletions number.  
                list.append(lst)
    for line in info2:
        last = []
        if line['total'] != 0:
            last.append(line['week'])        # Adding week number.  
            last.append(line['total'])       # Adding total commits number.  
            last.append(line['days'])        # Adding days with total commits by day.  
            last_y.append(last)
    
    # Printing a list of user stats.  
    for i in list:
        if type(i) == str:
            print
            print 'Author:', i
            print
        
        for k in last_y:
            if k[0] == i[0]:
                print 'Week', k[0]
                print 'Total commits per week', k[1]
                print 'Days', k[2]
                print 'Additions per week', i[2]
                print 'Deletions per week', i[3]


# print_git_user_repo_stats_per_year()