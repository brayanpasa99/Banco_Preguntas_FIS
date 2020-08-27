
from behave import *
import requests

#CRUD.feature Insert information in fields_______________________________
@given('an {entity} and {fields} to insert in DB')
def step_impl(context, entity, fields):
    context.api_url = 'http://localhost:8000/insert/' + entity
    context.entity = entity
    context.fields = fields
    
@when('the user inserts the information in fields')
def step_impl(context):
    response = requests.get(url=context.api_url, headers="")
    context.texto = context.fields+" was insert in "+context.entity

@then('the register was created with {data}')
def step_impl(context, data):
    assert (data in context.texto)

#CRUD.feature Get data to erase_____________________________________________________
@given('an {fieldid} and an {entity} to erase information')
def step_impl(context, fieldid, entity):
    context.api_url = 'http://localhost:8000/insert/pregunta'
    context.fieldid = fieldid
    context.entity = entity
    
@when('the register with {id} will be erased')
def step_impl(context, id):
    response = requests.get(url=context.api_url, headers="")
    context.texto = "El registro "+id+" en el campo "+context.fieldid+" fue borrado en la tabla "+context.entity

@then('the {register} was erased')
def step_impl(context, register):
    assert (register in context.texto)