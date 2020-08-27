
from behave import *
import requests

#Pregunta.feature Get data to modify________________________________________________
@given('a {pre_id} {pre_texto} {cat_id} {com_id} {tpr_id} to update information')
def step_impl(context, pre_id, pre_texto, cat_id, com_id, tpr_id):
    context.api_url = 'http://localhost:8000/insert/pregunta'
    
@when('the fields are updated')
def step_impl(context):
    response = requests.get(url=context.api_url, headers="")
    context.texto = "Los campos fueron actualizados"

@then('the {fields} are modified')
def step_impl(context, fields):
    assert (fields in context.texto)

#Prueba.feature Get data to list_______________________________________________
@given('a {pre_id} {pre_texto} {cat_id} {com_id} {tpr_id} to show information')
def step_impl(context, pre_id, pre_texto, cat_id, com_id, tpr_id):
    context.api_url = 'http://localhost:8000/insert/pregunta'
    
@when('the fields are called')
def step_impl(context):
    response = requests.get(url=context.api_url, headers="")
    context.texto = "Los campos fueron listados"

@then('the {fields} are showed')
def step_impl(context, fields):
    assert (fields in context.texto)