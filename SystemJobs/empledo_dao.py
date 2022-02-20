from empleado import Empleados
from cursor_jobs import CursorPoolJobs


class EmpleadoDao:
    """
    DAO = DATA ACCESS OBJECT
    """

    _SELECT = 'SELECT * FROM empleado ORDER BY id_empleado'
    _BUSCADOR = 'SELECT * FROM empleado WHERE cedula=%s'
    _INSERT = 'INSERT INTO empleado(nombre,direccion,telefono,cedula,puesto_trabajo,sueldo,seguro_medico)VALUES(%s,%s,%s,%s,%s,%s,%s)'
    _ACTUALIZAR = 'UPDATE empleado  SET nombre=%s,direccion=%s, telefono=%s,puesto_trabajo=%s,sueldo=%s, seguro_medico=%s WHERE cedula=%s'
    _ELIMINAR = 'DELETE FROM empleado WHERE cedula=%s'

    @classmethod
    def MostrarEmpleado(cls):
        with CursorPoolJobs() as cursor:
            cursor.execute(cls._SELECT)
            empleado = cursor.fetchall()
            emple = []
            for x in empleado:
                em = Empleados(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7])
                emple.append(em)
            return emple

    @classmethod
    def BuscarEmpleado(cls, empleado):
        with CursorPoolJobs() as cursor:
            perimetros = (empleado.cedula,)
            cursor.execute(cls._BUSCADOR, perimetros)
            employed = cursor.fetchall()
            emplo = []
            for x in employed:
                emple = Empleados(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7])
                emplo.append(emple)
            return emplo

    @classmethod
    def RegistrarEmpleado(cls, empleado):
        with CursorPoolJobs() as cursor:
            valores = (empleado.nombre, empleado.direccion, empleado.telefono, empleado.cedula,
                       empleado.puesto, empleado.sueldo, empleado.seguroMedico)
            cursor.execute(cls._INSERT, valores)
            print('Registrando empleado..!!'.center(50, '*'))

    @classmethod
    def ActualizarEmpleado(cls, empleado):
        with CursorPoolJobs() as cursor:
            parametros = (empleado.nombre, empleado.direccion, empleado.telefono, empleado.puesto, empleado.sueldo,
                          empleado.seguroMedico, empleado.cedula,)
            cursor.execute(cls._ACTUALIZAR, parametros)
            print(f'Empleado Actualizado: {empleado}'.center(50, '*'))
            return cursor.rowcount

    @classmethod
    def EliminarEmpleado(cls, empleado):
        with CursorPoolJobs() as cursor:
            parametros = (empleado.cedula,)
            cursor.execute(cls._ELIMINAR, parametros)
            print(f'Empleado eliminado...!!: {empleado}'.center(50, '*'))
            return cursor.rowcount


if __name__ == '__main__':
    j = EmpleadoDao.MostrarEmpleado()
    for p in j:
        print(p)

    # job1= EmpleadoDao.BuscarEmpleado('01-001695-4')
    # print(f'empleado encontrado..!!'.capitalize())
    # for h in job1:
    #     print(h)
    #
    # employed1 = Empleados(cedula='402-3028284-6',nombre='Joel German', direccion='Dajabon', telefono='809-703-5011',
    #                      puestoTrabajo='Ingeniero de sistemas', sueldo='75,000.00', seguroMedico='067508302 (senasa)', )
    # EmpleadoDao.ActualizarEmpleado(employed1)
    # print(f'Empleado Actualizado: {employed1}')

    # employed = Empleados(nombre='Joel German', direccion='Dajabon', telefono= '809-703-5011',cedula ='402-3028284-6',
    #                      puestoTrabajo='Ingeniero en sistemas', sueldo='75,500', seguroMedico='Senasa')
    # EmpleadoDao.RegistrarEmpleado(employed)
    # print(f'Empleado Registrado: {employed}')

    # employed = Empleados(cedula='402-3028284-6')
    # EmpleadoDao.EliminarEmpleado(employed)
    # print(f'Empleado eliminado: {employed}')
