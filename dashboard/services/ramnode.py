import datetime
import re
import requests


class RamNode:

    def __init__(self):
        self.http = requests.Session()

    def start(self, login, password, data):
        page = self.http.get('https://clientarea.ramnode.com/clientarea.php').text

        token = re.search(r'name="token" value="([^"]+)', page)
        if not token:
            print('no token')
            return {}

        token = token.group(1)

        post = {
            'token': token,
            'username': login,
            'password': password,
            'rememberme': 'on',
        }
        # print(post)

        page = self.http.post('https://clientarea.ramnode.com/dologin.php', post).text

        if 'href="/logout.php"' not in page:
            print('no login')
            return {}

        page = self.http.get('https://clientarea.ramnode.com/clientarea.php?action=services').text

        resp = re.search(r'target="_blank">{}[\s\S]+?data-order="([^"]+)[\s\S]+?<span class="hidden">([^<]+)'.format(data['server']), page)

        if resp:
            resp = resp.groups()
            return {
                'server': data['server'],
                'date': resp[1],
                'cost': resp[0],
                # 'class': 'red-text' if (datetime.datetime.strptime(resp[1], '%Y-%m-%d') - datetime.datetime.now()).days < 15 else '',
                # 'alert': (datetime.datetime.strptime(resp[1], '%Y-%m-%d') - datetime.datetime.now()).days < 15
            }
        else:
            print('no data')
            return {}