class CerebroLocal:
    def __init__(self):
        # Palabras clave de alta relevancia para tu perfil de datos
        self.keywords = ["business intelligence", "analyst", "power bi", "sql", "data", "operations"]

    def analizar_puesto(self, texto_trabajo):
        print("[AI Agent] Analizando texto mediante motor semántico local...")
        texto_limpio = texto_trabajo.lower()
        
        # Encuentra qué palabras de tu perfil hacen match con la vacante
        matches = [palabra for palabra in self.keywords if palabra in texto_limpio]
        
        if matches:
            summary = f"✓ Puesto Compatible. Detectadas competencias clave: {', '.join(matches)}."
            return f"\n[Resumen del Sistema]: {summary}\n[Decisión]: Proceder con la automatización."
        else:
            return "\n[Resumen del Sistema]: El puesto no cumple con los requisitos técnicos de tu perfil."

if __name__ == "__main__":
    bot = CerebroLocal()
    print("\n[AI Agent] Ejecutando prueba de conexión local...")
    vacante_prueba = "Se busca Business Intelligence Analyst con experiencia en Power BI y SQL."
    print(bot.analizar_puesto(vacante_prueba))
