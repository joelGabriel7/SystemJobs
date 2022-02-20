#Aqui creamos la clase empleado con sus atributos e instancias

class Empleados:
    def __init__(self, id_empleado=None, nombre=None,
                 direccion=None, telefono=None, cedula=None,
                 puestoTrabajo=None, sueldo=None, seguroMedico=None):
        self.id_empledo = id_empleado
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.cedula = cedula
        self.puesto = puestoTrabajo
        self._sueldo = sueldo
        self.seguroMedico = seguroMedico
# Aqui encapsule solamente el atributo de sueldo

    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self, sueldo):
        self._sueldo = sueldo
# Aqui en esta funcion o metodo dunder lo use para darle formatos a los datos que regresaran de  la base de datos.

    def __str__(self):
        return f""" 
                Id: {self.id_empledo} 
                Nombre:{self.nombre}
                Direccion:{self.direccion}
                Telefono:{self.telefono}
                Cedula:{self.cedula}
                Puesto:{self.puesto}
                Sueldo:{self._sueldo}
                Seguro Medico:{self.seguroMedico}
                """
