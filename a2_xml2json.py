__author__ = 'SANTHOSH'

from xmlutils.xml2json import xml2json

converter = xml2json("a2.xml", encoding="utf-8")

fjson = open("a2.json","w")

fjson.write(converter.get_json(pretty=True))
fjson.close()