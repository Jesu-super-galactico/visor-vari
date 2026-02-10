
texto_esplicativo= """
COMO SE DESCRIBE EN EL README (COMUN) DE ESTA LIBRERIA,
EXISTEN TAN SOLO OTRAS DOS FORMAS ADICIONALES DE EJECUTAR VISOR_VARI,
QUE SON LAS SIGUIENTES:

1. Predefiniendo anteriormente a los 'gentil'
una funcion llamada 'en_cadena', la cual recibe tres argumentos:
  1. un numero
  2. una lista de indices
  3. pausado
  
En este modo (en_cadena) pausado se define dentro de 'en_cadena'
como tercer argumento y por defecto es True. En los gentiles no
se requiere definirlos.

Por otro lado, el primer argumento que se le pasa a 'en_cadena'
es un numero con el cual son comparados los gentiles...
y los que, coincidan son ejecutados, los que no, no lo seran.

La lista de indices, hace referencia a cuales de esos 
"numeros que coinciden" son los que se ejecutaran.
si la lista no se le pasa como argumento, se ejecutaran todos.
El primer 'gentil' que coincide tiene el indice 0, el segundo el indice 1
y asi sucesivamente.

Para esta forma de ejecutar la libreria
se requiere que 'gentil' exprese su numero.
Los cuales serviran para compararlos con el numero que se dio, a 'en_cadena'.
ejemplo: gentil(1)

Un ejemplo mas completo seria el siguiente:

en_cadena(1, [0, 1], pausado=True)
gentil(1) # Este 'gentil' se ejecutaria, porque su numero coincide con el numero dado a 'en_cadena'.
gentil(2) # Este 'gentil' no se ejecutaria, porque su numero no coincide con el numero dado a 'en_cadena'.
gentil(1) # Este 'gentil' se ejecutaria, porque su numero tambien coincide con el numero dado a 'en_cadena'.
gentil(1) # Este 'gentil' no se ejecutaria, porque en la lista no aparece su indice (2).


2. La otra forma de ejecutar la libreria visor_vari es
predefiniendo anteriormente a los 'gentil'
una funcion llamada 'faseypulso', la cual recibe tres argumentos:
  1. bajada (la cual a mi me gusta llamarla profundidad)
  2. una lista, que es una lista de diccionarios que tienen (en su interior)
    otra lista... list[ {0: [x]}, {1: [y]}, {2: [z]}...]
  3. pausado
  
En este modo (faseypulso) pausado se define dentro de 'faseypulso'
como tercer argumento y por defecto es True. En los gentiles no
se requiere definirlos.

El primer argumento que se llama 'bajada' indica:
si solo ejecutara los primeros 'gentil' que coincidan 
o si buscara ejecutar todos (los que coincidan).
por defecto este argumento es 'False', por los que, por defecto,
solo se ejecutan los primeros 'gentil' que coincidan.

Aqui quiero detenerme un momento y explicar, cual es la diferncia con el modo 'en_cadena'.
Esta diferencia es que en el modo 'en_cadena' se considera, solo un pulso,
algo asi como se ejecuta un modulo de arriba a abajo y ya.
sin embargo, en el modo 'faseypulso' se consideran varios pulsos, 
como si se estuviera dentro de un ciclo o bucle.
podria ser de while o de for.

He aqui otro detalle y es que en este modo (faseypulso) los 'gentil' no se
comparan con un numero dado (como ocurre en 'en_cadena') sino con la "ola", 
en la que se encuentran en ese momento los 'gentil' 
o todo el script.

Para que la libreria identifique cada pulso y le asigne un numero
se ha establecido que al final del ciclo se cierre con la funcion 'ultimate'.
Esto garantiza que la libreria sepa 
que la siguiente vez... que se entre a la libreria, 
ya se esta en el numero_de_pulso aumentado (aumentado en 1).

A cada pulso se le considera ola y comienza a contar
desde el pulso cero (0) 
aunque tengase en cuenta, que, en el titulo de la
ventana (donde se muestran los valores de las variables)
se empieza con ola=1, por lo que deberia usted mentalmente descontarle un 1,
a ese numero que se muestra en la ventana, para saber realmente con
cual pulso se esta trabajando.
esta ocurre asi, 
ya que en 'gentil' se esta considerando desde cero... gentil(0)
por lo que se ha dejado la diferencia de una (1) unidad, para la ola.

Ademas recuerde que en este modo (faseypulso) se esta comparando con algo...
y ese algo es la ola.
Asi que los 'gentil' deben expresar un numero, que indica el numero de ola, 
a la cual responden.

Si a 'bajada' se le da el valor True, sin 'lista' ni 'pausado', entonces; 
se ejecutaran todos los 'gentil' que coincidan (segun la ola)
sin importar su posicion en el script.

La lista pretende actuar similar, que como ocurre, 
en el modo 'en_cadena'.
Pero puesto que aqui se esta tratando de pulsos u olas, entiendase como se quiera.
la lista de este modo (faseypulso) es una lista que contiene diccionarios, 
cada diccionario tiene una clave/llave que es un numero (0, 1, 2...) y ese numero
hace referencia a una ola. la 0 hace referencia a la ola 0, la 1 hace referencia a la ola 1 
y asi sucesivamente. {0: []}, {1: []}, {2: []}
A su vez, cada uno de estos numeros/indices, tiene una lista interna, 
que hace referencia a los 'gentil' que se quieren ejecutar para cada ola.

Por ejemplo, si se quieren ejecutar los 'gentil' que responden a la ola 0:
{0: [del_gentil_0_en_primera_posicion, del_gentil_0_en_tercera_posicion]}
o lo que es lo mismo: {0: [0, 2]} 

gentil(0) # este 'gentil' se ejecutaria, porque su indice aparece.
gentil(0) # este 'gentil' no se ejecutaria, porque su indice no aparece..
gentil(0) # este 'gentil' se ejecutaria, porque su indice aparece.

tenga mucho cuidado a la hora de emplear este modo (faseypulso)
ya que dentro del modulo o script, pueden aparecer intercalados 'gentil' con
diferentes numeros (que responden a diferentes olas).
por lo que si no tiene cuidado se podria confundir.
Ademas siempre recuerde que cuando es _el_primer_pulso... gentil(0) 
en la ventana se muestra como ola 1.

Ejemplo para falseypulso:
faseypulso(False, listando_los_gentiles_que_quiero_ver, pausado=True)
# ya en bucle.
gentil(0) # ... y otros mas.
ultimate() # para que se incremente el numero de ola o pulso.

En esta version de visor_vari (2.0) no se han hecho 
las funcionalidades para 'pausado' por lo que no tiene porque modificarlo
si se encuentra en esta version.

Ademas, tenga en cuenta que si la libreria identifica un modo...
ya no se cambiara a otro metodo.
esta, en el modo en_cadena cuando a lo primero que entra es a en_cadena(),
esta, en el modo faseypulso, cuando a lo primero que entra es a faseypulso().
y si lo primero que encuentra es un gentil()... tambien ese es un modo.

Las diferentes ventanas que van apareciendo, se les ha dispuesto, para que 
se vallan cambiando de color. esta es una medida para que usted desarrollador se 
encuentre mas agusto e identifique mas facilmente, cada ventana.
"""

print(texto_esplicativo)

