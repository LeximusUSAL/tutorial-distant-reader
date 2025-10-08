#!/usr/bin/env python3
"""
Spanish Distant Reader - Generic Version
Complete Distant Reader functionality with Spanish stopwords filtering from the start

Usage:
    python3 spanish-distant-reader.py <carrel-name> <source-directory>
    python3 spanish-distant-reader.py mi-corpus /ruta/a/archivos/txt

Features:
- Filters 610 Spanish stopwords automatically
- Creates all Distant Reader visualizations
- Generates SQLite database with Spanish-filtered content
- Produces HTML index in Distant Reader style
- Optimized for Spanish text analysis

Author: Digital Humanities Research - Universidad de Salamanca
Compatible with: Spanish text corpora, literary texts, newspapers, magazines
"""

import os
import sys
import re
import json
import sqlite3
import shutil
from collections import Counter, defaultdict
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from datetime import datetime

# Set matplotlib backend for headless operation
import matplotlib
matplotlib.use('Agg')

# Spanish stopwords (610 words from critica-espana collection)
SPANISH_STOPWORDS = """
http https a actualmente adelante además afirmó agregó ahora ahí al algo alguna algunas alguno algunos algún alrededor ambos ampleamos ante anterior antes apenas aproximadamente aquel aquellas aquellos aqui aquí arriba aseguró así atras aunque ayer añadió aún bajo bastante bien buen buena buenas bueno buenos cada casi cerca cierta ciertas cierto ciertos cinco comentó como con conocer conseguimos conseguir considera consideró consigo consigue consiguen consigues contra cosas creo cual cuales cualquier cuando cuanto cuatro cuenta cómo da dado dan dar de debe deben debido decir dejó del demás dentro desde después dice dicen dicho dieron diferente diferentes dijeron dijo dio donde dos durante e ejemplo el ella ellas ello ellos embargo empleais emplean emplear empleas empleo en encima encuentra entonces entre era erais eramos eran eras eres es esa esas ese eso esos esta estaba estabais estaban estabas estad estada estadas estado estados estais estamos estan estando estar estaremos estará estarán estarás estaré estaréis estaría estaríais estaríamos estarían estarías estas este estemos esto estos estoy estuve estuviera estuvierais estuvieran estuvieras estuvieron estuviese estuvieseis estuviesen estuvieses estuvimos estuviste estuvisteis estuviéramos estuviésemos estuvo está estábamos estáis están estás esté estéis estén estés ex existe existen explicó expresó fin fue fuera fuerais fueran fueras fueron fuese fueseis fuesen fueses fui fuimos fuiste fuisteis fuéramos fuésemos gran grandes gueno ha haber habida habidas habido habidos habiendo habremos habrá habrán habrás habré habréis habría habríais habríamos habrían habrías habéis había habíais habíamos habían habías hace haceis hacemos hacen hacer hacerlo haces hacia haciendo hago han has hasta hay haya hayamos hayan hayas hayáis he hecho hemos hicieron hizo hoy hube hubiera hubierais hubieran hubieras hubieron hubiese hubieseis hubiesen hubieses hubimos hubiste hubisteis hubiéramos hubiésemos hubo igual incluso indicó informó intenta intentais intentamos intentan intentar intentas intento ir junto la lado largo las le les llegó lleva llevar lo los luego lugar manera manifestó mayor me mediante mejor mencionó menos mi mientras mio mis misma mismas mismo mismos modo momento mucha muchas mucho muchos muy más mí mía mías mío míos nada nadie ni ninguna ningunas ninguno ningunos ningún no nos nosotras nosotros nuestra nuestras nuestro nuestros nueva nuevas nuevo nuevos nunca o ocho os otra otras otro otros para parece parte partir pasada pasado pero pesar poca pocas poco pocos podeis podemos poder podria podriais podriamos podrian podrias podrá podrán podría podrían poner por porque posible primer primera primero primeros principalmente propia propias propio propios próximo próximos pudo pueda puede pueden puedo pues que quedó queremos quien quienes quiere quién qué realizado realizar realizó respecto sabe sabeis sabemos saben saber sabes se sea seamos sean seas segunda segundo según seis ser seremos será serán serás seré seréis sería seríais seríamos serían serías seáis señaló si sido siempre siendo siete sigue siguiente sin sino sobre sois sola solamente solas solo solos somos son soy su sus suya suyas suyo suyos sí sólo tal también tampoco tan tanto te tendremos tendrá tendrán tendrás tendré tendréis tendría tendríais tendríamos tendrían tendrías tened teneis tenemos tener tenga tengamos tengan tengas tengo tengáis tenida tenidas tenido tenidos teniendo tenéis tenía teníais teníamos tenían tenías tercera ti tiempo tiene tienen tienes toda todas todavía todo todos total trabaja trabajais trabajamos trabajan trabajar trabajas trabajo tras trata través tres tu tus tuve tuviera tuvierais tuvieran tuvieras tuvieron tuviese tuvieseis tuviesen tuvieses tuvimos tuviste tuvisteis tuviéramos tuviésemos tuvo tuya tuyas tuyo tuyos tú ultimo un una unas uno unos usa usais usamos usan usar usas uso usted va vais valor vamos van varias varios vaya veces ver verdad verdadera verdadero vez vosotras vosotros voy vuestra vuestras vuestro vuestros y ya yo él éramos ésta éstas éste éstos última últimas último últimos
""".strip().split()

