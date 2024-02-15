import os

def ram_usage():
    print("""
***********************************************************
                    Memoria RAM
***********************************************************
    """)
    while True:
        respuesta = input("""
(I)nformacion de la memoria Real
(M)ostrar la informacion de la memoria cache
(E)liminar la memoria cache
(S)alir
        ---->   """)
        if respuesta.upper() == "I":
            os.system('cat /proc/meminfo | grep "Mem" && cat /proc/meminfo | grep "Cache"')
        elif respuesta.upper() == "M":
            os.system("sudo free -m \"caché\" | awk '{print $5}' && echo $(sudo free -m |grep \"Mem\" | awk '{print$6}') \"Mb\"")
        elif respuesta.upper() == "E":
            os.system("sudo sync && sudo sysctl vm.drop_caches=1")
            print("Caché eliminado")
        elif respuesta.upper() == "S":
            return
        else:
            print("Opcion Incorrecta")

def vram_usage():
    while True:
        response = input("""
    (I)nformacion de la memoria Virtual
    (S)alir
    Ingresa una opcion  """)
        if response.upper() == "I":
            rawData = os.system('cat /proc/meminfo | grep "Swap"')
            print(rawData)
        elif response.upper() == "S":
            return
        else:
            print("Opcion Incorrecta")

def iout_options():
    while True:
        respuesta = input("""
(L)ista
(D)esmontar Discos
(S)alir
        ---->        """)
        if respuesta.upper() == "L":
            os.system('lsblk -o NAME,TYPE,SIZE,VERSION,MOUNTPOINT | grep "sd"')
        elif respuesta.upper() == "D":
            os.system('lsblk -o NAME,TYPE,SIZE,VERSION,MOUNTPOINT | grep "sd"')
            disco = input("Escribe el nombre del disco a desmontar (ej.) sda o sd: ")
            os.system(f"sudo eject /dev/{disco}")
        elif respuesta.upper() == "S":
            return
        else:
            print("Opcion Incorrecta")
