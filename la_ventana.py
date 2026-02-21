
""" Este es un modulo intermedio entre la ventana
    'muestra carapteres' y la subventana.

    En este modulo se llama la subventana """


"=============================================="

import tkinter as tk
from visor_vari.mas_bajo_nivel.datos import coloco

"=============================================="

def ver_registro(refer, ventana):

    class La_mini:

        def __init__(self):

            self.perimetro_1= None
            self.color_activado= True
            self.sub_ventana()
            
        def establece_color_de_celdas(self):
            
            if self.color_activado == False:
                self.perimetro_1.config (bg= "grey")
            else:
                if coloco.numero_de_ventana == 0:
                    self.perimetro_1.config (bg= "red")
                if coloco.numero_de_ventana == 1:
                    self.perimetro_1.config (bg= "yellow")
                if coloco.numero_de_ventana == 2:
                    self.perimetro_1.config (bg= "green")
                if coloco.numero_de_ventana == 3:
                    self.perimetro_1.config (bg= "blue")
                if coloco.numero_de_ventana == 4:
                    self.perimetro_1.config (bg= "purple")

                if coloco.numero_de_ventana == 5:
                    self.perimetro_1.config (bg= "orange")
                if coloco.numero_de_ventana == 6:
                    self.perimetro_1.config (bg= "pink")
                if coloco.numero_de_ventana == 7:
                    self.perimetro_1.config (bg= "cyan")
                if coloco.numero_de_ventana == 8:
                    self.perimetro_1.config (bg= "brown")
                if coloco.numero_de_ventana == 9:
                    self.perimetro_1.config (bg= "black")

                if coloco.numero_de_ventana == 10:
                    self.perimetro_1.config (bg= "white")
                if coloco.numero_de_ventana == 11:
                    self.perimetro_1.config (bg= "lime")
                if coloco.numero_de_ventana == 12:
                    self.perimetro_1.config (bg= "fuchsia")
                if coloco.numero_de_ventana == 13:
                    self.perimetro_1.config (bg= "teal")
                if coloco.numero_de_ventana == 14:
                    self.perimetro_1.config (bg= "grey")

        def singleton_para_cambiar_color(self):
            
            if self.color_activado == False:
                self.color_activado= True
            elif self.color_activado == True:
                self.color_activado= False
            
        def sale_de_la_ventana(self):
            ventana.destroy()
            
        def sub_ventana(self):
                        
            if True:    # visual y botones
                
                def formando_nombre_de_ventana():
                    mencion=""
                    
                    if coloco.ola_reajustada == False:
                        num_ola= "  ola_" + str(coloco.ola_numero)
                    else:
                        numero_reajustado= coloco.ola_numero - 1
                        num_ola= "  ola_" + str(numero_reajustado)
                    
                    num_vent= "  de_numero_" + str(coloco.numero_de_ventana)
                    
                    mencion= coloco.nombre_de_ventana + num_ola + num_vent
                    
                    return mencion
                    
                titulo= formando_nombre_de_ventana()
                ventana.title(titulo)

                dereizq= tk.LabelFrame(ventana, padx= 10, pady= 10, bd= 0)
                dereizq.pack (expand= True, fill= tk.BOTH)

                "... panel lateral derecho ..."

                perimetro= tk.LabelFrame(dereizq) # marco derecho (botones de control)
                perimetro.config(bd= 0)
                perimetro.pack (side= tk.RIGHT, fill= tk.Y, expand= True)

                boton_0= tk.Button(perimetro, text= "Cambia\nde\ncolor", command= self.singleton_para_cambiar_color)
                boton_0.pack(fill= tk.BOTH, expand= True)

                boton_1= tk.Button(perimetro, text= "Actualiza\nceldas", command= self.sale_de_la_ventana)
                boton_1.pack(fill= tk.BOTH, expand= True)

                "... Creo el LabelFrame del marco de la ventana ..."
                "... y que contendra los otros marcos (celdas) ..."

                self.perimetro_1= tk.LabelFrame(dereizq, padx= 10, pady= 10, bg= "red")
                self.perimetro_1.pack (expand= True, fill= tk.BOTH)

                entorno= tk.LabelFrame(self.perimetro_1, padx= 30, pady= 30) # marco izquierdo (de texto)
                entorno.pack (expand= True, fill= tk.BOTH)
    
            if True:    # aqui estan los marcos de las celdas
                self.gajo_0= tk.LabelFrame(entorno, padx= 15, pady= 15)
                self.gajo_0.grid(row= 0, column= 0)

                self.gajo_1= tk.LabelFrame(entorno, padx= 15, pady= 15)
                self.gajo_1.grid(row= 0, column= 1)

                self.gajo_2= tk.LabelFrame(entorno, padx= 15, pady= 15)
                self.gajo_2.grid(row= 0, column= 2)


                self.gajo_3= tk.LabelFrame(entorno, padx= 15, pady= 15)
                self.gajo_3.grid(row= 1, column= 0)

                self.gajo_4= tk.LabelFrame(entorno, padx= 15, pady= 15)
                self.gajo_4.grid(row= 1, column= 1)

                self.gajo_5= tk.LabelFrame(entorno, padx= 15, pady= 15)
                self.gajo_5.grid(row= 1, column= 2)


                self.gajo_6= tk.LabelFrame(entorno, padx= 15, pady= 15)
                self.gajo_6.grid(row= 2, column= 0)

                self.gajo_7= tk.LabelFrame(entorno, padx= 15, pady= 15)
                self.gajo_7.grid(row= 2, column= 1)

                self.gajo_8= tk.LabelFrame(entorno, padx= 15, pady= 15)
                self.gajo_8.grid(row= 2, column= 2)

            self.visual_celda_0()
            self.establece_color_de_celdas()
                        
        "........................"

        def visual_celda_0(self):

            self.prueva0_0= tk.Button (self.gajo_0, text= refer.selda_0)
            self.prueva0_0.config (bg= "white")
            self.prueva0_0.grid(row= 0, column= 0)

            self.prueva1_0= tk.Button (self.gajo_0, text= refer.selda_1)
            self.prueva1_0.config (bg= "white")
            self.prueva1_0.grid(row= 0, column= 1)

            self.prueva2_0= tk.Button (self.gajo_0, text= refer.selda_2)
            self.prueva2_0.config (bg= "white")
            self.prueva2_0.grid(row= 0, column= 2)

            ""
            self.prueva3_0= tk.Button (self.gajo_0, text= refer.selda_3)
            self.prueva3_0.config (bg= "white")
            self.prueva3_0.grid(row= 1, column= 0)

            self.prueva4_0= tk.Button (self.gajo_0, text= refer.selda_4)
            self.prueva4_0.config (bg= "white")
            self.prueva4_0.grid(row= 1, column= 1)

            self.prueva5_0= tk.Button (self.gajo_0, text= refer.selda_5)
            self.prueva5_0.config (bg= "white")
            self.prueva5_0.grid(row= 1, column= 2)

            ""
            self.prueva6_0= tk.Button (self.gajo_0, text= refer.selda_6)
            self.prueva6_0.config (bg= "white")
            self.prueva6_0.grid(row= 2, column= 0)

            self.prueva7_0= tk.Button (self.gajo_0, text= refer.selda_7)
            self.prueva7_0.config (bg= "white")
            self.prueva7_0.grid(row= 2, column= 1)

            self.prueva8_0= tk.Button (self.gajo_0, text= refer.selda_8)
            self.prueva8_0.config (bg= "white")
            self.prueva8_0.grid(row= 2, column= 2)

            self.visual_celda_1()

        def visual_celda_1(self):

            self.prueva0_1= tk.Button (self.gajo_1, text= refer.selda_9)
            self.prueva0_1.config (bg= "white")
            self.prueva0_1.grid(row= 0, column= 0)

            self.prueva1_1= tk.Button (self.gajo_1, text= refer.selda_10)
            self.prueva1_1.config (bg= "white")
            self.prueva1_1.grid(row= 0, column= 1)

            self.prueva2_1= tk.Button (self.gajo_1, text= refer.selda_11)
            self.prueva2_1.config (bg= "white")
            self.prueva2_1.grid(row= 0, column= 2)

            ""
            self.prueva3_1= tk.Button (self.gajo_1, text= refer.selda_12)
            self.prueva3_1.config (bg= "white")
            self.prueva3_1.grid(row= 1, column= 0)

            self.prueva4_1= tk.Button (self.gajo_1, text= refer.selda_13)
            self.prueva4_1.config (bg= "white")
            self.prueva4_1.grid(row= 1, column= 1)

            self.prueva5_1= tk.Button (self.gajo_1, text= refer.selda_14)
            self.prueva5_1.config (bg= "white")
            self.prueva5_1.grid(row= 1, column= 2)

            ""
            self.prueva6_1= tk.Button (self.gajo_1, text= refer.selda_15)
            self.prueva6_1.config (bg= "white")
            self.prueva6_1.grid(row= 2, column= 0)

            self.prueva7_1= tk.Button (self.gajo_1, text= refer.selda_16)
            self.prueva7_1.config (bg= "white")
            self.prueva7_1.grid(row= 2, column= 1)

            self.prueva8_1= tk.Button (self.gajo_1, text= refer.selda_17)
            self.prueva8_1.config (bg= "white")
            self.prueva8_1.grid(row= 2, column= 2)

            self.visual_celda_2()

        def visual_celda_2(self):

            self.prueva0= tk.Button (self.gajo_2, text= refer.selda_18)
            self.prueva0.config (bg= "white")
            self.prueva0.grid(row= 0, column= 0)

            self.prueva1= tk.Button (self.gajo_2, text= refer.selda_19)
            self.prueva1.config (bg= "white")
            self.prueva1.grid(row= 0, column= 1)

            self.prueva2= tk.Button (self.gajo_2, text= refer.selda_20)
            self.prueva2.config (bg= "white")
            self.prueva2.grid(row= 0, column= 2)

            ""
            self.prueva3= tk.Button (self.gajo_2, text= refer.selda_21)
            self.prueva3.config (bg= "white")
            self.prueva3.grid(row= 1, column= 0)

            self.prueva4= tk.Button (self.gajo_2, text= refer.selda_22)
            self.prueva4.config (bg= "white")
            self.prueva4.grid(row= 1, column= 1)

            self.prueva5= tk.Button (self.gajo_2, text= refer.selda_23)
            self.prueva5.config (bg= "white")
            self.prueva5.grid(row= 1, column= 2)

            ""
            self.prueva6= tk.Button (self.gajo_2, text= refer.selda_24)
            self.prueva6.config (bg= "white")
            self.prueva6.grid(row= 2, column= 0)

            self.prueva7= tk.Button (self.gajo_2, text= refer.selda_25)
            self.prueva7.config (bg= "white")
            self.prueva7.grid(row= 2, column= 1)

            self.prueva8= tk.Button (self.gajo_2, text= refer.selda_26)
            self.prueva8.config (bg= "white")
            self.prueva8.grid(row= 2, column= 2)

            self.visual_celda_3()

        def visual_celda_3(self):

            self.prueva0= tk.Button (self.gajo_3, text= refer.selda_27)
            self.prueva0.config (bg= "white")
            self.prueva0.grid(row= 0, column= 0)

            self.prueva1= tk.Button (self.gajo_3, text= refer.selda_28)
            self.prueva1.config (bg= "white")
            self.prueva1.grid(row= 0, column= 1)

            self.prueva2= tk.Button (self.gajo_3, text= refer.selda_29)
            self.prueva2.config (bg= "white")
            self.prueva2.grid(row= 0, column= 2)

            ""
            self.prueva3= tk.Button (self.gajo_3, text= refer.selda_30)
            self.prueva3.config (bg= "white")
            self.prueva3.grid(row= 1, column= 0)

            self.prueva4= tk.Button (self.gajo_3, text= refer.selda_31)
            self.prueva4.config (bg= "white")
            self.prueva4.grid(row= 1, column= 1)

            self.prueva5= tk.Button (self.gajo_3, text= refer.selda_32)
            self.prueva5.config (bg= "white")
            self.prueva5.grid(row= 1, column= 2)

            ""
            self.prueva6= tk.Button (self.gajo_3, text= refer.selda_33)
            self.prueva6.config (bg= "white")
            self.prueva6.grid(row= 2, column= 0)

            self.prueva7= tk.Button (self.gajo_3, text= refer.selda_34)
            self.prueva7.config (bg= "white")
            self.prueva7.grid(row= 2, column= 1)

            self.prueva8= tk.Button (self.gajo_3, text= refer.selda_35)
            self.prueva8.config (bg= "white")
            self.prueva8.grid(row= 2, column= 2)

            self.visual_celda_4()

        def visual_celda_4(self):

            self.prueva0= tk.Button (self.gajo_4, text= refer.selda_36)
            self.prueva0.config (bg= "white")
            self.prueva0.grid(row= 0, column= 0)

            self.prueva1= tk.Button (self.gajo_4, text= refer.selda_37)
            self.prueva1.config (bg= "white")
            self.prueva1.grid(row= 0, column= 1)

            self.prueva2= tk.Button (self.gajo_4, text= refer.selda_38)
            self.prueva2.config (bg= "white")
            self.prueva2.grid(row= 0, column= 2)

            ""
            self.prueva3= tk.Button (self.gajo_4, text= refer.selda_39)
            self.prueva3.config (bg= "white")
            self.prueva3.grid(row= 1, column= 0)

            self.prueva4= tk.Button (self.gajo_4, text= refer.selda_40)
            self.prueva4.config (bg= "white")
            self.prueva4.grid(row= 1, column= 1)

            self.prueva5= tk.Button (self.gajo_4, text= refer.selda_41)
            self.prueva5.config (bg= "white")
            self.prueva5.grid(row= 1, column= 2)

            ""
            self.prueva6= tk.Button (self.gajo_4, text= refer.selda_42)
            self.prueva6.config (bg= "white")
            self.prueva6.grid(row= 2, column= 0)

            self.prueva7= tk.Button (self.gajo_4, text= refer.selda_43)
            self.prueva7.config (bg= "white")
            self.prueva7.grid(row= 2, column= 1)

            self.prueva8= tk.Button (self.gajo_4, text= refer.selda_44)
            self.prueva8.config (bg= "white")
            self.prueva8.grid(row= 2, column= 2)

            self.visual_celda_5()

        def visual_celda_5(self):

            self.prueva0= tk.Button (self.gajo_5, text= refer.selda_45)
            self.prueva0.config (bg= "white")
            self.prueva0.grid(row= 0, column= 0)

            self.prueva1= tk.Button (self.gajo_5, text= refer.selda_46)
            self.prueva1.config (bg= "white")
            self.prueva1.grid(row= 0, column= 1)

            self.prueva2= tk.Button (self.gajo_5, text= refer.selda_47)
            self.prueva2.config (bg= "white")
            self.prueva2.grid(row= 0, column= 2)

            ""
            self.prueva3= tk.Button (self.gajo_5, text= refer.selda_48)
            self.prueva3.config (bg= "white")
            self.prueva3.grid(row= 1, column= 0)

            self.prueva4= tk.Button (self.gajo_5, text= refer.selda_49)
            self.prueva4.config (bg= "white")
            self.prueva4.grid(row= 1, column= 1)

            self.prueva5= tk.Button (self.gajo_5, text= refer.selda_50)
            self.prueva5.config (bg= "white")
            self.prueva5.grid(row= 1, column= 2)

            ""
            self.prueva6= tk.Button (self.gajo_5, text= refer.selda_51)
            self.prueva6.config (bg= "white")
            self.prueva6.grid(row= 2, column= 0)

            self.prueva7= tk.Button (self.gajo_5, text= refer.selda_52)
            self.prueva7.config (bg= "white")
            self.prueva7.grid(row= 2, column= 1)

            self.prueva8= tk.Button (self.gajo_5, text= refer.selda_53)
            self.prueva8.config (bg= "white")
            self.prueva8.grid(row= 2, column= 2)

            self.visual_celda_6()

        def visual_celda_6(self):

            self.prueva0= tk.Button (self.gajo_6, text= refer.selda_54)
            self.prueva0.config (bg= "white")
            self.prueva0.grid(row= 0, column= 0)

            self.prueva1= tk.Button (self.gajo_6, text= refer.selda_55)
            self.prueva1.config (bg= "white")
            self.prueva1.grid(row= 0, column= 1)

            self.prueva2= tk.Button (self.gajo_6, text= refer.selda_56)
            self.prueva2.config (bg= "white")
            self.prueva2.grid(row= 0, column= 2)

            ""
            self.prueva3= tk.Button (self.gajo_6, text= refer.selda_57)
            self.prueva3.config (bg= "white")
            self.prueva3.grid(row= 1, column= 0)

            self.prueva4= tk.Button (self.gajo_6, text= refer.selda_58)
            self.prueva4.config (bg= "white")
            self.prueva4.grid(row= 1, column= 1)

            self.prueva5= tk.Button (self.gajo_6, text= refer.selda_59)
            self.prueva5.config (bg= "white")
            self.prueva5.grid(row= 1, column= 2)

            ""
            self.prueva6= tk.Button (self.gajo_6, text= refer.selda_60)
            self.prueva6.config (bg= "white")
            self.prueva6.grid(row= 2, column= 0)

            self.prueva7= tk.Button (self.gajo_6, text= refer.selda_61)
            self.prueva7.config (bg= "white")
            self.prueva7.grid(row= 2, column= 1)

            self.prueva8= tk.Button (self.gajo_6, text= refer.selda_62)
            self.prueva8.config (bg= "white")
            self.prueva8.grid(row= 2, column= 2)

            self.visual_celda_7()

        def visual_celda_7(self):

            self.prueva0= tk.Button (self.gajo_7, text= refer.selda_63)
            self.prueva0.config (bg= "white")
            self.prueva0.grid(row= 0, column= 0)

            self.prueva1= tk.Button (self.gajo_7, text= refer.selda_64)
            self.prueva1.config (bg= "white")
            self.prueva1.grid(row= 0, column= 1)

            self.prueva2= tk.Button (self.gajo_7, text= refer.selda_65)
            self.prueva2.config (bg= "white")
            self.prueva2.grid(row= 0, column= 2)

            ""
            self.prueva3= tk.Button (self.gajo_7, text= refer.selda_66)
            self.prueva3.config (bg= "white")
            self.prueva3.grid(row= 1, column= 0)

            self.prueva4= tk.Button (self.gajo_7, text= refer.selda_67)
            self.prueva4.config (bg= "white")
            self.prueva4.grid(row= 1, column= 1)

            self.prueva5= tk.Button (self.gajo_7, text= refer.selda_68)
            self.prueva5.config (bg= "white")
            self.prueva5.grid(row= 1, column= 2)

            ""
            self.prueva6= tk.Button (self.gajo_7, text= refer.selda_69)
            self.prueva6.config (bg= "white")
            self.prueva6.grid(row= 2, column= 0)

            self.prueva7= tk.Button (self.gajo_7, text= refer.selda_70)
            self.prueva7.config (bg= "white")
            self.prueva7.grid(row= 2, column= 1)

            self.prueva8= tk.Button (self.gajo_7, text= refer.selda_71)
            self.prueva8.config (bg= "white")
            self.prueva8.grid(row= 2, column= 2)

            self.visual_celda_8()

        def visual_celda_8(self):

            self.prueva0= tk.Button (self.gajo_8, text= refer.selda_72)
            self.prueva0.config (bg= "white")
            self.prueva0.grid(row= 0, column= 0)

            self.prueva1= tk.Button (self.gajo_8, text= refer.selda_73)
            self.prueva1.config (bg= "white")
            self.prueva1.grid(row= 0, column= 1)

            self.prueva2= tk.Button (self.gajo_8, text= refer.selda_74)
            self.prueva2.config (bg= "white")
            self.prueva2.grid(row= 0, column= 2)

            ""
            self.prueva3= tk.Button (self.gajo_8, text= refer.selda_75)
            self.prueva3.config (bg= "white")
            self.prueva3.grid(row= 1, column= 0)

            self.prueva4= tk.Button (self.gajo_8, text= refer.selda_76)
            self.prueva4.config (bg= "white")
            self.prueva4.grid(row= 1, column= 1)

            self.prueva5= tk.Button (self.gajo_8, text= refer.selda_77)
            self.prueva5.config (bg= "white")
            self.prueva5.grid(row= 1, column= 2)

            ""
            self.prueva6= tk.Button (self.gajo_8, text= refer.selda_78)
            self.prueva6.config (bg= "white")
            self.prueva6.grid(row= 2, column= 0)

            self.prueva7= tk.Button (self.gajo_8, text= refer.selda_79)
            self.prueva7.config (bg= "white")
            self.prueva7.grid(row= 2, column= 1)

            self.prueva8= tk.Button (self.gajo_8, text= refer.selda_80)
            self.prueva8.config (bg= "white")
            self.prueva8.grid(row= 2, column= 2)
            
    "........................"

    La_mini()

