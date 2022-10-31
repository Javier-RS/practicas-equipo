from flask import Flask, request,url_for,render_template,redirect
from database import db
from flask_migrate import Migrate
from models import Libro,Autor,Genero
from forms import AutorForm,LibroForm,GeneroForm
import logging
logging.basicConfig(filename='info.log',  level=logging.DEBUG)
# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this, too')
# logging.error('And non-ASCII stuff, too, like Øresund and Malmö')
app = Flask(__name__)

#Configuracion de la BD 
USER_DB = 'postgres'
PASS_DB = 'admin'
URL_DB = 'localhost'
NAME_DB= 'practica'
FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

#configurar migracion
migrate = Migrate()
migrate.init_app(app,db)

#Form
app.config["SECRET_KEY"]="secret key"

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def inicio():
    autores = Autor.query.all()
    return render_template('index.html',autores=autores)


@app.route('/agregar', methods=['GET','POST'])
def agregar():
    autor = Autor()
    autorForm = AutorForm(obj=autor)
    if request.method =="POST":
        if autorForm.validate_on_submit():
            autorForm.populate_obj(autor)
            #insert
            db.session.add(autor)
            db.session.commit()
            return  redirect(url_for('inicio'))
    app.logger.debug(f'procediendo a agregar.html mandando:') 
    app.logger.debug(autorForm)      
    return render_template('agregar.html',forma = autorForm)

@app.route('/editar/<int:id>',methods=['GET','POST'])
def editar(id):
    autor = Autor.query.get_or_404(id)
    autorForm = AutorForm(obj=autor)
    if request.method =="POST":
        if autorForm.validate_on_submit():
            autorForm.populate_obj(autor)
            db.session.commit()
            return  redirect(url_for('inicio'))
    return  render_template('editar.html',forma =autorForm)

@app.route('/eliminar/<int:id>')
def eliminar(id):
    autor = Autor.query.get_or_404(id)
    db.session.delete(autor)
    db.session.commit()
    return redirect(url_for('inicio'))


#Autores


@app.route('/autores.html')
def autores():
    autores = Autor.query.all()
    app.logger.debug(f'cargando autores') 
   
    return render_template('autores.html',autores=autores)




@app.route('/agregarautor', methods=['GET','POST'])
def agregarautor():
    autor = Autor()
    autorForm = AutorForm(obj=autor)
    if request.method =="POST":
        if autorForm.validate_on_submit():
            autorForm.populate_obj(autor)
            #insert
            db.session.add(autor)
            db.session.commit()
            return  redirect(url_for('inicio'))
    app.logger.debug(f'procediendo a agregarautor.html mandando:') 
    app.logger.debug(autorForm)  
    return render_template('agregarautor.html',forma = autorForm)

@app.route('/editarautor/<int:id>',methods=['GET','POST'])
def editarautor(id):
    autor = Autor.query.get_or_404(id)
    autorForm = AutorForm(obj=autor)
    if request.method =="POST":
        if autorForm.validate_on_submit():
            autorForm.populate_obj(autor)
            db.session.commit()
            return  redirect(url_for('inicio'))
    app.logger.debug(f'procediendo a editarautor.html mandando:') 
    app.logger.debug(autorForm) 
    return  render_template('editarautor.html',forma =autorForm)

@app.route('/eliminarautor/<int:id>')
def eliminarautor(id):
    autor = Autor.query.get_or_404(id)
    db.session.delete(autor)
    db.session.commit()
    app.logger.debug(f'procediendo a eliminar autor') 
    app.logger.debug(autor) 
    return redirect(url_for('inicio'))


### Libros

@app.route('/libros.html')
def libros():
    libros = Libro.query.all()
    app.logger.debug(f'cargando libros') 
    return render_template('libros.html',libros=libros)




@app.route('/agregarlibro', methods=['GET','POST'])
def agregarlibro():
    libro = Libro()
    libroForm = LibroForm(obj=libro)
    if request.method =="POST":
        if libroForm.validate_on_submit():
            libroForm.populate_obj(libro)
            #insert
            db.session.add(libro)
            db.session.commit()
            return  redirect(url_for('inicio'))
    return render_template('agregarlibro.html',forma = libroForm)



@app.route('/editarlibro/<int:id>',methods=['GET','POST'])
def editarlibro(id):
    libro = Libro.query.get_or_404(id)
    libroForm = LibroForm(obj=libro)
    if request.method =="POST":
        if libroForm.validate_on_submit():
            libroForm.populate_obj(libro)
            db.session.commit()
            return  redirect(url_for('inicio'))
    app.logger.debug(f'procediendo a editarlibro.html mandando:') 
    app.logger.debug(libroForm) 
    return  render_template('editarlibro.html',forma =libroForm)

@app.route('/eliminarlibro/<int:id>')
def eliminarlibro(id):
    libro = Libro.query.get_or_404(id)
    db.session.delete(libro)
    db.session.commit()
    app.logger.debug(f'procediendo a eliminar libro') 
    app.logger.debug(libro) 
    return redirect(url_for('inicio'))

### Generos

@app.route('/generos.html')
def generos():
    generos = Genero.query.all()
    app.logger.debug(f'cargando generos') 
    return render_template('generos.html',generos=generos)




@app.route('/agregargenero', methods=['GET','POST'])
def agregargenero():
    genero = Genero()
    generoForm = GeneroForm(obj=genero)
    if request.method =="POST":
        if generoForm.validate_on_submit():
            generoForm.populate_obj(genero)
            #insert
            db.session.add(genero)
            db.session.commit()
            return  redirect(url_for('inicio'))
    return render_template('agregargenero.html',forma = generoForm)




@app.route('/editargenero/<int:id>',methods=['GET','POST'])
def editargenero(id):
    genero = Genero.query.get_or_404(id)
    generoForm = GeneroForm(obj=genero)
    if request.method =="POST":
        if generoForm.validate_on_submit():
            generoForm.populate_obj(genero)
            db.session.commit()
            return  redirect(url_for('inicio'))
    app.logger.debug(f'procediendo a editargenero.html mandando:') 
    app.logger.debug(generoForm) 
    return  render_template('editargenero.html',forma =generoForm)

@app.route('/eliminargenero/<int:id>')
def eliminargenero(id):
    genero = Genero.query.get_or_404(id)
    db.session.delete(genero)
    db.session.commit()
    app.logger.debug(f'procediendo a eliminar genero') 
    app.logger.debug(genero) 
    return redirect(url_for('inicio'))