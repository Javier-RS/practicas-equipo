from app import db 
# class Persona(db.Model):  # type: ignore
#     id = db.Column(db.Integer,primary_key=True)
#     nombre = db.Column(db.String(250))
#     apellido = db.Column(db.String(250))
#     email = db.Column(db.String(250))

#     def __str__(self) -> str:
#         return (f'ID : {self.id} ,'
#                 f'Nombre : {self.nombre} ,'
#                 f'Apellido: {self.apellido} ,'
#                 f'Email: {self.email}'
        
#         )
        
class Libro(db.Model):  # type: ignore
    id = db.Column(db.Integer,primary_key=True)
    titulo = db.Column(db.String(250))
    genero = db.Column(db.String(250))
    autor = db.Column(db.String(250))
    descripcion = db.Column(db.String(250))
    def __str__(self) -> str:
        return (f'ID : {self.id} ,'
                f'Nombre : {self.nombre} ,'
                f'Apellido: {self.genero} ,'
                f'Email: {self.autor},'
                f'Email: {self.descripcion}'
        
        )
        
class Genero(db.Model):  # type: ignore
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(250))
    descripcion = db.Column(db.String(250))
    

    def __str__(self) -> str:
        return (f'ID : {self.id} ,'
                f'Nombre : {self.nombre} ,'
                f'descripcion: {self.descripcion}'
                
        
        )
        
class Autor(db.Model):  # type: ignore
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(250))
    apellido = db.Column(db.String(250))
    email = db.Column(db.String(250))

    def __str__(self) -> str:
        return (f'ID : {self.id} ,'
                f'Nombre : {self.nombre} ,'
                f'Apellido: {self.apellido} ,'
                f'Email: {self.email}'
        
        )