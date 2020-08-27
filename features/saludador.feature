Feature: Formato_Pregunta

Scenario Outline: Obtener pregunta valida
  Given a <materia> <tema> <competencia> <tipo> <texto> to create_question
  When the creator create_question
  Then the <creation> of question is correct

  Examples: datos
  | materia                                 | tema                      | competencia  | tipo               | texto  | creation                | 
  | Ciencias de la computación 3            | Árboles                   | competencia1 | Selección múltiple | texto1 | La creación es correcta |
  | Cibernética 1                           | Función de transferencia  | competencia2 | Abierta            | texto2 | La creación es correcta |
  | Cibernética 2                           | Espacio de estados        | competencia3 | Cerrada            | texto3 | La creación es correcta |
  | Fundamentos de Ingeniería de Software   | Metodología de Sowftware  | competencia4 | Abierta            | texto4 | La creación es correcta |
