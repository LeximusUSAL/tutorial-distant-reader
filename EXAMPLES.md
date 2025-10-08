# Spanish Distant Reader - Examples and Use Cases

## 📚 Literary Analysis Examples

### Example 1: Analyzing Federico García Lorca's Complete Works

```bash
# Create corpus directory
mkdir lorca-corpus

# Add text files (poems, plays, prose)
# - romancero-gitano.txt
# - poeta-nueva-york.txt
# - bodas-sangre.txt
# - casa-bernarda-alba.txt

# Run analysis
python3 spanish-distant-reader.py lorca-completo lorca-corpus/

# Expected results:
# Top keywords: sangre, luna, muerte, verde, gitano, caballo, agua, noche
# Entities: Granada, Andalucía, Nueva York, España
# Themes: Color symbolism, nature imagery, death motifs
```

### Example 2: Generation of '27 Comparative Study

```bash
# Compare different poets of the Generation of '27
python3 spanish-distant-reader.py generacion-27-alberti alberti-texts/
python3 spanish-distant-reader.py generacion-27-cernuda cernuda-texts/
python3 spanish-distant-reader.py generacion-27-aleixandre aleixandre-texts/

# Compare results across the three carrels
# Analyze differences in vocabulary, themes, and style
```

## 🗞️ Historical Newspaper Analysis

### Example 3: Spanish Civil War Press Coverage

```bash
# Directory structure:
# guerra-civil-prensa/
# ├── abc-1936-1939/
# ├── el-socialista-1936-1939/
# └── la-vanguardia-1936-1939/

python3 spanish-distant-reader.py guerra-civil-abc abc-1936-1939/
python3 spanish-distant-reader.py guerra-civil-socialista el-socialista-1936-1939/
python3 spanish-distant-reader.py guerra-civil-vanguardia la-vanguardia-1936-1939/

# Compare political vocabularies across different newspapers
# Expected differences:
# ABC: More conservative terminology
# El Socialista: Socialist and republican vocabulary
# La Vanguardia: Regional Catalan perspective
```

### Example 4: Evolution of Spanish Press (1900-1950)

```bash
# Chronological analysis
python3 spanish-distant-reader.py prensa-1900-1910 periodicos-1900s/
python3 spanish-distant-reader.py prensa-1920-1930 periodicos-1920s/
python3 spanish-distant-reader.py prensa-1940-1950 periodicos-1940s/

# Track vocabulary evolution across 50 years
# Observe technological, social, and political changes
```

## 🎵 Musical and Cultural Publications

### Example 5: Spanish Musical Magazines Analysis

```bash
# Early radio magazines (1920s-1930s)
python3 spanish-distant-reader.py ondas-revista ondas-txt-files/

# Expected results:
# Top terms: música, radio, jazz, concierto, orquesta
# Entities: Haydn, Fauré, Gershwin (popular in 1920s)
# Technology terms: estación, radiodifusión, ondas
```

### Example 6: Flamenco and Traditional Music Study

```bash
# Flamenco publications and studies
python3 spanish-distant-reader.py flamenco-corpus flamenco-texts/

# Expected vocabulary:
# Musical terms: cante, baile, toque, guitarra, palmas
# Regional: andaluz, jerez, sevilla, triana
# Technical: compás, falseta, escobilla, remate
```

## 🏛️ Historical and Cultural Studies

### Example 7: Medieval Spanish Texts

```bash
# Medieval chronicles and literature
python3 spanish-distant-reader.py medieval-espanol textos-medievales/

# Results show evolution of Spanish language:
# Archaic vocabulary and forms
# Historical events and figures
# Religious and feudal terminology
```

### Example 8: Golden Age Spanish Literature

```bash
# Siglo de Oro analysis
python3 spanish-distant-reader.py siglo-oro-cervantes cervantes-corpus/
python3 spanish-distant-reader.py siglo-oro-quevedo quevedo-corpus/
python3 spanish-distant-reader.py siglo-oro-gongora gongora-corpus/

# Compare baroque styles:
# Cervantes: Narrative vocabulary, character types
# Quevedo: Satirical and philosophical terms
# Góngora: Complex imagery, mythological references
```

