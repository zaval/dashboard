import re
import json
import requests

from services.base import BaseService


class KeyCDN(BaseService):

    def __init__(self):
        self.http = requests.Session()

    def start(self, login, password, data):
        page = self.http.get('https://app.keycdn.com/login').text

        token = re.search(r'name="data\[_Token\]\[key\]" value="([^"]+)', page)
        if not token:
            print('no token')
            return {}

        token_fields = re.search(r'name="data\[_Token\]\[fields\]" value="([^"]+)', page)
        if not token_fields:
            print('no token fields')
            return {}

        post = {
            '_method': 'POST',
            'data[_Token][key]': token.group(1),
            'data[User][username]': login,
            'data[User][password]': password,
            'data[User][code]': '',
            'data[_Token][fields]': token_fields.group(1),
            'data[_Token][unlocked]': '',
        }

        page = self.http.post('https://app.keycdn.com/login', post).text
        # print(page)

        page = self.http.get('https://app.keycdn.com/users/view').text

        credits_re = re.search(r'credits = (\[\[.+?]]);', page)
        if not credits_re:
            print(page)
            print('credits re')
            return {}

        credits_var = json.loads(credits_re.group(1))
        return {
            'cost': '%.2f' % credits_var[-1][1]
        }
