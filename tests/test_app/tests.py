# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.test import TestCase
from silly_search import q_search
from .models import Article


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

    def test_search_for_one_model(self):
        article = Article.objects.create(
            title='The good thing about science',
            description='Neil deGrasse Tyson',
            text="The good thing about science is that "
                 "it's true whether or not you believe in it."
        )

        # field 'title'
        result = q_search(Article, 'title', 'science')
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], article)

        # field 'desc'
        result = q_search(Article, 'description', 'Tyson')
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], article)

        # field 'text'
        result = q_search(Article, 'text', 'good thing about science')
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], article)

        # fields 'title' or 'text'
        result = q_search(Article, ['title', 'text'], 'science')
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], article)

        # fields 'title' with wrong 'spam'
        result = q_search(Article, ['title', 'spam'], 'science')
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], article)

        # bad search phrase
        result = q_search(Article, 'title', q='spam')
        self.assertEqual(len(result), 0)
