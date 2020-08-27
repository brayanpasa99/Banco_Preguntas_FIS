from behave import *
import requests


@given('a {materia} {tema} {competencia} {tipo} {texto} to create_question')
def step_impl(context, materia, tema, competencia, tipo, texto):
    print('La materia es: ' + materia + ' El tema es: ' + tema + ' La competencia es: ' + competencia + ' El tipo es: ' + tipo + ' El texto es: ' + texto)

@when('the creator create_question')
def step_impl(context):
    print('El creador creó la pregunta')

@then('the {creation} of question is correct')
def step_impl(context, creation):
    print('La creación es correcta')