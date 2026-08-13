
""" En este documento se llama la ventana donde se muestran los diferentes valores. """


#################################
#   importaciones               #
"==============================="

en_prueba= False
if en_prueba == False:

    from visor_vari.mas_bajo_nivel.see import refer_0 # la refer estandar.
    from visor_vari.mas_bajo_nivel.datos import verifico
    from visor_vari.mas_bajo_nivel.datos import coloco # para el nombre de la ventana.
    from visor_vari.la_ventana import ver_registro
    import threading
    from copy import deepcopy
    import time
    
    if True: # todo el resto de refer_
        from visor_vari.mas_bajo_nivel.see import refer_1
        from visor_vari.mas_bajo_nivel.see import refer_2
        from visor_vari.mas_bajo_nivel.see import refer_3
        from visor_vari.mas_bajo_nivel.see import refer_4
        from visor_vari.mas_bajo_nivel.see import refer_5
        from visor_vari.mas_bajo_nivel.see import refer_6
        from visor_vari.mas_bajo_nivel.see import refer_7
        from visor_vari.mas_bajo_nivel.see import refer_8
        from visor_vari.mas_bajo_nivel.see import refer_9
else:

    from mas_bajo_nivel.see import refer_0 # la refer estandar.
    from mas_bajo_nivel.datos import verifico
    from mas_bajo_nivel.datos import coloco # para el nombre de la ventana.
    from la_ventana import ver_registro
    import threading
    from copy import deepcopy
    import time

    if True: # todo el resto de refer_
        from mas_bajo_nivel.see import refer_1
        from mas_bajo_nivel.see import refer_2
        from mas_bajo_nivel.see import refer_3
        from mas_bajo_nivel.see import refer_4
        from mas_bajo_nivel.see import refer_5
        from mas_bajo_nivel.see import refer_6
        from mas_bajo_nivel.see import refer_7
        from mas_bajo_nivel.see import refer_8
        from mas_bajo_nivel.see import refer_9

#################################
#   el numero de hilo.          #
"==============================="

class Cuenta_hilo:
    
    def __init__(self):
        self.numero= 1
        
    def sumale(self):
        self.numero += 1
    
entrada= Cuenta_hilo()

#################################
#   Estados y comprobaciones    #
"==============================="

import tkinter as tk

def crea_primero():
    
    venta= tk.Tk()
    venta.withdraw()
            
    venta.mainloop()

