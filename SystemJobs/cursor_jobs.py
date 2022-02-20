from logger_base import log
from conexion_job import ConexionJob

class CursorPoolJobs:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        log.debug('Iniciando el metodo enter'.upper())
        self._conexion = ConexionJob.CrearConexionJob()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, tipo_excepcion, valor_excepcion, detalle_excepcion):
        log.debug('Se ejecuta metodo __exit__')
        if valor_excepcion:
            self._conexion.rollback()
            log.info(f'Ocurrio un error: {tipo_excepcion}, {valor_excepcion}, {detalle_excepcion}')

        else:
            self._conexion.commit()
            log.debug('Se hizo commit de la transaccion')
        self._cursor.close()
        ConexionJob.LiberarConexionJob(self._conexion)

if __name__ == '__main__':
    with CursorPoolJobs() as cursor:
        print('Abriendo el cursor con with')
        cursor.execute('SELECT * FROM empleado ORDER BY id_empleado ASC ')
        print(cursor.fetchall())