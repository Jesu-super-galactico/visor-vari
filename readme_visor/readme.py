
print("\
\n\
Para que pueda emplear la libreria visor_vari \n\
usted deberá traer la clase 'Super_tabla' del \n\
modulo 'see' que se encuentra en \n\
la ruta: visor_vari.mas_bajo_nivel \n\
o en su defecto traerse el objeto 'refer_0' de ese \n\
modulo, que es un objeto ya formado alli. \n\
\n\
Con ese objeto usted podra guardar su variable \n\
en cualquier instancia. A usted, la libreria le \n\
proporciona (81) instancias, de refer_0, para guardar diferentes \n\
valores. \n\
Comprendida desde 'self.selda_0' \n\
hasta 'self.selda_80' \n\
Sirvase usar la que usted prefiera. \n\
\n\
Cuando quiera ver sus datos recogidos \n\
(en cierto punto de la ejecucion de su programa) \n\
deberá hacer la llamada a la funcion 'gentil' \n\
que se encuentra en el modulo 'viendo' \n\
del mismo paquete 'visor_vari'. \n\
Por supuesto, tambien deberá hacer \n\
esta importacion antes, en su propio modulo. \n\
\n\
visor vari tiene tres formas de trabajar \n\
de las cuales dos necesitan una predefinicion \n\
llamadas 'en_cadena' y 'faseypulso' \n\
esta ultima faseypulso requiere del empleo del metodo 'ultimate'\n\
despues de todos los gentiles.\n\
Pero, los detalles de estas formas de trabajo se describen en el readme_tipos\n\
\n\
La primera forma de trabajo (la simple) en \n\
la funcion 'gentil' puede no recibir agumentos. \n\
\n\
''' Ejemplo de ejecución en su forma mas simple ''' \n\
    (no recibe atributos de entrada) \n\
\n\
from visor_vari import gentil \n\
from visor_vari.mas_bajo_nivel.see import refer_0 \n\
\n\
a= 10 \n\
b= 15 \n\
\n\
refer_0.selda_0= a \n\
refer_0.selda_1= b \n\
\n\
gentil() \n\
\n\
refer_0.selda_0= 43   # Se modifica el valor internamente \n\
                    # quizas al presionarse un boton. \n\
\n\
c= 17               # Se hacen presente otros valores \n\
refer_0.selda_41= c   # y... tambien se quieren ver. \n\
\n\
gentil() \n\
\n\
Como podra darse cuenta 'visor_vari' aqui, detecta, \n\
los cambios que puedan darse en 'self.selda_0' \n\
que es, en el programa, la variable 'a'. \n\
(En la linea donde se le asigna el valor 43 a esa variable) \n\
estamos dando a entender \n\
que la variable podria modificarse (internamente). \n\
\n\
Por ejemplo: \n\
En el trayecto de ejecucion del programa \n\
se ejecuto una funcion que la modifico (reseteo la variable) \n\
al haber entrado a una seccion que hace tal cosa. \n\
O porque se encuentra usando tkinter y tk quedo \n\
esperando una entrada de valor, \n\
que usted posteriormente ingreso. \n\
Yo coloco la linea: 'refer.selda_0= 43' en este codigo de ejemplo, \n\
solo para indicar el cambio. \n\
Pero en realidad, es el programa como tal, el que se encuentra \n\
realizando cambios, \n\
los que usted... por supuesto, quiere ver con mayor detalle. \n\
\n\
Ademas... agregando posteriores un segundo... 'gentil()' \n\
como en el ejemplo de arriba, \n\
podrá ver esos cambios. \n\
\n\
En la forma simple de usar visor_vari, en la funcion 'gentil', \n\
se toman dos argumentos: 1.numero y 2.pausado\n\
estos dos argumentos son por defecto, cero (0) y True, respectivamente. \n\
Pausado se podria poner en False, para que no se detenga la ejecucion, \n\
pero eso sera en versiones posteriores de visor_vari. \n\
por otro lado, numero= 0, si se recomienda usarlo con cero, ya que no se\n\
considero otro valor para esta forma simple de visor_vari.\n\
\n\
La funcion gentil como usted sabra \n\
podra llamarla cuantas veces quiera.\n\
\n\
Para efectos practicos... donde necesite \n\
hacer revicion de alguna variable, \n\
en cierto punto de su programa, \n\
debera colocar 'gentil()'. \n\
Pero antes de eso, \n\
cree y llame a una funcion \n\
(colocandole el nombre que usted mismo quiera) \n\
Y en ella, haga las \n\
actualizaciones de los objetos/imagenes refer_x. \n\
Por ejemplo, las de: \n\
selda_0= 'a' \n\
selda_1= 'b' \n\
selda_41= 'c' \n\
... \n\
en este caso, \n\
\n\
Con esto garantizara \n\
que se le este mostrando, \n\
la configuracion de las variables, \n\
que usted realmente quiere ver, \n\
para este momento de la ejecucion. \n\
\n\
Pero trabajar asi (con viso_vari) le permite a usted, tambien, \n\
que esta misma funcion, la pueda usar en otros puntos... \n\
sin tener que indicar nuevamente, una por una, las variables \n\
que se quieran ver. \n\
Inclusive hasta podria, de ser posible, \n\
crear un modulo aparte donde se encuentren \n\
todas estas funciones. \n\
Evitando asi, apilar tanto codigo en su propio modulo. \n\
\n\
En el readme que se encuentra adjunto con este y que \n\
es llamado readme_tipos \n\
(import visor_vari.readme_visor.readme_tipos) \n\
podra conocer con mas profundidad \n\
las otras formas de usar visor_vari. \n\
")

