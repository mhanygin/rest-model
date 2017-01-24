# -*- coding: utf-8 -*-
import logging
import operator
from json import dumps, loads
from functools import reduce

from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.forms.models import model_to_dict
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db.models import Q

from . import modelName

logger = logging.getLogger(__name__)


def change_model(request, model, id):
    m = modelName.get(model, None)
    if m is None:
        return HttpResponse(dumps({'error': "model {model} not found".format(model=model)}),
                            content_type="application/json",
                            status=404)
    try:
        m = m.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponse(dumps({'error': "instance {id} not found".format(id=id)}),
                            content_type="application/json",
                            status=404)

    if request.method == "GET":
        return HttpResponse(dumps(model_to_dict(m, fields=[], exclude=[]), cls=DjangoJSONEncoder),
                            content_type="application/json")

    elif request.method == "PUT":
        fields = m._meta.get_all_field_names()
        for k, v in request.GET.items():
            if k not in fields:
                return HttpResponse(dumps({'error': "field {name} not found".format(name=k)}),
                                    content_type="application/json",
                                    status=404)
            setattr(m, k, v)
        try:
            m.full_clean()
        except ValidationError as e:
            print(e)
            return HttpResponse(dumps({'error': "validate error"}),
                                content_type="application/json",
                                status=404)
        m.save()
    elif request.method == "DELETE":
        m.delete()

    return HttpResponse(dumps({'error': "method {method} not support".format(method=request.method)}),
                        content_type="application/json",
                        status=405)


def new_model(request, model):
    m = modelName.get(model, None)
    if m is None:
        return HttpResponse(dumps({'error': "model {model} not found".format(model=model)}),
                            content_type="application/json",
                            status=404)
    if request.method == "GET":
        filter_list = [Q(**{key: val}) for key, val in request.GET.items()]
        print(filter_list)
        if filter_list:
            query = m.objects.filter(reduce(operator.or_, filter_list))
        else:
            query = m.objects.all()

        print(query)

        result = list()
        for i in query:
            result.append(model_to_dict(i, fields=[], exclude=[]))
        return HttpResponse(dumps(result, cls=DjangoJSONEncoder), content_type="application/json")

    elif request.method == "POST":
        params = loads(request.body.decode("utf-8"))
        fields = m._meta.get_all_field_names()
        for k, v in params.items():
            if k not in fields:
                return HttpResponse(dumps({'error': "field {name} not found".format(name=k)}),
                                    content_type="application/json",
                                    status=404)
        try:
            _m = m(**params)
            _m.save()
            return HttpResponse(dumps({'id': _m.id}),
                                content_type="application/json")
        except:
            return HttpResponse(status=400)

    return HttpResponse(dumps({'error': "method {method} not support".format(method=request.method)}),
                        content_type="application/json",
                        status=405)
