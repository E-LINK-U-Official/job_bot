import time
from scraper import MotorNavegacion
from ai_agent import CerebroLocal

class AutomatedDataPipeline:
    def __init__(self):
        print("==================================================")
        print("[Pipeline] Iniciando Pipeline de Automatización...")
        print("==================================================")
        # Cargamos los dos módulos que creaste desde cero
        self.navegador = MotorNavegacion()
        self.analizador = CerebroLocal()

    def ejecutar_workflow(self, puesto_objetivo):
        # Paso 1: El navegador extrae la información de la web
        texto_extraido = self.navegador.simular_extraccion(puesto_objetivo)
        time.sleep(1)
        
        # Paso 2: El analizador local procesa el texto extraído
        resultado_analisis = self.analizador.analizar_puesto(texto_extraido)
        
        print("\n=================== RESULTADO ===================")
        print(resultado_analisis)
        print("==================================================\n")

if __name__ == "__main__":
    # Ejecutamos el flujo completo del sistema para tu portafolio
    pipeline = AutomatedDataPipeline()
    pipeline.ejecutar_workflow("Data Analyst")

