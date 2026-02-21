
""" muestro las variables, deteniendose en cada ventana. """


"==============================="
#   importaciones
################################

#visor_vari.
from visor_vari.mas_bajo_nivel.see import refer_0 # la refer estandar.
from visor_vari.mas_bajo_nivel.datos import verifico
from visor_vari.mas_bajo_nivel.datos import coloco # para el nombre de la ventana.
from visor_vari.la_ventana import ver_registro
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

"==============================="
#   Estados y comprobaciones
################################

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

"==============================="
#   Procesando tareas de gentil
################################

def ejecutando_gentil_para_visualizar_variables(el_tipo_es_1= False):
    
    # creando objeto... ventana...
    if coloco.posible_tk == None:
        import tkinter as tk
        
        ventana= tk.Tk()
    else:
        ventana= coloco.posible_tk.Toplevel()
    
    # configurandolo
    ventana.resizable(0,0)
    alcon= None
    
    # comprobando las dispocisiones.
    enemigo= verificacion_normal()
    if enemigo == False:
        ver_registro(refer_0, ventana)
    
    else:
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

    if coloco.posible_tk == None:
        ventana.mainloop()
    else:
        if coloco.pausado == True:
            ventana.wait_window() # Espera hasta que la ventana se cierre

"==============================="
#   Entradas
################################

def proceden_de_sin_lista(tipo= False):
    "para identificaar que la situacion por la que se ha llegado aqui es porque no se han creado listas."
    #print("en: sin_lista")
    ejecutando_gentil_para_visualizar_variables(tipo)

def proceden_de_con_lista():
    "para identificaar que la situacion por la que se ha llegado aqui es porque se han creado listas."
    #print("en: con_lista")
    ejecutando_gentil_para_visualizar_variables()

