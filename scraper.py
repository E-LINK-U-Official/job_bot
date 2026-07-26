import time

class MotorNavegacion:
    def __init__(self):
        print("[Sistema] Iniciando motor de exploración web...")
        self.sitio_objetivo = "https://linkedin.com"

    def simular_extraccion(self, puesto_busqueda):
        print(f"[Navegador] Buscando vacantes para: {puesto_busqueda}...")
        time.sleep(2) # Simula el tiempo de carga de la página
        
        # Texto de prueba que el bot "encuentra" al leer la web
        texto_encontrado = (
            "We are looking for a Data Specialist. The ideal candidate will manage "
            "data operations using Bullhorn CRM and build automated dashboards with "
            "SQL and Business Intelligence tools. Recruiter contact: corporate.talent@recruitment.com"
        )
        print("[Navegador] Extracción de texto completada con éxito.")
        return texto_encontrado

if __name__ == "__main__":
    # Prueba local del navegador simulado
    explorador = MotorNavegacion()
    datos_web = explorador.simular_extraccion("Business Intelligence Analyst")
    print(f"\n[Datos extraídos de la web]: {datos_web}")
