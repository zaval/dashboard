import os
from django.test import TestCase

import services
from panel.models import ParseTask
# Create your tests here.


class PanelTestCase(TestCase):

    def service_run(self, data, service):
        task = ParseTask(**data)
        rn = services.ParseService(service)
        data = rn.start(task.login, task.password, task.extra_data)
        task.result = data
        task.save()
        return task.pk

    def test_google(self):
        pass