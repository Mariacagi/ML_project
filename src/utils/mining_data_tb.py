#FUNCIÓN PARA AÑADIR DOBLE BARRA A UNA RUTA

def funcion_para_añadir_una_barra(string):
    result = string.replace("\\", r"\\")
    print(result)
    return result


#FUNCIÓN PARA SEPARAR UNA COLUMNA EN DOS
def split_columna(df, columna, objeto_separacion, numero_veces):
    separado = df[columna].str.split(objeto_separacion, n=numero_veces, expand=True)
    return separado


#FUNCIÓN PARA SEPARAR UNA COLUMNA CON NAN VALUES
def split_columna_con_nan(x):
  try: 
    return(x.split("/")[-1])
  except:
    return("Ninguna")