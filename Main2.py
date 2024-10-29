from datetime import datetime, timedelta

class RecoleccionResiduos:
    def __init__(self):
        self.residuos = {
            'peligrosos': [],
            'biodegradables': [],
            'reciclables': [],
            'plasticos': []
        }
        self.dia_actual = datetime.now()

    def recolectar_residuos(self):
        dia = self.dia_actual.day
        dia_semana = self.dia_actual.weekday()  # 0 = Lunes, 1 = Martes, ..., 6 = Domingo

        
        if dia_semana == 1 or dia_semana == 3: 
            print("Recolección en la sede de oficina.")
        if dia % 2 == 1:  # Días impares
            print("Recolección en la planta principal.")
        if dia % 2 == 0:  # Días pares
            print("Recolección en la planta secundaria.")

    def almacenar_residuos(self, tipo_residuo, cantidad):
        if tipo_residuo in self.residuos:
            self.residuos[tipo_residuo].append(cantidad)
            print(f"Almacenados {cantidad} de residuos {tipo_residuo}.")
        else:
            print("Tipo de residuo no válido.")

    def distribuir_residuos(self):
        if self.dia_actual.day % 3 == 0:
            print("Distribuyendo residuos al almacén.")
            self.residuos = {k: [] for k in self.residuos}
        else:
            print("No es día de distribución.")

    def avanzar_dia(self):
        self.dia_actual += timedelta(days=1)