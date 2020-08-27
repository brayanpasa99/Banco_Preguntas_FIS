Feature: Pregunta

Scenario Outline: Get data to list
  Given a <pre_id> <pre_texto> <cat_id> <com_id> <tpr_id> to show information
  When the fields are called
  Then the <fields> are showed

  Examples: listed
  | pre_id  | pre_texto   | cat_id | com_id | tpr_id | fields                     |
  | 27      | Pregunta 1  | 8      | 6      | 34     | Los campos fueron listados |
  | 19      | Pregunta 2  | 12     | 1      | 19     | Los campos fueron listados |
  | 56      | Pregunta 3  | 67     | 3      | 17     | Los campos fueron listados |

Scenario Outline: Ged data to modify
  Given a <pre_id> <pre_texto> <cat_id> <com_id> <tpr_id> to update information
  When the fields are updated
  Then the <fields> are modified

  Examples: updated
  | pre_id  | pre_texto   | cat_id | com_id | tpr_id | fields                         |
  | 27      | Pregunta 1  | 8      | 6      | 34     | Los campos fueron actualizados |
  | 19      | Pregunta 2  | 12     | 1      | 19     | Los campos fueron actualizados |
  | 56      | Pregunta 3  | 67     | 3      | 17     | Los campos fueron actualizados |
 

