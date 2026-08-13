
""" modulo de entrada del paquete visor_vari """


"==============================="

en_prueba= False
if en_prueba == False:

    from visor_vari.mas_bajo_nivel.datos import coloco
    from visor_vari.procesando_tareas_de_gentil import proceden_de_sin_lista, proceden_de_con_lista
    from visor_vari.procesando_en_hilos import proceden_de_sin_lista_hilo, proceden_de_con_lista_hilo
    from visor_vari.mas_bajo_nivel.see import aborrar
    from visor_vari.tratando_las_visualizaciones import nueva_confg
    import time
else:

    from mas_bajo_nivel.datos import coloco
    from procesando_tareas_de_gentil import proceden_de_sin_lista, proceden_de_con_lista
    from procesando_en_hilos import proceden_de_sin_lista_hilo, proceden_de_con_lista_hilo
    from mas_bajo_nivel.see import aborrar
    from tratando_las_visualizaciones import nueva_confg
    import time

"==============================="

class Comienzo:
    
    def __init__(self):
        
        self.gentil_normal= False
        self.pulso_y_fase= False
        self.en_cadena= False
                
        self.se_ha_comprobado_1= False
        self.se_ha_comprobado_2= False
        self.se_ha_comprobado_3= False
    
class Cofiguracion_local:
    
    def __init__(self):
        
        self.tipo_de_ejecucion= 1
        self.numero_a_ejecutar= None # hace las veces de ciclo (que utiliza 'ultimate')
        
        self.aumento_para_modo_en_cadena= 0
        self.aumento_para_modo_faseypulso= 0
        self.aumento_para_modo_no_simple= 0
        
        self.execcion_de_aumento_en_falseypulso= False
        
class Informacion:
    
    def __init__(self):
        
        self.lista_de_entrada_en_cadena= None
        
        self.bajada_de_entrada_faseypulso= None
        self.lista_de_entrada_faseypulso= None
    
class Configuracion_de_con_hilo:
    
    def __init__(self):
        
        self.refer_comun= False
        self.falseypulso_en_bajada= False
        self.confirmo_falseypulso= False
    
comienzo= Comienzo()
configurate= Cofiguracion_local()
data= Informacion()
indicacion_a_modulo= Configuracion_de_con_hilo()

"==============================="

class Interpretacion_de_modos:
        
    def en_cadena(self, numero):
        aprovacion= None
        
        if numero == configurate.numero_a_ejecutar:
            if data.lista_de_entrada_en_cadena == []:
                "ejecuta todas las ventanas (sin lista)."
                aprovacion= 1
            else:
                if configurate.aumento_para_modo_en_cadena in data.lista_de_entrada_en_cadena:
                                                
                    "ejecuta las ventanas (que estan en la lista)."
                    aprovacion= 2
                    configurate.aumento_para_modo_en_cadena += 1
                else: # (no hace nada) pero aun asi aumenta el numero a ejecutar.
                    configurate.aumento_para_modo_en_cadena += 1

        return aprovacion
    
    def falseypulso(self, numero):
        aprovacion= None
        
        if data.bajada_de_entrada_faseypulso == False:
            ciclo_con_base_cero= coloco.ola_numero - 1
            
            def aumentando_para_evadir_primera():
                configurate.aumento_para_modo_faseypulso += 1
            
            if data.lista_de_entrada_faseypulso == []:
                if ciclo_con_base_cero == numero: # solo se manifiestan los numeros con sus respectivos ciclos.
                    
                    if configurate.aumento_para_modo_faseypulso == 0:
                        "ejecuto solamente la primera vez que se cumple la condicion"
                        
                        aprovacion= 3
                        configurate.execcion_de_aumento_en_falseypulso= True
                        coloco.numero_de_ventana= 1 # la primera, que sale, tambien debe ser 1.
                    
                    # apenas entra se sube, asi que se ejecuta solo la primera vez.
                    aumentando_para_evadir_primera()
            else:
                
                if ciclo_con_base_cero == numero: # solo se manifiestan los numeros con sus respectivos ciclos.
                    acto= False
                    
                    try:
                        actuacion= data.lista_de_entrada_faseypulso[numero]
                        acto= True
                    except IndexError:
                        pass
                    
                    if acto == True:
                        actua= actuacion[numero]
                        
                        if actua != []:
                            solo_esta= actua[0]
                            
                            if solo_esta == configurate.aumento_para_modo_faseypulso: # solo se manifiestan los numeros con sus respectivos ciclos.
                                
                                aprovacion= 4
                                configurate.execcion_de_aumento_en_falseypulso= True
                                coloco.numero_de_ventana= 1 # la primera, que sale, tambien debe ser 1.
                                
                                # ya no seria numerica para que no vuelva a entrar.
                                configurate.aumento_para_modo_faseypulso= None
                                
                            if configurate.aumento_para_modo_faseypulso != None:
                                aumentando_para_evadir_primera()
        else:
            ciclo_con_base_cero= coloco.ola_numero - 1
            
            if data.lista_de_entrada_faseypulso != []:
                #print("entrado a faseypulso con lista")
                
                # en cada ciclo, saco los diccionarios con sus respectivas listas.
                for e, i in enumerate(data.lista_de_entrada_faseypulso):
                    # 'i' es el diccionario (para algun momento).
                                    
                    if isinstance(i, dict):
                        
                        # para los numeros en lista.
                        if ciclo_con_base_cero == e: # comparo con el ciclo actual (para filtrar, ya que el 'for' se ejecuta en cada ciclo)
                            numeros_contenidos_para_faseypulso= i[e] # lista (para el mismo momento).
                            
                            # para entrada actual.
                            if numero == ciclo_con_base_cero: # solo se manifiestan los numeros con sus respectivos ciclos.
                                
                                if configurate.aumento_para_modo_faseypulso in numeros_contenidos_para_faseypulso:
                                    #print("faseypulso con lista, ejecutandose")
                                    "ejecuto las ventanas que estan en la lista (numeros contenidos)"
                                    aprovacion= 4
                                else: # (no hace nada) pero aun asi aumenta el numero a ejecutar.
                                    #print("faseypulso con lista, no ejecutandose"); print(".")
                                    pass
                                    
                                configurate.aumento_para_modo_faseypulso += 1
            
            else:
                if ciclo_con_base_cero == numero: # solo se manifiestan los numeros con sus respectivos ciclos.
                    
                    "ejecuto todas las ventanas"
                    aprovacion= 3
        
        return aprovacion