def print_header():
    """Print welcome header"""
    print("🎼 Spanish Distant Reader - Generic Version")
    print("=" * 60)
    print("📖 Complete Distant Reader functionality with Spanish filtering")
    print("🚫 Eliminates 610 Spanish stopwords automatically")
    print("🎯 Optimized for Spanish text analysis")
    print("=" * 60)

def print_usage():
    """Print usage instructions"""
    print("Usage:")
    print("  python3 spanish-distant-reader.py <carrel-name> <source-directory>")
    print("")
    print("Examples:")
    print("  python3 spanish-distant-reader.py mi-corpus ./archivos-txt/")
    print("  python3 spanish-distant-reader.py cervantes /Users/maria/textos-cervantes/")
    print("  python3 spanish-distant-reader.py periodicos-1900 './periodicos/*.txt'")
    print("")
    print("Requirements:")
    print("  - Source directory with .txt files")
    print("  - Python libraries: matplotlib, wordcloud")
    print("")

def validate_inputs(carrel_name, source_dir):
    """Validate input parameters"""
    if not carrel_name.strip():
        print("❌ ERROR: Carrel name cannot be empty")
        return False

    if not os.path.exists(source_dir):
        print(f"❌ ERROR: Source directory not found: {source_dir}")
        print("💡 Make sure the path exists and contains .txt files")
        return False

    # Check for txt files
    txt_files = [f for f in os.listdir(source_dir) if f.endswith('.txt')]
    if not txt_files:
        print(f"❌ ERROR: No .txt files found in: {source_dir}")
        print("💡 Make sure your directory contains text files with .txt extension")
        return False

    print(f"✅ Found {len(txt_files)} .txt files in source directory")
    return True

def create_directory_structure(carrel_name):
    """Create complete carrel directory structure"""
    print("🏗️ Creating carrel directory structure...")
    directories = ['txt', 'figures', 'etc', 'cache', 'bib', 'pos', 'wrd', 'ent']

    for dir_name in directories:
        os.makedirs(f"{carrel_name}/{dir_name}", exist_ok=True)

    return True

def install_stopwords(carrel_name):
    """Install Spanish stopwords"""
    stopwords_path = f"{carrel_name}/etc/stopwords.txt"

    with open(stopwords_path, 'w', encoding='utf-8') as f:
        for word in SPANISH_STOPWORDS:
            f.write(word + '\n')

    print(f"✅ Installed {len(SPANISH_STOPWORDS)} Spanish stopwords")
    return set(word.lower() for word in SPANISH_STOPWORDS)

