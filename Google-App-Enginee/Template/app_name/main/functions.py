import calendar
import datetime
import decimal
import re
import logging
from flask import Response


__author__ = "DC"
__version__ = "0.1"


def json_serial(obj):
    """Default JSON serializer."""

    if isinstance(obj, datetime.datetime):
        if obj.utcoffset() is not None:
            obj = obj - obj.utcoffset()
        millis = int(
            calendar.timegm(obj.timetuple()) * 1000 + obj.microsecond / 1000
        )
        return millis

    if isinstance(obj, decimal.Decimal):
        return float(obj)

    raise TypeError('Object of type %s with value of %s is not JSON serializable' % (type(obj), repr(obj)))


def to_json(dicts):
    import json

    return json.dumps(dicts, default=json_serial)


def json_response(response):

    return Response(to_json(response), mimetype='application/json')


def entities_to_dicts(entities):
    dicts = []

    for entity in entities:
        dicts.append(entity_to_dict(entity))

    return dicts


def entity_to_dict(entity):
    e = entity.to_dict()
    e["_hash"] = entity.key.urlsafe()

    return e


def get_value_from_dict(dic, key):
    if key in dic.keys():
        return dic.get(key)
    else:
        logging.log(logging.WARN, to_json(dic))

        raise ValueError("Key not found in dictionary: " + key)


def blank_str_to_int(s=""):
    s = s.strip()

    return int(s) if s else 0


# Lowercase function
def lowercase_match_group(match_obj):

    return match_obj.group().lower()


# Make titles human friendly
# http://daviseford.com/python-string-to-title-including-punctuation
def title_extended(title):
    if title is not None:
        # Take advantage of title(), we'll fix the apostrophe issue afterwards
        title = title.title()

        # Special handling for contractions
        poss_regex = r"(?<=[a-z])[\']([A-Z])"
        title = re.sub(poss_regex, lowercase_match_group, title)

    return title


def title_one_liner(title):

    return re.sub(r"(?<=[a-z])[\']([A-Z])", lambda x: x.group().lower(), title.title())
