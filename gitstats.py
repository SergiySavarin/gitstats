"""This module take statistic data from github.com.
Data includes names of git users, user's repositories, names commits
contributors, additions and deletions, total commits by days, weeks
and by last year.
"""
import json
import urllib

GIT_URL = 'https://api.github.com/'

def git_user_repos(user):
    """Form a list of user repos from github.com.
    Args:
        user: name of user , as string
    Return:
        All user repos info , or None
    """
    user_url = GIT_URL + user + '/repos'
    response = urllib.urlopen(user_url)
    if response is not None:
        return json.loads(response.read())
    return None


def git_user_repo_stats(user, repo):
    """Form a list of user stats from github.com  by selected repo for all time.
        Print users list. Print selected user repos list. Connect to api url
        and read statistic data. Load data like a json.
    Args:
        user: user name as string
        repo: repo name as string
    Returns:
        Statistic list selected user's repo. List include contributors names,
        commit's week, total commits, additions and deletions.

    """
    result = []
    repo_url = GIT_URL + 'repos/' + user + '/' + repo + 'stats/contributors'
    response = urllib.urlopen(repo_url).read()
    if response is not None:
        content = response.read()
        if content is not None:
            data = json.loads(content)
            for line in data:
                author = line['author']
                result.append(author[u'login'])
                for week in line['weeks']:
                    lst = []
                    if week['c']:
                        lst.append(week['w'])
                        lst.append(week['c'])
                        lst.append(week['a'])
                        lst.append(week['d'])
                    result.append(lst)
            return result
    return None

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


print_git_user_repo_stats_per_year()
