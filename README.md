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

## PASO 3: Instalar Distant Reader

**Distant Reader (reader-toolbox)** es el programa que construye carrels. Necesitas instalarlo antes de poder analizar textos.

### 3.1. Instalación en Mac

En Mac tienes dos opciones: instalación directa con pip (más simple) o instalación con Conda (recomendada para trabajos de investigación).

#### Opción A: Instalación simple con pip

Esta es la forma más rápida si solo quieres probar Distant Reader.

1. Abre Terminal

2. Escribe este comando y presiona Enter:

```bash
pip install reader-toolbox
```

3. Espera a que termine la instalación (puede tardar 1-2 minutos)

4. Verifica que funcionó escribiendo:

```bash
rdr --help
```

Deberías ver un mensaje de ayuda con una lista de comandos disponibles.

**¿Ya terminaste?** Ve directamente al PASO 4 para construir tu primer carrel.

---

#### Opción B: Instalación con Conda (recomendada para investigación)

**¿Qué es Conda?**

Conda es un gestor de "entornos virtuales" que mantiene tus proyectos organizados y separados. Es especialmente útil si trabajas con múltiples proyectos de investigación o si planeas usar Distant Reader regularmente.

**Ventajas de usar Conda:**
- Mantiene las dependencias de Distant Reader separadas de otros programas
- Evita conflictos entre diferentes versiones de Python
- Te permite tener múltiples versiones de herramientas instaladas sin problemas
- Es la forma profesional de gestionar proyectos de programación

**Paso 1: Instalar Conda (solo la primera vez)**

Si no tienes Conda instalado:

1. Descarga Miniconda (versión ligera de Conda) desde: https://docs.conda.io/en/latest/miniconda.html

2. Descarga el instalador para macOS y ejecútalo

3. Sigue las instrucciones en pantalla (acepta las opciones por defecto)

4. Cierra y vuelve a abrir Terminal

**Paso 2: Crear un entorno para Distant Reader**

Abre Terminal y ejecuta estos comandos uno por uno:

```bash
# Crear un entorno nuevo llamado "reader-toolbox" con Python 3.9
conda create -n reader-toolbox python=3.9
```

Te preguntará si quieres continuar, escribe `y` y presiona Enter.

```bash
# Activar el entorno (esto es importante)
conda activate reader-toolbox
```

Verás que el prompt de tu terminal cambia y ahora muestra `(reader-toolbox)` al principio. Esto significa que estás dentro del entorno.

```bash
# Instalar reader-toolbox dentro del entorno
pip install reader-toolbox
```

**Paso 3: Verificar la instalación**

```bash
rdr --help
```

Deberías ver el mensaje de ayuda.

**¿Cómo usar Conda cada vez que trabajes con Distant Reader?**

**Cada vez que abras Terminal** y quieras usar Distant Reader, necesitas activar el entorno:

```bash
conda activate reader-toolbox
```

Ahora puedes usar todos los comandos de Distant Reader (`rdr build`, `rdr summarize`, etc.)

**Cuando termines tu trabajo**, desactiva el entorno:

```bash
conda deactivate
```

**Resumen del flujo de trabajo con Conda:**

```bash
# Al empezar tu sesión de trabajo:
conda activate reader-toolbox

# Trabajar con Distant Reader normalmente:
rdr build mi-carrel ~/Desktop/MiCorpus
rdr summarize mi-carrel

# Al terminar:
conda deactivate
```

---

### 3.2. Instalación en Windows

**IMPORTANTE PARA WINDOWS:** En Windows, la instalación con Conda es **OBLIGATORIA para la mayoría de usuarios** porque evita errores de compilación de paquetes C++ (cymem, murmurhash, pandas). La instalación directa con pip requiere instalar Visual C++ Build Tools (7 GB, 30-45 minutos) y puede fallar.

#### Opción A: Instalación con Conda (RECOMENDADA para Windows)

**Paso 1: Instalar Miniconda (solo la primera vez)**

1. Descarga Miniconda para Windows desde: https://docs.conda.io/en/latest/miniconda.html
2. Descarga el instalador `.exe` para Windows
3. Ejecuta el instalador y sigue las instrucciones
4. **IMPORTANTE:** Durante la instalación, marca la opción "Add Miniconda to PATH" si aparece
5. Completa la instalación

**Paso 2: Abrir Anaconda Prompt**

1. Presiona la tecla Windows
2. Busca "Anaconda Prompt" (se instaló con Miniconda)
3. Ábrelo (NO uses CMD normal, usa Anaconda Prompt)

**Paso 3: Crear entorno e instalar reader-toolbox**

Ejecuta estos comandos uno por uno en Anaconda Prompt:

```bash
# Crear entorno con Python 3.9
conda create -n reader-toolbox python=3.9

# Cuando pregunte, escribe 'y' y presiona Enter

# Activar el entorno
conda activate reader-toolbox

# Instalar reader-toolbox
pip install reader-toolbox
```

**Paso 4: Verificar la instalación**

```bash
rdr --help
```

Deberías ver un mensaje de ayuda con la lista de comandos.

**Para usar Distant Reader en el futuro:**
1. Abre "Anaconda Prompt"
2. Ejecuta: `conda activate reader-toolbox`
3. Ya puedes usar todos los comandos `rdr`

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

El script `spanish-distant-reader.py` está disponible en tu sistema o puedes descargarlo de plataformas educativas como Studium.

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

**Creado por:** María (Universidad de Salamanca)
**Proyecto:** LexiMus - Léxico y ontología de la música en español
**Licencia:** Creative Commons CC-BY 4.0
