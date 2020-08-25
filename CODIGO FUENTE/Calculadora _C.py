import RPi.GPIO as GPIO
import math
class CalcuCientifica():
    operacion=0
    resultado=0
    def _init_(self,operacion,resultado):
        self.operacion=operacion
        self.resultado=resultado
    def menu(self):

        print("***************************Calculadora Cientifica***************************")
        print("°         Elija que tipo de operación desea realizar:                      °")
        print("°                                                                          °")
        print("°    Pin3: Operaciones Basicas     Pin5: Funciones trigonometricas         °")
        print("°    Pin7: Logaritmos              Pin8: Más                               °")
        
        selec=input("Selecione el Pin y presione OK\n")
        if GPIO.input(3) == GPIO.HIGH:
            self.basicas()
        elif GPIO.input(5) == GPIO.HIGH:
            self.trigonometricas()
        elif GPIO.input(7) == GPIO.HIGH:
            self.racExpLog()
        elif GPIO.input(8) == GPIO.HIGH:
            self.otros()
        else:
            print("Opcion no valida")
            self.menu()

#Seccion de operaciones basicas
    def basicas(self):

        print("*******************************Basicas*******************************")
        print("°     Seleccione opcion a realizar:                                 °")
        print("°                                                                   °")
        print("°  Pin3: Suma     Pin5: Resta      Pin7: Multiplicacion             °")
        print("°  Pin8: Division Pin10: Raices    Pin12: Potencia                  °")
        selec=input("Selecione el Pin y presione OK\n")
        if GPIO.input(3) == GPIO.HIGH:
            self.suma()
        elif GPIO.input(5) == GPIO.HIGH:
            self.resta()
        elif GPIO.input(7) == GPIO.HIGH:
            self.multipli()
        elif GPIO.input(8) == GPIO.HIGH:
            self.division()
        elif GPIO.input(10) == GPIO.HIGH:
            self.raices()
        elif GPIO.input(12) == GPIO.HIGH:
            self.potencia()
        else:
            print("Opcion no valida")
            self.basicas()

    def suma(self):
        print("Ingrese el primer numero")
        num1=int(input())
        print("Ingrese el número a sumar")
        num2=int(input())
        resultado=num1+num2
        print(num1,'+',num2,'=',resultado)
    def resta(self):
        print("Ingrese el primer número")
        num1=int(input())
        print("Ingrese el número a restar")
        num2=int(input())
        resultado=num1-num2
        print(num1,'-',num2,'=',resultado)
    def multipli(self):
        print("Ingrese el primer numero")
        num1=int(input())
        print("Ingrese el numero de veces a multiplicar")
        num2=int(input())
        resultado=num1*num2
        print(num1,'*',num2,'=',resultado)
    def division(self):
        print("Ingrese el dividendo")
        num1=int(input())
        print("Ingrese el divisor")
        num2=int(input())
        resultado=num1/num2
        print(num1,'/',num2,'=',resultado)

#seccion funciones trigonometricas

    def trigonometricas(self):

        print("*****************************Trigonometricas**************************")
        print("°         Seleccione tipo de funcion trigonometrica:                 °")
        print("°                                                                    °")
        print("°           Pin3: SENO     Pin5: COSENO     Pin7: TANGENTE           °") 
        print("°         Pin8: ARCOSENO Pin10: ARCOCOSENO Pin12: ARCOTANGENTE       °")
        selec=input("Selecione el Pin y presione OK\n")
        if GPIO.input(3) == GPIO.HIGH:
            self.seno()
        elif GPIO.input(5) == GPIO.HIGH:
            self.coseno()

        elif GPIO.input(7) == GPIO.HIGH:
            self.tangente()

        elif GPIO.input(8) == GPIO.HIGH:
            self.arcoseno()

        elif GPIO.input(10) == GPIO.HIGH:
            self.arcocoseno()

        elif GPIO.input(12) == GPIO.HIGH:
            self.arcotangente()

        else:
            print("Opcion no valida")
            self.trigonometricas()

    def seno(self):
        print("Seno(x)")
        print("Ingrese el valor del angulo x en radianes")
        angulo=float(input())
        resultado=math.sin(angulo)
        print("El seno de ",angulo," es: ",resultado)
    def coseno(self):
        print("Coseno(x)")
        print("Ingrese el valor del angulo x en radianes")
        angulo=float(input())
        resultado=math.cos(angulo)
        print("El coseno de ",angulo," es: ",resultado)
    def tangente(self):
        print("Tangente(x)")
        print("Ingrese el valor del angulo x en radianes")
        angulo=float(input())
        resultado=math.tan(angulo)
        print("La tangente de ",angulo," es: ",resultado)
    def arcoseno(self):
        print("ArcoSeno(x)")
        print("Ingrese el valor de x ")
        angulo=float(input())
        resultado=math.asin(angulo)
        print("El arcoseno de ",angulo," es el angulo: ",resultado," rad")
    def arcocoseno(self):
        print("ArcoCoseno(x)")
        print("Ingrese el valor de x ")
        angulo=float(input())
        resultado=math.acos(angulo)
        print("El arcocoseno de ",angulo," es el angulo: ",resultado," rad")
    def arcotangente(self):
        print("ArcoTangente(x)")
        print("Ingrese el valor de x ")
        angulo=float(input())
        resultado=math.atan(angulo)
        print("La arcotangente de ",angulo," es el angulo: ",resultado," rad")


