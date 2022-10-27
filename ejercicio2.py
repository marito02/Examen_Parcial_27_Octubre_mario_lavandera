class Alumno():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        print(f"el alumno {self.nombre} se ha creado correctamente")
    def __str__(self):
        return(f"el alumno tiene de nombre {self.nombre} y ha obtenido un {self.nota}")
    def calificacion(self):
        if self.nota >= 5:
            print(f"el alumno {self.nombre} ha aprobado el examen con un {self.nota}")
        else:
            print(f"el alumno {self.nombre} ha suspendido el examen con un {self.nota}")

alumno1=Alumno("Juan Gutierrez", 7)
alumno2=Alumno("Javier Martinez", 4)
alumno3=Alumno("Manolo Gomez", 8)

lista=[alumno1, alumno2, alumno3]

print(alumno1.calificacion())
print(alumno2.calificacion())
print(alumno3.calificacion())