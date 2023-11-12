import pandas as pd
import numpy as np
import random
import joblib
from sklearn.tree import DecisionTreeClassifier

MyOutfitData = pd.read_csv("../../datathon-2023-fashion-compatibility-main/datathon/dataset/outfit_data.csv")
MyProductData = pd.read_csv("../../datathon-2023-fashion-compatibility-main/datathon/dataset/product_data.csv")
MyProductData.head()

des_color_specification_esp = ["AGUA","AMARILLO","AMARILLO FLUOR","AMARILLO PASTEL","ANTRACITA","ARENA","ASFALTO","AZUL","AZUL NOCHE","BEIGE","BERMELLON","BILLAR","BLANCO","BLEACH","BLOOD","BLUEBLACK","BOTELLA","BURDEOS","CALDERO","CAMEL","CANELA","CARAMELO","CAZA","CELESTE","CENIZA","CEREZA","CHICLE","CHOCOLATE","CIRUELA","COBRE","COFFEE","COGNAC","CORAL","CRUDO","CUERO","CURRY","DIRTY","DIRTY CLARO","DIRTY OSCURO","ELECTRICO","ESMERALDA","FRESA","FUCSIA","GERANIO","GRANATE","GRIS","GRIS CLARO VIGORE","GRIS MEDIO VIGORE","GRIS OSCURO VIGORE","GUNMETAL","HIELO","INDIGO","KHAKI","LILA","LIMA","MALVA","MANDARINA","MANZANA","MARFIL","MARINO","MARRON","MENTA","MISTERIO","MORADO","MOSTAZA","MUSGO","NARANJA","NARANJA PASTEL","NAVY","NEGRO","NUDE","OCRE","OFFWHITE","OLIVA","ORO","PEACH","PERLA","PETROLEO","PIEDRA","PIMENTON","PLATA","PORCELANA","PRUSIA","ROJO","ROSA","ROSA FLUOR","ROSA LIGHT","ROSA PALO","ROSA PASTEL","SALMON","TABACO","TAUPE","TEJANO CLARO","TEJANO GRIS","TEJANO GRIS CLARO","TEJANO GRIS OSCURO","TEJANO MEDIO","TEJANO NEGRO","TEJANO OSCURO","TEJANO SOFT","TERRACOTA","TINTA","TOPO","TURQUESA","VAINILLA","VERDE","VERDE PASTEL","VINO","VIOLETA","VISON"]
des_agrup_color_eng = ["BLUE","BROWN","GREEN","GREY","ORANGE","PINK","PURPLE","RED","WHITE","YELLOW"]
des_sex = ["Female","Male","Unisex"]
des_age = ["Adult","Kids"]
des_line = ["HE","HOME","KIDS","SHE","VIOLETA"]
des_fabric = ["C-COMPLEMENTOS","J-JEANS","K-CIRCULAR","L-PIEL","O-POLIPIEL","P-PLANA","T-TRICOT"]
des_product_category = ["Accesories, Swim and Intimate","Beauty","Bottoms","Dresses, jumpsuits and Complete set","Home","Outerwear","Tops"]
des_product_aggregated_family = ["Accessories","Bedroom","Coats and Parkas","Decor","Dinning Room","Dresses and jumpsuits","Fragance","Jackets and Blazers","Jeans","Shirts","Skirts and shorts","Sweaters and Cardigans","Swim and intimate","T-shirts","Tops","Trousers & leggings"]
des_product_family = ["Bags","Bedding","Belts and Ties","Blazers","Bodysuits","Cardigans","Coats","Deco Accessories","Deco Textiles","Dresses","Footwear","Fragances","Gadgets","Glasses","Glassware","Hats, scarves and gloves","Intimate","Jackets","Jeans","Jewellery","Jumpsuit","Leather jackets","Leggings and joggers","Outer Vest","Parkas","Poloshirts","Puffer coats","Shirt","Shorts","Skirts","Sweater","Sweatshirts","Swimwear","T-shirt","Tops","Trenchcoats","Trousers","Vest","Wallets & cases"]
des_product_type = ["Ankle Boots","Backpack","Basket","Beach Towel","Beanie","Bed Cushion Case","Bedspread","Belt","Belt bag","Bermudas","Bikini pantie","Bikini top","Blazer","Blouse","Bodymist","Bodysuit","Boots","Box","Bracelet","Braces","Bras","Bucket bag","Candle","Candle Holder","Cap","Cape","Card holder","Cardigan","Cardigan Vest","Carpet Yarn","Case","Citybag","Clogs","Clutch and Pochettes","Coat","Cosmetic bag","Crossbody bag","Curtain","Cushion Case","Dress","Dressing Gown (Bata)","Duvet Covers","Earrings","Foulard","Fragance","Gadget","Glasses","Glasses case","Gloves","Hairband","Hairclip","Handbag","Hat","Headband","Home Spray","Jacket","Jacket (Cazadora)","Jeans","Joggers","Jug","Jumpsuit","Kaftan","Kerchief","Keyring","Knicker","Leather Jacket","Leggings","Mini Bag","Necklace","Nightgown","Organiser","Outer vest","Overall","Overshirt","Parka","Pichi","Pillow Case","Plaid","Poloshirt","Poncho","Puffer coat","Purse","Pyjama","Pyjama Cardigan","Pyjama Shirt","Pyjama Shorts","Pyjama Sweatshirt","Pyjama T-Shirt","Pyjama Top","Pyjama Trousers","Pyjiama Sweater","Quilt","Ring","Sandals","Scarf","Shape","Shirt","Shoes","Shorts","Shoulder bag","Skirt","Skort","Slippers","Sock (Pack)","Socks","Sunglasses","Sweater","Sweater Vest","Sweatshirt","Swimsuit","T-Shirt","Tie","Tights","Top","Totes bag","Trainers","Trenchcoat","Trousers","Tumblers","Turban","Umbrella","Vest","Wallet"]

