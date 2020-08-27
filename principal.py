from flask import Flask, request, flash, url_for, redirect, render_template, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco_preguntas.sqlite3'
app.config['SECRET_KEY'] = "123456789"

db = SQLAlchemy(app)
inspector = inspect(db.engine)
schemas = inspector.get_schema_names()
metadata = MetaData()


class categoria(db.Model):
    id = db.Column('cat_id', db.Integer, primary_key=True)
    cat_nombre = db.Column(db.String(100))
    cat_tipo = db.Column(db.Integer)
    children = db.relationship("Pregunta")

    def __init__(self, nombre, tipo):
        self.cat_nombre = nombre
        self.cat_tipo = tipo


class tipo_categoria(db.Model):
    id = db.Column('tca_id', db.Integer, primary_key=True)
    tca_nombre = db.Column(db.String(50))

    def __init__(self, nombre):
        self.cat_nombre = nombre


class pregunta(db.Model):
    id = db.Column('pre_id', db.Integer, primary_key=True)
    pre_texto = db.Column(db.String(150))
    # cat_id = db.Column(db.Integer, db.ForeignKey('categoria.id'))
    cat_id = db.Column(db.Integer, db.ForeignKey('categoria.cat_id'))
    com_id = db.Column(db.Integer, db.ForeignKey('competencia.com_id'))
    tpr_id = db.Column(db.Integer, db.ForeignKey('tipo.tca_id'))

    def __init__(self, texto, categoria, tipo, competencia):
        self.pre_texto = texto
        self.cat_id = categoria
        self.com_id = competencia
        self.tpr_id = tipo


class competencia(db.Model):
    id = db.Column('com_id', db.Integer, primary_key=True)
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
    id = db.Column('eva_id', db.Integer, primary_key=True)
    eva_nombre = db.Column(db.String(30))
    eva_pregunta = db.Column(db.Integer, db.ForeignKey('pregunta.pre_id'))
    eva_pagina = db.Column(db.Integer)
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
    id = db.Column('res_id', db.Integer, primary_key=True)
    res_valor = db.Column(db.Float)
    res_descripcion = db.Column(db.String(500))
    res_pregunta = db.Column(db.Integer, db.ForeignKey(
        'pregunta.pre_id'), nullable=False)

    def __init__(self, valor, descripcion, pregunta):
        self.res_valor = valor
        self.res_descripcion = descripcion
        self.res_pregunta = pregunta


class usuario(db.Model):
    id = db.Column('user_id', db.Integer, primary_key=True)
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
    return render_template('home.html', entidades=entidades)


@app.route('/list/<entidad>')
def list(entidad):
    campos = inspector.get_columns(entidad)
    registros = db.engine.execute("SELECT * FROM "+entidad+" ;")
    registros = registros.fetchall()
    return render_template('list.html', entidad=entidad, campos=campos, registros=registros)


@app.route('/insert/<entidad>')
def insert(entidad):
    campos = inspector.get_columns(entidad)
    nombres_campos = []
    for c in campos:
       nombres_campos.append(c['name'])

    session['campos'] = nombres_campos
    return render_template('insert.html', entidad=entidad, campos=campos)


@app.route('/registered/<entidad>', methods=["POST", "GET"])
def confirmar(entidad):
    campos = inspector.get_columns(entidad)
    valores = []
    if request.method == "POST":
        for campo in campos:
            valores.append(request.form[campo['name']])

        for table_name in metadata.tables.keys():
            if table_name == entidad:
                inst = "INSERT INTO "+table_name+" ("
                for campo in range(len(campos)-1):
                    inst = inst+str(campos[campo]['name'])+", "
                inst = inst + str(campos[len(campos)-1]['name']) + ") VALUES ("
                for valor in range(len(valores)-1):
                    inst = inst+"'"+str(valores[valor])+"'"+", "
                inst = inst + "'"+str(valores[len(valores)-1])+"'" + ");"
                print(inst)
                # db.engine.execute("INSERT INTO categoria (cat_id, cat_nombre, cat_tipo) VALUES ('1', 'nombreprueba1', '1')")
                db.engine.execute(inst)
        return render_template('confirmacion.html', entidad=entidad)
    else:
        return render_template('falla.html')


@app.route('/delete/<entidad>', methods=["POST", "GET"])
def borrado(entidad):
    campos = inspector.get_columns(entidad)
    if request.method == "POST":
        idborrar = request.form["idborrar"]
        for campo in campos:
            if campo['primary_key'] == 1:
                inst = "DELETE FROM "+entidad+" WHERE " + \
                    str(campo['name'])+" IN ('"+idborrar+"');"
                db.engine.execute(inst)
        # db.engine.execute("DELETE FROM "main"."categoria" WHERE _rowid_ IN ('0');")
        return render_template('confirmacion.html', entidad=entidad)
    else:
        return render_template('falla.html', entidad=entidad)


@app.route('/formupdate/<entidad>', methods=['POST', 'GET'])
def formactualizar(entidad):
    campos = inspector.get_columns(entidad)
    if request.method == "POST":
        idact = request.form["idact"]
        for campo in campos:
            if campo['primary_key'] == 1:
                registros = db.engine.execute(
                    "SELECT * FROM "+entidad+" WHERE "+str(campo['name'])+" IN ('"+idact+"');")
                registros = registros.fetchall()
        return render_template('formupdate.html', entidad=entidad, registros=registros, campos=campos)
    else:
        return render_template('falla.html', entidad=entidad)


@app.route('/update/<entidad>', methods=['POST', 'GET'])
def actualizar(entidad):
    campos = inspector.get_columns(entidad)
    valores = []
    if request.method == "POST":
        for campo in campos:
            valores.append(request.form[campo['name']])
        inst = "UPDATE "+entidad+" SET "
        for campo in range(1, len(campos)-1):
            inst = inst+str(campos[campo]['name'])+"='"+valores[campo]+"', "
        inst = inst + str(campos[len(campos)-1]['name']) + \
            "='"+valores[len(valores)-1]+"' WHERE "
        inst = inst + str(campos[0]['name'])+"="+valores[0]+";"
        print(inst)
        # "UPDATE table_name SET column1 = value1, column2 = value2 WHERE condition; "
        # db.engine.execute("INSERT INTO categoria (cat_id, cat_nombre, cat_tipo) VALUES ('1', 'nombreprueba1', '1')")
        db.engine.execute(inst)
        return render_template('confirmacion.html', entidad=entidad)
    else:
        return render_template('falla.html')



if __name__ == '__main__':

    db.create_all()
    metadata = db.metadata
    print(metadata.tables.keys())

    # for schema in schemas:
    #   print("schema: %s" % schema)
    #   for table_name in inspector.get_table_names(schema=schema):
    #      print(table_name)
    #      for column in inspector.get_columns(table_name, schema=schema):
    #            print("Column: %s" % column)

    # engine = db.engine
    # connection = engine.connect()
    # metadata = db.MetaData()
    # pregunta = db.Table('pregunta', metadata, autoload=True, autoload_with=engine)

    # query = db.select([pregunta])

    # ResultProxy = connection.execute(query)
    # ResultSet = ResultProxy.fetchall()
    # print(ResultSet)

    app.run('localhost', 8000, debug=True)