def creando_ventana(refer_actual, esquiva= False):
    "desde aqui creo verdaderamente la ventana, sea por tk."

    esq= esquiva
    
    if esq == False:
        ventana= tk.Tk()

    else:
        subventana= tk.Toplevel()
        
    def verificacion_normal():
        venganza= False
        
        if verifico.estado_refer_0== False:
            venganza= True
        elif verifico.estado_refer_1== True:
            venganza= True
        elif verifico.estado_refer_2== True:
            venganza= True
        elif verifico.estado_refer_3== True:
            venganza= True
        elif verifico.estado_refer_4== True:
            venganza= True
        elif verifico.estado_refer_5== True:
            venganza= True
        elif verifico.estado_refer_6== True:
            venganza= True
        elif verifico.estado_refer_7== True:
            venganza= True
        elif verifico.estado_refer_8== True:
            venganza= True
        elif verifico.estado_refer_9== True:
            venganza= True
            
        return venganza

    enemigo= verificacion_normal()
    
    if esq == False:    # para la mayoria de los casos
        
        if enemigo == False:
            ver_registro(refer_actual, ventana)
        #
        else:
            el_tipo_es_1= True
            if el_tipo_es_1 == True: # para que solo trabaje con gentil()... vacio.
            
                if verifico.estado_refer_0 == True: # de todas formas este se ejecuta.
                    ver_registro(refer_0, ventana)
                if verifico.estado_refer_1 == True:
                    coloco.nombre_de_ventana= "Referencia_1"
                    ver_registro(refer_1, ventana)
                if verifico.estado_refer_2 == True:
                    coloco.nombre_de_ventana= "Referencia_2"
                    ver_registro(refer_2, ventana)
                if verifico.estado_refer_3 == True:
                    coloco.nombre_de_ventana= "Referencia_3"
                    ver_registro(refer_3, ventana)
                if verifico.estado_refer_4 == True:
                    coloco.nombre_de_ventana= "Referencia_4"
                    ver_registro(refer_4, ventana)
                if verifico.estado_refer_5 == True:
                    coloco.nombre_de_ventana= "Referencia_5"
                    ver_registro(refer_5, ventana)
                if verifico.estado_refer_6 == True:
                    coloco.nombre_de_ventana= "Referencia_6"
                    ver_registro(refer_6, ventana)
                if verifico.estado_refer_7 == True:
                    coloco.nombre_de_ventana= "Referencia_7"
                    ver_registro(refer_7, ventana)
                if verifico.estado_refer_8 == True:
                    coloco.nombre_de_ventana= "Referencia_8"
                    ver_registro(refer_8, ventana)
                if verifico.estado_refer_9 == True:
                    coloco.nombre_de_ventana= "Referencia_9"
                    ver_registro(refer_9, ventana)
                    
                coloco.nombre_de_ventana= "Referencia_0"
    
    elif esq == True:   # para cuando, falseypulso en: bajada= True, pausado= False.
    
        if enemigo == False:
            ver_registro(refer_actual, subventana)
        #
        else:
            el_tipo_es_1= True
            if el_tipo_es_1 == True: # para que solo trabaje con gentil()... vacio.
            
                if verifico.estado_refer_0 == True: # de todas formas este se ejecuta.
                    ver_registro(refer_0, subventana)
                if verifico.estado_refer_1 == True:
                    coloco.nombre_de_ventana= "Referencia_1"
                    ver_registro(refer_1, subventana)
                if verifico.estado_refer_2 == True:
                    coloco.nombre_de_ventana= "Referencia_2"
                    ver_registro(refer_2, subventana)
                if verifico.estado_refer_3 == True:
                    coloco.nombre_de_ventana= "Referencia_3"
                    ver_registro(refer_3, subventana)
                if verifico.estado_refer_4 == True:
                    coloco.nombre_de_ventana= "Referencia_4"
                    ver_registro(refer_4, subventana)
                if verifico.estado_refer_5 == True:
                    coloco.nombre_de_ventana= "Referencia_5"
                    ver_registro(refer_5, subventana)
                if verifico.estado_refer_6 == True:
                    coloco.nombre_de_ventana= "Referencia_6"
                    ver_registro(refer_6, subventana)
                if verifico.estado_refer_7 == True:
                    coloco.nombre_de_ventana= "Referencia_7"
                    ver_registro(refer_7, subventana)
                if verifico.estado_refer_8 == True:
                    coloco.nombre_de_ventana= "Referencia_8"
                    ver_registro(refer_8, subventana)
                if verifico.estado_refer_9 == True:
                    coloco.nombre_de_ventana= "Referencia_9"
                    ver_registro(refer_9, subventana)
                    
                coloco.nombre_de_ventana= "Referencia_0"

    if esq == False:
        ventana.mainloop()

def ejecutando_gentil_para_visualizar_variables(indicador):
    # creo la ventana en segundo plano
    
    if indicador.falseypulso_en_bajada == False:
        # Sin confg previa (en 'viendo.py') todas deberian entrar aqui.
        
        esquiva= False
        snapshot = deepcopy(refer_0)
        linea= threading.Thread(target=creando_ventana, args=(snapshot, esquiva))
        linea.start()
        
    if (indicador.confirmo_falseypulso == True) and (indicador.falseypulso_en_bajada == True):
        # La transicion... no es muy buena, deberia mejorar eso.
        
        if entrada.numero == 1:
            
            linea= threading.Thread(target=crea_primero, daemon= True)
            linea.start()
            
            entrada.sumale()
            time.sleep(0.5)
        
        esquiva= True
        snapshot = deepcopy(refer_0)
        linea= threading.Thread(target=creando_ventana, args=(snapshot, esquiva), daemon= True)
        linea.start()
        time.sleep(0.7)
        
"==============================="
#   Entradas
################################

def proceden_de_sin_lista_hilo(indicador):
    "para identificaar que la situacion por la que se ha llegado aqui es porque no se han creado listas."
    #print("en: sin_lista de hilo")
    ejecutando_gentil_para_visualizar_variables(indicador)

def proceden_de_con_lista_hilo(indicador):
    "para identificaar que la situacion por la que se ha llegado aqui es porque se han creado listas."
    #print("en: con_lista de hilo")
    ejecutando_gentil_para_visualizar_variables(indicador)

