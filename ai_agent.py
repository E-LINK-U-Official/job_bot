class CerebroLocal:
    def __init__(self):
        # 1. Target Core Technical Competencies
        self.keywords = ["data", "analyst", "analytics", "sql", "power bi", "operations", "bi"]
        
        # 2. BLACKLIST: Spam agencies, generic aggregators, and known scam keywords
        self.blacklist = [
            "jobot", "bravado", "cybercoders", "gss", "crossing hurdles", 
            "hiring fast", "immediate start", "no experience required", 
            "whatsapp", "telegram", "commission only", "unspecified"
        ]

    def analizar_puesto(self, texto_trabajo):
        texto_limpio = texto_trabajo.lower()
        
        # Guard Clause 1: Immediately drop anything matching the scam/agency blacklist
        for item_bloqueado in self.blacklist:
            if item_bloqueado in texto_limpio:
                return f"[RECHAZADO] Filtrado por lista negra de Spam/Agencia: '{item_bloqueado}'"
        
        # Guard Clause 2: Ensure it has an established company name structure (contains 'at' or '|')
        if " at " not in texto_limpio and "|" not in texto_limpio:
            return "[RECHAZADO] Estructura corporativa no verificada (Falta nombre de empresa)"

        # Check for genuine skillset matches
        matches = [palabra for palabra in self.keywords if palabra in texto_limpio]
        
        if matches:
            return f"✓ Puesto Compatible. Detectadas competencias clave: {', '.join(matches)}."
        else:
            return "[RECHAZADO] No cumple con los requisitos técnicos de tu perfil."
