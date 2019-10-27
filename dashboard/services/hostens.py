import requests
from requests.auth import HTTPBasicAuth

from services.base import BaseService


class Hostens(BaseService):

    def start(self, login, password, data):

        service_id = None
        service_domain = None
        server_name = None

        if "id" in data:
            service_id = data["id"]
            server_name = service_id
        elif "domain" in data:
            service_domain = data["domain"]
            server_name = service_domain

        if (service_domain, service_id,) == 2 * (None,):
            return {}

        if not service_id:
            try:
                resp = requests.get("https://billing.hostens.com/api/service", auth=HTTPBasicAuth(login, password)).json()
                s_id = [x["id"] for x in resp["services"] if x["domain"] == service_domain]
                service_id = s_id[0]
            except Exception as e:
                print(e)
                return
            if not s_id:
                return {}

        try:
            resp = requests.get(
                "https://billing.hostens.com/api/service/{service_id}".format(**locals()),
                auth=HTTPBasicAuth(login, password)
            ).json()
            due_date = resp['service']['next_due']
            cost = resp['service']['total']
            resp = requests.get(
                "https://billing.hostens.com/api/invoices",
                auth=HTTPBasicAuth(login, password)
            ).json()
            if resp.get('invoices', [{}])[-1].get('status', 'Paid') != 'Paid':
                due_date = resp['invoices'][-1]['paybefore']
            result = {
                'server': server_name,
                'date': due_date,
                'cost': cost,
            }
            return result
        except Exception as e:
            print(e)
            return {}
