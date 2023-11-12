import pandas as pd
import random
import numpy as np

#ejecutar con i=0
def generateCoherentOutfit(item,df_clothes, df_outfits,i):
    alpha=1
    NN=5
    df_param=df_clothes[df_clothes['cod_modelo_color']==item]

    #----------------------------------------------millorable-----------------------------------
    #1r conjunt de vehins
    df_out1=df_outfits[ df_outfits['cod_modelo_color']==item]
    df_items1=df_outfits[ df_outfits['cod_outfit'].isin( df_out1['cod_outfit'] ) ]
    #2n conjunt de vehins
    df_out2=df_outfits[ df_outfits['cod_modelo_color'].isin( df_items1['cod_modelo_color'] ) ]
    df_items2=df_outfits[ df_outfits['cod_outfit'].isin( df_out2['cod_outfit'] ) ]
    #--------------------------------------------------------------------------------------------
    df0=df_clothes[ df_clothes['cod_modelo_color'].isin( df_items2['cod_modelo_color']) ]


    #1 filtro tontorron x eliminar peces d'altres estils(---cal_fer-ho_en_funcio_del_item)
    df1 = df0[(df0['des_sex']==df_param['des_sex'].iloc[0]) & (df0['des_age']==df_param['des_age'].iloc[0]) & (df0['des_product_family']!=df_param['des_product_family'].iloc[0]) & (df0['des_product_type']!=df_param['des_product_type'].iloc[0]) ]

    #trec frequencies de cada un
    df_FREQ_peces=df_outfits.groupby("cod_modelo_color").agg(frequency=("cod_modelo_color", "count"))

    #segmento
    df_acc=df1[df_clothes['des_product_category']=='Accesories, Swim and Intimate']
    df_bea=df1[df_clothes['des_product_category']=='Beauty']
    df_bot=df1[df_clothes['des_product_category']=='Bottoms']
    df_DJC=df1[df_clothes['des_product_category']=='Dresses, jumpsuits and Complete set']
    df_hom=df1[df_clothes['des_product_category']=='Home']
    df_out=df1[df_clothes['des_product_category']=='Outerwear']
    df_top=df1[df_clothes['des_product_category']=='Tops']


    merged_data = pd.merge(df_FREQ_peces, df_acc, on='cod_modelo_color', how='right')
    f_acc = merged_data['frequency'].sum()
    merged_data = pd.merge(df_FREQ_peces, df_bea, on='cod_modelo_color', how='right')
    f_bea = merged_data['frequency'].sum()
    merged_data = pd.merge(df_FREQ_peces, df_bot, on='cod_modelo_color', how='right')
    f_bot = merged_data['frequency'].sum()
    merged_data = pd.merge(df_FREQ_peces, df_DJC, on='cod_modelo_color', how='right')
    f_DJC = merged_data['frequency'].sum()
    merged_data = pd.merge(df_FREQ_peces, df_hom, on='cod_modelo_color', how='right')
    f_hom = merged_data['frequency'].sum()
    merged_data = pd.merge(df_FREQ_peces, df_out, on='cod_modelo_color', how='right')
    f_out = merged_data['frequency'].sum()
    merged_data = pd.merge(df_FREQ_peces, df_top, on='cod_modelo_color', how='right')
    f_top = merged_data['frequency'].sum()
    f_TOT=sum([f_acc,f_bea,f_bot,f_DJC,f_hom])

    f_acc=f_acc/f_TOT
    f_bea=f_bea/f_TOT
    f_bot=f_bot/f_TOT
    f_DJC=f_DJC/f_TOT
    f_hom=f_hom/f_TOT
    f_out=f_out/f_TOT
    f_top=f_top/f_TOT


    [f_acc,f_bea,f_bot,f_DJC,f_hom]=[alpha*f_acc,alpha*f_bea,alpha*f_bot,alpha*f_DJC,alpha*f_hom]

    #clasifica los elementso seleccionados
    df1_acc=df1[df1['des_product_category']=='Accesories, Swim and Intimate']
    df1_bea=df1[df1['des_product_category']=='Beauty']
    df1_bot=df1[df1['des_product_category']=='Bottoms']
    df1_DJC=df1[df1['des_product_category']=='Dresses, jumpsuits and Complete set']
    df1_hom=df1[df1['des_product_category']=='Home']
    df1_out=df1[df1['des_product_category']=='Outerwear']
    df1_top=df1[df1['des_product_category']=='Tops']

    outfit=[]
    for ii in range(NN):
        if random.random()<f_acc :
            a = random.randint(1,len(df1_acc)-1)
            outfit.append(df1_acc.iloc[a]['cod_modelo_color'])
        if random.random()<f_bea :
            a = random.randint(1,len(df1_bea)-1)
            outfit.append(df1_bea.iloc[a]['cod_modelo_color'])
        if random.random()<f_bot :
            a = random.randint(1,len(df1_bot)-1)
            outfit.append(df1_bot.iloc[a]['cod_modelo_color'])
        if random.random()<f_DJC :
            a = random.randint(1,len(df1_DJC)-1)
            outfit.append(df1_DJC.iloc[a]['cod_modelo_color'])
        if random.random()<f_hom :
            a = random.randint(1,len(df1_hom)-1)
            outfit.append(df1_hom.iloc[a]['cod_modelo_color'])
        if random.random()<f_out :
            a = random.randint(1,len(df1_out)-1)
            outfit.append(df1_out.iloc[a]['cod_modelo_color'])
        if random.random()<f_top :
            a = random.randint(1,len(df1_top)-1)
            outfit.append(df1_top.iloc[a]['cod_modelo_color'])

    #return outfit
    V=None
    L= len(outfit)    
    if L<2 or L>20:
        V=False
    else:
        V = True

    if V:
        return outfit
    elif i>100:
        return 'Error'
    else:
        i+=1
        return generateCoherentOutfit(item,df_clothes, df_outfits, i)


df_clothes = pd.read_csv('product_data.csv')
df_outfits = pd.read_csv('outfit_data.csv')


item='53030594-08' #peça de roba
n=10 #<-----------numero de outfits
cod_outfit=[]
prendas_ids=[]

for i in range(10):
    cods_prendas=generateCoherentOutfit(item,df_clothes, df_outfits,i=1)
    cod_outfit.append(7900+i)
    prendas_ids.append(cods_prendas)

print(cod_outfit)
print(prendas_ids)




