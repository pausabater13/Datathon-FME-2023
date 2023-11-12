import pandas as pd

# Cargar el DataFrame de outfits desde el archivo CSV
datos_outfits = pd.read_csv("outfits_data.csv", names=['cod_outfit', 'cod_modelo_color'])

# Agrupar por el código de outfit y obtener una lista de códigos de modelo de color
datos_outfits_agrupados = datos_outfits.groupby('cod_outfit')['cod_modelo_color'].apply(list).reset_index()

# Crear el DataFrame final
datos_outfits_final = pd.DataFrame({
    'cod_outfit': datos_outfits_agrupados['cod_outfit'],
    'cod_modelo_color': datos_outfits_agrupados['cod_modelo_color']
})

# Imprimir el DataFrame final
print("Datos de Outfits:")
print(datos_outfits_final)
