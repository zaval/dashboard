from django_cron import CronJobBase, Schedule
import services
from panel.models import *


class RamnodeCron(CronJobBase):
    RUN_EVERY_MINS = 60*24
    code = 'cron.ramnode'

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)

    def do(self):
        tasks = ParseTask.objects.filter(service='RN')
        # print(tasks)
        for task in tasks:

            rn = services.ParseService("RN")
            data = rn.start(task.login, task.password, task.extra_data)
            # print(data)
            task.result = data
            task.save()


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
    RUN_EVERY_MINS = 1
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
        for task in tasks:
            rn = services.ParseService("HS")
            data = rn.start(task.login, task.password, task.extra_data)
            task.result = data
            task.save()
