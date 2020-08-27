Feature: CRUD

Scenario Outline: Insert information in fields
  Given an <entity> and <fields> to insert in DB
  When the user inserts the information in fields
  Then the register was created with <data>

  Examples: insert 
  |  entity      | fields   | data                            |
  |  pregunta    | pre_id   | pre_id was insert in pregunta   |
  |  categoria   | cat_id   | cat_id was insert in categoria  |
  |  usuario     | user_id  | user_id was insert in usuario   |
  |  evaluacion  | eva_id   | eva_id was insert in evaluacion |

Scenario Outline: Ged data to erase 
  Given an <fieldid> and an <entity> to erase information
  When the register with <id> will be erased
  Then the <register> was erased

  Examples: updated
  | fieldid  | entity     | id | register                                                            |
  | cat_id   | categoria  | 3  | El registro 3 en el campo cat_id fue borrado en la tabla categoria  |
  | pre_id   | pregunta   | 75 | El registro 75 en el campo pre_id fue borrado en la tabla pregunta  |
  | user_id  | usuario    | 12 | El registro 12 en el campo user_id fue borrado en la tabla usuario  |