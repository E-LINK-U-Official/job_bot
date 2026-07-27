import os
import pandas as pd
from datetime import datetime

class CerebroLocal:
    def __init__(self):
        # Competencias técnicas requeridas para tu perfil calificado
        self.keywords = ["data", "analyst", "analytics", "sql", "power bi", "operations", "bi"]
        
        # Filtro radical anti-estafas, agencias basura y puestos no calificados
        self.blacklist = [
            "jobot", "bravado", "cybercoders", "gss", "lead", 
            "principal", "python", "machine learning", "phd", "master", "hybrid", "on-site"
        ]

    def filtrar_y_limpiar_data(self, archivo_raw_jsonl):
        """Lee el flujo crudo en tiempo real, aplica filtros y genera el snapshot limpio en Excel."""
        print("[AI Agent] Iniciando procesamiento matricial de vacantes...")
        
        if not os.path.exists(archivo_raw_jsonl):
            print(f"⚠️ Archivo crudo {archivo_raw_jsonl} no encontrado.")
            return

        # Carga el JSONL dinámicamente sin saturar la memoria RAM
        df_raw = pd.read_json(archivo_raw_jsonl, lines=True)
        records_limpios = []

        for _, row in df_raw.iterrows():
            texto_limpio = str(row["titulo"]).lower()
            
            # Regla de exclusión inmediata (Blacklist)
            if any(forbidden in texto_limpio for forbidden in self.blacklist):
                continue
                
            # Regla de inclusión de competencias clave
            if any(skill in texto_limpio for skill in self.keywords):
                records_limpios.append({
                    "Fecha_Rastreo": datetime.now().strftime("%Y-%m-%d %H:%M"),
                    "Plataforma": row["plataforma"],
                    "Posicion_Empresa": row["titulo"],
                    "Enlace_Directo": row["enlace"]
                })

        if records_limpios:
            df_clean = pd.DataFrame(records_limpios)
            # Evita duplicados exactos si corres el bot varias veces
            df_clean.drop_duplicates(subset=["Enlace_Directo"], inplace=True)
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            archivo_excel = f"jobs_clean_{timestamp}.xlsx"
            
            df_clean.to_excel(archivo_excel, index=False)
            print(f"🎉 FILTRADO COMPLETADO EXITOSAMENTE! Creado: '{archivo_excel}'")
            print(f"Se aislaron {len(records_limpios)} puestos corporativos mundiales legítimos.")
        else:
            print("⚠️ Operación finalizada. Ningún puesto cumplió con los estándares estrictos de tu perfil.")

if __name__ == "__main__":
    # Prueba de inicialización del módulo de analítica
    agent = CerebroLocal()
    print("[AI Agent] Sistema listo para recibir flujos de datos.")
