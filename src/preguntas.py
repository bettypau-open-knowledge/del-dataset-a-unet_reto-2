"""Banco de preguntas · Unidad 2: Ingeniería y auditoría del dataset.
Índices de respuesta correcta: 0=A, 1=B, 2=C.
"""

def pregunta_1():
    """Exploración de un dataset de segmentación: pregunta 1."""
    return {"titulo": 'Función de una máscara', "enunciado": 'En un dataset de segmentación supervisada, ¿cuál es la función principal de una máscara?', "opciones": ['Indicar la categoría general de la imagen sin información espacial.', 'Indicar la clase o región correspondiente a los píxeles de la imagen.', 'Almacenar las dimensiones y el formato de la imagen.'], "correcta": 1}

def pregunta_2():
    """Exploración de un dataset de segmentación: pregunta 2."""
    return {"titulo": 'Búsqueda de archivos con `pathlib`', "enunciado": "¿Cuál es la diferencia entre `glob('*.jpg')` y `rglob('*.jpg')` cuando se aplican sobre un directorio con `pathlib`?", "opciones": ['`glob` busca archivos JPG en el directorio indicado, mientras que `rglob` también busca en sus subdirectorios.', '`glob` busca imágenes y `rglob` busca únicamente máscaras.', 'Ambos buscan siempre en todos los subdirectorios, pero `rglob` ordena los resultados.'], "correcta": 0}

def pregunta_3():
    """Exploración de un dataset de segmentación: pregunta 3."""
    return {"titulo": 'Correspondencia entre imágenes y máscaras', "enunciado": 'Tenemos `gato_01.jpg`, `gato_02.jpg` y `gato_03.jpg` en `images/`, pero únicamente `gato_01.png` y `gato_03.png` en `masks/`. Si la correspondencia se establece mediante el nombre base, ¿cuántos pares completos existen?', "opciones": ['Tres pares, porque existen tres imágenes.', 'Dos pares, porque `gato_02` no tiene máscara correspondiente.', 'Un par, porque las extensiones de imágenes y máscaras son distintas.'], "correcta": 1}

def pregunta_4():
    """Inventario y configuración del dataset: pregunta 4."""
    return {"titulo": 'Propósito del manifest', "enunciado": '¿Cuál es el propósito principal de un *manifest* en un proyecto de segmentación?', "opciones": ['Guardar todos los píxeles de las imágenes en un único archivo.', 'Registrar de forma estructurada las muestras, sus rutas y sus atributos relevantes.', 'Modificar automáticamente las máscaras para que todas tengan el mismo tamaño.'], "correcta": 1}

def pregunta_5():
    """Inventario y configuración del dataset: pregunta 5."""
    return {"titulo": 'Interpretación de una fila del manifest', "enunciado": 'En un *manifest*, ¿qué información representa correctamente una fila con `image_id`, `image_path`, `mask_path`, `width` y `height`?', "opciones": ['Una muestra con su imagen, máscara y dimensiones registradas.', 'Una categoría con todas las imágenes que pertenecen a ella.', 'Un experimento de entrenamiento con sus hiperparámetros.'], "correcta": 0}

def pregunta_6():
    """Inventario y configuración del dataset: pregunta 6."""
    return {"titulo": 'Centralización de rutas', "enunciado": '¿Por qué es conveniente centralizar las rutas del dataset en un archivo de configuración?', "opciones": ['Porque elimina la necesidad de almacenar las imágenes físicamente.', 'Porque permite cambiar la ubicación del dataset sin modificar manualmente las rutas en varios notebooks o scripts.', 'Porque garantiza que todas las imágenes tendrán el mismo número de canales.'], "correcta": 1}

def pregunta_7():
    """Auditoría y análisis exploratorio: pregunta 7."""
    return {"titulo": 'Resolución espacial', "enunciado": 'Una imagen mide 800 × 600 píxeles. ¿Cuántos píxeles espaciales contiene?', "opciones": ['1,400 píxeles.', '480,000 píxeles.', '1,440,000 píxeles, porque una imagen RGB tiene tres canales.'], "correcta": 1}

def pregunta_8():
    """Auditoría y análisis exploratorio: pregunta 8."""
    return {"titulo": 'Interpretación del histograma de resoluciones', "enunciado": 'Un histograma de resoluciones muestra que la mayoría de las imágenes tienen entre 200,000 y 400,000 píxeles, pero algunas superan los 2 millones. ¿Qué conclusión está justificada?', "opciones": ['Todas las imágenes tienen dimensiones idénticas.', 'El dataset presenta variabilidad de resolución y contiene imágenes considerablemente mayores que la mayoría.', 'Las imágenes más grandes necesariamente tienen mejores máscaras.'], "correcta": 1}

def pregunta_9():
    """Auditoría y análisis exploratorio: pregunta 9."""
    return {"titulo": 'Ocupación del primer plano', "enunciado": 'Dos datasets tienen 100 imágenes cada uno. En el primero, el objeto ocupa aproximadamente el 5% de cada imagen; en el segundo, el 60%. ¿Qué diferencia importante revela este análisis?', "opciones": ['El primer dataset tiene menos imágenes que el segundo.', 'El segundo dataset necesariamente contiene más categorías.', 'Existe una diferencia en la proporción de píxeles de primer plano y fondo, aunque ambos tengan el mismo número de imágenes.'], "correcta": 2}

def pregunta_10():
    """Auditoría y análisis exploratorio: pregunta 10."""
    return {"titulo": 'Auditoría visual de las máscaras', "enunciado": 'Una máscara tiene dimensiones correctas y valores permitidos, pero delimita una región equivocada. ¿Qué procedimiento ayudaría a detectar este problema?', "opciones": ['Inspeccionar visualmente una muestra seleccionada mediante un procedimiento de muestreo adecuado.', 'Comprobar únicamente que el archivo tenga extensión PNG.', 'Contar el número total de imágenes del dataset.'], "correcta": 0}

PREGUNTAS = {
    1: pregunta_1,
    2: pregunta_2,
    3: pregunta_3,
    4: pregunta_4,
    5: pregunta_5,
    6: pregunta_6,
    7: pregunta_7,
    8: pregunta_8,
    9: pregunta_9,
    10: pregunta_10,
}
