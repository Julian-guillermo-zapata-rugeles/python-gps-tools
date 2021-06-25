import folium


"""


        Desarollado por Julian Guillermo Zapata Rugeles 2020
                        licencia GPL V3
                    Licencia pública de GNU
Este código puede ser modificado , compartido y distribuido bajo
la licencia publica de Gnu v3, las librias aquí inscritas pueden
  contener derechos, es conveniente revisar licencia folium
 cualquier alusión a folium y agradecimientos a sus creadores.
El script fue realizado por Julian Guillermo Zapata Rugeles y NO
es necesario autorización previa para su uso. solo distribuyelo
            bajo software libre utíl para todos.


Este script utiliza la librería folium para graficar puntos en mapa
los datos previamente exportados corresponden a latitud y longitud
del script gps.

para instalar la librería folium use: sudo pip3 install folium (gnu/linux)



llamado a set_point    50,  [5.95971778,-75.73417013] , "Blue" , False
                      radio         coordenadas          color   relleno
radio = se generará un color_circulo de radio 50 (o el numero que se le pase )
        en base a las coordenadas latitud y longitud dadas.
coordenadas = [latitud,longitud] debe ser una lista
color = establece el color del color_circulo generado con radio -> radio en color RGB #HTML
relleno = False o True para relleno

"""



class GpsManager():

    def __init__(self):
        self.modo = "Stamen Terrain"
        self.modos_disponibles = ["Stamen Terrain"]


    def info(self):
        #print(open("ayuda.txt").read())
        print("documentacion en proceso")

    def graficar_pares(self, vector_pares_latitud_longitud , ruta_salida ):
        # este método debe recibir una lista de pares coordenadas de la siguiente manera
        # [ [latitud1,longitud]  [latitud,longitud] [n latitud , n longitud ] ... ... ]
        # la lista será procesada y se generará como salida un Archivo de tipo html
        # que contendrá las latitudes y longitudes en un mapa
        print("[Procesando]")
        iterator = 0
        try:
            for pares_ordenados in vector_pares_latitud_longitud:
                latitud  = pares_ordenados[0]
                longitud = pares_ordenados[1]
                if iterator==0:
                    map=folium.Map(
                    location=[float(latitud),float(longitud)],
                    tiles= self.modo, # modo por defecto
                    zoom_start=10 )
                    iterator=iterator+1
                else:
                    print("añadiendo punto ",latitud,longitud)
                    folium.Circle(
                        radius=3,
                        location=[float(latitud),float(longitud)],
                        popup=str(iterator),
                        color="red",
                        fill=True,
                        fill_color="red"
                        ).add_to(map)
                iterator+=1
            # se guarda el mapa con el nombre solicitado por el usuario
            map.save(ruta_salida)

        # -----------------------------------------------------------------------------
        #   exepción del error generado en try :
        #            se muestra informacion de un posible error en el manejo
        #            de la estructura y se da informacion del error especifico


        except Exception as e:
            mensaje = """
+-------------------------------------------------------------------------+
[INFORMACION DE USO]

    Ocurrió un error mientras se graficaban los pares ordenados
    Verifique que el valor enviado tenga la siguiente estructura :

    <list> o <tuple>
        [[latitud1,longitud],[latitud,longitud],[latitud,longitud ]]

    ejemplo:
        [[-5.1121212,5.322323] , [-5.1212131,5.3121212] .. etc ]

        NOTA:
        los valores de latitud y longitud pueden ser numeros flotantes
        o cadenas alfanuméricas que puedan convertirse a travéz de
        float()

+-------------------------------------------------------------------------+
Adicionalmente se presenta más INFORMACION del error """
            print(mensaje)
            print(e)
