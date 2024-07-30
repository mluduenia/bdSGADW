from django.db import models

class Registro(models.Model):
    t_time = models.DateTimeField(db_column='T_TIME', primary_key=True)  # Mapea a la columna T_TIME
    t_data = models.FloatField(db_column='T_DATA')    # Mapea a la columna T_DATA

    class Meta:
        managed = False
        db_table = 's703_0'  # Reemplaza con el nombre de tu tabla

    def __str__(self):
        return f"{self.t_time} {self.t_data}"
