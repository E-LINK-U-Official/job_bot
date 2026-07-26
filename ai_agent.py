class CerebroLocal:
    def __init__(self):
        self.keywords = ["data", "analyst", "analytics", "sql", "power bi", "operations", "bi", "verification"]
        self.unqualified_keywords = ["senior", "sr.", "lead", "principal", "python", "machine learning", "phd"]

    def analizar_puesto(self, texto_trabajo):
        texto_limpio = texto_trabajo.lower()
        
        for word in self.unqualified_keywords:
            if word in texto_limpio:
                return f"[RECHAZADO] Requiere '{word}'"
        
        matches = [p for p in self.keywords if p in texto_limpio]
        
        if matches:
            return f"✓ Puesto Compatible. Competencias: {', '.join(matches)}."
        else:
            return "[RECHAZADO] No cumple perfil."
