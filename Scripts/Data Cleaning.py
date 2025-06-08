import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from unidecode import unidecode


# Leer el DataFrame
comments_df = pd.read_csv('../data/raw/comentarios.csv')

# Eliminamos signos de puntuación y caracteres especiales
comments_df['Comentarios'] = comments_df['Comentarios'].str.replace(r'[^\w\s]', '', regex=True)

# Convertimos a minúsculas todas las palabras
comments_df['Comentarios'] = comments_df['Comentarios'].str.lower()

# Eliminar acentos
comments_df['Comentarios'] = comments_df['Comentarios'].apply(unidecode)

# Eliminamos stopwords
nltk.download('stopwords')

# Seleccionamos las stopwords en español, debido a que es el idioma en que tenemos nuestros comentarios
stopwords_es = set(stopwords.words('spanish'))

# Creamos nuestra función para eliminar las stopwords
def eliminar_stopwords(comments):
    palabras = comments.split()
    palabras_limpias = [p for p in palabras if p.lower() not in stopwords_es]
    return ' '.join(palabras_limpias)

comments_df['Comentarios'] = comments_df['Comentarios'].apply(eliminar_stopwords)
comments_df.to_csv('../data/processed/clean_comments.csv', index=False)