def copy_and_process_files(carrel_name, source_dir, stopwords):
    """Copy and process all text files with Spanish filtering"""
    print("📄 Processing source text files with Spanish filtering...")

    all_words = []
    all_text = ""
    file_stats = []

    # Copy files and process
    txt_files = [f for f in os.listdir(source_dir) if f.endswith('.txt')]

    for filename in txt_files:
        source_path = os.path.join(source_dir, filename)
        dest_path = f"{carrel_name}/txt/{filename}"

        try:
            # Copy file
            shutil.copy2(source_path, dest_path)

            # Process content
            with open(source_path, 'r', encoding='utf-8') as f:
                content = f.read()

                # Clean text (remove URLs, non-Spanish chars)
                clean_content = re.sub(r'http\S+|https\S+', '', content)
                clean_content = re.sub(r'[^a-záéíóúñüA-ZÁÉÍÓÚÑÜ\s]', ' ', clean_content)
                clean_content = ' '.join(clean_content.split()).lower()

                # Filter words (remove stopwords)
                words = clean_content.split()
                filtered_words = []
                for word in words:
                    if (len(word) >= 3 and
                        word not in stopwords and
                        word.isalpha()):
                        filtered_words.append(word)

                all_words.extend(filtered_words)
                all_text += " " + clean_content

                # Calculate basic readability (simplified Flesch formula for Spanish)
                sentences = content.count('.') + content.count('!') + content.count('?') + 1
                words_count = len(words)
                syllables = sum(count_syllables_spanish(word) for word in filtered_words)

                if sentences > 0 and words_count > 0:
                    avg_sentence_length = words_count / sentences
                    avg_syllables = syllables / words_count if words_count > 0 else 0
                    readability = 206.835 - (1.02 * avg_sentence_length) - (60 * avg_syllables)
                    readability = max(0, min(100, readability))  # Clamp between 0-100
                else:
                    readability = 50  # Default

                file_stats.append({
                    'filename': filename,
                    'words': len(filtered_words),
                    'chars': len(content),
                    'readability': int(readability)
                })

        except Exception as e:
            print(f"⚠️ Error processing {filename}: {e}")

    total_files = len(file_stats)
    total_words = sum(stat['words'] for stat in file_stats)

    print(f"✅ Processed {total_files} files")
    print(f"✅ Extracted {total_words:,} words (Spanish-filtered)")

    return all_words, all_text, file_stats

def count_syllables_spanish(word):
    """Simple Spanish syllable counter"""
    vowels = 'aeiouáéíóúü'
    word = word.lower()
    count = 0
    prev_was_vowel = False

    for char in word:
        is_vowel = char in vowels
        if is_vowel and not prev_was_vowel:
            count += 1
        prev_was_vowel = is_vowel

    return max(1, count)  # At least 1 syllable

def analyze_morphology_spanish(all_words):
    """Analyze Spanish parts-of-speech based on morphological patterns"""
    print("🔤 Analyzing Spanish morphology...")

    pos_data = {'nouns': [], 'verbs': [], 'adjectives': [], 'adverbs': []}

    # Common Spanish musical and cultural terms (treated as nouns)
    cultural_nouns = {
        'música', 'arte', 'obra', 'obras', 'teatro', 'concierto', 'sinfonía',
        'ópera', 'jazz', 'radio', 'orquesta', 'piano', 'guitarra', 'violín',
        'compositor', 'artista', 'cultura', 'literatura', 'poesía'
    }

    for word in all_words:
        if len(word) < 3:
            continue

        # Cultural/musical terms as nouns
        if word in cultural_nouns:
            pos_data['nouns'].append(word)
        # Spanish noun patterns
        elif word.endswith(('ción', 'sión', 'dad', 'tad', 'eza', 'ismo', 'ista', 'ura', 'aje', 'anza', 'encia', 'ancia')):
            pos_data['nouns'].append(word)
        # Spanish verb patterns
        elif word.endswith(('ar', 'er', 'ir', 'ando', 'iendo', 'ado', 'ido', 'aba', 'ían', 'aste', 'aron')):
            pos_data['verbs'].append(word)
        # Spanish adjective patterns
        elif word.endswith(('oso', 'osa', 'ivo', 'iva', 'ante', 'ente', 'able', 'ible', 'ico', 'ica')):
            pos_data['adjectives'].append(word)
        # Spanish adverb patterns
        elif word.endswith(('mente', 'ísimo', 'ísima')):
            pos_data['adverbs'].append(word)
        # Default: longer words likely nouns
        elif len(word) > 4:
            pos_data['nouns'].append(word)

    return pos_data

