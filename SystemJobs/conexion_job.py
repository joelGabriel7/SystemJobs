import sys
from logger_base import log
from psycopg2 import pool

# Aqui estamos definiedo la clase para hacer la conexion
class ConexionJob:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'GERMAN'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CONE= 1
    _MAX_CONE = 5
    _pool = None

# Aqui hacemos la funcion con el decorador class method y esa funcion nos regresara la conexion al pool
# Usamos tambien un try except para si nos da error no se nos rompa el codigo y poder identificar rapido el error.
    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CONE, cls._MAX_CONE,
                                                      host=cls._HOST,
                                                      user=cls._USERNAME,
                                                      password=cls._PASSWORD,
                                                      port=cls._DB_PORT,
                                                      database=cls._DATABASE
                                                      )
                log.debug(f'Conexion del pool exitosa: {cls._pool}')
                return cls._pool
            except Exception as e:
               log.info(f'Ocurrio un error en la conexion del pool: {e}')
               sys.exit()
        else:
            return cls._pool
# Aqui hacemos una funcion que nos conecta con el pool de conexiones creado anteriormente

    @classmethod
    def CrearConexionJob(cls):
        conexion = cls.obtenerPool().getconn()
        log.debug(f'Conexion con el pool creada: {conexion}')
        return conexion

#Aqui liberamos la conexion
    @classmethod
    def LiberarConexionJob(cls, conexion):
        cls.obtenerPool().putconn(conexion)
        log.debug(f'Conexion del pool liberada: {conexion}')
        return conexion

# Aqui la cerramos

    @classmethod
    def CerrarConexionJob(cls, conexion):
        cls.obtenerPool().closeall()
        log.debug(f'Conexion del pool cerrada...!!: {conexion}')
        return conexion

# Hacemos pruebas para ver si funciona bien
if __name__ == '__main__':
    cone1 = ConexionJob.CrearConexionJob()
    ConexionJob.LiberarConexionJob(cone1)
    ConexionJob.CerrarConexionJob(cone1)
