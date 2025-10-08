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

### 3.1. Instalación en Mac

#### Opción A: Instalación simple con pip (recomendada)

Abre Terminal y escribe:

```bash
pip install reader-toolbox
```

Espera a que termine la instalación. Luego verifica que funcionó escribiendo:

```bash
rdr --help
```

Deberías ver un mensaje de ayuda con instrucciones.

#### Opción B: Instalación con Conda (avanzada)

Si ya usas Conda para proyectos de programación:

```bash
conda create -n reader-toolbox python=3.9
conda activate reader-toolbox
pip install reader-toolbox
```

Para activar el entorno cada vez que lo uses:
```bash
conda activate reader-toolbox
```

Para desactivarlo cuando termines:
```bash
conda deactivate
```

---

### 3.2. Instalación en Windows

1. Abre el **Símbolo del sistema (CMD)** o **PowerShell**

2. Escribe este comando:

```bash
pip install reader-toolbox
```

3. Espera a que termine la instalación

4. Verifica que funcionó escribiendo:

```bash
rdr --help
```

Deberías ver un mensaje de ayuda.

---

## PASO 4: Construir tu primer Carrel

Ahora viene la parte más importante: crear tu carrel.

### 4.1. Comando básico de construcción

#### En Mac:

Abre Terminal y escribe:

```bash
rdr build mi-primer-carrel ~/Desktop/MiCorpus
```

Donde:
- `mi-primer-carrel` es el nombre que le das a tu carrel (puedes cambiarlo)
- `~/Desktop/MiCorpus` es la ruta a tu carpeta con archivos .txt

#### En Windows:

Abre CMD y escribe:

```bash
rdr build mi-primer-carrel "C:\Users\TuNombre\Desktop\MiCorpus"
```

Donde:
- `mi-primer-carrel` es el nombre de tu carrel
- `"C:\Users\TuNombre\Desktop\MiCorpus"` es la ruta a tu carpeta (pon las comillas si hay espacios)

---

### 4.2. Esperar a que se construya

El proceso puede tardar varios minutos dependiendo de cuántos documentos tengas. Verás mensajes en la pantalla mientras Distant Reader:

- Lee tus archivos
- Extrae palabras clave
- Identifica nombres de personas y lugares
- Calcula estadísticas
- Crea visualizaciones

**¡No cierres la ventana hasta que termine!**

---

## PASO 5: Analizar tu Carrel

Una vez construido el carrel, puedes obtener información sobre él.

### 5.1. Ver resumen del carrel

#### En Mac y Windows:

```bash
rdr summarize mi-primer-carrel
```

Esto te mostrará estadísticas básicas: número de documentos, palabras totales, palabras únicas, etc.

---

### 5.2. Leer el carrel (ver archivos generados)

```bash
rdr read mi-primer-carrel
```

Este comando abrirá la carpeta donde Distant Reader guardó todos los archivos de análisis.

---

## PASO 6: Entender los resultados

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

## PASO 7: Comandos útiles adicionales

### Ver todos tus carrels creados:

```bash
rdr catalog
```

### Ver la versión de Distant Reader instalada:

```bash
rdr --version
```

### Ver ayuda general:

```bash
rdr --help
```

---

## Consejos para principiantes

### 1. **Nombres de archivos**
- No uses espacios en los nombres de tus archivos PDF o carpetas
- En lugar de `Mi Corpus.pdf`, usa `MiCorpus.pdf` o `mi_corpus.pdf`

### 2. **Rutas de carpetas**
- Si la ruta tiene espacios, ponla entre comillas: `"C:\Mis Documentos\Corpus"`
- Mejor evita espacios completamente

### 3. **Errores comunes**

**Error: "pip: command not found"**
- Solución: Instala Python desde [python.org](https://www.python.org/downloads/)

**Error: "rdr: command not found"**
- Solución: Asegúrate de haber instalado reader-toolbox correctamente con `pip install reader-toolbox`

**Error al construir el carrel**
- Verifica que la carpeta contenga archivos .txt válidos
- Asegúrate de que los archivos no estén vacíos

### 4. **Optimización**
- Para mejores resultados, usa textos en inglés o español
- Asegúrate de que tus PDFs sean digitales (no imágenes escaneadas)
- Si tienes PDFs escaneados, necesitarás usar OCR primero

---

## Flujo de trabajo completo (resumen)

### Para Mac:

```bash
# 1. Instalar herramientas
pip install pdfminer.six
pip install reader-toolbox

# 2. Convertir PDFs a texto
for f in ~/Desktop/MiCorpus/*.pdf; do
  pdf2txt.py "$f" --outfile "${f%.pdf}.txt"
done

# 3. Construir carrel
rdr build mi-primer-carrel ~/Desktop/MiCorpus

# 4. Ver resumen
rdr summarize mi-primer-carrel

# 5. Abrir carpeta con resultados
rdr read mi-primer-carrel
```

### Para Windows:

```bash
# 1. Instalar herramientas
pip install pdfminer.six
pip install reader-toolbox

# 2. Convertir PDFs a texto (en PowerShell)
Get-ChildItem "C:\Users\TuNombre\Desktop\MiCorpus\*.pdf" | ForEach-Object {
  pdf2txt.py $_.FullName -o ($_.FullName -replace '\.pdf$', '.txt')
}

# 3. Construir carrel (en CMD)
rdr build mi-primer-carrel "C:\Users\TuNombre\Desktop\MiCorpus"

# 4. Ver resumen
rdr summarize mi-primer-carrel

# 5. Abrir carpeta con resultados
rdr read mi-primer-carrel
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

### Problema: Mi carrel no se construye correctamente
**Solución:**
- Verifica que los archivos .txt no estén vacíos
- Intenta con menos documentos primero (5-10 archivos)
- Revisa que no haya caracteres especiales en los nombres de archivos

---

## Siguiente nivel: Procesamiento de textos en español

Para análisis avanzados de textos en español (como los del proyecto LexiMus), puedes crear scripts personalizados que se integren con Distant Reader. Consulta el archivo `spanish-distant-reader.py` disponible en plataformas educativas como Studium.

---

**¿Preguntas o problemas?** Consulta la documentación oficial o busca ayuda en foros de Digital Humanities.

---

**Creado por:** María (Universidad de Salamanca)
**Proyecto:** LexiMus - Léxico y ontología de la música en español
**Licencia:** Creative Commons CC-BY 4.0
