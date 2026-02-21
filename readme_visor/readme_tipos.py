
texto_esplicativo= """
CONTENIDO:

Punto 1.  - explicacion para 'encadena'.
punto 2.  - explicacion para 'faseypulso'.
add 1     - explicacion de nueva funcion 'guia'.
add 2     - explicacion de nueva funcion 'borratodo'.


...
COMO SE DESCRIBE EN EL README (COMUN) DE ESTA LIBRERIA,
EXISTEN TAN SOLO OTRAS DOS FORMAS ADICIONALES DE EJECUTAR VISOR_VARI,
QUE SON LAS SIGUIENTES:


1. Predefiniendo anteriormente a los 'gentil'
una funcion llamada 'encadena', la cual recibe tres argumentos:
  1. un numero
  2. una lista de indices
  3. pausado
  
En este modo (encadena) pausado se define dentro de 'encadena'
como tercer argumento y por defecto es True. En los gentiles no
se requiere definirlos.

Por otro lado, el primer argumento que se le pasa a 'encadena'
es un numero con el cual son comparados los gentiles...
y los que, coincidan son ejecutados, los que no, no lo seran.

La lista de indices, hace referencia a cuales de esos 
"numeros que coinciden" son los que se ejecutaran.
si la lista no se le pasa como argumento, se ejecutaran todos.
El primer 'gentil' que coincide tiene el indice 0, el segundo el indice 1
y asi sucesivamente.

Para esta forma de ejecutar la libreria
se requiere que 'gentil' exprese su numero.
Los cuales serviran para compararlos con el numero que se dio, a 'encadena'.
ejemplo: 

gentil(1) # de como deberia verse 'gentil'

... Un ejemplo mas completo seria el siguiente:

encadena(1, [0, 1], pausado=True)

gentil(1) # Este 'gentil' se ejecutaria, porque su numero coincide con el numero dado a 'encadena'.
gentil(2) # Este 'gentil' no se ejecutaria, porque su numero no coincide con el numero dado a 'encadena'.
gentil(1) # Este 'gentil' se ejecutaria, porque su numero tambien coincide con el numero dado a 'encadena'.
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

Aqui quiero detenerme un momento y explicar, cual es la diferncia con el modo 'encadena'.
Esta diferencia es que en el modo 'encadena' se considera, solo un pulso,
algo asi como se ejecuta un modulo de arriba a abajo y ya.
sin embargo, en el modo 'faseypulso' se consideran varios pulsos, 
como si se estuviera dentro de un ciclo o bucle.
podria ser de while o de for.

He aqui otro detalle y es que en este modo (faseypulso) los 'gentil' no se
comparan con un numero dado (como ocurre en 'encadena') sino con la "ola", 
en la que se encuentran en ese momento los 'gentil' 
o todo el script.

Para que la libreria identifique cada pulso y le asigne un numero
se ha establecido que al final del ciclo se cierre con la funcion 'ultimate'.
Esto garantiza que la libreria sepa 
que la siguiente vez... que se entre a la libreria, 
ya se esta en el numero_de_pulso aumentado (aumentado en 1).

A cada pulso se le considera ola y comienzan a contarse
desde el pulso cero (0) si se reajusta con la funcion 'guia'.
la explicasion de esta funcion (guia) aparece al final de esta documentacion,
"valla a la parte de abajo".
Si no se reajusta, con la funcion 'guia', empezara a contar desde uno (1) 
esto ocurre asi, para mantener coherancia con la version anterior.
Tambien... quiero explicar... uno poco, las razones por lo que se creo el reajuste 
para la 'ola':
1. y es que, los 'gentil' pueden llegar a empezar desde cero (0), asi
que, deberia tambien haber un espacio para ellos ¿verdad?.
2. Otra razon, es que python busca contar todo empezando desde cero (0), 
esta libreria busca hacer eso tambien, 
manteniendo entonces, la misma filosofia.

Continuando... le recomiendo que recuerde siempre que:
"este modo (faseypulso), se esta comparando con algo...
y ese algo es la ola".
Asi que los 'gentil' deben expresar un numero, que indica el numero de ola, 
a la cual RESPONDEN.

Si a 'bajada' se le da el valor True, sin 'lista' ni 'pausado', entonces; 
se ejecutaran todos los 'gentil' que coincidan (segun la ola)
sin importar su posicion en el script.

La lista pretende actuar similar, que como ocurre, 
en el modo 'encadena'.
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
Ademas siempre, recuerde que cuando es _el_primer_pulso... gentil(0), 
en la ventana, se muestra como ola 1 si es que no ha hecho el reajuste con la
funcion 'guia'.

Ejemplo para falseypulso:
faseypulso(False, listando_los_gentiles_que_quiero_ver, pausado=True)
# ya en bucle.
gentil(0) # ... y otros mas.
ultimate() # para que se incremente el numero de ola o pulso.

En esta version, de visor_vari (2.5) 
se han hecho las funcionalidades de 'pausado', para cuando usted usa tkinter. 
Sin embargo, cuando no es asi, no podra emplearlo para esta version.

Ademas, tenga en cuenta que si la libreria identifica un modo...
ya no se cambiara a otro metodo.
Esta... en el modo encadena, cuando, a lo primero que entra es a encadena(),
esta... en el modo faseypulso, cuando a lo primero que entra es a faseypulso().
y si lo primero que encuentra es un gentil()... tambien ese es un modo.

Las diferentes ventanas que van apareciendo, se les ha dispuesto, para que 
se vallan cambiando de color (al menos las primeras 20).
Esta es una medida para que usted desarrollador se 
encuentre mas agusto e identifique mas facilmente, cada ventana.



Explicación de la funcion 'guia':

`guia` es una funcion que le ingresan tres argumentos. 
El primero es el Tk con que usted, usuario, 
se encuentre utilizando en su aplicacion.
ejemplo:

# En su modulo.
import tkinter as tk
guia(tkin= tk)
ventana_del_usuario= tk.Tk()
# ...
ventana_del_usuario.mainloop()

El segundo argumento que se pasa, 
es un reajuste para que, en el titulo de la ventana, donde se visualizan 
los valores guardados... en la libreria... (refer_x)) 
el numero de olas empiece a contar desde 0 
(si es True= desde 0, si es False= desde 1). 
Por defecto este argumento es False, 
Por lo que, por defecto empezaria a contar desde 1.
ejemplo:

guia(tkin= tk, reajusteola= False)

El tercer y ultimo argumento 
se trata de una lista, la lista que indica cuales refer_x se 
estaran ejecutando (recuerde ingresar los valores para estos refers). 
la lista es una lista simple `[0, 1, 2, 3 ...]` y deben 
aparecer segun los refers que quiera ver. cero (0) para refer_0, 
uno (1) para refer_1, dos (2) para refer_2, etc. 
No necesariamente tendrian que aparecer en orden.
ejemplo:

lista_de_refers= [0, 1, 2]
guia(tkin= tk, reajusteola= False, lista= lista_de_refers)

Ademas debo indicarle que: 
podria ingresar exclusivamente tk, `guia(tk)` 
o reajuste... unicamente: `guia(reajusteola= False)` 
o la lista... exclusivamente: `guia(lista= lista_de_refers)`.
Tambien, puede ingresar el primero y el ultimo: `guia(tk, lista_de_refers)` 
directamente, sin nombrarlos.

Tenga en cuenta que la funcion 'guia' 
busca que los refers (las ventanas que muestran los valores) se abran 
en una subventana cuando se le pasa tk. 
sin embargo, cuando a la libreria no se le pasa tk 
procura abrir los valores, de refer, en una ventana principal.



Explicasion de la funcion borratodo (que es otra funcion que se ha agregado):

`borratodo` tambien tiene tres argumentos de entrada:
 
- El primero es `numero` que señala el conjunto de seldas a borrar 
(las 9 primeras o las otras).
Si usted ingresa el numero diez (10) se borraran todas las seldas. 
- El segundo argumento es `limit` que es una indicacion que se coloca, 
si lo que se quiere es, que se borren desde la cero (0) hasta el 'numero' 
(el primer argumento).
Para este segundo argumento, hay que ingresar el string 'super' o 
simplemente la letra 's', si se quiere activar, 
esta forma de borrado de las seldas.
- Por ultimo, el tercer argumento es `lista`, que indica los refers 
que usted quiere... que se borren 
(seborraran como se lo indican los dos primeros argumentos).
Ejemplo:

lista_de_refers= [0, 2, 3]
borratodo(3, 's', lista_de_refers)
# Se han borrado en: refer_0, refer_2 y refer_3 las primeras 27 (3x9) seldas.

Por defecto, en la libreria, se señala a `refer_0` por lo que usted 
puede escribir lo siguiente:

borratodo(3)
# En este caso, se borrara unicamente, desde la selda 18 hasta la 27 de refer_0
"""

print(texto_esplicativo)

