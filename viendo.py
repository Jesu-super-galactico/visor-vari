
""" modulo de entrada del paquete visor_vari """


"==============================="

#visor_vari.
from visor_vari.mas_bajo_nivel.datos import coloco
from visor_vari.procesando_tareas_de_gentil import proceden_de_sin_lista, proceden_de_con_lista
from visor_vari.mas_bajo_nivel.see import aborrar
from visor_vari.tratando_las_visualizaciones import nueva_confg

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
        
        self.pausado= True
        self.tipo_de_ejecucion= 1
        self.numero_a_ejecutar= 0 # hace las veces de ciclo (que utiliza 'ultimate')
        
        self.aumento_para_modo_en_cadena= 0
        self.aumento_para_modo_faseypulso= 0
        self.aumento_para_modo_no_simple= 0
    
class Informacion:
    
    def __init__(self):
        
        self.lista_de_entrada_en_cadena= None
        
        self.bajada_de_entrada_faseypulso= None
        self.lista_de_entrada_faseypulso= None
    
comienzo= Comienzo()
configurate= Cofiguracion_local()
data= Informacion()

"==============================="

def compruebo_inicio():
    resultado= False
    
    if (comienzo.gentil_normal == False) and (comienzo.pulso_y_fase == False) and (comienzo.en_cadena == False):
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
            
    coloco.numero_de_ventana += 1
    
def iniciar_visor_vari_en_hilo():
    # En esta seccion se decide que tipo de ejecucion se va a llevar a cabo
    # (pero, la apertura de ventana se produce en un hilo aparte).
    pass
    
"==============================="
    
def gentil(numero= None, pausado= True):
    canal= compruebo_inicio()
        
    if (canal == True) or (comienzo.se_ha_comprobado_1 == True) or (comienzo.se_ha_comprobado_2 == True) or (comienzo.se_ha_comprobado_3 == True):
        
        if configurate.numero_a_ejecutar == 0: # si no se ha entrado ni en en_cadena ni en faseypulso
            
            comienzo.gentil_normal= True
            configurate.pausado= pausado # solo se modifica con gentil, si no se ha entrado ni en en_cadena ni en faseypulso.
            comienzo.se_ha_comprobado_1= True
                    
        if configurate.pausado == True:
            
            if (numero == None) and (configurate.numero_a_ejecutar == 0):
                "ejecuto gentil simplemente" # para cuando gentil este vacio.
                iniciar_visor_vari(False, 1)

            elif configurate.tipo_de_ejecucion == 2:
                
                comienzo.se_ha_comprobado_2= True
                
                if numero == configurate.numero_a_ejecutar:
                    if data.lista_de_entrada_en_cadena == []:
                        "ejecuta todas las ventanas"
                        iniciar_visor_vari(False, 2)
                    else:
                        if configurate.aumento_para_modo_en_cadena in data.lista_de_entrada_en_cadena:
                                                        
                            "ejecuta las ventanas que estan en la lista"
                            iniciar_visor_vari(True, 2)
                            configurate.aumento_para_modo_en_cadena += 1
                        else: # (no hace nada) pero aun asi aumenta el numero a ejecutar.
                            configurate.aumento_para_modo_en_cadena += 1
                
            elif configurate.tipo_de_ejecucion == 3:
                
                comienzo.se_ha_comprobado_3= True
                if data.bajada_de_entrada_faseypulso == False:
                    ciclo_con_base_cero= coloco.ola_numero - 1
                    
                    if ciclo_con_base_cero == numero: # solo se manifiestan los numeros con sus respectivos ciclos.
                        if ciclo_con_base_cero == configurate.aumento_para_modo_faseypulso: # con esto, se asegura que se ejecute solo la primera que se entra a un ciclo.
                            
                            "ejecuto solamente la primera vez que se cumple la condicion"
                            #print(ciclo_con_base_cero, numero)
                            iniciar_visor_vari(False, 3)
                            
                            # apenas entra se sube, asi que se ejecuta solo la primera vez.
                            configurate.aumento_para_modo_faseypulso += 1
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
                                            iniciar_visor_vari(True, 3)
                                        else: # (no hace nada) pero aun asi aumenta el numero a ejecutar.
                                            #print("faseypulso con lista, no ejecutandose"); print(".")
                                            pass
                                            
                                        configurate.aumento_para_modo_faseypulso += 1
                    
                    else:
                        if ciclo_con_base_cero == numero: # solo se manifiestan los numeros con sus respectivos ciclos.
                            
                            "ejecuto todas las ventanas"
                            iniciar_visor_vari(False, 3)
                        
        else:
            print("en pausado")
            # de aqui va para 'iniciar_visor_vari_en_hilo'.
            pass
        
    
"==============================="

def preparo_configuracion(segun):
    
    "si segun es 2, me preparo para 'en_cadena' "
    "si segun es 3, me preparo para 'faseypulso' "
    #print("preparo configuracion segun: ")
    configurate.tipo_de_ejecucion= segun
    #print("configurate.tipo_de_ejecucion: ", configurate.tipo_de_ejecucion)
    
def en_cadena(numero= 0, lista= [], pausado= True):
    canal= compruebo_inicio()
    
    if (canal == True) or (comienzo.se_ha_comprobado_3 == True):
        comienzo.en_cadena= True
        configurate.pausado= pausado
        comienzo.se_ha_comprobado_3= True
        
        data.lista_de_entrada_en_cadena= lista
        
        configurate.numero_a_ejecutar= numero
        
        preparo_configuracion(2)
    
def faseypulso(bajada= False, lista= [], pausado= True):
    canal= compruebo_inicio()
    
    if (canal == True) or (comienzo.se_ha_comprobado_2 == True):
        comienzo.pulso_y_fase= True
        configurate.pausado= pausado
        comienzo.se_ha_comprobado_2= True
        
        data.bajada_de_entrada_faseypulso= bajada
        data.lista_de_entrada_faseypulso= lista
        
        preparo_configuracion(3)
    
def ultimate():
    if configurate.tipo_de_ejecucion == 3:
        
        solo_detiene= input("Presiona Enter para continuar... ")
        coloco.ola_numero += 1
        configurate.aumento_para_modo_faseypulso= 0
    
"==============================="

def borrar_todo(lista= None, numero= None, all= None):
    aborrar(lista, num= numero, todos= all)
    
def nuevas_refers(lista):
    nueva_confg(lista)
    
