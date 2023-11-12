import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler








# Cargar el DataFrame de prendas desde el archivo CSV
datos_prendas = pd.read_csv("prendas_data.csv")
datos_prendas = datos_prendas[['cod_modelo_color', 'cod_color_code', 'des_color_specification_esp', 'des_agrup_color_eng', 'des_sex', 'des_age', 'des_line', 'des_fabric', 'des_product_category', 'des_product_aggregated_family', 'des_product_family','des_product_type' ]]
# Imprimir los DataFrames
print("Datos de Prendas:")
print(datos_prendas)







datos_outfits = pd.read_csv("outfits_data.csv", names=['cod_outfit', 'cod_modelo_color'])

# Agrupar por el código de outfit y obtener una lista de códigos de modelo de color
datos_outfits_agrupados = datos_outfits.groupby('cod_outfit')['cod_modelo_color'].apply(list).reset_index()

# Crear el DataFrame final
datos_outfits_final = pd.DataFrame({
    'cod_outfit': datos_outfits_agrupados['cod_outfit'],
    'cod_modelo_color': datos_outfits_agrupados['cod_modelo_color']
})
datos_outfits_final.rename(columns={'cod_modelo_color': 'prenda_ids'}, inplace=True)
# Imprimir el DataFrame final
print("Datos de Outfits:")
print(datos_outfits_final)


datos_outfits= datos_outfits_final

















# Expandir la lista en 'prenda_ids'
datos_outfits_expandidos = datos_outfits.explode('prenda_ids')



# Realizar la fusión
datos_combinados = pd.merge(datos_outfits_expandidos, datos_prendas, left_on='prenda_ids', right_on='cod_modelo_color', how='inner')

# Separar características (X)
X = datos_combinados[['cod_color_code', 'cod_color_code', 'des_color_specification_esp', 'des_agrup_color_eng','des_sex', 'des_age', 'des_line', 'des_fabric', 'des_product_category', 'des_product_aggregated_family', 'des_product_family', 'des_product_type']]

# Codificación one-hot para variables categóricas
X = pd.get_dummies(X)

# Normalizar las características
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Construir el modelo
model = Sequential()
model.add(Dense(64, activation='relu', input_shape=(X.shape[1],)))
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compilar el modelo
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Todas las combinaciones son exitosas, asumimos que todas las predicciones serán cercanas a 1
y = np.array([1] * len(X))  # Convertir la lista a un array NumPy

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar el modelo
model.fit(X_train, y_train, epochs=10, batch_size=10, validation_data=(X_test, y_test))

# Evaluar el rendimiento del modelo en el conjunto de prueba
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Accuracy: {accuracy:.2f}')

# Predecir las etiquetas para el conjunto de prueba
predicciones = model.predict(X_test)

# Imprimir outfits y predicciones
outfits_predichos = pd.DataFrame({
    'outfit_id': range(len(X_test)),  # Crear un rango de índices
    'prediccion': predicciones.flatten()
})

print("Outfits y sus predicciones:")
print(outfits_predichos)






















import pandas as pd
import numpy as np

# Generar datos aleatorios para prueba
np.random.seed(42)  # Para reproducibilidad
num_outfits = 100
prenda_ids_aleatorios = [np.random.choice(datos_prendas['cod_modelo_color'], size=np.random.randint(1, 4), replace=False) for _ in range(num_outfits)]

datos_prueba = pd.DataFrame({
    'outfit_id': range(1, num_outfits + 1),
    'prenda_ids': prenda_ids_aleatorios
})
print(datos_prueba)
# Expandir la lista en 'prenda_ids'
datos_prueba_expandidos = datos_prueba.explode('prenda_ids')

# Realizar la fusión con los datos reales de prendas
datos_prueba_combinados = pd.merge(datos_prueba_expandidos, datos_prendas, left_on='prenda_ids', right_on='cod_modelo_color', how='inner')

# Separar características (X)
X_prueba = datos_prueba_combinados[['cod_color_code', 'cod_color_code', 'des_color_specification_esp', 'des_agrup_color_eng','des_sex', 'des_age', 'des_line', 'des_fabric', 'des_product_category', 'des_product_aggregated_family', 'des_product_family', 'des_product_type']]

# Codificación one-hot para variables categóricas
X_prueba = pd.get_dummies(X_prueba)

# Normalizar las características
X_prueba = scaler.transform(X_prueba)

# Predecir las etiquetas para el conjunto de prueba aleatorio
predicciones_prueba = model.predict(X_prueba)
print(predicciones_prueba)
# Imprimir outfits generados aleatoriamente y sus predicciones
outfits_aleatorios_predichos = pd.DataFrame({
    'outfit_id': datos_prueba_combinados['outfit_id'],
    'prediccion': predicciones_prueba.flatten()
})

print("Outfits aleatorios y sus predicciones:")
print(outfits_aleatorios_predichos)


















