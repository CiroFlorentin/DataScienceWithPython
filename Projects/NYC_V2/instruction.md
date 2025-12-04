<!-- English -->

# New York City schoolbus

Every year, American high school students take SATs, which are standardized tests intended to measure literacy, numeracy, and writing skills. There are three sections - reading, math, and writing, each with a maximum score of 800 points. These tests are extremely important for students and colleges, as they play a pivotal role in the admissions process.

Analyzing the performance of schools is important for a variety of stakeholders, including policy and education professionals, researchers, government, and even parents considering which school their children should attend.

You have been provided with a dataset called schools.csv, which is previewed below.

You have been tasked with answering three key questions about New York City (NYC) public school SAT performance.

# Questions

Which NYC schools have the best math results?

    The best math results are at least 80% of the *maximum possible score of 800* for math.
    Save your results in a pandas DataFrame called best_math_schools, including "school_name" and "average_math" columns, sorted by "average_math" in descending order.

What are the top 10 performing schools based on the combined SAT scores?

    Save your results as a pandas DataFrame called top_10_schools containing the "school_name" and a new column named "total_SAT", with results ordered by "total_SAT" in descending order ("total_SAT" being the sum of math, reading, and writing scores).

Which single borough has the largest standard deviation in the combined SAT score?

    Save your results as a pandas DataFrame called largest_std_dev.
    The DataFrame should contain one row, with:
        "borough" - the name of the NYC borough with the largest standard deviation of "total_SAT".
        "num_schools" - the number of schools in the borough.
        "average_SAT" - the mean of "total_SAT".
        "std_SAT" - the standard deviation of "total_SAT".
    Round all numeric values to two decimal places.

<!-- Español -->

# New York City autobus escolar

Cada año, los estudiantes de secundaria estadounidenses presentan el SAT, un examen estandarizado que mide las habilidades de lectoescritura, aritmética y escritura. Consta de tres secciones: lectura, matemáticas y escritura, cada una con una puntuación máxima de 800 puntos. Estos exámenes son fundamentales para estudiantes y universidades, ya que desempeñan un papel fundamental en el proceso de admisión.

Analizar el rendimiento de las escuelas es crucial para diversas partes interesadas, como profesionales de la política y la educación, investigadores, el gobierno e incluso padres que deciden a qué escuela deberían asistir sus hijos.

Se le ha proporcionado un conjunto de datos llamado schools.csv, cuya vista previa se muestra a continuación.

Se le ha encomendado responder tres preguntas clave sobre el rendimiento de las escuelas públicas de la ciudad de Nueva York (NYC) en el SAT.

# Preguntas

¿Qué escuelas de Nueva York tienen los mejores resultados en matemáticas?

Los mejores resultados en matemáticas son, como mínimo, el 80 % de la puntuación máxima posible de 800 en matemáticas.
Guarde los resultados en un DataFrame de pandas llamado best_math_schools, que incluya las columnas «school_name» y «average_math», ordenadas por «average_math» en orden descendente.

¿Cuáles son las 10 escuelas con mejor rendimiento según las puntuaciones combinadas del SAT?

Guarde los resultados en un DataFrame de pandas llamado top_10_schools que contenga el «school_name» y una nueva columna llamada «total_SAT», con los resultados ordenados por «total_SAT» en orden descendente («total_SAT» es la suma de las puntuaciones de matemáticas, lectura y escritura).

¿Qué distrito tiene la mayor desviación estándar en la puntuación combinada del SAT?

Guarde los resultados en un DataFrame de pandas llamado largest_std_dev.
El DataFrame debe contener una fila con:
«borough»: el nombre del distrito de Nueva York con la mayor desviación estándar de «total_SAT».
«num_schools»: el número de escuelas del distrito.
«average_SAT»: la media de «total_SAT».
«std_SAT»: la desviación estándar de «total_SAT».
Redondee todos los valores numéricos a dos decimales.

Traducción realizada con la versión gratuita del traductor DeepL.com
