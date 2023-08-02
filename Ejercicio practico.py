#Compañia multinacional rappi
print("==============================")
print("=        Aplicacion          =")
print("=    Sistema Vacacional      =")
print("=          Rappi             =")
print("============================== \n")

print("Departamento de Atención al cliente.(Clave 1)")
print("Departamento de Logística.(Clave 2)")
print("Gerencia.(Clave 3)")

nombre = input("\n Por favor introduzca un nombre: ")    
Clave = int(input("\n Introduzca Clave de departamento: "))
            
if Clave == 1:
    vacaciones = float(input ("\n introduzca '1 a 7' años para sus vacaciones: "))
    print("\n Bienvenido")
    if vacaciones == 1:
        print("\n El empleado", nombre, "dispone de 6 dias de vacaciones")
        print("\n Fin.")
    elif vacaciones > 1 and vacaciones < 7:
        print("\n El empleado", nombre," dispone de 14 dias de vacaciones")
        print("\n Fin.")
    elif vacaciones >=7:
        print("\n El empleado", nombre, " dispone de 20 dias de vacaciones")
        print("\n Fin.")
    elif vacaciones == 0:
        print("\n El empleado", nombre,"Sin derecho a vacaciones")
        print("\n Fin.")
        
elif Clave == 2:
    vacaciones = float(input ("\n introduzca '1 a 7' años para sus vacaciones: "))
    print("\n Bienvenido" )
    if vacaciones == 1:
        print("\n El empleado",nombre," dispone de 7 dias de vacaciones")
        print("\n Fin.")
    elif vacaciones > 1 and vacaciones <7:
        print("\n El empleado",nombre," dispone de 15 dias de vacaciones")
        print("\n Fin.")
    elif vacaciones >= 7:
        print("\n El empleado", nombre, "dispone de 22 dias de vacaciones")
        print("\n Fin.")
    elif vacaciones == 0:
        print("\n El empleado", nombre, "Sin derecho a vacaciones")
        print("\n Fin.")

elif Clave == 3:
    vacaciones = float(input ("\n introduzca '1 a 7' años para sus vacaciones: "))
    print("\n Bienvenido" )
    if vacaciones == 1:
        print("\n El empleado", nombre, " dispone de 10 dias de vacaciones")
        print("\n Fin.")
    elif vacaciones > 1 and vacaciones < 7:
        print("\n El empleado",nombre ,"dispone de 20 dias de vacaciones")
        print("\n Fin.")
    elif vacaciones >= 7:
        print("\n El empleado",nombre," dispone de 30 dias de vacaciones")
        print("\n Fin.")
    elif vacaciones == 0:
        print("\n El empleado",nombre,"derecho a vacaciones")
        print("\n Fin.")

else:
    print("\n Su contraseña no existe")


#Alternativa
""" if vacaciones == 1 and vacaciones menor q 2:
    2 and menor igual q 6:
    vacaciones mayor igual q 7"""
        
 




    

    
    












