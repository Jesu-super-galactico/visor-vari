
texto_esplicativo= """
CONTENIDO:

Punto 1.  - explicacion para 'encadena'.
punto 2.  - explicacion para 'faseypulso'.
add 1     - explicacion de la funcion 'guia'.
add 2     - explicacion de la funcion 'borratodo'.


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
comparan con un numero dado (como ocurre con 'encadena') sino con la "ola", 
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
esto ocurre asi, para mantener coherancia con las versiones anteriores.
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
Pero puesto que aqui se esta tratando de pulsos u olas.
la lista de este modo (faseypulso) es una lista que contiene diccionarios, 
cada diccionario tiene una 'llave' que es un numero (0, 1, 2...) y ese numero
hace referencia a una ola. la 0 hace referencia a la ola 0, la 1 hace referencia a la ola 1 
y asi sucesivamente. {0: []}, {1: []}, {2: []}
A su vez, a cada uno de estos "numeros" le corresponde una lista, 
que hace referencia a los 'gentil' que se quieren ejecutar,
en esa ola.

Por ejemplo, si se quieren ejecutar los 'gentil' que responden a la ola 0:
{0: [del_gentil_0_en_primera_posicion, del_gentil_0_en_tercera_posicion]}
o lo que es lo mismo: {0: [0, 2]} 

gentil(0) # este 'gentil' se ejecutaria, porque su indice aparece.
gentil(0) # este 'gentil' no se ejecutaria, porque su indice no aparece..
gentil(0) # este 'gentil' se ejecutaria, porque su indice aparece.

tenga mucho cuidado a la hora de emplear este modo (faseypulso)
ya que dentro del modulo o 'su script', pueden aparecer intercalados 'gentil' con
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

Ademas, tenga en cuenta que si la libreria identifica un modo...
ya no se cambiara a otro modo.
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
guia(tkin= tk, reajusteola= True, lista= lista_de_refers)

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
(excepto cuando falseypulso esta: bajada= True, pausado= False
en tal caso, tambien estaria abriendo subventanas).



Explicasion de la funcion borratodo:

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

    (english translation)

CONTENTS:

Point 1. - Explanation for 'encadena'.
Point 2. - Explanation for 'faseypulso'.
Add 1 - Explanation of the 'guia' function.
Add 2 - Explanation of the 'borratodo' function.

... 
AS DESCRIBED IN THE (COMMON) README OF THIS LIBRARY,
THERE ARE ONLY TWO OTHER ADDITIONAL WAYS TO EXECUTE VISOR_VARI,
WHICH ARE THE FOLLOWING:


1. By predefining a function called 'encadena' within the 'gentil', 
which takes three arguments:

1. A number
2. A list of indices
3. Paused

In this mode, 'pausado' is defined within 'encadena' as the third argument 
and is set to True by default. It is not necessary to define it within the 'gentil'.

On the other hand, the first argument passed to 'encadena'
is a number against which the 'gentil' are compared...
and those that match are executed; those that don't are not.

The index list refers to which of those
"matching numbers" will be executed.
If the list is not passed as an argument, all of them will be executed.
The first 'gentil' that matches has index 0, the second index 1,
and so on.

For this way of running the library,
'gentil' must specify its number.
These numbers will be used to compare them with the number given to 'encadena'.
Example:

gentil(1) # How 'gentil' should look

... A more complete example would be the following:

encadena(1, [0, 1], pausado=True)

gentil(1) # This 'gentil' would be executed because its number matches the number given to 'encadena'.
gentil(2) # This 'gentil' would not be executed because its number does not match the number given to 'encadena'.
gentil(1) # This 'gentil' would be executed because its number also matches the number given to 'encadena'.
gentil(1) # This 'gentil' would not be executed because its index (2) does not appear in the list.


2. The other way to run the visor_vari library is by
predefining the 'gentil' functions with a function called 'faseypulso', 
which takes three arguments:
  1. descent (which I prefer to call depth)
  2. a list, which is a list of dictionaries that contain (within them)
  another list... list[ {0: [x]}, {1: [y]}, {2: [z]}...]
  3. paused

In this mode (faseypulso), paused is defined within 'faseypulso' 
as the third argument and is set to True by default. 
It is not necessary to define it within the gentil functions.

The first argument, called 'bajada', indicates whether to execute 
only the first 'gentil' functions that match or whether to execute all of them.

By default, this argument is 'False', so, by default,
only the first 'gentil' that matches are executed.

Here I want to pause for a moment and explain the difference with 'chain' mode.
The difference is that in 'chain' mode, only one pulse is considered,
something like executing a module from top to bottom and that's it.
However, in 'phaseandpulse' mode, several pulses are considered,
as if inside a loop.
It could be a while or a for loop.

Here's another detail: in this mode (phase and pulse), 
the 'gentil' pulses are not compared to a given number (as with 'chain') 
but to the "wave" in which the 'gentil' pulses, or the entire script, 
are currently located.

To ensure the library identifies each pulse and assigns it a number, 
it has been established that the loop will close with the 'ultimate' function.
This guarantees that the library knows that the next time it is accessed, 
it will already be at the incremented pulse number (increased by 1).

Each pulse is considered a wave, and counting begins from pulse zero (0) 
if reset with the 'guide' function.
The explanation of this function (guide) 
appears at the end of this documentation; scroll to the bottom.
If it's not reset, the 'guide' function will start counting from one (1). 
This happens to maintain consistency with previous versions.
Also... I want to explain a little about the reasons 
for creating the reset for the 'wave':
1. Because 'gentle' elements can start from zero (0),
there should also be a space for them, right?
2. Another reason is that Python aims to count everything starting from zero (0),
this library also aims to do that,
maintaining the same philosophy.

Continuing... I recommend you always remember that:
"this mode (phase and pulse) is being compared to something...
and that something is the wave."
So, 'gentil' elements must express a number that indicates the wave number
to which they respond.

If 'bajada' is set to True, without 'list' or 'paused', then:
all matching 'gentil' instances (according to the wave) will be executed, 
regardless of their position in the script.

The list is intended to function similarly to how it works in 'chain' mode.
However, since we are dealing with pulses or waves here,
the list in this mode (phaseandpulse) is a list containing dictionaries.
Each dictionary has a 'key' which is a number (0, 1, 2...) and that number
refers to a wave. 0 refers to wave 0, 1 refers to wave 1,
and so on. {0: []}, {1: []}, {2: []}
In turn, each of these "numbers" corresponds to a list
that refers to the 'gentil' elements to be executed
in that wave.

For example, if you want to execute the 'gentil' elements corresponding to wave 0:
{0: [del_gentil_0_en_primera_posicion, del_gentil_0_en_tercera_posicion]}
or equivalently: {0: [0, 2]}

gentil(0) # this 'gentil' element would be executed because its index appears.
gentil(0) # this 'gentil' element would not be executed because its index does not appear.
gentil(0) # this 'gentil' element would be executed because its index appears.

Be very careful when using this mode (phaseandpulse)
since within the module or 'your script', 
'gentil' elements with different numbers (corresponding to different waves) 
may appear interspersed.
Therefore, if you are not careful, you could get confused.
Also, always remember that when it is _the_first_pulse... gentil(0),
in the window, it is shown as wave 1 
if you have not made the readjustment with the 'guia' function.

Example for false and pulse:
phaseandpulse(False, listing_the_gentles_I_want_to_see, paused=True)
# already in a loop.
gentil(0) # ... and others.
ultimate() # to increment the wave or pulse number.

Also, keep in mind that if the library identifies a mode...
it will not switch to another mode.
It is... in chain mode, when the first thing it enters is chain(),
it is... in phaseandpulse mode, when the first thing it enters is phaseandpulse().
And if the first thing it finds is a gentil()... that is also a mode.

The different windows that appear have been arranged so that
they change color (at least the first 20).
This is a measure so that you, the developer, feel more comfortable and 
can more easily identify each window.


Explanation of the 'guia' function:

`guia` is a function that takes three arguments.
The first is the Tk that you, the user, are using in your application.
Example:

# In your module.
import tkinter as tk
guia(tkin= tk)
user_window= tk.Tk()
# ...
user_window.mainloop()

The second argument passed is a reset so that, in the window title, 
where the values saved in the library (refer_x) are displayed, 
the number of waves starts counting from 0.
(True = from 0, False = from 1).
By default, this argument is False, so it would start counting from 1 by default.
Example:

guia(tkin= tk, reajusteola= False)

The third and final argument
is a list, the list that indicates which refer_x will be executed 
(remember to enter the values for these refer_x).
The list is a simple list `[0, 1, 2, 3 ...]` and should appear according 
to the refer_x you want to see. Zero (0) for refer_0,
one (1) for refer_1, two (2) for refer_2, etc.
They don't necessarily have to appear in order.
Example:

refer_list = [0, 1, 2]
guia(tkin= tk, reajusteola= True, lista= lista_de_refers)

I should also point out that:
you could enter only tk, `guia(tk)`
or readjustment... only: `guia(reajusteola = False)`
or the list... only: `guia(lista = refer_list)`.
You can also enter the first and last references directly: `guia(tk, refer_list)`
without naming them.

Keep in mind that the 'guide' function
aims to open the refer values (the windows that display the values)
in a subwindow when tk is passed to it.
However, when tk is not passed to the library,
it attempts to open the refer values in a main window.
(except when falseypulso is: down= True, paused= False
in that case, it would also be opening subwindows).


Explanation of the deleteAll function:

`borratodo` also has three input arguments:

- The first is `number`, which specifies the set of cells to delete 
(the first 9 or the others).
If you enter the number ten (10), all cells will be deleted.
- The second argument is `limit`, which is an indication placed 
if you want to delete cells from zero (0) up to the 'number' (the first argument).
For this second argument, you must enter the string 'super' 
or simply the letter 's' if you want to activate this method of deleting cells.
- Finally, the third argument is `list`, which indicates 
the references that you want to delete (they will be deleted 
as indicated by the first two arguments).
Example:

refer_list = [0, 2, 3]
borratodo(3, 's', refer_list)
# The first 27 (3x9) cells have been deleted in: refer_0, refer_2, and refer_3.

By default, the library points to `refer_0`, so you can write the following:

borratodo(3)
# In this case, only cells 18 through 27 of `refer_0` will be deleted
"""

print(texto_esplicativo)