def extract_spanish_entities(all_words):
    """Extract named entities relevant to Spanish culture and literature"""
    print("🏷️ Extracting Spanish cultural entities...")

    entities = {
        'persons': [
            # Classical composers
            'bach', 'mozart', 'beethoven', 'chopin', 'haydn', 'brahms', 'schubert', 'schumann',
            # Spanish composers
            'falla', 'granados', 'albéniz', 'turina', 'rodrigo', 'halffter',
            # Writers
            'cervantes', 'lorca', 'machado', 'jiménez', 'alberti', 'neruda', 'borges',
            # Other cultural figures
            'dalí', 'picasso', 'miró', 'goya', 'velázquez'
        ],
        'places': [
            # Spanish cities
            'madrid', 'barcelona', 'valencia', 'sevilla', 'bilbao', 'zaragoza', 'málaga',
            # International
            'parís', 'viena', 'berlín', 'londres', 'nueva york', 'roma', 'milán',
            # Countries
            'españa', 'francia', 'alemania', 'italia', 'austria'
        ],
        'organizations': [
            'orquesta', 'conservatorio', 'teatro', 'sociedad', 'filarmónica', 'universidad',
            'academia', 'instituto', 'compañía', 'ensemble'
        ],
        'cultural_terms': [
            'sinfonía', 'concierto', 'ópera', 'zarzuela', 'jazz', 'flamenco', 'vals', 'marcha',
            'fantasía', 'sonata', 'preludio', 'nocturno', 'estudios', 'balada'
        ]
    }

    entity_counts = {}
    for category, terms in entities.items():
        entity_counts[category] = {}
        for term in terms:
            count = sum(1 for word in all_words if term in word.lower())
            if count > 0:
                entity_counts[category][term] = count

    return entity_counts

def create_all_visualizations(carrel_name, all_words, file_stats, pos_data, entity_counts):
    """Create all Distant Reader visualizations with Spanish filtering"""
    print("🎨 Creating all Distant Reader visualizations...")

    # Word frequency analysis
    word_counts = Counter(all_words)
    top_words = word_counts.most_common(100)

    if not top_words:
        print("❌ No words found for visualization")
        return False

    # Generate bigrams
    bigrams = []
    for i in range(len(all_words) - 1):
        bigram = f"{all_words[i]} {all_words[i+1]}"
        bigrams.append(bigram)
    bigram_counts = Counter(bigrams).most_common(30)

    # 1. Unigrams cloud
    if top_words:
        unigram_text = ' '.join([word for word, _ in top_words[:50]])
        create_wordcloud(unigram_text, f'{carrel_name}/figures/unigrams-cloud.png',
                        'Unigrams (Spanish Filtered)', 'viridis')

    # 2. Bigrams cloud
    if bigram_counts:
        bigram_text = ' '.join([bigram for bigram, _ in bigram_counts[:25]])
        create_wordcloud(bigram_text, f'{carrel_name}/figures/bigrams-cloud.png',
                        'Bigrams (Spanish Filtered)', 'plasma')

    # 3. Keywords cloud
    if top_words:
        keywords_text = ' '.join([word for word, _ in top_words[:75]])
        create_wordcloud(keywords_text, f'{carrel_name}/figures/keywords-cloud.png',
                        'Keywords (Spanish Filtered)', 'viridis')

    # 4. Parts-of-speech clouds
    for pos_type, words in pos_data.items():
        if words:
            pos_counts = Counter(words).most_common(30)
            if pos_counts:
                pos_text = ' '.join([word for word, _ in pos_counts])
                create_wordcloud(pos_text, f'{carrel_name}/figures/pos-{pos_type[:-1]}.png',
                               f'{pos_type.title()} (Spanish Filtered)', 'Set2')

    # 5. Entity clouds
    entity_filenames = {
        'persons': 'entities-person.png',
        'places': 'entities-gpe.png',
        'organizations': 'entities-org.png',
        'cultural_terms': 'entities-any.png'
    }

    for entity_type, entity_dict in entity_counts.items():
        if entity_dict:
            # Create weighted text
            weighted_text = []
            for entity, count in entity_dict.items():
                weighted_text.extend([entity] * min(count, 10))  # Cap for visualization

            if weighted_text:
                entity_text = ' '.join(weighted_text)
                filename = entity_filenames.get(entity_type, f'entities-{entity_type}.png')
                create_wordcloud(entity_text, f'{carrel_name}/figures/{filename}',
                               f'{entity_type.replace("_", " ").title()} (Spanish Filtered)', 'tab10')

    # 6. Size and readability distributions
    create_distribution_plots(carrel_name, file_stats)

    print("✅ All visualizations created!")
    return top_words, bigram_counts

