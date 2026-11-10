

""" Encuentra la forma, de comparacion, adecuada usando 'visor-vari'.
    
"""


"==============================="
#   Importaciones.
#################################

en_prueba= False
if en_prueba == False:
    
    from visor_vari._mas_bajo_nivel.see import refer_0
else:
    from _mas_bajo_nivel.see import refer_0

"==============================="
#   Cuerpo del modulo.
#################################


class Estructura:
    
    def __init__(self):
        
        self.entradas_definidas= False

        self.selda_00_a= None
        self.selda_01_a= None
        self.selda_02_a= None
        
        self.selda_03_a= None
        self.selda_04_a= None
        self.selda_05_a= None
        
        self.selda_06_a= None
        self.selda_07_a= None
        self.selda_08_a= None

        "__________________"
    
        self.selda_00_b= None
        self.selda_01_b= None
        self.selda_02_b= None
        
        self.selda_03_b= None
        self.selda_04_b= None
        self.selda_05_b= None
        
        self.selda_06_b= None
        self.selda_07_b= None
        self.selda_08_b= None
        
        "__________________"
    
        self.a_guardar= 0
        self.continuo= True
        
    def filtrando_coordenadas(self, bloque_a, selda_a, bloque_b, selda_b):
        
        if type(bloque_a) is int:
            if (bloque_a > 2) or (0 > bloque_a):
                self.entradas_definidas= False
                return
        else:
            self.entradas_definidas= False
            return
        
        if type(bloque_b) is int:
            if (bloque_b > 2) or (0 > bloque_b):
                self.entradas_definidas= False
                return
        else:
            self.entradas_definidas= False
            return
        
        "______________________________________"
        
        if type(selda_a) is int:
            if (selda_a > 2) or (0 > selda_a):
                self.entradas_definidas= False
                return
        else:
            self.entradas_definidas= False
            return

        if type(selda_b) is int:
            if (selda_b > 2) or (0 > selda_b):
                self.entradas_definidas= False
                return
        else:
            self.entradas_definidas= False
            return
        
        "______________________________________"
        
        if (bloque_a == bloque_b) and (selda_a == selda_b):
            self.entradas_definidas= False
            return

        self.entradas_definidas= True
        
    def preconfg_primero(self, bloque_a, selda_a, bloque_b, selda_b):
        
        self.filtrando_coordenadas(bloque_a, selda_a, bloque_b, selda_b)
        
        if self.entradas_definidas == False:
            raise ValueError("Los datos, de entrada, aportados no son validos (visor-vari).")
        
        if bloque_a == 0:
            
            if selda_a == 0:
            
                self.selda_00_a= refer_0.selda_0
                self.selda_01_a= refer_0.selda_1
                self.selda_02_a= refer_0.selda_2
                
                self.selda_03_a= refer_0.selda_3
                self.selda_04_a= refer_0.selda_4
                self.selda_05_a= refer_0.selda_5
                
                self.selda_06_a= refer_0.selda_6
                self.selda_07_a= refer_0.selda_7
                self.selda_08_a= refer_0.selda_8
                
            if selda_a == 1:

                self.selda_00_a= refer_0.selda_9
                self.selda_01_a= refer_0.selda_10
                self.selda_02_a= refer_0.selda_11
                
                self.selda_03_a= refer_0.selda_12
                self.selda_04_a= refer_0.selda_13
                self.selda_05_a= refer_0.selda_14
                
                self.selda_06_a= refer_0.selda_15
                self.selda_07_a= refer_0.selda_16
                self.selda_08_a= refer_0.selda_17
            
            if selda_a == 2:

                self.selda_00_a= refer_0.selda_18
                self.selda_01_a= refer_0.selda_19
                self.selda_02_a= refer_0.selda_20
                
                self.selda_03_a= refer_0.selda_21
                self.selda_04_a= refer_0.selda_22
                self.selda_05_a= refer_0.selda_23
                
                self.selda_06_a= refer_0.selda_24
                self.selda_07_a= refer_0.selda_25
                self.selda_08_a= refer_0.selda_26
            
        if bloque_a == 1:
            
            if selda_a == 0:
            
                self.selda_00_a= refer_0.selda_27
                self.selda_01_a= refer_0.selda_28
                self.selda_02_a= refer_0.selda_29
                
                self.selda_03_a= refer_0.selda_30
                self.selda_04_a= refer_0.selda_31
                self.selda_05_a= refer_0.selda_32
                
                self.selda_06_a= refer_0.selda_33
                self.selda_07_a= refer_0.selda_34
                self.selda_08_a= refer_0.selda_35
                
            if selda_a == 1:

                self.selda_00_a= refer_0.selda_36
                self.selda_01_a= refer_0.selda_37
                self.selda_02_a= refer_0.selda_38
                
                self.selda_03_a= refer_0.selda_39
                self.selda_04_a= refer_0.selda_40
                self.selda_05_a= refer_0.selda_41
                
                self.selda_06_a= refer_0.selda_42
                self.selda_07_a= refer_0.selda_43
                self.selda_08_a= refer_0.selda_44
            
            if selda_a == 2:

                self.selda_00_a= refer_0.selda_45
                self.selda_01_a= refer_0.selda_46
                self.selda_02_a= refer_0.selda_47
                
                self.selda_03_a= refer_0.selda_48
                self.selda_04_a= refer_0.selda_49
                self.selda_05_a= refer_0.selda_50
                
                self.selda_06_a= refer_0.selda_51
                self.selda_07_a= refer_0.selda_52
                self.selda_08_a= refer_0.selda_53
            
        if bloque_a == 2:
            
            if selda_a == 0:
            
                self.selda_00_a= refer_0.selda_54
                self.selda_01_a= refer_0.selda_55
                self.selda_02_a= refer_0.selda_56
                
                self.selda_03_a= refer_0.selda_57
                self.selda_04_a= refer_0.selda_58
                self.selda_05_a= refer_0.selda_59
                
                self.selda_06_a= refer_0.selda_60
                self.selda_07_a= refer_0.selda_61
                self.selda_08_a= refer_0.selda_62
                
            if selda_a == 1:

                self.selda_00_a= refer_0.selda_63
                self.selda_01_a= refer_0.selda_64
                self.selda_02_a= refer_0.selda_65
                
                self.selda_03_a= refer_0.selda_66
                self.selda_04_a= refer_0.selda_67
                self.selda_05_a= refer_0.selda_68
                
                self.selda_06_a= refer_0.selda_69
                self.selda_07_a= refer_0.selda_70
                self.selda_08_a= refer_0.selda_71
            
            if selda_a == 2:

                self.selda_00_a= refer_0.selda_72
                self.selda_01_a= refer_0.selda_73
                self.selda_02_a= refer_0.selda_74
                
                self.selda_03_a= refer_0.selda_75
                self.selda_04_a= refer_0.selda_76
                self.selda_05_a= refer_0.selda_77
                
                self.selda_06_a= refer_0.selda_78
                self.selda_07_a= refer_0.selda_79
                self.selda_08_a= refer_0.selda_80
            
        if bloque_b == 0:
            
            if selda_b == 0:
            
                self.selda_00_b= refer_0.selda_0
                self.selda_01_b= refer_0.selda_1
                self.selda_02_b= refer_0.selda_2
                
                self.selda_03_b= refer_0.selda_3
                self.selda_04_b= refer_0.selda_4
                self.selda_05_b= refer_0.selda_5
                
                self.selda_06_b= refer_0.selda_6
                self.selda_07_b= refer_0.selda_7
                self.selda_08_b= refer_0.selda_8
                
            if selda_b == 1:

                self.selda_00_b= refer_0.selda_9
                self.selda_01_b= refer_0.selda_10
                self.selda_02_b= refer_0.selda_11
                
                self.selda_03_b= refer_0.selda_12
                self.selda_04_b= refer_0.selda_13
                self.selda_05_b= refer_0.selda_14
                
                self.selda_06_b= refer_0.selda_15
                self.selda_07_b= refer_0.selda_16
                self.selda_08_b= refer_0.selda_17
            
            if selda_b == 2:

                self.selda_00_b= refer_0.selda_18
                self.selda_01_b= refer_0.selda_19
                self.selda_02_b= refer_0.selda_20
                
                self.selda_03_b= refer_0.selda_21
                self.selda_04_b= refer_0.selda_22
                self.selda_05_b= refer_0.selda_23
                
                self.selda_06_b= refer_0.selda_24
                self.selda_07_b= refer_0.selda_25
                self.selda_08_b= refer_0.selda_26
            
        if bloque_b == 1:
            
            if selda_b == 0:
            
                self.selda_00_b= refer_0.selda_27
                self.selda_01_b= refer_0.selda_28
                self.selda_02_b= refer_0.selda_29
                
                self.selda_03_b= refer_0.selda_30
                self.selda_04_b= refer_0.selda_31
                self.selda_05_b= refer_0.selda_32
                
                self.selda_06_b= refer_0.selda_33
                self.selda_07_b= refer_0.selda_34
                self.selda_08_b= refer_0.selda_35
                
            if selda_b == 1:

                self.selda_00_b= refer_0.selda_36
                self.selda_01_b= refer_0.selda_37
                self.selda_02_b= refer_0.selda_38
                
                self.selda_03_b= refer_0.selda_39
                self.selda_04_b= refer_0.selda_40
                self.selda_05_b= refer_0.selda_41
                
                self.selda_06_b= refer_0.selda_42
                self.selda_07_b= refer_0.selda_43
                self.selda_08_b= refer_0.selda_44
            
            if selda_b == 2:

                self.selda_00_b= refer_0.selda_45
                self.selda_01_b= refer_0.selda_46
                self.selda_02_b= refer_0.selda_47
                
                self.selda_03_b= refer_0.selda_48
                self.selda_04_b= refer_0.selda_49
                self.selda_05_b= refer_0.selda_50
                
                self.selda_06_b= refer_0.selda_51
                self.selda_07_b= refer_0.selda_52
                self.selda_08_b= refer_0.selda_53
            
        if bloque_b == 2:
            
            if selda_b == 0:
            
                self.selda_00_b= refer_0.selda_54
                self.selda_01_b= refer_0.selda_55
                self.selda_02_b= refer_0.selda_56
                
                self.selda_03_b= refer_0.selda_57
                self.selda_04_b= refer_0.selda_58
                self.selda_05_b= refer_0.selda_59
                
                self.selda_06_b= refer_0.selda_60
                self.selda_07_b= refer_0.selda_61
                self.selda_08_b= refer_0.selda_62
                
            if selda_b == 1:

                self.selda_00_b= refer_0.selda_63
                self.selda_01_b= refer_0.selda_64
                self.selda_02_b= refer_0.selda_65
                
                self.selda_03_b= refer_0.selda_66
                self.selda_04_b= refer_0.selda_67
                self.selda_05_b= refer_0.selda_68
                
                self.selda_06_b= refer_0.selda_69
                self.selda_07_b= refer_0.selda_70
                self.selda_08_b= refer_0.selda_71
            
            if selda_b == 2:

                self.selda_00_b= refer_0.selda_72
                self.selda_01_b= refer_0.selda_73
                self.selda_02_b= refer_0.selda_74
                
                self.selda_03_b= refer_0.selda_75
                self.selda_04_b= refer_0.selda_76
                self.selda_05_b= refer_0.selda_77
                
                self.selda_06_b= refer_0.selda_78
                self.selda_07_b= refer_0.selda_79
                self.selda_08_b= refer_0.selda_80
    
    def asigna_a_refer_0(self, paq, bloque, selda):
        
        if bloque == 0:
        
            if selda == 0:
        
                refer_0.selda_0= paq[0]
                refer_0.selda_1= paq[1]
                refer_0.selda_2= paq[2]
                
                refer_0.selda_3= paq[3]
                refer_0.selda_4= paq[4]
                refer_0.selda_5= paq[5]
                
                refer_0.selda_6= paq[6]
                refer_0.selda_7= paq[7]
                refer_0.selda_8= paq[8]
                
            if selda == 1:
        
                refer_0.selda_9= paq[0]
                refer_0.selda_10= paq[1]
                refer_0.selda_11= paq[2]
                
                refer_0.selda_12= paq[3]
                refer_0.selda_13= paq[4]
                refer_0.selda_14= paq[5]
                
                refer_0.selda_15= paq[6]
                refer_0.selda_16= paq[7]
                refer_0.selda_17= paq[8]
                
            if selda == 2:
        
                refer_0.selda_18= paq[0]
                refer_0.selda_19= paq[1]
                refer_0.selda_20= paq[2]
                
                refer_0.selda_21= paq[3]
                refer_0.selda_22= paq[4]
                refer_0.selda_23= paq[5]
                
                refer_0.selda_24= paq[6]
                refer_0.selda_25= paq[7]
                refer_0.selda_26= paq[8]
                
        if bloque == 1:
        
            if selda == 0:
        
                refer_0.selda_27= paq[0]
                refer_0.selda_28= paq[1]
                refer_0.selda_29= paq[2]
                
                refer_0.selda_30= paq[3]
                refer_0.selda_31= paq[4]
                refer_0.selda_32= paq[5]
                
                refer_0.selda_33= paq[6]
                refer_0.selda_34= paq[7]
                refer_0.selda_35= paq[8]
                
            if selda == 1:
        
                refer_0.selda_36= paq[0]
                refer_0.selda_37= paq[1]
                refer_0.selda_38= paq[2]
                
                refer_0.selda_39= paq[3]
                refer_0.selda_40= paq[4]
                refer_0.selda_41= paq[5]
                
                refer_0.selda_42= paq[6]
                refer_0.selda_43= paq[7]
                refer_0.selda_44= paq[8]
                
            if selda == 2:
        
                refer_0.selda_45= paq[0]
                refer_0.selda_46= paq[1]
                refer_0.selda_47= paq[2]
                
                refer_0.selda_48= paq[3]
                refer_0.selda_49= paq[4]
                refer_0.selda_50= paq[5]
                
                refer_0.selda_51= paq[6]
                refer_0.selda_52= paq[7]
                refer_0.selda_53= paq[8]
                
        if bloque == 2:
        
            if selda == 0:
        
                refer_0.selda_54= paq[0]
                refer_0.selda_55= paq[1]
                refer_0.selda_56= paq[2]
                
                refer_0.selda_57= paq[3]
                refer_0.selda_58= paq[4]
                refer_0.selda_59= paq[5]
                
                refer_0.selda_60= paq[6]
                refer_0.selda_61= paq[7]
                refer_0.selda_62= paq[8]
                
            if selda == 1:
        
                refer_0.selda_63= paq[0]
                refer_0.selda_64= paq[1]
                refer_0.selda_65= paq[2]
                
                refer_0.selda_66= paq[3]
                refer_0.selda_67= paq[4]
                refer_0.selda_68= paq[5]
                
                refer_0.selda_69= paq[6]
                refer_0.selda_70= paq[7]
                refer_0.selda_71= paq[8]
                
            if selda == 2:
        
                refer_0.selda_72= paq[0]
                refer_0.selda_73= paq[1]
                refer_0.selda_74= paq[2]
                
                refer_0.selda_75= paq[3]
                refer_0.selda_76= paq[4]
                refer_0.selda_77= paq[5]
                
                refer_0.selda_78= paq[6]
                refer_0.selda_79= paq[7]
                refer_0.selda_80= paq[8]
    
    "______________________________"
    
    # ¿ El_formato_de_la_salida ?
    
    def es_correcta(self, bloq, seld):
        
        respuesta= True
        
        if isinstance(bloq, int):
            if (bloq < 0) or (2 < bloq):
                respuesta= False
        else:
            respuesta= False
        
        if isinstance(seld, int):
            if (seld < 0) or (2 < seld):
                respuesta= False
        else:
            respuesta= False
                
        return respuesta
    
    def tipo_de_comparacion(self, tipo, back, bloque= None, selda= None):
        
        la_root_salida= self.es_correcta(bloque, selda)
        
        if la_root_salida == False:
            
            if (back == True) and (bloque == None) and (selda == None):
                pass
            else:
                raise TypeError("La salida no esta bien definida (visor-vari).")
        
        " Tipo de trabajo que se esta haciendo. "
        if tipo == 1:   # Devuelve, el valor, si no es iguales (bloque_b, selda_b).
            paquete= self.procesa_01()
        
        elif tipo == 2: # Devuelve en booleano, si son iguales.
            paquete= self.procesa_02()
        
        elif tipo == 3: # Devuelve, el valor, si es superior.
            paquete= self.procesa_03()
        
        elif tipo == 4: # Devuelve en booleano, si es superior.
            paquete= self.procesa_04()
        
        elif tipo == 5: # Devuelve, el valor, si es inferior.
            paquete= self.procesa_05()
        
        elif tipo == 6: # Devuelve en booleano, si es inferior.
            paquete= self.procesa_06()
        
        " Resultado devuelto. "
        if back == True:    # Para esta forma de uso, no se necesita 'bloque' ni 'selda'.
            
            if self.continuo == False:
                self.entradas_definidas= False
            
            return paquete
        
        elif back == False: # Mostrando las diferencias en visor-vari.
            
            self.asigna_a_refer_0(paquete, bloque, selda)
            
            if self.continuo == False:
                self.entradas_definidas= False
        
        else:
            raise TypeError("El argumento 'back' solo puede ser 'True' o 'False' (visor-vari).")
    
    def confg_piso(self, sign, continuo):
        self.a_guardar= sign
        self.continuo= continuo
        
    "______________________________"
    "______________________________"
    
    def porvalor(self, back, bloque= None, selda= None):
        return self.tipo_de_comparacion(1, back, bloque, selda)

    def procesa_01(self):
        
        if self.entradas_definidas == False:
            raise EOFError("No se han establecido las seldas a filtrar (visor-vari).")
        
        salida= []
        
        if self.selda_00_a == self.selda_00_b:
            salida.append(self.a_guardar)
        else:
            salida.append(self.selda_00_b)
            
        if self.selda_01_a == self.selda_01_b:
            salida.append(self.a_guardar)
        else:
            salida.append(self.selda_01_b)
            
        if self.selda_02_a == self.selda_02_b:
            salida.append(self.a_guardar)
        else:
            salida.append(self.selda_02_b)
            
        if self.selda_03_a == self.selda_03_b:
            salida.append(self.a_guardar)
        else:
            salida.append(self.selda_03_b)
            
        if self.selda_04_a == self.selda_04_b:
            salida.append(self.a_guardar)
        else:
            salida.append(self.selda_04_b)
            
        if self.selda_05_a == self.selda_05_b:
            salida.append(self.a_guardar)
        else:
            salida.append(self.selda_05_b)
            
        if self.selda_06_a == self.selda_06_b:
            salida.append(self.a_guardar)
        else:
            salida.append(self.selda_06_b)
            
        if self.selda_07_a == self.selda_07_b:
            salida.append(self.a_guardar)
        else:
            salida.append(self.selda_07_b)
            
        if self.selda_08_a == self.selda_08_b:
            salida.append(self.a_guardar)
        else:
            salida.append(self.selda_08_b)
                
        return salida

    "______________________________"

    def porboolean(self, back, bloque= None, selda= None):
        return self.tipo_de_comparacion(2, back, bloque, selda)

    def procesa_02(self):
        
        if self.entradas_definidas == False:
            raise EOFError("No se han establecido las seldas a filtrar (visor-vari).")
        
        salida= []
        
        if self.selda_00_a != self.selda_00_b:
            salida.append(True)
        else:
            salida.append(False)
            
        if self.selda_01_a != self.selda_01_b:
            salida.append(True)
        else:
            salida.append(False)
            
        if self.selda_02_a != self.selda_02_b:
            salida.append(True)
        else:
            salida.append(False)
            
        if self.selda_03_a != self.selda_03_b:
            salida.append(True)
        else:
            salida.append(False)
            
        if self.selda_04_a != self.selda_04_b:
            salida.append(True)
        else:
            salida.append(False)
            
        if self.selda_05_a != self.selda_05_b:
            salida.append(True)
        else:
            salida.append(False)
            
        if self.selda_06_a != self.selda_06_b:
            salida.append(True)
        else:
            salida.append(False)
            
        if self.selda_07_a != self.selda_07_b:
            salida.append(True)
        else:
            salida.append(False)
            
        if self.selda_08_a != self.selda_08_b:
            salida.append(True)
        else:
            salida.append(False)
        
        return salida

    "______________________________"
    "______________________________"

    def valorsuperior(self, back, bloque= None, selda= None):
        return self.tipo_de_comparacion(3, back, bloque, selda)

    def procesa_03(self):
        
        if self.entradas_definidas == False:
            raise EOFError("No se han establecido las seldas a filtrar (visor-vari).")
        
        salida= []
        
        if self.selda_00_a >= self.selda_00_b:
            salida.append(self.a_guardar)
        if self.selda_00_a < self.selda_00_b:
            salida.append(self.selda_00_b)
            
        if self.selda_01_a >= self.selda_01_b:
            salida.append(self.a_guardar)
        if self.selda_01_a < self.selda_01_b:
            salida.append(self.selda_01_b)
            
        if self.selda_02_a >= self.selda_02_b:
            salida.append(self.a_guardar)
        if self.selda_02_a < self.selda_02_b:
            salida.append(self.selda_02_b)
            
        if self.selda_03_a >= self.selda_03_b:
            salida.append(self.a_guardar)
        if self.selda_03_a < self.selda_03_b:
            salida.append(self.selda_03_b)
            
        if self.selda_04_a >= self.selda_04_b:
            salida.append(self.a_guardar)
        if self.selda_04_a < self.selda_04_b:
            salida.append(self.selda_04_b)
            
        if self.selda_05_a >= self.selda_05_b:
            salida.append(self.a_guardar)
        if self.selda_05_a < self.selda_05_b:
            salida.append(self.selda_05_b)
            
        if self.selda_06_a >= self.selda_06_b:
            salida.append(self.a_guardar)
        if self.selda_06_a < self.selda_06_b:
            salida.append(self.selda_06_b)
            
        if self.selda_07_a >= self.selda_07_b:
            salida.append(self.a_guardar)
        if self.selda_07_a < self.selda_07_b:
            salida.append(self.selda_07_b)
            
        if self.selda_08_a >= self.selda_08_b:
            salida.append(self.a_guardar)
        if self.selda_08_a < self.selda_08_b:
            salida.append(self.selda_08_b)
        
        return salida

    "______________________________"

    def booleansuperior(self, back, bloque= None, selda= None):
        return self.tipo_de_comparacion(4, back, bloque, selda)

    def procesa_04(self):
        
        if self.entradas_definidas == False:
            raise EOFError("No se han establecido las seldas a filtrar (visor-vari).")
        
        salida= []
        
        if self.selda_00_a >= self.selda_00_b:
            salida.append(False)
        if self.selda_00_a < self.selda_00_b:
            salida.append(True)
            
        if self.selda_01_a >= self.selda_01_b:
            salida.append(False)
        if self.selda_01_a < self.selda_01_b:
            salida.append(True)
            
        if self.selda_02_a >= self.selda_02_b:
            salida.append(False)
        if self.selda_02_a < self.selda_02_b:
            salida.append(True)
            
        if self.selda_03_a >= self.selda_03_b:
            salida.append(False)
        if self.selda_03_a < self.selda_03_b:
            salida.append(True)
            
        if self.selda_04_a >= self.selda_04_b:
            salida.append(False)
        if self.selda_04_a < self.selda_04_b:
            salida.append(True)
            
        if self.selda_05_a >= self.selda_05_b:
            salida.append(False)
        if self.selda_05_a < self.selda_05_b:
            salida.append(True)
            
        if self.selda_06_a >= self.selda_06_b:
            salida.append(False)
        if self.selda_06_a < self.selda_06_b:
            salida.append(True)
            
        if self.selda_07_a >= self.selda_07_b:
            salida.append(False)
        if self.selda_07_a < self.selda_07_b:
            salida.append(True)
            
        if self.selda_08_a >= self.selda_08_b:
            salida.append(False)
        if self.selda_08_a < self.selda_08_b:
            salida.append(True)
        
        return salida

    "______________________________"
    "______________________________"

    def valorinferior(self, back, bloque= None, selda= None):
        return self.tipo_de_comparacion(5, back, bloque, selda)

    def procesa_05(self):
        
        if self.entradas_definidas == False:
            raise EOFError("No se han establecido las seldas a filtrar (visor-vari).")
        
        salida= []
        
        if self.selda_00_a <= self.selda_00_b:
            salida.append(self.a_guardar)
        if self.selda_00_a > self.selda_00_b:
            salida.append(self.selda_00_b)
            
        if self.selda_01_a <= self.selda_01_b:
            salida.append(self.a_guardar)
        if self.selda_01_a > self.selda_01_b:
            salida.append(self.selda_01_b)
            
        if self.selda_02_a <= self.selda_02_b:
            salida.append(self.a_guardar)
        if self.selda_02_a > self.selda_02_b:
            salida.append(self.selda_02_b)
            
        if self.selda_03_a <= self.selda_03_b:
            salida.append(self.a_guardar)
        if self.selda_03_a > self.selda_03_b:
            salida.append(self.selda_03_b)
            
        if self.selda_04_a <= self.selda_04_b:
            salida.append(self.a_guardar)
        if self.selda_04_a > self.selda_04_b:
            salida.append(self.selda_04_b)
            
        if self.selda_05_a <= self.selda_05_b:
            salida.append(self.a_guardar)
        if self.selda_05_a > self.selda_05_b:
            salida.append(self.selda_05_b)
            
        if self.selda_06_a <= self.selda_06_b:
            salida.append(self.a_guardar)
        if self.selda_06_a > self.selda_06_b:
            salida.append(self.selda_06_b)
            
        if self.selda_07_a <= self.selda_07_b:
            salida.append(self.a_guardar)
        if self.selda_07_a > self.selda_07_b:
            salida.append(self.selda_07_b)
            
        if self.selda_08_a <= self.selda_08_b:
            salida.append(self.a_guardar)
        if self.selda_08_a > self.selda_08_b:
            salida.append(self.selda_08_b)
        
        return salida

    "______________________________"

    def booleaninferior(self, back, bloque= None, selda= None):
        return self.tipo_de_comparacion(6, back, bloque, selda)

    def procesa_06(self):
        
        if self.entradas_definidas == False:
            raise EOFError("No se han establecido las seldas a filtrar (visor-vari).")
        
        salida= []
        
        if self.selda_00_a <= self.selda_00_b:
            salida.append(False)
        if self.selda_00_a > self.selda_00_b:
            salida.append(True)
            
        if self.selda_01_a <= self.selda_01_b:
            salida.append(False)
        if self.selda_01_a > self.selda_01_b:
            salida.append(True)
            
        if self.selda_02_a <= self.selda_02_b:
            salida.append(False)
        if self.selda_02_a > self.selda_02_b:
            salida.append(True)
            
        if self.selda_03_a <= self.selda_03_b:
            salida.append(False)
        if self.selda_03_a > self.selda_03_b:
            salida.append(True)
            
        if self.selda_04_a <= self.selda_04_b:
            salida.append(False)
        if self.selda_04_a > self.selda_04_b:
            salida.append(True)
            
        if self.selda_05_a <= self.selda_05_b:
            salida.append(False)
        if self.selda_05_a > self.selda_05_b:
            salida.append(True)
            
        if self.selda_06_a <= self.selda_06_b:
            salida.append(False)
        if self.selda_06_a > self.selda_06_b:
            salida.append(True)
            
        if self.selda_07_a <= self.selda_07_b:
            salida.append(False)
        if self.selda_07_a > self.selda_07_b:
            salida.append(True)
            
        if self.selda_08_a <= self.selda_08_b:
            salida.append(False)
        if self.selda_08_a > self.selda_08_b:
            salida.append(True)
        
        return salida

ejecuto= Estructura()

