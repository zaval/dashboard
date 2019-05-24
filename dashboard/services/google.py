from googleapiclient.discovery import build
from httplib2 import Http
# from oauth2client import client, tools
from oauth2client import client


class Google_AdSense():

    def start(self, login, password, data):
        creds = client.Credentials.new_from_json(data['auth'])
        service = build('adsense', 'v1.4', http=creds.authorize(Http()))
        accounts = service.accounts().list().execute()
        account_id = accounts['items'][0]['id']
        res = service.accounts().reports().generate(startDate='today', endDate='today', dimension=['DATE'], metric=['EARNINGS'], accountId=account_id).execute()
        print(res)
        return {
            'cost': res['totals'][1]
        }
