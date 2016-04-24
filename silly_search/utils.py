# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import operator
from functools import reduce

from django.core.exceptions import FieldDoesNotExist
from django.db.models import Q
from django.db.models.base import ModelBase


def q_search(models=(), fields=(), q=None):
    # type: (tuple(BaseModel), tuple(str)) -> list(QuerySet)
    """
        TODO: Add Docs
    """
    if not isinstance(models, tuple) or not isinstance(fields, tuple):
        raise TypeError('"models" and "fields" must be tuple')

    if not len(models) > 0 and not len(fields) > 0:
        raise TypeError('"models" and "fields" arguments can not be empty')

    result = list()
    predicates = list()
    for model in models:
        if not isinstance(model, ModelBase):
            raise TypeError('"fields" argument can not be empty')

        if len(fields) > 0:
            for field in fields:
                try:
                    if model._meta.get_field(field):
                        predicates.append((field + '__icontains', q))
                except FieldDoesNotExist:
                    # TODO: make something
                    pass

            q_list = [Q(x) for x in predicates]
            if len(q_list) > 0:
                q_result = model.objects.filter(reduce(operator.or_, q_list))
                if len(q_result) > 0:
                    result.append(q_result)

        return result
