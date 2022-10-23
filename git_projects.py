
import requests
username = "sabhapathi0306"

url = f"https://api.github.com/users/{username}/repos"



results = requests.get(f'https://api.github.com/users/{username}/repos').json()
class GitRepos:
    def git(self):
        data = results
        stared_git_dict = {}
        for i in data:
            if i['stargazers_count'] !=0 and i['fork']== False:
                stared_git_dict[i['name']] = i['html_url']

        return stared_git_dict
    def git_non(self):
        non_star_repo= {}
        for i in results:
            if i['stargazers_count'] == 0 and i['fork']== False:
                non_star_repo[i['name']] = i['html_url']

        return non_star_repo
