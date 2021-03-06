import json


def obtener_combinaciones():
    with open("../Archivos_JSON/palabras_ciberseguridad.json", "r") as filtros_file:
        diccionario_filtros_fintech = json.load(filtros_file)
        listado_palabras = diccionario_filtros_fintech["palabras"]
    lista_combinaciones = list()
    for dict_palabra in listado_palabras:
        palabra = dict_palabra["palabra"]
        lista_combinaciones.append([palabra])
        for dict_palabra2 in listado_palabras:
            if dict_palabra2["palabra"] != palabra:
                if [palabra, dict_palabra2["palabra"]] in lista_combinaciones or [dict_palabra2["palabra"], palabra] in lista_combinaciones:
                    continue
                else:
                    lista_combinaciones.append([palabra, dict_palabra2["palabra"]])
    diccionario_nuevo_json = {"combinaciones": lista_combinaciones}
    with open("../Archivos_JSON/combinaciones_palabras.json", "w") as combinaciones_file:
        json.dump(diccionario_nuevo_json, combinaciones_file)

if __name__ == '__main__':
    obtener_combinaciones()