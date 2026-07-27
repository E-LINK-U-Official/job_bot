import os
from scraper import MotorNavegacion
from ai_agent import CerebroLocal

class MasterPipeline:
    def __init__(self):
        self.raw_data_file = "jobs_raw.jsonl"
        # Resetea el archivo crudo para iniciar una corrida limpia desde cero
        if os.path.exists(self.raw_data_file):
            os.remove(self.raw_data_file)
            
        self.navegador = MotorNavegacion()
        self.analizador = CerebroLocal()

    def arrancar_sistema_produccion(self):
        # Canales globales estables de alto volumen y acceso abierto
        feeds = {
            "WeWorkRemotely": "https://weworkremotely.com",
            "RemoteOK": "https://remoteok.com"
        }

        # Paso 1: Extracción y escritura en caliente en formato JSONL
        for plataforma, url in feeds.items():
            self.navegador.extraer_y_hacer_stream(url, plataforma)

        # Apaga el navegador inmediatamente al terminar el raspado para liberar RAM
        self.navegador.cerrar_navegador()

        # Paso 2: El Cerebro procesa la data local acumulada y crea el Excel final
        print("\n==========================================================")
        self.analizador.filtrar_y_limpiar_data(self.raw_data_file)
        print("==========================================================\n")

if __name__ == "__main__":
    pipeline = MasterPipeline()
    pipeline.arrancar_sistema_produccion()
