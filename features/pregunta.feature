Feature: Pregunta

Scenario Outline: Insertar
  Given <fields> to insert in DB
  When the user insert the data
  Then the fields have <information>

  Examples: entities
  |  fields     | information       |
  |  pre_id     | 0                 |
  |  pre_texto  | Soy una pregunta  |
  |  cat_id     | 1                 |
  |  com_id     | 2                 |
  |  tpr_id     | 9                 |

Scenario Outline: Leer
Scenario Outline: Actualizar
Scenario Outline: Eliminar
