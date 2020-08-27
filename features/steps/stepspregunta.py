
from behave import *
import requests

@given('{fields} to sent in the form')
def step_impl(context, entity):
    context.api_url = 'http://localhost:8000/insert/preguntas'
    response = requests.get(url=context.api_url, headers="")
    context.texto = response.text

@when('the user insert the data')
def step_impl(context):
    pass

@then('the fields have {information}')
def step_impl(context, fields):
    assert (fields in context.texto)