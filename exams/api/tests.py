import datetime
from http import HTTPStatus

from indicators.models import IndicatorsMetrics, References, Scores
from mixer.backend.django import mixer
from public.models import Labs, Tests
from rest_framework.test import APITestCase


class TestsAPIViewTests(APITestCase):
    tests_url = "/api/tests/"

    def setUp(self):
        self.indicators_metrics = mixer.cycle(4).blend(IndicatorsMetrics)
        self.references = mixer.cycle(4).blend(
            References, indicator_metric_id__in=self.indicators_metrics
        )
        self.lab = mixer.blend(Labs)
        self.other_lab = mixer.blend(Labs)
        self.tests = mixer.cycle(3).blend(
            Tests,
            lab_id=self.lab,
            started_at=datetime.datetime.now(),
            completed_at=datetime.datetime.now() + datetime.timedelta(seconds=100),
        )
        self.tests = mixer.cycle(3).blend(Tests, lab_id=self.lab)
        self.tests = mixer.cycle(3).blend(
            Tests,
            lab_id=self.other_lab,
            started_at=datetime.datetime.now(),
            completed_at=datetime.datetime.now() + datetime.timedelta(seconds=100),
        )
        self.scores = mixer.cycle(3).blend(Scores, test_id__in=self.tests)

    def test_api_response(self):
        response = self.client.get(self.tests_url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_lab_filter(self):
        response = self.client.get(self.tests_url + f"?lab_id={self.lab.id}")
        for lab in response.data:
            self.assertEqual(lab.get("lab_id"), self.lab.id)

    def test_without_filter_lab(self):
        count = len(Tests.objects.all().exclude(completed_at__isnull=True))
        response = self.client.get(self.tests_url)
        self.assertEqual(count, len(response.data))
