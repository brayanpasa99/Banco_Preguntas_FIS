from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco_preguntas.sqlite3'
app.config['SECRET_KEY'] = "123456789"

db = SQLAlchemy(app)
inspector = inspect(db.engine)


class categoria(db.Model):
   id = db.Column('cat_id', db.Integer, primary_key = True)
   cat_nombre = db.Column(db.String(100))
   cat_tipo = db.Column(db.Integer)
   children = db.relationship("Pregunta")

   def __init__(self, nombre, tipo):
       self.cat_nombre = nombre
       self.cat_tipo = tipo

class tipo_categoria(db.Model):
   id = db.Column('tca_id', db.Integer, primary_key = True)
   tca_nombre = db.Column(db.String(50))

   def __init__(self, nombre):
       self.cat_nombre = nombre  

class pregunta(db.Model):
   id = db.Column('pre_id', db.Integer, primary_key = True)
   pre_texto = db.Column(db.String(150))
   #cat_id = db.Column(db.Integer, db.ForeignKey('categoria.id')) 
   cat_id = db.Column(db.Integer, db.ForeignKey('categoria.cat_id')) 
   com_id = db.Column(db.Integer, db.ForeignKey('competencia.com_id'))
   tpr_id = db.Column(db.Integer, db.ForeignKey('tipo.tca_id'))

   def __init__(self, texto, categoria, tipo, competencia):
      self.pre_texto = texto
      self.cat_id = categoria
      self.com_id = competencia
      self.tpr_id = tipo

class competencia(db.Model):
    id = db.Column('com_id', db.Integer, primary_key = True)
    com_codigo = db.Column(db.String(15))
    com_nombre = db.Column(db.String(20))
    com_tipo = db.Column(db.String(20))
    com_descripcion = db.Column(db.String(500))

    def __init__(self, codigo, nombre, tipo, descripcion):
      self.com_codigo = codigo
      self.com_nombre = nombre
      self.com_tipo = tipo
      self.com_descripcion = descripcion

    

class evaluacion(db.Model):
    id = db.Column('eva_id', db.Integer, primary_key = True)
    eva_nombre = db.Column(db.String(30))
    eva_pregunta = db.Column(db.Integer,db.ForeignKey('pregunta.pre_id'))
    eva_pagina= db.Column(db.Integer)
    eva_puntos = db.Column(db.Integer)
    eva_puntuacionMax = db.Column(db.Integer)
    eva_conjunta = db.Column(db.Boolean)

    def __init__(self, nombre, pregunta, pagina, puntos, puntuacionMax, conjunta):
      self.eva_nombre = nombre
      self.eva_pagina = pagina
      self.eva_pagina = pagina
      self.eva_puntos = puntos
      self.eva_puntuacionMax = puntuacionMax
      self.eva_conjunta = conjunta

    
class respuesta(db.Model):
    id = db.Column('res_id', db.Integer, primary_key = True)
    res_valor = db.Column(db.Float)
    res_descripcion = db.Column(db.String(500))
    res_pregunta = db.Column(db.Integer, db.ForeignKey('pregunta.pre_id'), nullable=False)

    def __init__(self, valor, descripcion, pregunta):
      self.res_valor = valor
      self.res_descripcion = descripcion
      self.res_pregunta = pregunta

class usuario(db.Model):
    id = db.Column('user_id', db.Integer, primary_key = True)
    user_nombre = db.Column(db.String(50))
    user_correo = db.Column(db.String(50))
    user_contrasenia = db.Column(db.String(100))
    user_codigo = db.Column(db.Integer)
    user_proyectoCurricular = db.Column(db.String(25))
    user_rol = db.Column(db.String(25))

    def __init__(self, nombre, correo, contrasenia, codigo, proyectoCurricular, rol):
        self.user_nombre = nombre
        self.user_correo = correo
        self.user_contrasenia = contrasenia
        self.user_codigo = codigo
        self.user_proyectoCurricular = proyectoCurricular
        self.user_rol = rol

@app.route('/')
def home():
   entidades = db.engine.table_names()
   return render_template('home.html', entidades = entidades)

@app.route('/list/<entidad>')
def list(entidad):
   campos = inspector.get_columns(entidad)
   return render_template('list.html', entidad = entidad, campos = campos )

@app.route('/insert/<entidad>')
def insert(entidad):
   campos = inspector.get_columns(entidad)
   return render_template('insert.html', entidad = entidad, campos = campos )

@app.route('/')


if __name__ == '__main__':
   db.create_all()
   app.run('localhost', 8000, debug=True)
