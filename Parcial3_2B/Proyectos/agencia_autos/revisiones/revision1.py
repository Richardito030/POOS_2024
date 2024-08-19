from conexionBD import *

class Revision:
    def __init__(self, cambiofiltro, cambioaceite, cambiodfrenos, otros, matricula):
        self.cambiofiltro = cambiofiltro
        self.cambioaceite = cambioaceite
        self.cambiofrenos = cambiodfrenos
        self.otros = otros
        self.matricula = matricula

    def insertar(self):
        try:
            cursor.execute(
                "insert into revisiones values(null,%s,%s,%s,%s,%s)",
                (self.cambiofiltro, self.cambioaceite, self.cambiofrenos, self.otros, self.matricula)
            )
            conexion.commit()
            return True
        except:
            return False   

    @staticmethod
    def consultar(matricula):
        try:
            cursor.execute(
                "select * from revisiones where matricula = %s",
                (matricula,)
            )
            return cursor.fetchall()
        except:
            return None    

    @staticmethod
    def actualizar(no_revision, cambiofiltro, cambioaceite, cambiofrenos, otros):
       try:
         cursor.execute(
            "update revisiones set cambiofiltro=%s, cambioaceite=%s, cambiofrenos=%s, otros=%s where no_revision=%s",
            (cambiofiltro, cambioaceite, cambiofrenos, otros, no_revision)
         )
         conexion.commit()
         return True
       except:
         return False  

    @staticmethod
    def eliminar(no_revision):
       try:
         cursor.execute(
            "delete from revisiones where no_revision=%s",
            (no_revision,)
         )
         conexion.commit()
         return True
       except:
         return False  
