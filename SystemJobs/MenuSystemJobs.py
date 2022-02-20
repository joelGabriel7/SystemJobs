from empleado import Empleados
from empledo_dao import EmpleadoDao

op = None
print('Bienvinidos al Menú System Employed'.center(50, '*'))
# print()
while op != 6:
    print('1.Registrar un Nuevo Empleado')
    print('2.Mostrar Registros')
    print('3.Actualizar Empleado')
    print('4.Eliminar Empleado')
    print('5.Buscar Empleado')
    print('6.Salir')
    op = int(input('Ingresa una opcion del menú (1-6): ').strip())

    if op == 1:
        nom = input('Ingresa el nombre del empleado: ')
        dire = input('Ingresa la direccion del empleado: ')
        tele = input('Ingresa el Numero telefonico del empleado: ')
        cedu = input('Ingresa la cedula o DNI del empleado: ')
        puesto = input('Ingresa el puesto del empleado: ')
        sueldo = input('Ingresa el sueldo a pagar del empleado: ')
        security = input('Ingresa el seguro medico del empleado: ')

        x = Empleados(nombre=nom, direccion=dire, telefono=tele, cedula=cedu, puestoTrabajo=puesto, sueldo=sueldo,
                      seguroMedico=security)
        EmpleadoDao.RegistrarEmpleado(x)
        print(f'Empleado resgistrado: {x}')

    elif op == 2:
        mostrar = EmpleadoDao.MostrarEmpleado()
        print('Mostrando registros'.strip().center(50, '*'))
        for mostrando in mostrar:
            print(mostrando)

    elif op == 3:
        nom = input('Ingresa el nombre del empleado: ')
        dire = input('Ingresa la direccion del empleado: ')
        tele = input('Ingresa el Numero telefonico del empleado: ')
        cedu = input('Ingresa la cedula o DNI del empleado: ')
        puesto = input('Ingresa el puesto del empleado: ')
        sueldo = input('Ingresa el sueldo a pagar del empleado: ')
        security = input('Ingresa el seguro medico del empleado: ')
        x = Empleados(nombre=nom, direccion=dire, telefono=tele, puestoTrabajo=puesto, sueldo=sueldo,
                      seguroMedico=security, cedula=cedu)
        EmpleadoDao.ActualizarEmpleado(x)

    elif op == 4:
        c = input('Ingresa la cedula o DNI  del empleado: ')
        cedula = Empleados(cedula=c)
        EmpleadoDao.EliminarEmpleado(cedula)

    elif op == 5:
        cb = input('Ingresa la cedula o DNI  del empleado: ')
        e = Empleados(cedula=cb)
        job1 = EmpleadoDao.BuscarEmpleado(e)
        h = ''
        print()
        for h in job1:
            print(f'empleado encontrado: {h}'.capitalize())

        if h not in job1:
            print(f'Empleado no esta registrado..!!'.center(50, '*'))
            print()

    elif op == 6:
        print('Estamos fuera del sistema'.center(50, '*'))
        break
    else:
        print('Por favor ingrese una opcion valida del menu..!!')
        continue
