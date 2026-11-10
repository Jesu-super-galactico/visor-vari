
texto_esplicativo= """
ESTA LIBRERIA 'COMPARANDO' ESTA INCLUIDA DENTRO DEL PAQUETE 'VISOR_VARI'
Y PERMITE LA COMPARACION ENTRE CELDAS.

Como entrada, esta libreria toma 18 celdas (de refer_0) en dos partes. 
9 las aloja en "selda_a" y las otras 9 las aloja en "selda_b".
Luego la comparacion de esas 18 celdas las devuelve como lista o
las puede alojar en 9 celdas (las que usted escoja).
Estas 9 celdas de salida las puede indicar en el metodo de salida.

Con el metodo 'preconfg_primero' usted debe introducir las 18 celda.
Tanto para 'selda_a' como para 'selda_b' se debe señalar primero el 
bloque, el bloque son tres conjuntos de 9 selda (alineadas horizontalmente)
asi que como entendera solo pueden haber tres (bloques), ya que las refers
solo puede albergar 81 celdas.
El segundo argumento de entrada de 'preconfg_primero' es "selda", que 
indica a cual, de estos tres grupos de 9 celda apunta.
Si usted se fija en la ventana de visor-vari podra darse cuenta mas fasilmente
de estos detalles.

Sin embargo, este primer y segundo argumento de entrada de 'preconfg_primero'
solo se refieren a la 'selda_a' por lo tanto, el tercer y cuarto argumento 
de entrada de 'preconfg_primero' se refieren a 'selda_b'.
El metodo 'preconfg_primero' solo tiene 4 argumentos de entrada.

Para la salida, usted puede escoger entre varios metodos disponibles.
y determinar el estado de 'selda_b' en comparacion con 'selda_a'.
Usted puede entonces determinar si los valores de 'selda_b' son 
iguales, diferentes, superiores o inferiores a 'selda_a'.
Ademas tambien tiene la opcion, de que la salida devuelva simplemente un booleano 
indicando cuales de los valores de 'selda_b' son diferentes de 'selda_a'.

... LOS METODOS QUE PUEDE ENCONTRAR SON:
- 'porvalor' (Devuelve el valor en 'selda_b', si es diferente a 'selda_a'.)
- 'porboolean' (Devuelve 'True' si 'selda_b' y 'selda_a' son diferentes.
                De lo contrario debuelve 'False'.)
- 'valorsuperior' (Devuelve los valores de 'selda_b' cuando son 
                    superiores a 'selda_a'.)
- 'booleansuperior' (Devuelve 'True' si 'selda_b' es superior a
                    'selda_a'. De lo contrario debuelve 'False'.)
- 'valorinferior' (Devuelve los valores de 'selda_b' cuando son 
                    inferiores a 'selda_a'.)
- 'booleaninferior' (Devuelve 'True' si 'selda_b' es inferior a
                    'selda_a'. De lo contrario debuelve 'False'.)

Pero porsupuesto, recuerde llamar primero al metodo 'preconfg_primero', antes, para
que la libreria encuentre los datos a comparar.

Todos estos metodos de salida devuelven una lista de 9 elementos, que usted puede
alojar en 9 celdas de su preferencia, o simplemente puede recibirlos como return
del metodo de salida.
para esto, cada meetodo de salida recibe como primer argumento de entrada 
un booleano, que si es 'False' la salida se alojara en las 9 celdas 
indicadas en el mismo metodo de salida.
Y si es 'True' el metodo devolvera, como return, una lista con los resultados.

Cada metodo, de salida, tiene otros dos (2) argumentos de entrada, 
que son 'bloque' y 'selda' y funcionan de la misma manera, que el metodo 
'preconfg_primero'. Es decir, el 'bloque' indica a cual de los tres grupos 
de 27 celdas apunta y 'selda' indica a cual de las 9 celdas de ese grupo apunta.

Los posibles valores para 'bloque' son:  0, 1 y 2.
Y los posibles valores para 'selda' son: 0, 1 y 2.

La libreria contiene un metodo adicional, que permite establecer un signo para las
celdas que siguen siendo las mismas.
Este metodo se llama 'confg_piso' y recibe un argumento de entrada (el primero), 
que es el signo que usted desea establecer para las celdas que siguen siendo las mismas.
Este metodo se creo para que cuando usted espere manejar o recibir numeros enteros
que incluyen el cero (0), pueda establecer un signo diferente 
para que usted identifique donde no se han producido cambios en las celdas comparadas.

El segundo argumento de entrada de 'confg_piso' es un booleano, que si es 'True'
usted podra seguir llamando a los metodos de salida, 
sin necesidad de volver a llamar al metodo 'preconfg_primero'.
pero si es 'False', usted tendra que volver a llamar al metodo 'preconfg_primero'.
La libreria establece por defecto este segundo argumento de entrada en 'True', 
para que usted pueda hacer varias comparaciones.

    (english translation)

This library, 'COMPARANDO', is included in 
the 'VISOR_VARI' package and allows cell comparison.

As input, this library takes 18 cells (from refer_0) in two parts.
9 are stored in "selda_a" and the other 9 in "selda_b".
The comparison of these 18 cells is then returned as a list, or
it can be stored in 9 cells (of your choosing).
These 9 output cells can be specified in the output method.

The 18 cells must be entered using the 'preconfig_primero' method.
For both 'selda_a' and 'selda_b', you must first specify the block. 
The block consists of three sets of 9 cells (aligned horizontally). 
Therefore, as you can understand, there can only be three blocks, since 
the references can only hold 81 cells. 
The second input argument of 'preconfig_primero' is "selda", 
which indicates which of these three groups of 9 cells it points to. 
If you look at the visor-vari window, you can more easily see these details.

However, these first and second input arguments of 'preconfig_primero' 
only refer to 'selda_a'. Therefore, the third and fourth input arguments 
of 'preconfig_primero' refer to 'selda_b'. The 'preconfig_primero' method 
only has 4 input arguments.

For the output, you can choose from several available methods.
You can determine the state of 'selda_b' compared to 'selda_a'.
You can then determine if the values of 'selda_b' are equal to, 
different from, greater than, or less than 'selda_a'.
You also have the option of having the output simply return a 
Boolean value indicating which of the values of 'selda_b' are different 
from 'selda_a'.

...THE METHODS YOU CAN FIND ARE:
- 'byvalue' (Returns the value in 'selda_b', if it is different from 'selda_a'.)
- 'byboolean' (Returns 'True' if 'selda_b' and 'selda_a' are different. Otherwise, it returns 'False'.)
- 'highervalue' (Returns the values of 'selda_b' when they are greater than 'selda_a'.)
- 'booleanhigher' (Returns 'True' if 'selda_b' is greater than 'selda_a'. Otherwise, it returns 'False'.)
- 'lowervalue' (Returns the values of 'selda_b' when they are less than 'selda_a'.)
- 'booleanlower' (Returns 'True' if 'selda_b' is less than 'selda_a'. Otherwise, it returns 'False'.

But of course, remember to call the 'preconfig_primero' method first, 
so that the library can find the data to compare.

All these output methods return a list of 9 elements, which you can store 
in 9 cells of your choice, or you can simply receive them as the return 
value of the output method.
For this, each output method receives a boolean as its first input argument. 
If 'False', the output will be stored in the 9 cells specified in the output method.
And if 'True', the method will return a list with the results.

Each output method has two (2) input arguments, which are 'bloque' and 'selda', 
and they function in the same way as the 'preconfig_primero' method. 
That is, 'bloque' indicates which of the three groups of 27 cells 
it points to, and 'selda' indicates which of the 9 cells in that group it points to.

The possible values for 'bloque' are: 0, 1, and 2.
And the possible values for 'selda' are: 0, 1, and 2.

The library contains an additional method that allows you to set 
a sign for cells that remain unchanged.
This method is called 'confg_piso' and receives one input argument (the first), 
which is the sign you wish to set for the cells that remain unchanged.
This method was created so that when you expect to handle 
or receive integers that include zero (0), you can set a different sign 
to identify where no changes have occurred in the compared cells.

The second input argument of 'confg_piso' is a Boolean value. If it is 'True', 
you can continue calling the output methods without needing 
to call the 'preconfg_primero' method again.
But if it is 'False', you will have to call the 'preconfg_primero' method again. 
The library defaults to 'True' for this second input argument,
so that you can make multiple comparisons.
"""

print(texto_esplicativo)

