import reads
num_gate = 2
in_gate = 0 #Inicialmente la puerta está cerrada



def access():
    dni = input('Ingrese DNI: ') #Esto puede ser reemplazado por un sensor
    reserve = reads.dni_read(dni)
    if reserve == [0,0] and reads.search(dni) == False: 
        print("Ingrese un DNI correcto \n\n")
        access()
    
    elif reserve == [0,0] and reads.search(dni) == True:
        _action = input('Ingresa S o N para definir si quieres reservar ahora: \n ')
        if _action == 'S':
            access_val = reads.reservation_now()[1] 
            gate = reads.reservation_now()[0]
            return [access_val, gate]
        else:
            access()
   
    else: 
        access_val = reserve[0]
        gate = reserve[1]
        print("\nSí tiene reserva")
        print(f"Ha reservado la cancha {gate}")
        print(f"Espere... \nabriendo la cancha {gate} \n\n")
        access()
    return [access_val, gate]   #Puerta a abrir
        

def save():
    print("Guardando... \n\n")
    return save
