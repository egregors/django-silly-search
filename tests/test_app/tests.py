# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.test import TestCase
from silly_search import q_search
from .models import Article, Item, News


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

    def test_search_for_few_models(self):
        items_1 = Item.objects.create(
            title='Electric guitar',
            description='Cool guitar for cool kids',
            price=1000.0
        )

        items_2 = Item.objects.create(
            title='Doll',
            description='Nice gift',
            price=100.0
        )

        news_1 = News.objects.create(
            title='We got new guitars!',
            text='Text about new guitar'
        )

        news_2 = News.objects.create(
            title='New toys!',
            text='Text about new toys'
        )

        article_1 = Article.objects.create(
            title='Same article',
            description='Desc for same article',
            text='Text for same article'
        )

        article_2 = Article.objects.create(
            title='Article about famous guitarists',
            description='Desc for article',
            text='Text for article'
        )

        result = q_search(
            models=[Article, News, Item],
            fields=['title', 'description', 'text'],
            q='guitar'
        )

        self.assertEqual(len(result), 3)
        self.assertIn(items_1, result)
        self.assertIn(news_1, result)
        self.assertIn(article_2, result)
