#Youtube Downloader (Audio & Video)

from pytube import YouTube

while True:
    print('''
Menú:
1 para Descargar.
2 para Salir
''')
    try:
        opcion = int(input("¿Que desea realizar? "))
                
    except:
            print("ERROR! Ingrese el dato como se pide....")
    
    else:
        if opcion == 1:
            print("Ingrese la URL del vídeo que quiere descargar: ")
            url = input('url: ')
            yt = YouTube(url) #Youtube Object
            path = r"C:\Users\MBayo\Downloads" #ubicación de la descarga

            #Información del vídeo a descargar
            print("\nTitulo:",yt.title)
            print("Autor:",yt.author)
            seg = yt.length
            min = seg // 60
            hrs = min // 60
            print(f"Duracion: {int(hrs)}:{int(min)}:{int(seg)}")

            #Proceso de descarga:

            print("Descargando vídeo....")
            try: 
                descarga_video = yt.streams.first().download(path)
                print(descarga_video)
                print("Descargado con Éxito! :D")

            except:
                print('ERROR! Ha ocurrido un error en la descarga. Intente de nuevo... :(')

        elif opcion == 2:
            break
        else:
            print("ERROR! Ingrese el dato como se pide....")
            

