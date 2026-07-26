import time
import pandas as pd
from scraper import MotorNavegacion
from ai_agent import CerebroLocal

class PipelineGlobalAbsoluto:
    def __init__(self):
        print("==========================================================")
        print("[Pipeline] AUTOMATED TRACKING ENGINE & EXCEL GENERATOR")
        print("==========================================================")
        self.navegador = MotorNavegacion()
        self.analizador = CerebroLocal()
        # Storage array to hold verified jobs before exporting
        self.save_bucket = []

    def ejecutar_rastreo_total(self):
        plataformas_objetivo = {
            "LinkedIn (Global)": (
                "https://linkedin.com?"
                "keywords=Data%20Analyst%20AND%20%22Worldwide%22%20OR%20%22Remote%20Global%22"
                "&location=Worldwide&f_WT=2&f_TPR=r2592000"
            ),
            "WeWorkRemotely (Data)": "https://weworkremotely.com",
            "RemoteOK (Worldwide)": "https://remoteok.com"
        }
        
        for nombre, url in plataformas_objetivo.items():
            print(f"\n📡 Connecting browser to: {nombre}...")
            datos_raw = self.navegador.buscar_y_extraer_web(url)
            time.sleep(2)
            
            print(f"[Pipeline] Analyzing {len(datos_raw)} postings from {nombre}...")
            
            for item in datos_raw:
                titulo = item["titulo"]
                enlace = item["enlace"]
                
                veredicto = self.analizador.analizar_puesto(titulo)
                
                if "✓ Puesto Compatible" in veredicto:
                    # Append data structure directly into our export bucket
                    self.save_bucket.append({
                        "Plataforma": nombre,
                        "Posicion_Empresa": titulo[:150],
                        "Enlace_Directo": enlace
                    })
        
        # EXCEL GENERATION STEP
        print(f"\n=================== EXPORTING DATA DATA ===================")
        if self.save_bucket:
            # Convert raw array into a structured Data Frame matrix
            df = pd.DataFrame(self.save_bucket)
            output_file = "jobs.xlsx"
            
            # Export data to local project directory
            df.to_excel(output_file, index=False)
            print(f"🎉 SUCCESS! Clean spreadsheet generated: '{output_file}'")
            print(f"Isolated {len(self.save_bucket)} genuine international leads.")
        else:
            print("⚠️ Complete. No qualified listings matched your criteria during this run.")
        print("===========================================================\n")
        
        self.navegador.cerrar_navegador()

if __name__ == "__main__":
    pipeline = PipelineGlobalAbsoluto()
    pipeline.ejecutar_rastreo_total()
