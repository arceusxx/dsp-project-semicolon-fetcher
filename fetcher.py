import requests
from datetime import datetime, timedelta


one_day_ago = datetime.now() - timedelta(days=1)


since_date = one_day_ago.strftime("%Y-%m-%dT%H:%M:%SZ")


url = f'https://api.github.com/repos/Discord-AntiScam/scam-links/commits?since={since_date}'


headers = {'Authorization': 'GITHUB_TOKEN_HERE', 'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)


commits = response.json()


links = ';'.join(commit['commit']['message'].split()[-1] for commit in commits)


print(links)
