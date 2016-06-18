# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import, print_function

import operator
from functools import reduce

from django.core.exceptions import FieldDoesNotExist
from django.db.models import Q
from django.db.models.base import ModelBase


def q_search(models=None, fields=None, q=None):
    """
    :param models: models for search
    :param fields: fields (strings) for search in each model
    :param q: query text

    :type models: list or ModelBase
    :type fields: list of str or str
    :type q: str

    :rtype: list
    :return: Model.filter() queryset

    example:
        q_search(models=[News, Post, Article], fields=['title', 'body', 'text'], q='spam')
        q_search(News, 'title', 'spam')
    """

    if not all([models, fields, q]):
        raise ValueError('"models", "fields", "q" arguments can not be empty')

    if not isinstance(models, ModelBase) and not isinstance(models, list):
        raise TypeError('"models" must be ModelBase or list of ModelBase')

    if not isinstance(fields, str) and not isinstance(fields, list):
        raise TypeError('"fields" must be str or list of str')

    result = list()
    predicates = list()
    q_list = list()

    # if models or fields are not list -> convert
    models_list = [models, ] if isinstance(models, ModelBase) else models
    fields_list = [fields, ] if isinstance(fields, str) else fields

    # construct query for each model
    for model in models_list:

        del predicates[:]
        del q_list[:]

        if not isinstance(model, ModelBase):
            raise TypeError('"models" must be ModelBase or list of ModelBase')

        for field in fields_list:
            try:
                if model._meta.get_field(field):
                    predicates.append((field + '__icontains', q))
            except FieldDoesNotExist:
                # field does not exist, go next
                pass

        q_list = [Q(x) for x in predicates]
        if q_list:
            q_result = model.objects.filter(reduce(operator.or_, q_list))

            if q_result:
                result += q_result

    return result
