import argparse as ap
from functions import ram_usage, vram_usage, iout_options

def run():#python3 main.py -r para ejecutarlo
    parser = ap.ArgumentParser(description="Aplicacion para manipular los datos de la memoria en linux")
    parser.add_argument("-r", "--ram", action="store_true", help="Acceder a las funciones de la memoria RAM")
    parser.add_argument("-v", "--vram", action="store_true", help="Acceder a la funcion de la memoria Virtual")
    parser.add_argument("-d", "--device", action="store_true", help="Acceder a las funciones de la administracion de discos")
    parser.add_argument("-m", "--manual", action="store_true", help="Ayuda a las aplicaciones")
    
    args = parser.parse_args()
    
    if args.ram:
        ram_usage()
    elif args.vram:
        vram_usage()
    elif args.device:
        iout_options()
    else:
        print("""
[args]

args:

-r --ram            Acceder a las opciones de la memoria RAM
-v --vram           Acceder a las opciones de la memoria Virtual
-d --device         Acceder a las opciones de discos montados en linux
        """)
    
if __name__ == '__main__':
    run()
