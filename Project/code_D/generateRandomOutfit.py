
def generateRandomOutfit():
    import pandas as pd
    import random

    df_clothes = pd.read_csv('product_data.csv')
    df_outfits = pd.read_csv('outfit_data.csv')
    df1=df_clothes

    df_acc=df1[df_clothes['des_product_category']=='Accesories, Swim and Intimate']
    df_bea=df1[df_clothes['des_product_category']=='Beauty']
    df_bot=df1[df_clothes['des_product_category']=='Bottoms']
    df_DJC=df1[df_clothes['des_product_category']=='Dresses, jumpsuits and Complete set']
    df_hom=df1[df_clothes['des_product_category']=='Home']
    #df_out=df1[df_clothes['des_product_category']=='Outwear']
    df_top=df1[df_clothes['des_product_category']=='Tops']


    outfit=[]
    if random.random()<0.5 :
        a = random.randint(1,len(df_acc)-1)
        outfit.append(df_acc.iloc[a]['cod_modelo_color'])
    if random.random()<0.5 :
        a = random.randint(1,len(df_bea)-1)
        outfit.append(df_bea.iloc[a]['cod_modelo_color'])
    if random.random()<0.5 :
        a = random.randint(1,len(df_bot)-1)
        outfit.append(df_bot.iloc[a]['cod_modelo_color'])
    if random.random()<0.5 :
        a = random.randint(1,len(df_DJC)-1)
        outfit.append(df_DJC.iloc[a]['cod_modelo_color'])
    if random.random()<0.5 :
        a = random.randint(1,len(df_hom)-1)
        outfit.append(df_hom.iloc[a]['cod_modelo_color'])
    if random.random()<0.5 :
        a = random.randint(1,len(df_top)-1)
        outfit.append(df_top.iloc[a]['cod_modelo_color'])

    return outfit
