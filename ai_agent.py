class CerebroLocal:
    def __init__(self):
        # Broad strategic keywords to match dynamic global listings
        self.keywords = ["data", "analyst", "analytics", "sql", "power bi", "operations", "bi"]

    def analizar_puesto(self, texto_trabajo):
        # Converts text to lowercase to ensure matching works perfectly
        texto_limpio = texto_trabajo.lower()
        
        # Check if ANY of your target tech keywords exist inside the job text
        matches = [palabra for palabra in self.keywords if palabra in texto_limpio]
        
        if matches:
            return f"✓ Puesto Compatible. Detectadas competencias clave: {', '.join(matches)}."
        else:
            return "\n[Resumen del Sistema]: El puesto no cumple con los requisitos técnicos de tu perfil."

if __name__ == "__main__":
    bot = CerebroLocal()
    print("\n[AI Agent] Ejecutando prueba de conexión local...")
    vacante_prueba = "Senior Data Specialist with SQL skills"
    print(bot.analizar_puesto(vacante_prueba))
