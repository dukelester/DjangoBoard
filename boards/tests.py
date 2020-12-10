# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.
import django.core.urlresolvers
from django.test import TestCase
from django.urls import reverse


class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('Home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)