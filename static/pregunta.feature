Feature: Pregunta

Scenario Outline: Crear pregunta
  Given a <pre_id> <pre_texto> <cat_id> <com_id> <tpr_id> to create_question
  When the creator create a question
  Then the <creation> of question is correct

  Examples: datos
  | pre_id   | pre_texto                         | cat_id | com_id  | tpr_id  | creation                                                        | 
  | 0        | Soy el texto de la pregunta 0     | 98     | 93      | 56      | La petición se efectuó correctamente para la tabla: {{entidad}} |
  | 50000    | Soy el texto de la pregunta 50000 | 19     | 76      | 28      | La petición se efectuó correctamente para la tabla: {{entidad}} |
  | 19       | Soy el texto de la pregunta 19    | 4      | 23      | 12      | La petición se efectuó correctamente para la tabla: {{entidad}} |
  | 23       | Soy el texto de la pregunta 23    | 35     | 114     | 11      | La petición se efectuó correctamente para la tabla: {{entidad}} |