vamos_sin_hilo= Interpretacion_de_modos()
vamos_con_hilo= Interpretacion_de_modos()

"==============================="

def compruebo_inicio():
    resultado= False
    
    if (comienzo.gentil_normal == False) and (comienzo.en_cadena == False) and (comienzo.pulso_y_fase == False):
        resultado= True
        
    return resultado        

"==============================="

def iniciar_visor_vari(con_lista, de_cual):
    # En esta seccion se decide que tipo de ejecucion se va a llevar a cabo
    # (entrando a la libreria y deteniendose en cada ventana).
        
    if con_lista == False:
        
        if de_cual == 1:
            proceden_de_sin_lista(True)
        elif de_cual == 2:
            proceden_de_sin_lista()
        elif de_cual == 3:
            proceden_de_sin_lista()
    
    if con_lista == True:
        
        if de_cual == 2:
            proceden_de_con_lista()
            
        elif de_cual == 3:
            proceden_de_con_lista()
            
    if configurate.execcion_de_aumento_en_falseypulso == False:
        coloco.numero_de_ventana += 1
    else:
        coloco.numero_de_ventana= 1
    
def iniciar_visor_vari_en_hilo(con_lista=False, de_cual=1):
    # En esta seccion se decide que tipo de ejecucion se va a llevar a cabo
        
    if con_lista == False:
        
        if de_cual == 1:    # simple
            indicacion_a_modulo.refer_comun= True
            proceden_de_sin_lista_hilo(indicacion_a_modulo)
        elif de_cual == 2:  # encadena
            proceden_de_sin_lista_hilo(indicacion_a_modulo)
        elif de_cual == 3:  # falseypulso
            indicacion_a_modulo.confirmo_falseypulso= True
            indicacion_a_modulo.falseypulso_en_bajada= data.bajada_de_entrada_faseypulso
            proceden_de_sin_lista_hilo(indicacion_a_modulo)
    
    if con_lista == True:
        
        if de_cual == 2:    # encadena
            proceden_de_con_lista_hilo(indicacion_a_modulo)
            
        elif de_cual == 3:  # falseypulso
            indicacion_a_modulo.confirmo_falseypulso= True
            indicacion_a_modulo.falseypulso_en_bajada= data.bajada_de_entrada_faseypulso
            proceden_de_con_lista_hilo(indicacion_a_modulo)
            
    time.sleep(0.1) # para que se ejecute el hilo antes de que se aumente el numero de ventana.
    
    if configurate.execcion_de_aumento_en_falseypulso == False:
        coloco.numero_de_ventana += 1
    else:
        coloco.numero_de_ventana= 1
    
"==============================="
    