## 🔬 Linguistic Research Applications

### Example 9: Regional Spanish Variations

```bash
# Analyze texts from different Spanish-speaking regions
python3 spanish-distant-reader.py espanol-mexico textos-mexicanos/
python3 spanish-distant-reader.py espanol-argentina textos-argentinos/
python3 spanish-distant-reader.py espanol-espana textos-espanoles/

# Compare regional vocabularies and expressions
# Identify distinctive terms and cultural references
```

### Example 10: Diachronic Language Change

```bash
# Track Spanish language evolution
python3 spanish-distant-reader.py espanol-1800 textos-s19/
python3 spanish-distant-reader.py espanol-1900 textos-s20/
python3 spanish-distant-reader.py espanol-2000 textos-s21/

# Observe vocabulary changes across centuries
# Track neologisms, archaisms, and semantic shifts
```

## 📊 Advanced Analysis Techniques

### Comparative Analysis Workflow

1. **Create multiple carrels** for comparison
2. **Export data** from each `index.json`
3. **Compare top keywords** across corpora
4. **Analyze entity differences**
5. **Study morphological patterns**

```python
# Python script for comparing multiple carrels
import json

def compare_carrels(carrel1_path, carrel2_path):
    with open(f"{carrel1_path}/index.json") as f1:
        data1 = json.load(f1)
    with open(f"{carrel2_path}/index.json") as f2:
        data2 = json.load(f2)

    # Compare top keywords
    keywords1 = set(data1['top_keywords'].keys())
    keywords2 = set(data2['top_keywords'].keys())

    unique_to_1 = keywords1 - keywords2
    unique_to_2 = keywords2 - keywords1
    common = keywords1 & keywords2

    print(f"Unique to {carrel1_path}: {unique_to_1}")
    print(f"Unique to {carrel2_path}: {unique_to_2}")
    print(f"Common keywords: {common}")

# Usage
compare_carrels("lorca-completo", "machado-completo")
```

### Database Queries

```sql
-- Query the SQLite database for advanced analysis
-- Connect to carrel.db and run SQL queries

-- Most frequent nouns
SELECT word, frequency FROM wrd
WHERE word IN (SELECT word FROM pos WHERE pos = 'noun')
ORDER BY frequency DESC LIMIT 20;

-- Entities by type
SELECT entity, type, frequency FROM ent
WHERE type = 'persons'
ORDER BY frequency DESC;

-- Files by readability
SELECT filename, readability FROM bib
ORDER BY readability DESC;
```

## 🎯 Best Practices

### Corpus Preparation
- **Consistent encoding**: Always use UTF-8
- **Clean text**: Remove headers, footers, page numbers
- **Meaningful names**: Use descriptive filenames
- **Proper segmentation**: One text per file

### Analysis Strategy
- **Start small**: Test with a few files first
- **Comparative approach**: Analyze related corpora
- **Context awareness**: Consider historical and cultural context
- **Manual verification**: Review surprising results

### Interpretation Tips
- **Top keywords**: Focus on domain-specific vocabulary
- **Entities**: Verify proper noun recognition
- **Bigrams**: Look for meaningful phrases
- **Distributions**: Consider file size variations

## 🔍 Troubleshooting Common Issues

### Empty Results
```bash
# If no words appear after filtering:
# Check file encoding (should be UTF-8)
# Verify files contain Spanish text
# Review file format (should be plain text)
```

### Encoding Problems
```bash
# Convert files to UTF-8 if needed
iconv -f ISO-8859-1 -t UTF-8 input.txt > output.txt
```

### Large Corpora
```bash
# For very large corpora (1000+ files):
# Process in smaller batches
# Monitor memory usage
# Consider using more powerful hardware
```

## 📈 Expected Processing Times

| Corpus Size | Files | Processing Time |
|-------------|-------|-----------------|
| Small       | 10-50 | 30 seconds - 2 minutes |
| Medium      | 51-200 | 2-8 minutes |
| Large       | 201-500 | 8-20 minutes |
| Very Large  | 500+ | 20+ minutes |

Times vary based on file sizes and system specifications.

---

**💡 These examples demonstrate the versatility of Spanish Distant Reader for various Spanish language research applications in digital humanities.**