
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class AutorForm(FlaskForm):
    nombre = StringField('Nombre',validators=[DataRequired()])
    apellido = StringField('Apellido')
    email = StringField('Email',validators=[DataRequired()])
    enviar = SubmitField('Enviar')
    
class LibroForm(FlaskForm):
    titulo = StringField('Titulo',validators=[DataRequired()])
    genero = StringField('Genero')
    descripcion = StringField('Descripcion')
    autor = StringField('Autor',validators=[DataRequired()])
    enviar = SubmitField('Enviar')
    
class GeneroForm(FlaskForm):
    nombre = StringField('Titulo',validators=[DataRequired()])
    descripcion = StringField('Descripcion')
    enviar = SubmitField('Enviar')