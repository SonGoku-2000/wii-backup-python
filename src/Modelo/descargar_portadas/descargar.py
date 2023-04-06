import urllib.request
from pathlib import Path


def descargarGametdb(ID, directorio, tipo, tamano:str = '', consola:str = 'wii', extension:str = 'png'):
    region = ''
    if consola in ('wii','ds','3ds','wiiu'):
        regiones = {'E': 'US',
                    'J': 'JA',
                    'K': 'KO',
                    'R': 'RU',
                    'W': 'ZH',
                    # = EN as default + FR, DE, ES, IT, NL, PT, NO, DK, FI, SE, AU, TR, other
                    'P': 'EN', 
                    'D': 'EN', 
                    'F': 'EN', 
                    'I': 'EN', 
                    'S': 'EN', 
                    'H': 'EN', 
                    'X': 'EN', 
                    'Y': 'EN', 
                    'Z': 'EN'
                    }
        
        region = regiones[ID[3]]
    URL = f'https://art.gametdb.com/{consola}/{tipo}{tamano}/{region}/{ID}.{extension}'
    with(open(f'{directorio}/{ID}.png', 'wb')) as f:
        print(f'Descargando {tipo}...')
        f.write(urllib.request.urlopen(URL).read())  # 'http:art.gametdb.com/wii/cover/US/RUUE01.png').read())
    print(f'Descargado {tipo}')
    print("---------------------")

def descargar2D(ID:str = 'RUUE01',dirBase:str = ''):
    'cover'
    dir2d = Path(dirBase).joinpath('usb-loader/covers/2d')
    dir2d.mkdir(parents=True,exist_ok=True)
    descargarGametdb(ID, dir2d.__str__(), 'cover')

def descargar3D(ID: str = 'RUUE01', dirBase: str = ''):
    '3d'
    dir2d = Path(dirBase).joinpath('usb-loader/covers/3d')
    dir2d.mkdir(parents=True,exist_ok=True)
    descargarGametdb(ID, dir2d.__str__(), 'cover3D')

def descargarCD(ID: str = 'RUUE01', dirBase: str = ''):
    'disc'
    dir2d = Path(dirBase).joinpath('usb-loader/covers/disc')
    dir2d.mkdir(parents=True, exist_ok=True)
    descargarGametdb(ID, dir2d.__str__(), 'disc')

def descargarCoverFull(ID: str = 'RUUE01', dirBase: str = ''):
    'full'
    dir2d = Path(dirBase).joinpath('usb-loader/covers/full')
    dir2d.mkdir(parents=True, exist_ok=True)
    descargarGametdb(ID, dir2d.__str__(), 'coverfullHQ')

if __name__ == '__main__':
    descargarCoverFull()
