import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class MotorNavegacion:
    def __init__(self):
        print("[Sistema] Iniciando navegador Chrome automatizado real...")
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-gpu")
        # Adds human-like interaction layers to blend in with standard web network traffic
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36")
        self.driver = webdriver.Chrome(options=chrome_options)

    def buscar_y_extraer_web(self, url_empleo):
        print(f"[Navegador] Conectando a la URL real: {url_empleo}...")
        try:
            self.driver.get(url_empleo)
            time.sleep(5)  # Let dynamic layouts finish loading completely
            
            print("[Navegador] Escaneando listados reales...")
            # We Work Remotely stores individual role listings inside standard list tags
            elementos = self.driver.find_elements(By.TAG_NAME, "li")
            
            lista_enlaces = []
            for el in elementos:
                try:
                    texto_completo = el.text.strip()
                    # Extracts hyperlinks containing target operational job paths
                    link_elements = el.find_elements(By.TAG_NAME, "a")
                    
                    for link_el in link_elements:
                        link = link_el.get_attribute("href")
                        if link and "/remote-jobs/" in link and texto_completo:
                            texto_limpio = texto_completo.replace("\n", " | ")
                            lista_enlaces.append({"titulo": texto_limpio, "enlace": link})
                except:
                    continue
            
            return lista_enlaces
            
        except Exception as e:
            print(f"[Error] Falla en la extracción avanzada: {str(e)}")
            return []

    def cerrar_navegador(self):
        print("[Sistema] Cerrando procesos del navegador.")
        self.driver.quit()