def gentil(numero= None, pausado= True):
    canal= compruebo_inicio()
        
    if (canal == True) or (comienzo.se_ha_comprobado_1 == True) or (comienzo.se_ha_comprobado_2 == True) or (comienzo.se_ha_comprobado_3 == True):
        
        if configurate.numero_a_ejecutar == None: # si no se ha entrado ni en en_cadena ni en faseypulso... configura.
            
            comienzo.gentil_normal= True
            coloco.pausado= pausado # solo se modifica con gentil, si no se ha entrado ni en en_cadena ni en faseypulso.
            comienzo.se_ha_comprobado_1= True
                    
        if (coloco.pausado == True) or (coloco.posible_tk != None):
            
            if (numero == None) and (configurate.numero_a_ejecutar == None):   # modo simple
                "ejecuto gentil simplemente" # para cuando gentil este vacio.
                iniciar_visor_vari(False, 1)
                
            elif configurate.tipo_de_ejecucion == 2:                        # modo encadena
                
                comienzo.se_ha_comprobado_2= True
                ejecuto= vamos_sin_hilo.en_cadena(numero)
                
                if ejecuto == 1:    # sin lista
                    iniciar_visor_vari(False, 2)
                
                elif ejecuto == 2:  # con lista
                    iniciar_visor_vari(True, 2)
                
            elif configurate.tipo_de_ejecucion == 3:                        # modo falseypulso
                
                comienzo.se_ha_comprobado_3= True
                ejecuto= vamos_sin_hilo.falseypulso(numero)
                
                if ejecuto == 3:    # sin lista
                    iniciar_visor_vari(False, 3)
                    
                elif ejecuto == 4:  # con lista
                    iniciar_visor_vari(True, 3)
                    
        else:
            if (coloco.posible_tk == None) and (coloco.pausado == False):
                # Ninguna de las siguientes trabaja con ventana del usuario.
                # No se detiene por pause pero pueden tener listas.
                
                #""" Coloque # para descomentar el bloque.
                
                if configurate.numero_a_ejecutar == None:
                    iniciar_visor_vari_en_hilo(False, 1)
                
                elif configurate.tipo_de_ejecucion == 2:
                    "ejecuto en_cadena en hilo"
                    
                    comienzo.se_ha_comprobado_2= True
                    ejecuto= vamos_con_hilo.en_cadena(numero)
                    
                    if ejecuto == 1:    # sin lista
                        iniciar_visor_vari_en_hilo(False, 2)
                    
                    elif ejecuto == 2:  # con lista
                        iniciar_visor_vari_en_hilo(True, 2)
                #"""
                
                
                #""" Coloque # para descomentar el bloque.
                    
                elif configurate.tipo_de_ejecucion == 3:
                    "ejecuto faseypulso en hilo"
                    
                    comienzo.se_ha_comprobado_3= True
                    ejecuto= vamos_con_hilo.falseypulso(numero)
                    
                    if ejecuto == 3:    # sin lista
                        iniciar_visor_vari_en_hilo(False, 3)
                        #print("ejec_ falsey_ sinlista")
                    
                    elif ejecuto == 4:  # con lista
                        iniciar_visor_vari_en_hilo(True, 3)
                        #print("ejec_ falsey_ conlista")
                #"""
    
"==============================="

def preparo_configuracion(segun):
    
    "si segun es 2, me preparo para 'en_cadena' "
    "si segun es 3, me preparo para 'faseypulso' "
    #print("preparo configuracion segun: ")
    configurate.tipo_de_ejecucion= segun
    #print("configurate.tipo_de_ejecucion: ", configurate.tipo_de_ejecucion)
    
def encadena(numero= 0, lista= [], pausado= True):
    canal= compruebo_inicio()
    
    if (canal == True) or (comienzo.se_ha_comprobado_2 == True):
        comienzo.en_cadena= True
        coloco.pausado= pausado
        comienzo.se_ha_comprobado_2= True
        
        data.lista_de_entrada_en_cadena= lista
        
        configurate.numero_a_ejecutar= numero
        
        preparo_configuracion(2)
    
def faseypulso(bajada= False, lista= [], pausado= True):
    canal= compruebo_inicio()
    
    if (canal == True) or (comienzo.se_ha_comprobado_3 == True):
        comienzo.pulso_y_fase= True
        coloco.pausado= pausado
        comienzo.se_ha_comprobado_3= True
        configurate.numero_a_ejecutar= True
        
        data.bajada_de_entrada_faseypulso= bajada
        data.lista_de_entrada_faseypulso= lista
        
        if data.bajada_de_entrada_faseypulso == False:
            coloco.pausado= True
        
        preparo_configuracion(3)
    
def ultimate():
    if configurate.tipo_de_ejecucion == 3:
        
        input("Presiona Enter para continuar... (se encuentra en visor-vari)")
        coloco.ola_numero += 1
        coloco.numero_de_ventana= 1
        configurate.aumento_para_modo_faseypulso= 0
        coloco.destruye_hilos= True
            
"==============================="

def borratodo(numero= None, limit= None, lista= None):
    aborrar(numero, limit, lista, )
    
def guia(tkin= None, reajusteola= False, lista= None):
    
    new_lista= [0]
    
    if tkin != None:
        coloco.posible_tk= tkin
    
    if lista == None:
        if isinstance(reajusteola, list):
            
            new_lista= reajusteola
            coloco.ola_reajustada= False
            
            nueva_confg(new_lista)
            
        if isinstance(reajusteola, bool):
            
            coloco.ola_reajustada= reajusteola
            nueva_confg(new_lista)
    
    eslist= False
    if isinstance(lista, list):
        eslist= True

    if (lista != None) and (eslist == True):
        a_saber= False
        if isinstance(reajusteola, list):
            a_saber= True
        #.
        adicio= False
        if isinstance(reajusteola, bool):
            adicio= True
        #.
        if (a_saber == False) and (adicio == True):
            coloco.ola_reajustada= reajusteola

        cantidad= len(lista)
        if cantidad == 0: # si es una 'list' y llega a estar vacia... reacomoda el contenido.
            new_lista= [0]
        else:
            new_lista= lista

        nueva_confg(new_lista)
    
