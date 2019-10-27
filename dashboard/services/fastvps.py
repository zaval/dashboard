import requests

from services.base import BaseService


class FastVPS(BaseService):

    def start(self, login, password, data):

        if 'token' not in data or 'ip' not in data:
            return {}
        token = data['token']
        ip = data['ip']

        try:

            resp = requests.post(
                'https://bill2fast.com/api/v1/token/refresh',
                data='{"refresh_token":"%s"}' % token,
                headers={
                    'X-Requested-With': 'XMLHttpRequest',
                    'Accept': 'application/json, text/plain, */*',
                    'Content-Type': 'application/json;charset=utf-8',
                }
            ).json()

            bearer = resp['token']
            refresh_token = resp['refresh_token']

            resp = requests.get(
                'https://bill2fast.com/api/v1/services?category=vps&direction=desc&include=product,options,node,billing,ips,invoices,estimate&limit=20&order=id&page=1',
                headers={
                    'Authorization': 'Bearer {}'.format(bearer)
                }
            ).json()
            for server in resp['data']:
                if server.get('ip', '') == ip:
                    result = {
                        'server': ip,
                        'date': server['billing']['due_at'].split('T')[0],
                        'cost': server['billing']['amount'],
                        'token': refresh_token,
                    }
                    return result
        except Exception as e:
            print(e)
            return {}
