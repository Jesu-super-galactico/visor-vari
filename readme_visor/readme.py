
texto_esplicativo= """
Esta librería "visor_vari" le permite observar un grupo de variables
de su código (las variables que usted quiera ver)

Tenga en cuenta, que la librería le proporciona (81) variables 
para que usted pueda guardar diferentes valores. 
Existen, además, varios objetos para que usted pueda realizar esto. 
Pero por defecto, la librería, pone a su disposición solo uno 
llamado 'refer_0'.
Este objeto lo puede encontrar en la ruta 'visor_vari.ayudandome.con_.py' 
La clase que forma estos objetos la puede 
encontrar en el módulo llamado 'see' que se encuentra
en la ruta 'visor_vari._mas_bajo_nivel'.

Las posibles variables guardadas están comprendidas desde 'self.selda_0'
hasta 'self.selda_80'. Sírvase usar la que usted prefiera.

Cuando quiera ver sus datos recogidos
(en cierto punto de la ejecución de su programa)
deberá hacer la llamada a la función 'gentil'
que se encuentra también en la ruta 'visor_vari.ayudandome.con_.py'
Por supuesto que deberá hacer, la importación de 'gentil' antes,
en su propio modulo.

visor_vari tiene tres formas de trabajar
de las cuales dos necesitan una predefinición
llamadas 'en_cadena' y 'faseypulso'
esta última, faseypulso requiere del empleo del método 'ultimate'
después de todos los gentiles.
Pero, los detalles de estas formas de trabajo se describen en el readme_tipos

En la primera forma de trabajar de la librería (la simple)
la función 'gentil', 
puede no recibir argumentos.

''' Ejemplo de ejecución en su forma más simple
    ('gentil' no recibe argumentos de entrada) '''

from visor_vari.ayudandome.con_ import gentil
from visor_vari.ayudandome.con_ import refer_0

a= 10
b= 15

refer_0.selda_0= a
refer_0.selda_1= b

gentil()

refer_0.selda_0= 43     # Se modifica el valor internamente
                        # quizás al presionarse un botón.

c= 17                   # Se hacen presentes otros valores
refer_0.selda_41= c     # y... también se quieren ver.

gentil()

Como podrá darse cuenta 'visor_vari' aqui, detecta,
los cambios que puedan darse en 'self.selda_0'
que es, en el programa, la variable 'a'.
(En la línea donde se le asigna el valor 43 a esa variable)
estamos dando a entender
que la variable podría modificarse (internamente).

Por ejemplo:
En el trayecto de ejecución del programa
se ejecutó una función que la modifico (reseteo la variable)
al haber entrado a una sección que hace tal cosa.
O porque se encuentra usando tkinter y tk quedo
esperando una entrada de valor,
que usted posteriormente ingreso.
Yo coloco la línea: 'refer.selda_0= 43' en este código de ejemplo,
solo para indicar el cambio.
Pero en realidad, es el programa como tal, el que se encuentra
realizando cambios,
los que usted... por supuesto, quiere ver con mayor detalle.

Además, agregando posteriores 'gentil()', un segundo... tercero... etc.
como en el ejemplo de arriba,
podrá ver esos cambios.

En la forma simple de usar visor_vari, en la función 'gentil',
se toman dos argumentos: 1. número y 2. pausado
estos dos argumentos son por defecto, None y True, respectivamente.
En esta versión, usted podrá usar pausado= False
por otro lado, numero= None, y se recomienda dejarlo así,
ya que para este modo 'simple' técnicamente no sería necesario usarlo.

La función 'gentil' como usted sabrá
podrá llamarla cuantas veces quiera,
donde necesite hacer revisión de alguna variable en su código.
Solo necesita colocar 'gentil()'.

Pero para efectos prácticos... 
puede optar por crear y llamar a una función
(colocándole el nombre que usted mismo quiera)
Y en ella, haga las actualizaciones de los objetos/imágenes refer_x.
Por ejemplo, las de:
selda_0= 'a'
selda_1= 'b'
selda_41= 'c'
...
como en el caso del ejemplo.

Después, puede utilizar estos dos comandos
(llamar a la función y posteriormente utilizar 'gentil').
    
Con esto garantizara
que se le esté mostrando,
la configuración de las variables,
que usted realmente quiere ver,
para este momento de la ejecución.

Pero trabajar así (con viso_vari) le permite a usted, también,
que esta misma función, la pueda usar en varios puntos,
sin tener que indicar nuevamente, una por una, las variables
que se quieran ver.
Dejando su código mucho más organizado.

Inclusive, hasta podría usted de ser posible,
crear esta función, en un módulo aparte.
Evitando así, apilar tanto código en su propio modulo.

También podría en este otro modulo, crear diferentes 
funciones, según las variables que desee ver 
para ese momento.

Lea el readme que se encuentra adjunto con este
(y que es llamado 'readme_tipos')
con el, podrá conocer con más profundidad,
las otras formas de usar visor_vari.
Su ruta exacta es:

from visor_vari.readme_visor import readme_tipos

    (english translation)

This "visor_vari" library allows you to view a group of variables
in your code (the variables you want to see).

Note that the library provides 81 variables
for you to store different values.
There are also several objects available to do this.
But by default, the library only provides one
called 'refer_0'.
This object can be found in the path 'visor_vari.ayudandome.con_.py'.
The class that creates these objects can be found
in the module called 'see', located
in the path 'visor_vari._mas_bajo_nivel'.

The possible stored variables range from 'self.selda_0'
to 'self.selda_80'. Please use whichever one you prefer.

When you want to view your collected data (at a certain point 
in your program's execution), you will need to call the 'gentil' function, 
which is also located in the 'visor_vari.ayudandome.con_.py' directory. 
Of course, you will need to import 'gentil' beforehand,
into its own module.

visor_vari has three ways of working, two of which require a predefinition: 
'en_cadena' and 'faseypulso'. The latter, 'faseypulso', 
requires the use of the 'ultimate' method after all the 'gentil' functions.
However, the details of these working methods are described in the readme_types file.

In the library's first (simple) working method, 
the 'gentil' function may not receive any arguments.

''' Example execution in its simplest form
'gentil' does not receive any input arguments' '''

from visor_vari.ayudandome.con_ import gentil
from visor_vari.ayudandome.con_ import refer_0

a= 10
b= 15

refer_0.selda_0= a
refer_0.selda_1= b

gentil()

refer_0.selda_0= 43     # The value is modified internally
                        # perhaps by pressing a button.

c= 17                   # Other values become present
refer_0.selda_41= c     # And... they also want to see each other.

gentil()

As you can see, 'visor_vari' here detects
changes that may occur in 'self.selda_0', which is the variable 'a' in the program.
(In the line where the value 43 is assigned to that variable)
we are implying
that the variable could be modified (internally).

For example:
During the program's execution,
a function was executed that modified it (reset the variable)
after entering a section that does so.
Or because it is using tkinter and tk is
waiting for an input value,
which you subsequently entered.
I include the line: 'refer.selda_0 = 43' in this example code,
only to indicate the change.
But in reality, it is the program itself that is
making changes,
which you... of course, want to see in more detail.

Furthermore, by adding subsequent 'gentil()' calls—a second, a third, and so on—
as in the example above,
you will be able to see these changes.

In the simple way of using visor_vari, the 'gentil' function takes two arguments: 1. number and 2. paused.
These two arguments are, by default, None and True, respectively.
In this version, you can use paused = False.
On the other hand, number = None, and it is recommended to leave it as is,
since for this 'simple' mode, it wouldn't technically be necessary to use it.

The 'gentil' function, as you know,
can be called as many times as you want
wherever you need to check a variable in your code.

You just need to include 'gentil()'.
But for practical purposes...
you can choose to create and call a function
(giving it any name you like)
and in that function, perform the updates for the refer_x objects/images.
For example, the values in:
selda_0 = 'a'
selda_1 = 'b'
selda_41 = 'c'
... as in the example.

Then, you can use these two commands:
(call the function and then use 'gentle').

This will ensure that you are shown
the configuration of the variables
that you actually want to see
at this point in execution.

But working this way (with viso_vari) also allows you to
use this same function at various points
without having to specify, one by one, the variables
that you want to see.
Leaving your code much more organized.

You could even, if possible,
create this function in a separate module.
Thus avoiding piling so much code in your own module.

You could also, in this other module, create different
functions, depending on the variables you want to see
at that moment.

Read the attached readme file (named 'readme_tipos')
It will give you a more in-depth look at
other ways to use visor_vari
Its exact path is:

from visor_vari.readme_visor import readme_tipos
"""

print(texto_esplicativo)