#seccion raices exponentes y logaritmos
    def racExpLog(self):
        if 1==1:
            self.logaritmos()
        else:
            print("Opcion no valida")
            self.racExpLog()

    def raices(self):
        print("Raices")
        print("Ingrese el indice")
        indice=int(input())
        print("Ingrese el radicando")
        radicando=float(input())
        resultado=radicando**(1/indice)
        print("La respuesta de esa raiz es: ",resultado)
    def potencia(self):
        print("Potencias")
        print("Ingrese la base")
        base=float(input())
        print("Ingrese el exponente")
        exponente=int(input())
        resultado=base**exponente
        print("La respuesta de la potencia es: ",resultado)
    def logaritmos(self):

        print("***********************Logaritmos***********************")
        print("°            Seleccione el tipo de Logaritmo           °")
        print("°                                                      °")
        print("°  Pin3: Logaritmo Decimal Pin5: Logaritmo Natural     °")
        selec=input("Selecione el Pin y presione OK\n")
        if GPIO.input(3) == GPIO.HIGH:
            self.logB()
        elif GPIO.input(5) == GPIO.HIGH:
            self.logNat()
        else:
            print("Opcion no valida")
            self.logaritmos()
    def logB(self):
        print("Logaritmos decimales")
        print("Ingrese la base:")
        base=int(input())
        print("Ingrese el argumento:")
        argumento=float(input())
        resultado=math.log(argumento,base)
        print("El logaritmo base ",base," de ",argumento," es: ",resultado)

    def logNat(self):
        print("Logaritmos naturales")
        print("Ingrese el argumento")
        argumento=float(input())
        resultado=math.log(argumento,math.e)
        print("El logaritmo natural de",argumento," es: ",resultado)


#seccion de operaciones
    def otros(self):

        print("***************************Otras operaciones*************************")
        print("°              Seleccione la opcion a realizar                      °")
        print("°                                                                   °")
        print("°  Pin3:Factorial de un numero Pin5:Valor Absoluto de un numero     °")
        print("°  Pin7:Funciones Hiperbolicas                                      °")
        selec=input("Selecione el Pin y presione OK\n")
        if GPIO.input(3) == GPIO.HIGH:
            self.factorial()
        elif GPIO.input(5) == GPIO.HIGH:
            self.vabsoluto()
        elif GPIO.input(7) == GPIO.HIGH:
            self.hiperbolicas()
        else:
            print("Opcion no valida")
            self.otros()

    def factorial(self):
        print("Factorial")
        print("Ingrese el numero")
        numerof=int(input())
        resultado=math.factorial(numerof)
        print("El factorial de ",numerof," es ",resultado)

    def vabsoluto(self):
        print("Valor Absoluto")
        print("Ingrese el numero")
        numero=float(input())
        resultado=math.fabs(numero)
        print("El valor absoluto de ",numero," es ",resultado)

    def hiperbolicas(self):

        print("**************************************Funciones hiperbolicas**************************************")
        print("°                          Seleccione tipo de funcion hiperbolica:                               °")
        print("°    Pin3: SENO HIPERBOLICO     Pin5: COSENO HIPERBOLICO     Pin7: TANGENTE HIPERBOLICA          °")
        print("°    Pin8: ARCOSENO HIPERBOLICO Pin10: ARCOCOSENO HIPERBOLICO Pin12: ARCOTANGENTE HIPERBOLICA    °")
        selec=input("Selecione el Pin y presione OK\n")
        if GPIO.input(3) == GPIO.HIGH:
            self.senoh()
        elif GPIO.input(5) == GPIO.HIGH:
            self.cosenoh()

        elif GPIO.input(7) == GPIO.HIGH:
            self.tangenteh()

        elif GPIO.input(8) == GPIO.HIGH:
            self.arcosenoh()

        elif GPIO.input(10) == GPIO.HIGH:
            self.arcocosenoh()

        elif GPIO.input(12) == GPIO.HIGH:
            self.arcotangenteh()

        else:
            print("Opcion no valida")
            self.hiperbolicas()

    def senoh(self):
        print("Senh(x)")
        print("Ingrese el valor de x")
        angulo=float(input())
        resultado=math.sinh(angulo)
        print("El seno hiperbolico de ",angulo," es: ",resultado)
    def cosenoh(self):
        print("Cosh(x)")
        print("Ingrese el valor de x")
        angulo=float(input())
        resultado=math.cosh(angulo)
        print("El coseno hiperbolico de ",angulo," es: ",resultado)
    def tangenteh(self):
        print("Tanh(x)")
        print("Ingrese el valor de x")
        angulo=float(input())
        resultado=math.tanh(angulo)
        print("La tangente hiperbolica de ",angulo," es: ",resultado)
    def arcosenoh(self):
        print("ArcSenh(x)")
        print("Ingrese el valor de x ")
        angulo=float(input())
        resultado=math.asinh(angulo)
        print("El arcoseno hiperbolico de ",angulo," es: ",resultado)
    def arcocosenoh(self):
        print("ArcCosh(x)")
        print("Ingrese el valor de x ")
        angulo=float(input())
        resultado=math.acosh(angulo)
        print("El arcocoseno hiperbolico de ",angulo," es: ",resultado)
    def arcotangenteh(self):
        print("ArcTanh(x)")
        print("Ingrese el valor de x ")
        angulo=float(input())
        resultado=math.atanh(angulo)
        print("La arcotangente hiperbolica de ",angulo," es: ",resultado)


opc="S"

while opc == "S":
    while True:
        import os

        calculo=CalcuCientifica()
        selecOperacion=calculo.menu()
        opc=input("Desea realizar otra operación Si=S/No=N\n")
        opc=opc.upper()
        if opc != "S":
            print("La calculadora se a finalizado")
        break