def create_wordcloud(text, filename, title, colormap):
    """Helper function to create word clouds"""
    if not text.strip():
        return

    wordcloud = WordCloud(
        width=800, height=400,
        background_color='white',
        colormap=colormap,
        max_words=50,
        relative_scaling=0.5,
        min_font_size=10
    ).generate(text)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(title, fontsize=16, pad=20)
    plt.tight_layout()
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()

def create_distribution_plots(carrel_name, file_stats):
    """Create size and readability distribution plots"""
    word_counts_list = [stat['words'] for stat in file_stats]
    readability_scores = [stat['readability'] for stat in file_stats]

    # Size distributions
    plt.figure(figsize=(8, 5))
    plt.hist(word_counts_list, bins=max(10, len(word_counts_list)//3),
             alpha=0.7, color='skyblue', edgecolor='black')
    plt.xlabel('Words per File', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.title('File Size Distribution (Words)', fontsize=14)
    plt.tight_layout()
    plt.savefig(f'{carrel_name}/figures/sizes-histogram.png', dpi=300, bbox_inches='tight')
    plt.close()

    plt.figure(figsize=(6, 8))
    plt.boxplot(word_counts_list, patch_artist=True,
                boxprops=dict(facecolor='lightblue', alpha=0.7))
    plt.ylabel('Words per File', fontsize=12)
    plt.title('File Size Distribution (Box Plot)', fontsize=14)
    plt.tight_layout()
    plt.savefig(f'{carrel_name}/figures/sizes-boxplot.png', dpi=300, bbox_inches='tight')
    plt.close()

    # Readability distributions
    plt.figure(figsize=(8, 5))
    plt.hist(readability_scores, bins=15, alpha=0.7, color='lightgreen', edgecolor='black')
    plt.xlabel('Readability Score', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.title('Readability Distribution', fontsize=14)
    plt.tight_layout()
    plt.savefig(f'{carrel_name}/figures/readability-histogram.png', dpi=300, bbox_inches='tight')
    plt.close()

    plt.figure(figsize=(6, 8))
    plt.boxplot(readability_scores, patch_artist=True,
                boxprops=dict(facecolor='lightgreen', alpha=0.7))
    plt.ylabel('Readability Score', fontsize=12)
    plt.title('Readability Distribution (Box Plot)', fontsize=14)
    plt.tight_layout()
    plt.savefig(f'{carrel_name}/figures/readability-boxplot.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_database(carrel_name, all_words, file_stats, pos_data, entity_counts):
    """Create complete SQLite database with Spanish-filtered content"""
    print("🗄️ Creating SQLite database...")

    conn = sqlite3.connect(f'{carrel_name}/etc/carrel.db')
    cursor = conn.cursor()

    # Create tables
    cursor.execute('''CREATE TABLE IF NOT EXISTS wrd (
        id INTEGER PRIMARY KEY, word TEXT, frequency INTEGER)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS bib (
        id INTEGER PRIMARY KEY, filename TEXT, words INTEGER, chars INTEGER, readability INTEGER)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS pos (
        id INTEGER PRIMARY KEY, pos TEXT, word TEXT, frequency INTEGER)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS ent (
        id INTEGER PRIMARY KEY, entity TEXT, type TEXT, frequency INTEGER)''')

    # Insert word frequencies
    word_counts = Counter(all_words)
    for word, freq in word_counts.most_common(1000):
        cursor.execute('INSERT INTO wrd (word, frequency) VALUES (?, ?)', (word, freq))

    # Insert bibliography
    for i, stat in enumerate(file_stats, 1):
        cursor.execute('INSERT INTO bib (id, filename, words, chars, readability) VALUES (?, ?, ?, ?, ?)',
                      (i, stat['filename'], stat['words'], stat['chars'], stat['readability']))

    # Insert POS data
    pos_id = 1
    for pos_type, words in pos_data.items():
        pos_counts = Counter(words)
        for word, freq in pos_counts.most_common(100):
            cursor.execute('INSERT INTO pos (id, pos, word, frequency) VALUES (?, ?, ?, ?)',
                          (pos_id, pos_type[:-1], word, freq))
            pos_id += 1

    # Insert entities
    ent_id = 1
    for entity_type, entity_dict in entity_counts.items():
        for entity, freq in entity_dict.items():
            cursor.execute('INSERT INTO ent (id, entity, type, frequency) VALUES (?, ?, ?, ?)',
                          (ent_id, entity, entity_type, freq))
            ent_id += 1

    conn.commit()
    conn.close()
    print("✅ Database created with Spanish-filtered content!")

def create_html_and_bibliography(carrel_name, file_stats, top_words, bigram_counts, entity_counts):
    """Create HTML index and bibliography files"""
    print("🌐 Creating HTML index and bibliography files...")

    total_files = len(file_stats)
    total_words = sum(stat['words'] for stat in file_stats)
    avg_readability = sum(stat['readability'] for stat in file_stats) // total_files
    top_keywords_str = "; ".join([f"{word} ({count})" for word, count in top_words[:5]])

    # HTML index (Distant Reader style)
    html_content = f'''<html>
<head>
<title>Simple summary of the Distant Reader study carrel named {carrel_name}</title>
</head>
<body style='margin: 7%'>

	<h1>Simple summary of the Distant Reader study carrel named {carrel_name}</h1>

	<p>Given a corpus of narrative text, the Distant Reader creates data sets -- affectionately called "study carrels" -- for the purposes of use &amp; understanding. This carrel has been processed with <strong>Spanish stopwords filtering</strong> from the beginning, eliminating 610 Spanish function words to reveal meaningful content. For more information about Spanish Distant Reader, please see the documentation.</p>

	<h2>Basic characteristics</h2>

		<table>
		<tr><td>Creator</td><td>Spanish Distant Reader</td></tr>
		<tr><td>Date created</td><td>{datetime.now().strftime('%Y-%m-%d')}</td></tr>
		<tr><td>Number of items</td><td>{total_files}</td></tr>
		<tr><td>Number of words</td><td>{total_words:,}</td></tr>
		<tr><td>Average readability score</td><td>{avg_readability}</td></tr>
		<tr><td>Spanish stopwords filtered</td><td>610 eliminated</td></tr>
		<tr><td>Bibliographics</td><td><a href="./index.txt">plain text</a>; <a href="./index.xhtml">HTML</a>; <a href="./index.json">JSON</a></td></tr>
		<tr><td>Other files</td><td><a href="./etc/stopwords.txt">stopwords</a>; <a href="./etc/carrel.db">database</a></td></tr>
		</table>

		<h3>Sizes</h3>
			<p style='text-align: center'>
			<img src='./figures/sizes-boxplot.png' width='49%' /> <img src='./figures/sizes-histogram.png' width='49%' />
			</p>

		<h3>Readability</h3>
			<p style='text-align: center'>
			<img src='./figures/readability-boxplot.png' width='49%' /> <img src='./figures/readability-histogram.png' width='49%' />
			</p>

		<h3>N-grams (Spanish filtered)</h3>
			<table>
				<tr align='center'>
					<td><img src='./figures/unigrams-cloud.png' width='100%' /><br /><br />unigrams</td>
					<td><img src='./figures/bigrams-cloud.png'  width='100%' /><br /><br />bigrams</td>
				</tr>
			</table>

		<h3>Parts-of-speech (Spanish filtered)</h3>
			<table>
				<tr align='center'>
					<td><img src='./figures/pos-noun.png'  width='100%' /><br /><br />nouns<br /><br /><br /></td>
					<td><img src='./figures/pos-verb.png'  width='100%'  /><br /><br />verbs<br /><br /><br /></td>
				</tr>
				<tr align='center'>
					<td><img src='./figures/pos-adjective.png'  width='100%'  /><br /><br />adjectives<br /><br /></td>
					<td><img src='./figures/pos-adverb.png'  width='100%'  /><br /><br />adverbs<br /><br /></td>
				</tr>
			</table>

		<h3>Entities (Spanish filtered)</h3>
			<table>
				<tr align='center'>
					<td><img src='./figures/entities-any.png' width='100%' /><br /><br />any entity<br /><br /><br /></td>
					<td><img src='./figures/entities-person.png' width='100%' /><br /><br />persons<br /><br /><br /></td>
				</tr>
				<tr align='center'>
					<td><img src='./figures/entities-gpe.png' width='100%' /><br /><br />geo-political entities</td>
					<td><img src='./figures/entities-org.png' width='100%' /><br /><br />organizations</td>
				</tr>
			</table>

		<h3>Keywords (Spanish filtered)</h3>
			<p style='text-align: center'>
			<img src='./figures/keywords-cloud.png' width='66%' />
			</p>

		<h3>Top Keywords (Spanish filtered)</h3>
			<p>The most frequent content words after filtering Spanish stopwords:</p>
			<p><strong>{top_keywords_str}</strong></p>

	<h2>About Spanish Distant Reader</h2>

		<p>This analysis was created using <strong>Spanish Distant Reader</strong>, a specialized tool that applies Spanish stopwords filtering from the beginning of the analysis process. It eliminates 610 Spanish function words including articles (la, las, los, el), prepositions (de, con, por, para), conjunctions (que, y, pero), and common verbs, revealing only meaningful cultural, literary, and domain-specific content.</p>

		<p>Features include N-gram analysis, parts-of-speech categorization optimized for Spanish morphology, named entity recognition for Spanish cultural figures and places, and complete SQLite database creation with filtered content.</p>

</body>
</html>'''

    with open(f'{carrel_name}/index.htm', 'w', encoding='utf-8') as f:
        f.write(html_content)

    # JSON bibliography
    bibliography_data = {
        'carrel_name': carrel_name,
        'creation_date': datetime.now().isoformat(),
        'spanish_distant_reader_version': '1.0',
        'total_files': total_files,
        'total_words': total_words,
        'average_readability': avg_readability,
        'spanish_stopwords_filtered': len(SPANISH_STOPWORDS),
        'files': file_stats,
        'top_keywords': dict(top_words[:50]),
        'top_bigrams': dict(bigram_counts[:25]) if bigram_counts else {},
        'entities': entity_counts
    }

    with open(f'{carrel_name}/index.json', 'w', encoding='utf-8') as f:
        json.dump(bibliography_data, f, indent=2, ensure_ascii=False)

    # Text bibliography
    with open(f'{carrel_name}/index.txt', 'w', encoding='utf-8') as f:
        f.write(f"Spanish Distant Reader Bibliography\n")
        f.write("=" * 50 + "\n\n")
        f.write(f"Carrel: {carrel_name}\n")
        f.write(f"Created: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        f.write(f"Tool: Spanish Distant Reader v1.0\n\n")
        f.write(f"Corpus Statistics:\n")
        f.write(f"- Files processed: {total_files}\n")
        f.write(f"- Total words (Spanish-filtered): {total_words:,}\n")
        f.write(f"- Average readability: {avg_readability}\n")
        f.write(f"- Spanish stopwords eliminated: {len(SPANISH_STOPWORDS)}\n\n")

        f.write("Top Keywords (Spanish-filtered):\n")
        for i, (word, count) in enumerate(top_words[:20], 1):
            f.write(f"  {i:2}. {word}: {count:,}\n")

        f.write(f"\nFile Details:\n")
        for stat in file_stats:
            f.write(f"- {stat['filename']}: {stat['words']:,} words, readability {stat['readability']}\n")

    # XHTML bibliography
    with open(f'{carrel_name}/index.xhtml', 'w', encoding='utf-8') as f:
        f.write(f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="es" lang="es">
<head>
<title>Bibliography for {carrel_name}</title>
</head>
<body>
<h1>Bibliography for {carrel_name}</h1>
<h2>Spanish Distant Reader Analysis</h2>
<ul>
<li>Files: {total_files}</li>
<li>Words: {total_words:,}</li>
<li>Readability: {avg_readability}</li>
<li>Spanish stopwords filtered: {len(SPANISH_STOPWORDS)}</li>
</ul>
<h3>Created with Spanish Distant Reader</h3>
<p>Complete Distant Reader functionality with Spanish stopwords filtering applied from the beginning.</p>
</body>
</html>''')

    print("✅ All bibliography files created!")

def main():
    """Main function"""
    print_header()

    # Check command line arguments
    if len(sys.argv) != 3:
        print_usage()
        return False

    carrel_name = sys.argv[1]
    source_dir = sys.argv[2]

    print(f"📂 Carrel name: {carrel_name}")
    print(f"📁 Source directory: {source_dir}")

    # Validate inputs
    if not validate_inputs(carrel_name, source_dir):
        return False

    try:
        # Create directory structure
        create_directory_structure(carrel_name)

        # Install Spanish stopwords
        stopwords = install_stopwords(carrel_name)

        # Copy and process files
        all_words, all_text, file_stats = copy_and_process_files(carrel_name, source_dir, stopwords)

        if not all_words:
            print("❌ ERROR: No words extracted after Spanish filtering")
            return False

        # Print top keywords
        word_counts = Counter(all_words)
        top_words = word_counts.most_common(20)
        print(f"\n🎼 Top 20 Spanish-filtered keywords:")
        for i, (word, count) in enumerate(top_words[:20], 1):
            print(f"  {i:2}. {word} ({count:,})")

        # Analyze morphology
        pos_data = analyze_morphology_spanish(all_words)

        # Extract entities
        entity_counts = extract_spanish_entities(all_words)

        # Create visualizations
        top_words_full, bigram_counts = create_all_visualizations(carrel_name, all_words, file_stats, pos_data, entity_counts)

        # Create database
        create_database(carrel_name, all_words, file_stats, pos_data, entity_counts)

        # Create HTML and bibliography
        create_html_and_bibliography(carrel_name, file_stats, top_words_full, bigram_counts, entity_counts)

        # Success message
        total_files = len(file_stats)
        total_words = sum(stat['words'] for stat in file_stats)

        print("\n" + "=" * 60)
        print("🎉 SPANISH DISTANT READER ANALYSIS COMPLETE!")
        print("=" * 60)
        print(f"📂 Carrel directory: {carrel_name}/")
        print(f"🌐 HTML index: {carrel_name}/index.htm")
        print(f"🗄️ Database: {carrel_name}/etc/carrel.db")
        print(f"📊 Visualizations: {carrel_name}/figures/")
        print(f"📚 Bibliography: {carrel_name}/index.json, index.txt, index.xhtml")
        print("")
        print("✅ Features created:")
        print("  • N-grams (unigrams, bigrams) - Spanish filtered")
        print("  • Parts-of-speech analysis - Spanish morphology")
        print("  • Named entity recognition - Spanish cultural")
        print("  • File size & readability distributions")
        print("  • Complete SQLite database - Spanish filtered")
        print("  • HTML index (Distant Reader style)")
        print("")
        print(f"🎯 Corpus: {total_files} files, {total_words:,} words")
        print("🚫 610 Spanish stopwords eliminated completely")
        print("=" * 60)
        print(f"\n🚀 Open {carrel_name}/index.htm in your browser!")

        return True

    except Exception as e:
        print(f"❌ ERROR: {e}")
        return False

if __name__ == "__main__":
    success = main()
    if not success:
        sys.exit(1)