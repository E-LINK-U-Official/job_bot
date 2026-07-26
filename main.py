import time
from scraper import MotorNavegacion
from ai_agent import CerebroLocal

class AutomatedDataPipeline:
    def __init__(self):
        print("==================================================")
        print("[Pipeline] Iniciando Pipeline de Producción Real...")
        print("==================================================")
        self.navegador = MotorNavegacion()
        self.analizador = CerebroLocal()

    def ejecutar_workflow_real(self, enlace_vacante):
        # 1. Extracts individual job dictionary matches
        datos_encontrados = self.navegador.buscar_y_extraer_web(enlace_vacante)
        time.sleep(1)
        
        print(f"\n[Pipeline] Se encontraron {len(datos_encontrados)} listados potenciales en la red.")
        print("=================== REPORTE DE EMPLEOS REALES ===================")
        
        # 2. Iterates and parses each item natively
        conteo_matches = 0
        for item in datos_encontrados[:10]:  # Analyzes the first 10 live postings to test stability
            titulo = item["titulo"]
            enlace = item["enlace"]
            
            # Checks profile compatibility using your technical keyword engine
            resultado_analisis = self.analizador.analizar_puesto(titulo)
            
            if "✓ Puesto Compatible" in resultado_analisis:
                conteo_matches += 1
                print(f"\n[MATCH #{conteo_matches}]")
                print(f"📌 Posición: {titulo}")
                print(f"🔗 Enlace Directo: {enlace}")
                print("-" * 50)
        
        print(f"\n[Pipeline] Análisis finalizado. Encontrados {conteo_matches} puestos óptimos.")
        print("=================================================================\n")
        self.navegador.cerrar_navegador()

if __name__ == "__main__":
    pipeline = AutomatedDataPipeline()
    
    # NEW TARGET: We Work Remotely (Open-access engine directory)
    url_production = "https://weworkremotely.com"
    
    pipeline.ejecutar_workflow_real(url_production)

