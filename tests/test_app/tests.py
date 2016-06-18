# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.test import TestCase
from silly_search import q_search
from .models import Article


def create_test_sets():
    pass


class SillySearchTestCase(TestCase):
    def setUp(self):
        pass

    def test_empty_arguments(self):
        with self.assertRaisesMessage(ValueError,
                                      '"models", "fields", "q" arguments can not be empty'):
            q_search()
            q_search(models=Article)
            q_search(models=Article, fields='title')
            q_search(models=Article, q='spam')
            q_search(fields='title')
            q_search(fields='title', q='spam')

    def test_bad_model_args(self):
        with self.assertRaisesMessage(TypeError,
                                      '"models" must be ModelBase or list of ModelBase'):
            q_search(models=42, fields='title', q='bar')

    def test_bad_fields_args(self):
        with self.assertRaisesMessage(TypeError,
                                      '"fields" must be str or list of str'):
            q_search(models=Article, fields=42, q='spam')
