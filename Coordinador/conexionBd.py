from pysqlite2 import dbapi2 as sqlite

class conexionBd:
	def __init__(self, bd):
		try:
			self.con = sqlite.connect(bd) # conecta a la bd. 
			#isolation_level="IMMEDIATE" si se quiere bloqueo para que otro hilo no pueda escribir
			self.cur = self.con.cursor() # obtenemos un cursor para ejecutar sql
		except Exception, e:
			print "Excepcion: __init__::conexionBd = ", e
			
	# ejecuta la sentencia sql pasada y retorna el resultado
	def ejecutarSQL(self, s):
		self.cur.execute(s)
		return self.cur.fetchall()
		
	def commit(self):
		self.con.commit();
		
	def rollback(self):
		self.con.rollback();
		

# ejemplillo
#c = conexionBd("test")
#c.ejecutarSQL("create table t (uno integer)")
#c.ejecutarSQL("insert into t values (23)")
#c.commit() # si no se hace el commit no compromete los cambios
