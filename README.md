# Tutorial: Cómo construir un Carrel con Distant Reader

## Guía completa para principiantes (Mac y Windows)

---

## ¿Qué es un Carrel?

Un **carrel** es una colección de textos procesados y analizados por Distant Reader, una herramienta que te permite estudiar grandes volúmenes de texto de forma automática. Distant Reader analiza tus documentos y te proporciona estadísticas, visualizaciones y datos útiles para investigación.

---

## Requisitos previos

### Para Mac:
- MacOS (cualquier versión reciente)
- Acceso a la aplicación **Terminal** (viene instalada por defecto)

### Para Windows:
- Windows 10 o superior
- Acceso al **Símbolo del sistema** (CMD) o **PowerShell**

### Para ambos sistemas:
- Python 3 instalado (normalmente ya viene en Mac; en Windows descárgalo de [python.org](https://www.python.org/downloads/))
- Conexión a Internet
- Tus documentos PDF o archivos de texto (.txt)

---

## PASO 1: Preparar tus documentos

### 1.1. Organiza tus archivos

Crea una carpeta en tu escritorio llamada `MiCorpus` y coloca todos tus archivos PDF dentro.

**En Mac:**
```
/Users/TuNombre/Desktop/MiCorpus/
```

**En Windows:**
```
C:\Users\TuNombre\Desktop\MiCorpus\
```

---

## PASO 2: Convertir PDFs a archivos de texto

Si tus documentos son PDF digitales (no escaneados), necesitas convertirlos a archivos de texto (.txt).

### 2.1. Instalar pdfminer

#### En Mac:

1. Abre la aplicación **Terminal** (busca "Terminal" con Spotlight presionando `Cmd + Espacio`)

2. Escribe este comando y presiona Enter:
```bash
pip install pdfminer.six
```

#### En Windows:

1. Abre el **Símbolo del sistema** (busca "CMD" en el menú Inicio)

2. Escribe este comando y presiona Enter:
```bash
pip install pdfminer.six
```

**Nota:** Si recibes un error diciendo que `pip` no se encuentra, primero instala Python desde [python.org](https://www.python.org/downloads/) y asegúrate de marcar la opción "Add Python to PATH" durante la instalación.

---

### 2.2. Convertir UN archivo PDF a texto

#### En Mac:

Abre Terminal y escribe:
```bash
pdf2txt.py -o ~/Desktop/salida.txt ~/Desktop/MiCorpus/documento.pdf
```

Reemplaza `documento.pdf` con el nombre real de tu archivo.

#### En Windows:

Abre CMD y escribe:
```bash
pdf2txt.py -o C:\Users\TuNombre\Desktop\salida.txt C:\Users\TuNombre\Desktop\MiCorpus\documento.pdf
```

Reemplaza `TuNombre` con tu nombre de usuario y `documento.pdf` con el nombre real de tu archivo.

---

### 2.3. Convertir MUCHOS archivos PDF a texto automáticamente

#### En Mac:

Abre Terminal y copia este comando completo:

```bash
for f in ~/Desktop/MiCorpus/*.pdf; do
  pdf2txt.py "$f" --outfile "${f%.pdf}.txt"
done
```

Presiona Enter. Este comando convertirá automáticamente todos los PDFs de la carpeta `MiCorpus` a archivos .txt

#### En Windows (usando PowerShell):

1. Abre **PowerShell** (busca "PowerShell" en el menú Inicio)

2. Copia este comando:

```powershell
Get-ChildItem "C:\Users\TuNombre\Desktop\MiCorpus\*.pdf" | ForEach-Object {
  pdf2txt.py $_.FullName -o ($_.FullName -replace '\.pdf$', '.txt')
}
```

Reemplaza `TuNombre` con tu nombre de usuario y presiona Enter.

---

## PASO 3: Instalar Distant Reader con Conda

**Distant Reader (reader-toolbox)** es el programa que construye carrels. Vamos a instalarlo usando **Conda**, un gestor de entornos que mantiene todo organizado y evita conflictos.

**¿Qué es Conda?**
Conda mantiene Distant Reader separado de otros programas en tu computadora, evitando problemas de compatibilidad.

---

### 3.1. Instalación en Mac

### **PASO 1: Descargar Miniconda para Mac**

1. **Abre tu navegador web** (Safari, Chrome, Firefox)

2. **Descarga el instalador correcto según tu Mac:**

   **Si tienes Mac con chip M1/M2/M3 (Apple Silicon):**
   - Ve a: https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.pkg
   - Se descargará `Miniconda3-latest-MacOSX-arm64.pkg` (60 MB aprox.)

   **Si tienes Mac Intel (anterior a 2020):**
   - Ve a: https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.pkg
   - Se descargará `Miniconda3-latest-MacOSX-x86_64.pkg` (70 MB aprox.)

   **¿No sabes qué Mac tienes?**
   - Haz clic en el menú  (Apple) en la esquina superior izquierda
   - Selecciona "Acerca de este Mac"
   - Si dice "Chip Apple M1/M2/M3" → usa ARM64
   - Si dice "Procesador Intel" → usa x86_64

3. **Espera a que termine la descarga** (verás el archivo en tu carpeta de Descargas)

---

### **PASO 2: Instalar Miniconda en Mac**

1. **Abre tu carpeta de Descargas**
   - Haz clic en el Finder
   - Ve a Descargas

2. **Busca el archivo descargado:**
   - `Miniconda3-latest-MacOSX-arm64.pkg` o
   - `Miniconda3-latest-MacOSX-x86_64.pkg`

3. **Haz doble clic en el archivo .pkg**

4. **Pantalla 1: Introducción**
   - Haz clic en "Continuar"

5. **Pantalla 2: Léeme**
   - Haz clic en "Continuar"

6. **Pantalla 3: Licencia**
   - Haz clic en "Continuar"
   - Luego haz clic en "Aceptar"

7. **Pantalla 4: Tipo de instalación**
   - **Deja "Instalar para mí únicamente"** (opción por defecto)
   - Haz clic en "Instalar"

8. **Introduce tu contraseña de Mac**
   - Escribe tu contraseña (la que usas para encender el Mac)
   - Haz clic en "Instalar software"

9. **Espera 2-3 minutos** mientras se instala

10. **Pantalla final: Resumen**
    - Haz clic en "Cerrar"

11. **IMPORTANTE: Reinicia Terminal**
    - Si tienes Terminal abierta, ciérrala completamente
    - Abre Terminal de nuevo (búscala con Spotlight: Cmd + Espacio)

---

### **PASO 3: Verificar que Miniconda se instaló correctamente**

1. **Abre Terminal:**
   - Presiona `Cmd + Espacio`
   - Escribe "Terminal"
   - Presiona Enter

2. **Escribe este comando y presiona Enter:**
   ```bash
   conda --version
   ```

3. **Si ves algo como `conda 24.x.x`** → ✅ ¡Perfecto! Continúa al PASO 4

4. **Si ves `zsh: command not found: conda`:**

   **Solución (ejecuta estos comandos uno por uno):**
   ```bash
   # Para zsh (Terminal por defecto en Mac modernas)
   echo 'export PATH="$HOME/miniconda3/bin:$PATH"' >> ~/.zshrc
   source ~/.zshrc
   ```

   **O si usas bash (Macs antiguas):**
   ```bash
   echo 'export PATH="$HOME/miniconda3/bin:$PATH"' >> ~/.bash_profile
   source ~/.bash_profile
   ```

   Luego vuelve a probar: `conda --version`

---

### **PASO 4: Crear entorno e instalar Distant Reader**

**En Terminal, ejecuta estos comandos UNO POR UNO:**

**Comando 1: Crear el entorno**
```bash
conda create -n reader-toolbox python=3.9
```

**Lo que verás:**
- Aparecerá una lista de paquetes
- Al final dirá: `Proceed ([y]/n)?`
- **Escribe `y` y presiona Enter**
- Espera 1-2 minutos

**Comando 2: Activar el entorno**
```bash
conda activate reader-toolbox
```

**Lo que verás:**
- Al principio de la línea aparecerá `(reader-toolbox)` ← ¡Esto es buena señal!
- Ejemplo: `(reader-toolbox) maria@MacBook ~ %`

**Comando 3: Instalar dependencias con conda (opcional en Mac, recomendado)**
```bash
conda install -c conda-forge spacy
```

**Lo que verás:**
- Lista de paquetes a instalar
- Preguntará: `Proceed ([y]/n)?`
- **Escribe `y` y presiona Enter**
- Tardará 1-2 minutos

**Nota:** En Mac este paso es opcional (generalmente funciona sin él), pero lo recomendamos para evitar posibles errores de compilación.

**Comando 4: Instalar reader-toolbox**
```bash
pip install reader-toolbox
```

**Lo que verás:**
- Empezará a descargar paquetes
- Tardará 2-3 minutos
- Al final dirá: `Successfully installed reader-toolbox...`

**⚠️ ERRORES CRÍTICOS al ejecutar `rdr build` (después de instalación):**

**Error 1: "No module named numpy"** o **Error 2: "ValueError: numpy.dtype size changed"**

Estos errores aparecen cuando intentas construir un carrel. **SOLUCIÓN:**

```bash
# Paso 1: Desinstalar numpy y pandas si existen
pip uninstall numpy pandas -y

# Paso 2: Reinstalar versiones compatibles con conda
conda install -c conda-forge numpy pandas
```

**Lo que verás:**
- Preguntará: `Proceed ([y]/n)?`
- Escribe `y` y presiona Enter
- Tardará 1-2 minutos instalando
- Al final verás: `done`

**Después de esto, vuelve a intentar construir tu carrel:**
```bash
rdr build prueba ~/Desktop/TXT
```

**⚠️ ERROR: "KeyError: notebooksHome" al ejecutar `rdr build`:**

Este error aparece cuando la configuración de Distant Reader está incompleta. **SOLUCIÓN:**

```bash
# Inicializar configuración de Distant Reader
rdr set -s tika
```

**Lo que verás:**
- Puede pedir confirmar la ubicación de tika-server.jar
- Presiona Enter para aceptar la ubicación por defecto
- Verás: "Configuration updated"

**Ahora SÍ construye tu carrel:**
```bash
rdr build prueba ~/Desktop/TXT
```

**NOTA IMPORTANTE sobre Java:**
- Tika necesita Java para funcionar
- En Mac normalmente Java ya viene instalado
- Si ves error "Java not found", descarga Java desde: https://www.java.com/download/

**Comando 5: Verificar**

**⚠️ IMPORTANTE: Asegúrate de ver `(reader-toolbox)` al inicio de la línea.**

Si NO lo ves, ejecuta primero: `conda activate reader-toolbox`

Una vez que veas `(reader-toolbox) maria@MacBook ~ %`, ejecuta:

```bash
rdr --help
```

**Lo que verás:**
- Una lista de comandos disponibles (catalog, build, summarize, etc.)
- Si ves esto, ¡TODO FUNCIONÓ! ✅

---

### **PASO 5: Cómo usar Distant Reader cada vez que trabajes**

**⚠️ MUY IMPORTANTE:** Cada vez que abras Terminal, debes activar el entorno ANTES de usar cualquier comando `rdr`.

**Pasos cada vez que trabajes:**

1. Abre Terminal
2. **PRIMERO ejecuta:** `conda activate reader-toolbox`
3. Verás `(reader-toolbox)` al inicio de la línea ← **Esto es obligatorio**
4. AHORA SÍ puedes usar comandos como `rdr build`, `rdr summarize`, etc.

**Para salir del entorno:**
```bash
conda deactivate
```

**Resumen del flujo de trabajo:**
```bash
# Al empezar:
conda activate reader-toolbox

# Trabajar normalmente:
rdr build mi-carrel ~/Desktop/MiCorpus
rdr summarize mi-carrel

# Al terminar:
conda deactivate
```

---

### **Solución de problemas en Mac:**

**Problema 1: "conda: command not found"**

**Solución:**
```bash
# Añade conda al PATH
echo 'export PATH="$HOME/miniconda3/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc

# Verifica
conda --version
```

**Problema 2: "conda activate" no funciona**

**Solución:**
```bash
# Inicializa conda para tu shell
conda init zsh  # o "conda init bash" si usas bash
# Cierra y vuelve a abrir Terminal
conda activate reader-toolbox
```

**Problema 3: Error de permisos durante instalación**

**Solución:**
- Asegúrate de elegir "Instalar para mí únicamente" en el instalador
- No uses `sudo` con conda
- Reinstala si es necesario

---

### 3.2. Instalación en Windows

### **PASO 1: Descargar Miniconda**

1. Abre tu navegador web (Chrome, Edge, Firefox)
2. Ve a esta dirección EXACTA: https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe
3. Se descargará un archivo llamado `Miniconda3-latest-Windows-x86_64.exe` (aproximadamente 90 MB)
4. Espera a que termine la descarga (verás el archivo en tu carpeta de Descargas)

**Alternativa si el enlace directo no funciona:**
1. Ve a: https://docs.conda.io/en/latest/miniconda.html
2. Busca la sección "Latest Miniconda installer links"
3. Haz clic en "Miniconda3 Windows 64-bit" (el archivo .exe)

---

### **PASO 2: Instalar Miniconda en Windows**

**Muy importante: Lee CADA pantalla cuidadosamente**

1. **Busca el archivo descargado:**
   - Abre tu carpeta de Descargas
   - Busca `Miniconda3-latest-Windows-x86_64.exe`
   - Haz doble clic en él

2. **Pantalla 1: Welcome**
   - Haz clic en "Next" (Siguiente)

3. **Pantalla 2: License Agreement**
   - Haz clic en "I Agree" (Acepto)

4. **Pantalla 3: Select Installation Type**
   - **IMPORTANTE:** Selecciona "Just Me (recommended)"
   - Haz clic en "Next"

5. **Pantalla 4: Choose Install Location**
   - **Deja la ruta por defecto** (algo como `C:\Users\TuNombre\miniconda3`)
   - **NO cambies nada aquí**
   - Haz clic en "Next"

6. **Pantalla 5: Advanced Installation Options** ← **LA MÁS IMPORTANTE**
   - ✅ **MARCA la casilla:** "Add Miniconda3 to my PATH environment variable"
   - ⚠️ Aparecerá un mensaje en rojo diciendo "Not recommended" - **IGNÓRALO**
   - ✅ **MARCA también:** "Register Miniconda3 as my default Python 3.x"
   - Haz clic en "Install"

7. **Pantalla 6: Installing**
   - Espera 2-3 minutos mientras se instala
   - Verás una barra de progreso

8. **Pantalla 7: Completing**
   - **DESMARCA** las casillas de "Learn more about Anaconda Cloud"
   - Haz clic en "Finish"

9. **Reinicia tu computadora** (opcional pero recomendado)

---

### **PASO 3: Verificar que Miniconda se instaló correctamente**

1. **Abre PowerShell:**
   - Presiona la tecla Windows
   - Escribe "PowerShell"
   - Presiona Enter

2. **Escribe este comando y presiona Enter:**
   ```bash
   conda --version
   ```

3. **Si ves algo como `conda 24.x.x`** → ✅ ¡Perfecto! Continúa al PASO 4

4. **Si ves `conda: command not found` o error:**
   - Cierra PowerShell
   - Busca en el menú de Windows: "Anaconda Prompt" o "Anaconda PowerShell Prompt"
   - Abre esa aplicación
   - Vuelve a probar `conda --version`
   - Si funciona, usa siempre "Anaconda Prompt" en lugar de PowerShell normal

---

### **PASO 4: Crear entorno e instalar Distant Reader**

**Abre PowerShell (o Anaconda Prompt si PowerShell no funcionó)**

**Comando 1: Crear el entorno**
```bash
conda create -n reader-toolbox python=3.9
```

**Lo que verás:**
- Aparecerá una lista de paquetes a instalar
- Al final dirá: `Proceed ([y]/n)?`
- **Escribe `y` y presiona Enter**
- Espera 1-2 minutos

**Comando 2: Activar el entorno**
```bash
conda activate reader-toolbox
```

**Lo que DEBES ver:**
- Al principio de la línea DEBE aparecer `(reader-toolbox)` ← ¡Esto es OBLIGATORIO!
- Ejemplo: `(reader-toolbox) PS C:\Users\Maria>`

**⚠️ SI NO APARECE `(reader-toolbox)`:**

Esto significa que conda no está inicializado para PowerShell. Ejecuta:

```powershell
# Inicializar conda
conda init powershell

# Cerrar PowerShell completamente
exit

# Vuelve a abrir PowerShell

# Ahora activa el entorno
conda activate reader-toolbox

# AHORA SÍ deberías ver: (reader-toolbox) PS C:\Users\User>
```

**Si aún no funciona, usa "Anaconda Prompt":**
- Busca en el menú Windows: "Anaconda Prompt"
- Ábrelo (en lugar de PowerShell)
- Ejecuta: `conda activate reader-toolbox`
- Ahí SÍ aparecerá: `(reader-toolbox)`

**Comando 3: Instalar dependencias con conda (IMPORTANTE - evita errores)**
```bash
conda install -c conda-forge spacy
```

**Lo que verás:**
- Lista de paquetes a instalar (incluyendo blis, cymem, murmurhash)
- Preguntará: `Proceed ([y]/n)?`
- **Escribe `y` y presiona Enter**
- Tardará 1-2 minutos instalando versiones precompiladas

**¿Por qué este paso?** Conda instala versiones precompiladas de paquetes que requieren compilación C++, evitando el error "Microsoft Visual C++ 14.0 required".

**Comando 4: Instalar reader-toolbox**
```bash
pip install reader-toolbox
```

**Lo que verás:**
- Empezará a descargar paquetes adicionales
- Tardará 2-3 minutos
- Al final dirá: `Successfully installed reader-toolbox...`

**⚠️ Si ves error "Microsoft Visual C++ 14.0 or greater is required" o "Failed building wheel for blis":**
- Significa que olvidaste ejecutar el Comando 3
- Vuelve atrás y ejecuta: `conda install -c conda-forge spacy`
- Luego vuelve a intentar: `pip install reader-toolbox`

**⚠️ ERRORES CRÍTICOS al ejecutar `rdr build` (después de instalación):**

**Error 1: "No module named numpy"** o **Error 2: "ValueError: numpy.dtype size changed"**

Estos errores aparecen cuando intentas construir un carrel. **SOLUCIÓN:**

```bash
# Paso 1: Desinstalar numpy y pandas si existen
pip uninstall numpy pandas -y

# Paso 2: Reinstalar versiones compatibles con conda
conda install -c conda-forge numpy pandas
```

**Lo que verás:**
- Preguntará: `Proceed ([y]/n)?`
- Escribe `y` y presiona Enter
- Tardará 1-2 minutos instalando
- Al final verás: `done`

**Después de esto, vuelve a intentar construir tu carrel:**
```bash
python -m rdr build prueba "C:\Users\User\Desktop\TXT"
```

**⚠️ ERROR: "KeyError: notebooksHome" al ejecutar `rdr build`:**

Este error aparece cuando la configuración de Distant Reader está incompleta. **SOLUCIÓN:**

```bash
# Inicializar configuración de Distant Reader
python -m rdr set -s tika
```

**Lo que verás:**
- Puede pedir confirmar la ubicación de tika-server.jar
- Presiona Enter para aceptar la ubicación por defecto
- Verás: "Configuration updated"

**Ahora SÍ construye tu carrel:**
```bash
python -m rdr build prueba "C:\Users\User\Desktop\TXT"
```

**NOTA IMPORTANTE sobre Java:**
- Tika necesita Java para funcionar
- Si ves error "Java not found", descarga Java desde: https://www.java.com/download/
- Instala Java y vuelve a intentar

**Comando 5: Verificar que todo funciona**

**⚠️ IMPORTANTE: Asegúrate de ver `(reader-toolbox)` al inicio de la línea.**

Si NO lo ves, ejecuta primero: `conda activate reader-toolbox`

Una vez que veas `(reader-toolbox) PS C:\Users\User>`, ejecuta:

```bash
python -m rdr --help
```

**NOTA:** En Windows PowerShell, debes usar `python -m rdr` en lugar de solo `rdr` porque PowerShell confunde `rdr` con un comando interno de Windows (Remove-PSDrive).

**Lo que verás:**
- Una lista de comandos disponibles (catalog, build, summarize, etc.)
- Si ves esto, ¡TODO FUNCIONÓ! ✅

**Si TODAVÍA ves error "No se encuentra la unidad" con `rdr --help`:**

**SOLUCIÓN 1 (recomendada): Usa `python -m rdr` siempre**
```bash
python -m rdr --help
python -m rdr build mi-carrel ~/Desktop/MiCorpus
python -m rdr summarize mi-carrel
```

**SOLUCIÓN 2: Usa Anaconda Prompt en lugar de PowerShell**
- Cierra PowerShell
- Busca "Anaconda Prompt" en el menú Windows
- Ábrelo
- Ejecuta: `conda activate reader-toolbox`
- En Anaconda Prompt SÍ funciona: `rdr --help`

**SOLUCIÓN 3: Usa CMD en lugar de PowerShell**
- Cierra PowerShell
- Busca "cmd" en el menú Windows
- Ábrelo
- Ejecuta: `conda activate reader-toolbox`
- En CMD SÍ funciona: `rdr --help`

---

### **PASO 5: Resumen de instalación completa**

**Comandos completos que ejecutaste:**
```bash
# 1. Crear entorno
conda create -n reader-toolbox python=3.9

# 2. Activar entorno
conda activate reader-toolbox

# 3. Instalar dependencias precompiladas
conda install -c conda-forge spacy

# 4. Instalar reader-toolbox
pip install reader-toolbox

# 5. Verificar
rdr --help
```

---

### **PASO 6: Cómo usar Distant Reader cada vez que trabajes**

**⚠️ MUY IMPORTANTE:** Cada vez que abras PowerShell/Anaconda Prompt, debes activar el entorno ANTES de usar cualquier comando `rdr`.

**Pasos cada vez que trabajes:**

1. Abre PowerShell (o Anaconda Prompt)
2. **PRIMERO ejecuta:** `conda activate reader-toolbox`
3. Verás `(reader-toolbox)` al inicio de la línea ← **Esto es obligatorio**
4. AHORA SÍ puedes usar comandos como `rdr build`, `rdr summarize`, etc.

**Para salir del entorno:**
```bash
conda deactivate
```

---

### **Solución de problemas en Windows:**

**Problema 1: "conda: command not found" en PowerShell**

**Solución:**
- Busca en el menú Windows: "Anaconda Prompt"
- Usa siempre "Anaconda Prompt" en lugar de PowerShell normal
- O reinstala Miniconda y asegúrate de marcar "Add to PATH"

**Problema 2: Error durante instalación de Miniconda**

**Solución:**
- Desinstala Miniconda desde Panel de Control → Programas
- Descarga de nuevo el instalador
- Vuelve a instalar siguiendo EXACTAMENTE los pasos del PASO 2
- **Crucial:** Marca "Add to PATH" en la pantalla 5

**Problema 3: "conda activate" funciona pero NO aparece (reader-toolbox)**

**Esto es el problema más común.** Ejecutas `conda activate reader-toolbox` pero el prompt NO cambia.

**Causa:** Conda no está inicializado para PowerShell.

**Solución:**
```powershell
# Inicializar conda para PowerShell
conda init powershell

# Cerrar PowerShell completamente (Ctrl+D o escribe exit)
exit

# Vuelve a abrir PowerShell

# Ahora activa el entorno
conda activate reader-toolbox

# AHORA SÍ deberías ver: (reader-toolbox) PS C:\Users\User>
```

**Alternativa más fácil:**
- Usa "Anaconda Prompt" del menú de Windows en lugar de PowerShell
- Anaconda Prompt ya está configurado correctamente

**Problema 4: Error "rdr : No se encuentra la unidad"**

**Este error significa que NO activaste el entorno conda.**

El error completo es:
```
rdr : No se encuentra la unidad. No existe ninguna unidad con el nombre '--help'.
```

**Solución:**
```bash
# PRIMERO activa el entorno
conda activate reader-toolbox

# AHORA verás (reader-toolbox) al principio de la línea
# Ejemplo: (reader-toolbox) PS C:\Users\User>

# AHORA SÍ puedes usar rdr
rdr --help
```

**RECUERDA:** Debes ejecutar `conda activate reader-toolbox` CADA VEZ que abras PowerShell antes de usar cualquier comando `rdr`.

---

#### Opción B: Instalación con pip + Visual C++ Build Tools (solo usuarios avanzados)

**⚠️ ADVERTENCIA:** Esta opción requiere instalar Microsoft Visual C++ Build Tools (7 GB, 30-45 minutos). **La Opción A con Conda es mucho más fácil y rápida.**

**Error común si intentas pip directamente:**

Si ejecutas `pip install reader-toolbox` sin preparación, obtendrás:
```
error: Microsoft Visual C++ 14.0 or greater is required
Failed building wheel for cymem
Failed building wheel for murmurhash
```

**Esto significa que NO se instaló.** Necesitas Build Tools primero.

**Paso 1: Instalar Visual C++ Build Tools**

1. Ve a: https://visualstudio.microsoft.com/visual-cpp-build-tools/
2. Descarga "Build Tools for Visual Studio 2022"
3. Ejecuta el instalador
4. Marca **"Desktop development with C++"**
5. Haz clic en "Install" (descargará ~7 GB)
6. Espera 20-30 minutos
7. **Reinicia tu computadora** (obligatorio)

**Paso 2: Abrir PowerShell e instalar**

Después de reiniciar:

```bash
pip install reader-toolbox
```

La instalación puede tardar 10-20 minutos compilando paquetes.

**Paso 3: Verificar**

```bash
rdr --help
```

**Comparación de opciones:**

| Aspecto | Opción A (Conda) | Opción B (pip + Build Tools) |
|---------|------------------|------------------------------|
| Tiempo total | 5 minutos | 45-60 minutos |
| Descarga | 500 MB | 7+ GB |
| Dificultad | Fácil | Difícil |
| Tasa de éxito | ~100% | ~80% |

**Recomendación:** Usa Conda (Opción A) a menos que tengas una razón específica para no hacerlo.

---

## PASO 4: Configuración adicional de Distant Reader

Antes de construir tu primer carrel, Distant Reader necesita descargar algunos modelos de lenguaje. Esto solo se hace **una vez**.

### 4.1. Instalar modelos de lenguaje

La primera vez que intentes construir un carrel, Distant Reader te preguntará si quieres instalar los modelos de spaCy. Son necesarios para analizar el texto.

**En Mac y Windows:**

Simplemente ejecuta el siguiente comando y cuando te pregunte si quieres instalar los modelos, escribe `y` y presiona Enter:

```bash
python3 -m spacy download en_core_web_sm
```

**Nota:** Este proceso puede tardar 2-5 minutos dependiendo de tu conexión a Internet.

Si trabajas con textos en español, también es recomendable instalar el modelo español:

```bash
python3 -m spacy download es_core_news_sm
```

**En Windows:** Si `python3` no funciona, intenta con `python`:

```bash
python -m spacy download en_core_web_sm
```

---

## PASO 5: Construir tu primer Carrel

Ahora sí, viene la parte más importante: crear tu carrel.

**Nota importante:** Distant Reader usa el servidor Apache Tika para procesar archivos. Tika requiere Java, pero no te preocupes: en la mayoría de computadoras modernas Java ya está instalado. Si recibes un error sobre Java, descárgalo gratis desde [java.com](https://www.java.com/).

### 5.1. Comando básico de construcción

#### En Mac:

Abre Terminal y escribe:

```bash
rdr build -s mi-primer-carrel ~/Desktop/MiCorpus
```

Donde:
- `-s` inicia el servidor Tika automáticamente (necesario para procesar archivos)
- `mi-primer-carrel` es el nombre que le das a tu carrel (puedes cambiarlo)
- `~/Desktop/MiCorpus` es la ruta a tu carpeta con archivos .txt

#### En Windows:

Abre CMD y escribe:

```bash
rdr build -s mi-primer-carrel "C:\Users\TuNombre\Desktop\MiCorpus"
```

Donde:
- `-s` inicia el servidor Tika automáticamente
- `mi-primer-carrel` es el nombre de tu carrel
- `"C:\Users\TuNombre\Desktop\MiCorpus"` es la ruta a tu carpeta (pon las comillas si hay espacios)

**IMPORTANTE:** Usa siempre la opción `-s` cuando construyas un carrel. Esto asegura que todos los componentes necesarios se inicien correctamente.

---

### 5.2. Esperar a que se construya

El proceso puede tardar varios minutos dependiendo de cuántos documentos tengas. Verás mensajes en la pantalla mientras Distant Reader:

- Lee tus archivos
- Extrae palabras clave
- Identifica nombres de personas y lugares
- Calcula estadísticas
- Crea visualizaciones

**¡No cierres la ventana hasta que termine!**

---

## PASO 6: Analizar tu Carrel

Una vez construido el carrel, puedes obtener información sobre él.

### 6.1. Ver resumen del carrel

#### En Mac y Windows:

```bash
rdr summarize mi-primer-carrel
```

Esto te mostrará estadísticas básicas: número de documentos, palabras totales, palabras únicas, etc.

---

### 6.2. Leer el carrel (ver archivos generados)

```bash
rdr read mi-primer-carrel
```

Este comando abrirá la carpeta donde Distant Reader guardó todos los archivos de análisis.

---

## PASO 7: Entender los resultados

Después de construir tu carrel, Distant Reader crea una carpeta en:

**Mac:**
```
~/reader-library/mi-primer-carrel/
```

**Windows:**
```
C:\Users\TuNombre\reader-library\mi-primer-carrel\
```

Dentro encontrarás:

### Archivos importantes:

1. **`index.htm`** - Abre este archivo en tu navegador para ver un panel interactivo con gráficos y estadísticas

2. **Carpeta `txt/`** - Contiene los archivos de texto procesados

3. **Carpeta `tsv/`** - Contiene tablas con datos extraídos:
   - `bibliographics.tsv` - Información de cada documento
   - `entities-persons.tsv` - Nombres de personas encontradas
   - `entities-places.tsv` - Lugares mencionados
   - `keywords.tsv` - Palabras clave importantes
   - `urls.tsv` - Enlaces web encontrados

4. **Carpeta `etc/`** - Contiene gráficos y visualizaciones

---

## PASO 8: Comandos útiles adicionales

### Ver todos tus carrels creados:

```bash
rdr catalog
```

### Ver información sobre Distant Reader (versión e información):

```bash
rdr about
```

### Ver ayuda general:

```bash
rdr --help
```

---

## Consejos para principiantes

### 1. **Paciencia con la instalación en Windows**
- La primera instalación con pip puede tardar 10-20 minutos (es normal)
- No canceles si ves "Getting requirements to build wheel" durante varios minutos
- Si tienes prisa, usa Conda (Opción A) que es mucho más rápido

### 2. **Nombres de archivos**
- No uses espacios en los nombres de tus archivos PDF o carpetas
- En lugar de `Mi Corpus.pdf`, usa `MiCorpus.pdf` o `mi_corpus.pdf`

### 3. **Rutas de carpetas**
- Si la ruta tiene espacios, ponla entre comillas: `"C:\Mis Documentos\Corpus"`
- Mejor evita espacios completamente

### 4. **Errores comunes**

**Error: "pip: command not found"**
- Solución: Instala Python desde [python.org](https://www.python.org/downloads/)

**Error: "rdr: command not found"**
- Solución: Asegúrate de haber instalado reader-toolbox correctamente con `pip install reader-toolbox`

**Error al construir el carrel**
- Verifica que la carpeta contenga archivos .txt válidos
- Asegúrate de que los archivos no estén vacíos

### 5. **Optimización**
- Para mejores resultados, usa textos en inglés o español
- Asegúrate de que tus PDFs sean digitales (no imágenes escaneadas)
- Si tienes PDFs escaneados, necesitarás usar OCR primero

---

## Flujo de trabajo completo (resumen)

### Para Mac (con instalación simple de pip):

```bash
# 1. Instalar herramientas
pip install pdfminer.six
pip install reader-toolbox

# 2. Instalar modelos de lenguaje (solo la primera vez)
python3 -m spacy download en_core_web_sm
python3 -m spacy download es_core_news_sm

# 3. Convertir PDFs a texto
for f in ~/Desktop/MiCorpus/*.pdf; do
  pdf2txt.py "$f" --outfile "${f%.pdf}.txt"
done

# 4. Construir carrel (con -s para iniciar servidor Tika)
rdr build -s mi-primer-carrel ~/Desktop/MiCorpus

# 5. Ver resumen
rdr summarize mi-primer-carrel

# 6. Abrir carpeta con resultados
rdr read mi-primer-carrel
```

### Para Mac (con Conda - recomendado):

```bash
# 1. Configuración inicial (solo la primera vez)
conda create -n reader-toolbox python=3.9
conda activate reader-toolbox
pip install pdfminer.six
pip install reader-toolbox

# 2. Instalar modelos de lenguaje (solo la primera vez)
python3 -m spacy download en_core_web_sm
python3 -m spacy download es_core_news_sm

# 3. En sesiones futuras: activar el entorno
conda activate reader-toolbox

# 4. Convertir PDFs a texto
for f in ~/Desktop/MiCorpus/*.pdf; do
  pdf2txt.py "$f" --outfile "${f%.pdf}.txt"
done

# 5. Construir carrel (con -s para iniciar servidor Tika)
rdr build -s mi-primer-carrel ~/Desktop/MiCorpus

# 6. Ver resumen
rdr summarize mi-primer-carrel

# 7. Abrir carpeta con resultados
rdr read mi-primer-carrel

# 8. Cuando termines: desactivar el entorno
conda deactivate
```

### Para Windows:

```bash
# 1. Instalar herramientas (en CMD)
pip install pdfminer.six
pip install reader-toolbox

# 2. Instalar modelos de lenguaje (solo la primera vez, en CMD)
python -m spacy download en_core_web_sm
python -m spacy download es_core_news_sm

# 3. Convertir PDFs a texto (en PowerShell)
Get-ChildItem "C:\Users\TuNombre\Desktop\MiCorpus\*.pdf" | ForEach-Object {
  pdf2txt.py $_.FullName -o ($_.FullName -replace '\.pdf$', '.txt')
}

# 4. Construir carrel (en CMD, con -s para iniciar servidor Tika)
rdr build -s mi-primer-carrel "C:\Users\TuNombre\Desktop\MiCorpus"

# 5. Ver resumen
rdr summarize mi-primer-carrel

# 6. Abrir carpeta con resultados
rdr read mi-primer-carrel
```

### Para Windows (con Conda - opcional):

```bash
# 1. Configuración inicial (solo la primera vez, en Anaconda Prompt)
conda create -n reader-toolbox python=3.9
conda activate reader-toolbox
pip install pdfminer.six
pip install reader-toolbox

# 2. Instalar modelos de lenguaje (solo la primera vez)
python -m spacy download en_core_web_sm
python -m spacy download es_core_news_sm

# 3. En sesiones futuras: activar el entorno
conda activate reader-toolbox

# 4. Convertir PDFs a texto
# (usa PowerShell o guarda los PDFs ya convertidos)

# 5. Construir carrel (con -s para iniciar servidor Tika)
rdr build -s mi-primer-carrel "C:\Users\TuNombre\Desktop\MiCorpus"

# 6. Ver resumen
rdr summarize mi-primer-carrel

# 7. Abrir carpeta con resultados
rdr read mi-primer-carrel

# 8. Cuando termines: desactivar el entorno
conda deactivate
```

---

## Recursos adicionales

- **Documentación oficial de Distant Reader:** [https://reader-toolbox.readthedocs.io](https://reader-toolbox.readthedocs.io)
- **PDFMiner:** [https://pypi.org/project/pdfminer.six/](https://pypi.org/project/pdfminer.six/)
- **Búsqueda de bibliografía académica:** [https://elicit.com/](https://elicit.com/), JSTOR

---

## Solución de problemas

### Problema: No puedo abrir Terminal en Mac
**Solución:** Presiona `Cmd + Espacio`, escribe "Terminal" y presiona Enter

### Problema: No puedo abrir CMD en Windows
**Solución:** Presiona la tecla Windows, escribe "cmd" y presiona Enter

### Problema: Los comandos no funcionan
**Solución:** Asegúrate de copiar el comando completo y presionar Enter

### Problema: "rdr: command not found" (usando Conda)
**Solución:** Probablemente olvidaste activar el entorno de Conda. Ejecuta:
```bash
conda activate reader-toolbox
```

### Problema: "conda: command not found"
**Solución:**
- En Mac: Cierra y vuelve a abrir Terminal después de instalar Miniconda
- En Windows: Usa "Anaconda Prompt" en lugar de CMD normal
- Si persiste, reinstala Miniconda y asegúrate de seleccionar la opción de agregar Conda al PATH

### Problema: Mi carrel no se construye correctamente
**Solución:**
- Verifica que los archivos .txt no estén vacíos
- Intenta con menos documentos primero (5-10 archivos)
- Revisa que no haya caracteres especiales en los nombres de archivos

### Problema: Error "Permission denied" en Mac
**Solución:** Algunos comandos pueden requerir permisos. Intenta usar `pip install --user reader-toolbox` en lugar de `pip install reader-toolbox`

### Problema: La instalación de pip tarda mucho o falla
**Solución:**
- Verifica tu conexión a Internet
- Intenta nuevamente (a veces los servidores están ocupados)
- En Mac, intenta `pip3` en lugar de `pip`

### Problema: Error "Language models not found" al construir carrel
**Solución:** Necesitas instalar los modelos de spaCy:
```bash
python3 -m spacy download en_core_web_sm
```
En Windows usa `python` en lugar de `python3`

### Problema: Error "Tika server is not running"
**Solución:** Usa la opción `-s` al construir el carrel:
```bash
rdr build -s mi-primer-carrel ~/Desktop/MiCorpus
```
La opción `-s` inicia automáticamente el servidor Tika necesario para procesar los archivos.

### Problema: El carrel se construye pero no aparecen resultados
**Solución:**
- Verifica que los archivos .txt tengan contenido (ábrelos y revisa que no estén vacíos)
- Asegúrate de que los archivos estén en formato texto plano (.txt)
- Verifica que instalaste los modelos de spaCy correctamente

---

## Siguiente nivel: Procesamiento avanzado de textos en español

### Opción A: Usar Distant Reader estándar con tus textos en español

Los pasos anteriores (PASOS 1-8) funcionan perfectamente para textos en español. Solo necesitas:
- Instalar el modelo español de spaCy: `python3 -m spacy download es_core_news_sm`
- Construir tu carrel normalmente con `rdr build -s`

### Opción B: Usar el script especializado para español (Spanish Distant Reader)

Para análisis más avanzados de textos en español (como los del proyecto LexiMus), existe un **script especializado** que:

- ✅ **Filtra automáticamente 610 palabras vacías** del español (de, la, el, que, en, etc.)
- ✅ **Optimiza el análisis morfológico** para español (sustantivos, verbos, adjetivos)
- ✅ **Identifica entidades culturales** españolas (escritores, compositores, lugares)
- ✅ **Genera visualizaciones avanzadas** (nubes de palabras, gráficos de frecuencia)
- ✅ **Crea base de datos SQLite** con todo el contenido filtrado

---

## PASO 9 (OPCIONAL): Usar Spanish Distant Reader para análisis avanzado

### 9.1. Descargar el script español

El script `spanish-distant-reader.py` está disponible en tu sistema o puedes descargarlo de plataformas educativas (solo para estudiantes del máster en Música Hispana - USAL).

**Archivos necesarios:**
- `spanish-distant-reader.py` - El script principal
- `README.md` - Documentación completa
- `EXAMPLES.md` - Ejemplos de uso
- `install.sh` - Script de instalación automática

### 9.2. Instalar dependencias adicionales

El script español necesita dos bibliotecas adicionales:

**En Mac:**
```bash
pip install matplotlib wordcloud
```

**En Windows:**
```bash
pip install matplotlib wordcloud
```

**Con Conda (Mac y Windows):**
```bash
conda activate reader-toolbox
pip install matplotlib wordcloud
```

**Instalación automática (solo Mac/Linux):**
```bash
cd ~/Desktop/spanish-distant-reader/
bash install.sh
```

### 9.3. Uso básico del script español

#### Sintaxis:
```bash
python3 spanish-distant-reader.py <nombre-del-carrel> <carpeta-con-textos>
```

#### Ejemplos prácticos:

**En Mac:**
```bash
# Analizar corpus de textos literarios
python3 spanish-distant-reader.py mi-corpus-literario ~/Desktop/MiCorpus/

# Analizar revistas musicales
python3 spanish-distant-reader.py revistas-musicales ~/Desktop/RevistasMusica/

# Analizar periódicos históricos
python3 spanish-distant-reader.py periodicos-1900 ~/Desktop/Periodicos/
```

**En Windows:**
```bash
# Analizar corpus de textos
python spanish-distant-reader.py mi-corpus "C:\Users\TuNombre\Desktop\MiCorpus"

# Analizar revistas
python spanish-distant-reader.py revistas "C:\Users\TuNombre\Desktop\Revistas"
```

### 9.4. Resultados generados

El script crea una carpeta con tu carrel que contiene:

**Archivos principales:**
- `index.htm` - Interfaz web profesional (estilo Distant Reader)
- `index.json` - Datos estructurados en formato JSON
- `index.txt` - Bibliografía en texto plano
- `index.xhtml` - Bibliografía en HTML

**Carpeta `figures/` con visualizaciones:**
- `unigrams-cloud.png` - Nube de palabras frecuentes
- `bigrams-cloud.png` - Nube de frases de dos palabras
- `keywords-cloud.png` - Nube de palabras clave generales
- `pos-noun.png` - Sustantivos más frecuentes
- `pos-verb.png` - Verbos más frecuentes
- `pos-adjective.png` - Adjetivos más frecuentes
- `pos-adverb.png` - Adverbios más frecuentes
- `entities-person.png` - Personas mencionadas (escritores, compositores)
- `entities-gpe.png` - Lugares (ciudades, países)
- `entities-org.png` - Organizaciones
- `sizes-histogram.png` - Distribución de tamaños de archivo
- `readability-histogram.png` - Distribución de legibilidad

**Carpeta `etc/`:**
- `stopwords.txt` - Lista de 610 palabras vacías filtradas
- `carrel.db` - Base de datos SQLite con todo el análisis

### 9.5. Ejemplos de uso académico

#### Ejemplo 1: Análisis de obras literarias
```bash
# Analizar las obras completas de Federico García Lorca
python3 spanish-distant-reader.py lorca-completo ~/Desktop/Lorca-Textos/

# Resultados esperados:
# Palabras clave: sangre, luna, muerte, verde, gitano, caballo
# Entidades: Granada, Andalucía, Nueva York
# Temas: simbolismo del color, imágenes de la naturaleza
```

#### Ejemplo 2: Revistas musicales españolas
```bash
# Analizar revistas de música de principios del siglo XX
python3 spanish-distant-reader.py revistas-musicales-1900 ~/Desktop/RevistasMusicales/

# Resultados esperados:
# Términos: música, concierto, orquesta, compositor, teatro, ópera
# Compositores: Falla, Albéniz, Granados, Debussy, Wagner
# Lugares: Teatro Real, Conservatorio, Ateneo
```

#### Ejemplo 3: Prensa histórica
```bash
# Analizar periódicos de la Guerra Civil
python3 spanish-distant-reader.py prensa-guerra-civil ~/Desktop/Periodicos-1936-39/

# Resultados esperados:
# Vocabulario político y militar
# Entidades: Franco, República, Madrid, Barcelona
# Términos: fascista, republicano, frente, milicia
```

### 9.6. Ventajas del script español vs. Distant Reader estándar

| Característica | Distant Reader estándar | Spanish Distant Reader |
|----------------|------------------------|------------------------|
| Idioma optimizado | Inglés | **Español** |
| Filtrado de palabras vacías | Inglés (a, the, is) | **610 palabras en español** |
| Análisis morfológico | Inglés | **Patrones españoles** |
| Entidades culturales | Genérico | **Figuras españolas/latinoamericanas** |
| Visualizaciones | Estándar | **Optimizadas para español** |
| Base de datos | Estándar | **Contenido pre-filtrado** |
| Interfaz web | Estándar | **Estilo Distant Reader** |

### 9.7. Consultar la base de datos SQLite

Puedes hacer consultas avanzadas a la base de datos:

```bash
# Abrir la base de datos
sqlite3 mi-corpus/etc/carrel.db

# Consultas SQL de ejemplo:

# Ver los 20 sustantivos más frecuentes
SELECT word, frequency FROM wrd
WHERE word IN (SELECT word FROM pos WHERE pos = 'noun')
ORDER BY frequency DESC LIMIT 20;

# Ver personas mencionadas
SELECT entity, frequency FROM ent
WHERE type = 'persons'
ORDER BY frequency DESC;

# Ver archivos por legibilidad
SELECT filename, readability FROM bib
ORDER BY readability DESC;
```

### 9.8. Comparar múltiples corpus

Puedes crear varios carrels y compararlos:

```bash
# Crear tres carrels diferentes
python3 spanish-distant-reader.py lorca-obras ~/Desktop/Lorca/
python3 spanish-distant-reader.py machado-obras ~/Desktop/Machado/
python3 spanish-distant-reader.py alberti-obras ~/Desktop/Alberti/

# Luego compara los archivos index.json de cada uno
# Analiza diferencias en vocabulario, temas y estilo
```

### 9.9. Solución de problemas del script español

#### Problema: "No module named 'matplotlib'"
**Solución:**
```bash
pip install matplotlib wordcloud
```

#### Problema: "No module named 'wordcloud'"
**Solución:**
```bash
pip install wordcloud
```

#### Problema: Archivos vacíos o sin resultados
**Solución:**
- Verifica que los archivos sean .txt en codificación UTF-8
- Asegúrate de que los archivos contienen texto en español
- Revisa que no haya caracteres especiales en nombres de archivo

#### Problema: Error de encoding
**Solución en Mac:**
```bash
# Convertir archivos a UTF-8
iconv -f ISO-8859-1 -t UTF-8 archivo.txt > archivo_utf8.txt
```

**Solución en Windows:**
- Abre el archivo en Notepad++
- Ve a "Encoding" → "Convert to UTF-8"
- Guarda el archivo

---

**¿Preguntas o problemas?** Consulta la documentación oficial o busca ayuda en foros de Digital Humanities.

---

**Creado por:** María Palacios Nieto mpalacios@usal.es (Universidad de Salamanca)
**Proyecto:** LexiMus - Léxico y ontología de la música en español
**Licencia:** Creative Commons CC-BY 4.0
