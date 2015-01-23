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
    user_url = GIT_URL + 'users/' + user + '/repos'
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
    repo_url = GIT_URL + 'repos/' + user + '/' + repo + '/stats/contributors'
    response = urllib.urlopen(repo_url).read()
    if response is not None:
        content = response
        if content is not None:
            data = json.loads(content)
            for line in data:
                author = line['author']
                result.append(str(author[u'login']))
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


def git_user_repo_last_year_full_stats(user, repo):
    """Form a list of user stats from github.com  by selected repo for all time.
        Print users list. Print selected user repos list. Connect to api url
        and read statistic data. Load data like a json.
    Args:
        user: user name as string
        repo: repo name as string
    Returns:
        Statistic list selected user's repo. List include contributors names,
        commit's week, total commits, additions and deletions, commits per day 
        weekly, statistic include last year.
    """
    result = []
    repo_url1 = GIT_URL + 'repos/' + user + '/' + repo + '/stats/contributors'
    repo_url2 = GIT_URL + 'repos/' + user + '/' + repo + '/stats/commit_activity'
    response1 = urllib.urlopen(repo_url1).read()
    response2 = urllib.urlopen(repo_url2).read()
    if response1 is not None:
        content1 = response1
        if content1 is not None:
            data1 = json.loads(content1)
            data2 = json.loads(response2)
            for line1 in data1:
                author = line1['author']
                result.append(str(author[u'login']))
                for week in line1['weeks']:
                    lst = []
                    if week['c']:
                        for line2 in data2:
                            if week['w'] == line2['week']:
                                lst.append(week['w'])
                                lst.append(week['c'])
                                lst.append(week['a'])
                                lst.append(week['d'])
                                lst.append(line2['days'])
                                result.append(lst)
            return result
    return None