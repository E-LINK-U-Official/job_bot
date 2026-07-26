import time
from scraper import MotorNavegacion
from ai_agent import CerebroLocal

class PipelineGlobalAbsoluto:
    def __init__(self):
        print("==========================================================")
        print("[Pipeline] SISTEMA GLOBAL DE BÚSQUEDA MULTIPLATFORMA REAL")
        print("==========================================================")
        self.navegador = MotorNavegacion()
        self.analizador = CerebroLocal()

    def ejecutar_rastreo_total(self):
        # The ultimate multi-platform global search list
        plataformas_objetivo = {
            "LinkedIn (Filtro Mundial)": (
                "https://linkedin.com?"
                "keywords=Data%20Analyst%20AND%20%22Worldwide%22%20OR%20%22Remote%20Global%22"
                "&location=Worldwide&f_WT=2&f_TPR=r2592000"
            ),
            "WeWorkRemotely (Data Global)": "https://weworkremotely.com",
            "RemoteOK (Worldwide Index)": "https://remoteok.com"
        }
        
        matches_encontrados = 0
        
        for nombre, url in plataformas_objetivo.items():
            print(f"\n📡 Conectando navegador con el feed de: {nombre}...")
            datos_raw = self.navegador.buscar_y_extraer_web(url)
            time.sleep(2)
            
            print(f"[Pipeline] Procesando {len(datos_raw)} listados extraídos de {nombre}...")
            
            for item in datos_raw:
                titulo = item["titulo"]
                enlace = item["enlace"]
                
                # Check eligibility locally against your anti-senior, anti-scam rules
                veredicto = self.analizador.analizar_puesto(titulo)
                
                if "✓ Puesto Compatible" in veredicto:
                    matches_encontrados += 1
                    print(f"\n🌍 [MATCH MUNDIAL REAL #{matches_encontrados}] via {nombre}")
                    print(f"📌 Puesto/Empresa: {titulo[:150]}")
                    print(f"🔗 Enlace de Aplicación: {enlace}")
                    print("-" * 75)
                    
        print(f"\n=================== INFORME DE CIERRE DE SISTEMA ===================")
        print(f"Análisis finalizado. Se aislaron {matches_encontrados} ofertas reales y cualificadas a nivel mundial.")
        print("====================================================================\n")
        self.navegador.cerrar_navegador()

if __name__ == "__main__":
    pipeline = PipelineGlobalAbsoluto()
    pipeline.ejecutar_rastreo_total()
