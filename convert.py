from json2xml import json2xml
from json2xml.utils import readfromurl, readfromstring, readfromjson

data = readfromjson("Action_repo1/response.json")
xml_data = json2xml.Json2xml(data).to_xml()
