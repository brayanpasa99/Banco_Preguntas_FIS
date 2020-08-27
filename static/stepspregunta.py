from behave import *
import requests


@given('a {entity} to insert data')
def step_impl(context, entity):
    url_buscar = 'http://localhost:8000/insertar' + entity
    context.browser.get(url_buscar)
    form = get_element(context.browser, tag='form')
    name_form="form"+entity
    get_element(form, name=name_form).send_keys('0')
    form.submit()

@when('the entity is preguntas')
def step_impl(context):
    requests.Response().
    response = requests.post(url=context.api_url, headers="")
    #print(session)
    #print("_______________________________________________________________________________")
    print(response.text)

@then('the {creation} of question is correct')
def step_impl(context, creation):
    print('La creación es correcta')