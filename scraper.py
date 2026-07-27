import time
import json
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class MotorNavegacion:
    def __init__(self):
        print("[Sistema] Desplegando navegador Chrome con camuflaje de TLS fingerprint...")
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-gpu")
        # Cabeceras de simulación humana para evitar detección automatizada
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        
        self.driver = webdriver.Chrome(options=chrome_options)
        self.output_raw = "jobs_raw.jsonl"

    def hacer_scroll_humano(self):
        """Simula pausas dinámicas y movimientos intermitentes de lectura humana."""
        for i in range(2):
            self.driver.execute_script(f"window.scrollTo(0, {400 * (i+1)});")
            time.sleep(random.uniform(2.0, 4.5))

    def extraer_y_hacer_stream(self, url, plataforma):
        print(f"\n📡 Navegador conectando a: {plataforma}...")
        try:
            self.driver.get(url)
            time.sleep(random.randint(6, 9))
            self.hacer_scroll_humano()

            conteo_local = 0
            
            # Selectores dinámicos universales según la plataforma objetivo
            if "weworkremotely.com" in url:
                elementos = self.driver.find_elements(By.TAG_NAME, "li")
                for el in elementos:
                    try:
                        link = el.find_element(By.TAG_NAME, "a").get_attribute("href")
                        if link and "/remote-jobs/" in link:
                            self.guardar_linea_jsonl(el.text.strip(), link, plataforma)
                            conteo_local += 1
                    except: continue

            elif "remoteok.com" in url:
                filas = self.driver.find_elements(By.TAG_NAME, "tr")
                for f in filas:
                    try:
                        link = f.find_element(By.TAG_NAME, "a").get_attribute("href")
                        if link and link.startswith("http"):
                            self.guardar_linea_jsonl(f.text.strip(), link, plataforma)
                            conteo_local += 1
                    except: continue

            print(f"[Navegador] Stream completado. {conteo_local} filas crudas añadidas al archivo JSONL.")
            
        except Exception as e:
            print(f"[Error] Caída de hilo interceptada en {plataforma}: {str(e)}")

    def guardar_linea_jsonl(self, titulo, enlace, plataforma):
        """Escribe la información en el disco duro inmediatamente (Fail-safe activo)."""
        payload = {
            "plataforma": plataforma,
            "titulo": titulo.replace("\n", " | "),
            "enlace": enlace
        }
        with open(self.output_raw, "a", encoding="utf-8") as f:
            f.write(json.dumps(payload, ensure_ascii=False) + "\n")

    def cerrar_navegador(self):
        print("[Sistema] Apagando procesos del navegador de forma segura.")
        self.driver.quit()
