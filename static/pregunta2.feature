Feature: Pregunta2

Scenario Outline: Crear pregunta
  Given a <entity> to insert data
  When the entity is preguntas
  Then the <creation> of question is correct

  Examples: datos
  | entity          | creation                                                        | 
  | pregunta        | La petición se efectuó correctamente para la tabla: {{entidad}} |
  | categorias      | La petición se efectuó correctamente para la tabla: {{entidad}} |
  | usuario         | La petición se efectuó correctamente para la tabla: {{entidad}} |
  | tipo_categoria  | La petición se efectuó correctamente para la tabla: {{entidad}} |
