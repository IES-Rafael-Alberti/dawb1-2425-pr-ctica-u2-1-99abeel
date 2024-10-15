
COMANDOS = ["compra", "venta", "saldo", "reset", "fin"]
MENSAJE_ERROR = "*ERROR* Entrada inválida"


def comprobar_importe(valor: str) -> bool:
    if valor.startswith("-"):
        valor = valor [1:]

    return valor.isdigit()
    


def comprobar_comando(comando: str) -> bool:
    comando = ["compra", "venta", "saldo", "reset", "fin"]
    if comando in (comando):
        comando = True
        return (comando)
    else:
        comando = False
        return (comando)

def mostrar_mensaje_error():
cont_compras = 0 
cont_ventas = 0 
    if cont_compras + cont_ventas == ""
        print("*ERROR* Entrada inválida")

    """
    Muestra el mensaje de error por entrada inválida.
    """


def procesar_compra(saldo: float, importe: float) -> float:
    saldo = saldo - importe
    return(saldo)
   


def procesar_venta(saldo: float, importe: float) -> float:
    saldo = saldo + importe
    return(saldo)


def mostrar_saldo(saldo: float, cont_compras: int, cont_ventas: int):
    saldo = 0
    print("El saldo actual es", saldo, ("("), cont_compras("compras y"), cont_ventas,("ventas)"))
    """
    Muestra el saldo actual junto con el número de compras y ventas.

    Args:
        saldo (float): El saldo actual.
        cont_compras (int): Número total de compras realizadas.
        cont_ventas (int): Número total de ventas realizadas.
    """


def resetear_saldo(saldo: float, cont_compras: int, cont_ventas: int) -> tuple[float, int, int]:
    print(f"El saldo actual es = {saldo}  ({cont_compras} compras y {cont_ventas} ventas)")


def recuperar_comando_e_importe(linea: str) -> tuple[str, str]:
    """
    Recupera el comando y, si lo hay, el importe de una línea de entrada.
    
    Args:
        linea (str): Línea de texto introducida por el usuario.

    Returns:
        tuple: El comando (str o  None) y el importe (str o None).
    
    Ejemplos:
        >>> recuperar_comando_e_importe("compra 100")
        ('compra', '100')
        
        >>> recuperar_comando_e_importe("saldo")
        ('saldo', None)

        >>> recuperar_comando_e_importe("")
        (None, None)        
    """
    lista_palabras = linea.split()

    if len(lista_palabras) == 1:
        return lista_palabras[0], None
    elif len(lista_palabras) == 2:
        return lista_palabras[0], lista_palabras[1]
    else:
        return None, None


def main():
    """
    Función principal que gestiona el flujo del programa. El programa permite al usuario realizar
    operaciones de compra y venta, consultar el saldo, restablecer las operaciones y finalizar.

    Funciona a través de un bucle que sigue las instrucciones del usuario hasta que el comando "fin" es ingresado.
    El saldo y las transacciones se actualizan según los comandos introducidos.

    Comandos disponibles:
        - compra [importe]: Resta el importe del saldo.
        - venta [importe]: Suma el importe al saldo.
        - saldo: Muestra el saldo actual junto con el número de compras y ventas.
        - reset: Restablece el saldo y las transacciones a cero.
        - fin: Termina el programa.
    
    Ejemplos:
        > compra 100
        > venta 50
        > venta
        *ERROR* Entrada inválida
        > venta cincuenta euros
        *ERROR* Entrada inválida
        > compra 50€
        *ERROR* Entrada inválida
        > saldo 666
        *ERROR* Entrada inválida
        > saldo
        Saldo actual = -50.00 (1 compras y 1 ventas)
        > venta 200
        > reset
        Saldo anterior = 150.00 (1 compras y 2 ventas)
        > saldo
        Saldo actual = 0.00 (0 compras y 0 ventas)
        > fin
    """
    encuentra_fin = False
    cont_compras = 0
    cont_ventas = 0
    saldo = 0

    while not encuentra_fin:

        comando, importe = recuperar_comando_e_importe(linea)

        if comando is None or not comprobar_comando(comando):
            mostrar_mensaje_error()
        elif comando in ("saldo", "reset", "fin") and importe is not None:
            
        elif comando == "saldo":
            
        elif comando == "reset":
            
        elif comando == "fin":
            
        elif importe is None or not comprobar_importe(importe):
            
        else:

            if comando == "compra":

            elif comando == "venta":


            
if __name__ == "__main__":
    main()
