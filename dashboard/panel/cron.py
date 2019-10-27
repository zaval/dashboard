from datetime import datetime

from django_cron import CronJobBase, Schedule
from webpush import send_user_notification

import services
from panel.models import *


class RamnodeCron(CronJobBase):
    RUN_EVERY_MINS = 60*24
    code = 'cron.ramnode'

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)

    def do(self):
        tasks = ParseTask.objects.filter(service='RN')
        users = []
        now = datetime.now()
        for task in tasks:

            rn = services.ParseService("RN")
            data = rn.start(task.login, task.password, task.extra_data)
            task.result = data
            task.save()
            d = datetime.strptime(data['date'], '%Y-%m-%d')
            if (d - now).days < 5:
                users.append(task.user)

        for user in users:

            send_user_notification(
                user=user,
                payload={
                    'head': 'Сервис требует внимания',
                    'body': 'На сервисе Ramnode заканчиваются деньги!'
                },
                ttl=604800
            )


class KeyCDNCron(CronJobBase):
    RUN_EVERY_MINS = 60
    code = 'cron.keycdn'

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)

    def do(self):
        tasks = ParseTask.objects.filter(service='KC')
        for task in tasks:
            rn = services.ParseService("KC")
            data = rn.start(task.login, task.password, task.extra_data)
            task.result = data
            task.save()


class Google_AdSenseCron(CronJobBase):
    RUN_EVERY_MINS = 10
    code = 'cron.adsense'

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)

    def do(self):
        tasks = ParseTask.objects.filter(service='AS')
        for task in tasks:
            rn = services.ParseService("AS")
            data = rn.start(task.login, task.password, task.extra_data)
            task.result = data
            task.save()


class HostensCron(CronJobBase):
    RUN_EVERY_MINS = 60*24
    code = 'cron.hostens'

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)

    def do(self):
        tasks = ParseTask.objects.filter(service='HS')
        users = []
        now = datetime.now()
        for task in tasks:
            rn = services.ParseService("HS")
            data = rn.start(task.login, task.password, task.extra_data)
            task.result = data
            task.save()
            d = datetime.strptime(data['date'], '%Y-%m-%d')
            if (d - now).days < 5:
                users.append(task.user)

        for user in users:
            send_user_notification(
                user=user,
                payload={
                    'head': 'Сервис требует внимания',
                    'body': 'На сервисе Hostens заканчиваются деньги!'
                },
                ttl=604800
            )


class FastvpsCron(CronJobBase):

    RUN_EVERY_MINS = 60*24
    code = 'cron.fastvps'

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)

    def do(self):
        tasks = ParseTask.objects.filter(service='FV')
        users = []
        now = datetime.now()
        for task in tasks:
            rn = services.ParseService("FV")
            data = rn.start(task.login, task.password, task.extra_data)
            token = data.pop('token')
            extra_data = task.extra_data
            extra_data['token'] = token
            task.extra_data = extra_data
            task.result = data
            task.save()
            d = datetime.strptime(data['date'], '%Y-%m-%d')
            if (d - now).days < 5:
                users.append(task.user)

        for user in users:

            send_user_notification(
                user=user,
                payload={
                    'head': 'Сервис требует внимания',
                    'body': 'На сервисе FastVPS заканчиваются деньги!'
                },
                ttl=604800
            )