def get_des_color_specification_esp(color):
    if color in des_color_specification_esp:    # Check if the input color is valid
        return des_color_specification_esp.index(color) # Return the position of the color in the list (0-based index)
    else:
        return null  # Return null for an invalid color


def get_des_agrup_color_eng(color2):
    if color2 in des_agrup_color_eng:   # Check if the input color2 is valid
        return des_agrup_color_eng.index(color2)# Return the position of the color2 in the list (0-based index)
    else:
        return null  # Return null for an invalid color2


def get_des_sex(sex):
    if sex in des_sex:# Check if the input sex is valid
        return des_sex.index(sex)# Return the position of the sex in the list (0-based index)
    else:
        return null  # Return null for an invalid sex


def get_des_age(age):
    if age in des_age:# Check if the input age is valid
        return des_age.index(age)# Return the position of the age in the list (0-based index)
    else:
        return null  # Return null for an invalid age


def get_des_line(line):
    if line in des_line:    # Check if the input line is valid
        return des_line.index(line) # Return the position of the line in the list (0-based index)
    else:
        return null  # Return null for an invalid line


def get_des_fabric(fabric):
    if fabric in des_fabric:# Check if the input fabric is valid
        return des_fabric.index(fabric)# Return the position of the fabric in the list (0-based index)
    else:
        return null  # Return null for an invalid fabric


def get_des_product_category(category):
    if category in des_product_category:# Check if the input category is valid
        return des_product_category.index(category)# Return the position of the category in the list (0-based index)
    else:
        return null  # Return null for an invalid category


def get_des_aggregated_family(ag_f):
    if ag_f in des_product_aggregated_family:# Check if the input ag_f is valid
        return des_product_aggregated_family.index(ag_f)# Return the position of the ag_f in the list (0-based index)
    else:
        return null  # Return null for an invalid ag_f


def get_des_product_family(family):
    if family in des_product_family: # Check if the input family is valid
        return des_product_family.index(family)# Return the position of the family in the list (0-based index)
    else:
        return null  # Return null for an invalid family


def get_des_product_type(type):
    if type in des_product_type:# Check if the input type is valid
        return des_product_type.index(type)# Return the position of the type in the list (0-based index)
    else:
        return null  # Return null for an invalid type
    
    #Returns the parameters given a clothe code (string)
def codeToProduct (code):
    found = False
    index = 0
    while (not found and index<len(MyProductData)):
        #print(MyProductData.loc[index, 'des_filename'])
        if code.replace("-","_") in MyProductData.loc[index, 'des_filename']:
            found= True
            return [MyProductData.loc[index, 'des_color_specification_esp'],
                MyProductData.loc[index, 'des_agrup_color_eng'],
                MyProductData.loc[index, 'des_sex'],
                MyProductData.loc[index, 'des_age'],
                MyProductData.loc[index, 'des_line'],
                MyProductData.loc[index, 'des_fabric'],
                MyProductData.loc[index, 'des_product_category'],
                MyProductData.loc[index, 'des_product_aggregated_family'],
                MyProductData.loc[index, 'des_product_family'],
                MyProductData.loc[index, 'des_product_type']]
        index+=1
    return [-1]

def productToDiscreteBox(a):
    return [    get_des_color_specification_esp(a[0]),
                get_des_agrup_color_eng(a[1]),
                get_des_sex(a[2]),
                get_des_age(a[3]),
                get_des_line(a[4]),
                get_des_fabric(a[5]),
                get_des_product_category(a[6]),
                get_des_aggregated_family(a[7]),
                get_des_product_family(a[8]),
                get_des_product_type(a[9]),
                np.random.randint(0, 8)]

#load and run model:
model = joblib.load('fashion_compatibility_V0800.jotlib')

def predict(code):
    predictions = model.predict([productToDiscreteBox(codeToProduct(code))])
    #print(predictions)
    A=[]
    for ii in range(len(predictions[0])):
        if predictions[0][ii]==1:
            A.append(ii)
    for ii in range(len(A)):
        print(A[ii])
        print(MyProductData.loc[A[ii], 'des_filename'])#A[ii]+2
    #print(A)
    return A

a = predict("2019_41065027_19")