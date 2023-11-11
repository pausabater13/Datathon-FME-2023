// See https://aka.ms/new-console-template for more information
using System.Drawing;

Console.WriteLine("Hello, World!");
def get_color_position(color):

    # List of valid colors
    valid_colors = [
        "AGUA", "AMARILLO", "AMARILLO FLUOR", "AMARILLO PASTEL", "ANTRACITA", "ARENA",
        "ASFALTO", "AZUL", "AZUL NOCHE", "BEIGE", "BERMELLON", "BILLAR", "BLANCO",
        "BLEACH", "BLOOD", "BLUEBLACK", "BOTELLA", "BURDEOS", "CALDERO", "CAMEL",
        "CANELA", "CARAMELO", "CAZA", "CELESTE", "CENIZA", "CEREZA", "CHICLE",
        "CHOCOLATE", "CIRUELA", "COBRE", "COFFEE", "COGNAC", "CORAL", "CRUDO",
        "CUERO", "CURRY", "DIRTY", "DIRTY CLARO", "DIRTY OSCURO", "ELECTRICO",
        "ESMERALDA", "FRESA", "FUCSIA", "GERANIO", "GRANATE", "GRIS", "GRIS CLARO VIGORE",
        "GRIS MEDIO VIGORE", "GRIS OSCURO VIGORE", "GUNMETAL", "HIELO", "INDIGO", "KHAKI",
        "LILA", "LIMA", "MALVA", "MANDARINA", "MANZANA", "MARFIL", "MARINO", "MARRON",
        "MENTA", "MISTERIO", "MORADO", "MOSTAZA", "MUSGO", "NARANJA", "NARANJA PASTEL",
        "NAVY", "NEGRO", "NUDE", "OCRE", "OFFWHITE", "OLIVA", "ORO", "PEACH", "PERLA",
        "PETROLEO", "PIEDRA", "PIMENTON", "PLATA", "PORCELANA", "PRUSIA", "ROJO", "ROSA",
        "ROSA FLUOR", "ROSA LIGHT", "ROSA PALO", "ROSA PASTEL", "SALMON", "TABACO", "TAUPE",
        "TEJANO CLARO", "TEJANO GRIS", "TEJANO GRIS CLARO", "TEJANO GRIS OSCURO",
        "TEJANO MEDIO", "TEJANO NEGRO", "TEJANO OSCURO", "TEJANO SOFT", "TERRACOTA", "TINTA",
        "TOPO", "TURQUESA", "VAINILLA", "VERDE", "VERDE PASTEL", "VINO", "VIOLETA", "VISON"
    ]

    # Check if the input color is valid
    if color in valid_colors:
        # Return the position of the color in the list (0-based index)
        return valid_colors.index(color)
    else:
        print(f"Invalid color: {color}")
        return null  # Return null for an invalid color


def get_agrup_color_position(color2)

    # List of valid colors2
    valid_colors2 = [ "BLUE", "BROWN", "GREEN", "GREY", "ORANGE", "PINK", "PURPLE", "RED", "WHITE", "YELLOW"]

    # Check if the input color2 is valid
    if color2 in valid_colors2:
        # Return the position of the color2 in the list (0-based index)
        return valid_colors2.index(color2)
    else:
        print(f"Invalid color2: {color2}")
        return null  # Return null for an invalid color2


def get_des_sex_position(sex)

     # List of valid sex
    valid_sex = ["Female", "Male", "Unisex"]

    # Check if the input sex is valid
    if sex in valid_sex:
        # Return the position of the sex in the list (0-based index)
        return valid_sex.index(sex)
    else:
        print(f"Invalid sex: {sex}")
        return null  # Return null for an invalid sex


def get_des_age_position(age)

     # List of valid ages
    valid_ages = ["Adult", "Kids"]

    # Check if the input age is valid
    if age in valid_ages:
        # Return the position of the age in the list (0-based index)
        return valid_ages.index(age)
    else:
        print(f"Invalid age: {age}")
        return null  # Return null for an invalid age


def get_des_line_position(line)

     # List of valid lines
    valid_lines = ["HE", "HOME", "KIDS", "SHE", "VIOLETA"]

    # Check if the input line is valid
    if line in valid_lines:
        # Return the position of the line in the list (0-based index)
        return valid_lines.index(line)
    else:
        print(f"Invalid line: {line}")
        return null  # Return null for an invalid line


def get_des_fabric_position(fabric)

    # List of valid fabriques
    valid_fabriques = ["C-COMPLEMENTOS", "J-JEANS", "K-CIRCULAR",
    "L-PIEL", "O-POLIPIEL", "P-PLANA", "T-TRICOT"]

    # Check if the input fabric is valid
    if fabric in valid_fabriques:
        # Return the position of the fabric in the list (0-based index)
        return valid_fabriques.index(fabric)
    else:
        print(f"Invalid fabric: {fabric}")
        return null  # Return null for an invalid fabric


def get_des_product_category_position(category)

    # List of valid categories
    valid_categories = ["Accesories, Swim and Intimate", "Beauty", "Bottoms",
    "Dresses, jumpsuits and Complete set", "Home", "Outerwear", "Tops"]

    # Check if the input category is valid
    if category in valid_categories:
        # Return the position of the category in the list (0-based index)
        return valid_categories.index(category)
    else:
        print(f"Invalid category: {category}")
        return null  # Return null for an invalid category


def get_des_aggregated_family_position(ag_f)

    # List of valid ag_fs
    valid_ag_fs = ["Accessories", "Bedroom", "Coats and Parkas", "Decor",
    "Dinning Room", "Dresses and jumpsuits", "Fragance", "Jackets and Blazers",
    "Jeans", "Shirts", "Skirts and shorts", "Sweaters and Cardigans", "Swim and intimate",
    "T-shirts", "Tops", "Trousers & leggings"]

    # Check if the input ag_f is valid
    if ag_f in valid_ag_fs:
        # Return the position of the ag_f in the list (0-based index)
        return valid_ag_fs.index(ag_f)
    else:
        print(f"Invalid family: {aggregated_family}")
        return null  # Return null for an invalid ag_f


def get_des_product_family_position(family)

     # List of valid families
    valid_families = ["Bags", "Bedding", "Belts and Ties", "Blazers", "Bodysuits",
    "Cardigans", "Coats", "Deco Accessories", "Deco Textiles", "Dresses", "Footwear",
    "Fragances", "Gadgets", "Glasses", "Glassware", "Hats, scarves and gloves",
    "Intimate", "Jackets", "Jeans", "Jewellery", "Jumpsuit", "Leather jackets",
    "Leggings and joggers", "Outer Vest", "Parkas", "Poloshirts", "Puffer coats",
    "Shirt", "Shorts", "Skirts", "Sweater", "Sweatshirts", "Swimwear", "T-shirt",
    "Tops", "Trenchcoats", "Trousers", "Vest", "Wallets & cases"]

    # Check if the input family is valid
    if family in valid_families:
        # Return the position of the family in the list (0-based index)
        return valid_families.index(family)
    else:
        print(f"Invalid family: {family}")
        return null  # Return null for an invalid family


def get_des_product_type_position(type)

     # List of valid tipes
    valid_tipes = ["Ankle Boots", "Backpack", "Basket", "Beach Towel", "Beanie",
    "Bed Cushion Case", "Bedspread", "Belt", "Belt bag", "Bermudas", "Bikini pantie",
    "Bikini top", "Blazer", "Blouse", "Bodymist", "Bodysuit", "Boots", "Box",
    "Bracelet", "Braces", "Bras", "Bucket bag", "Candle", "Candle Holder", "Cap",
    "Cape", "Card holder", "Cardigan", "Cardigan Vest", "Carpet Yarn", "Case",
    "Citybag", "Clogs", "Clutch and Pochettes", "Coat", "Cosmetic bag", "Crossbody bag",
    "Curtain", "Cushion Case", "Dress", "Dressing Gown (Bata)", "Duvet Covers", "Earrings",
    "Foulard", "Fragance", "Gadget", "Glasses", "Glasses case", "Gloves", "Hairband",
    "Hairclip", "Handbag", "Hat", "Headband", "Home Spray", "Jacket", "Jacket (Cazadora)",
    "Jeans", "Joggers", "Jug", "Jumpsuit", "Kaftan", "Kerchief", "Keyring", "Knicker",
    "Leather Jacket", "Leggings", "Mini Bag", "Necklace", "Nightgown", "Organiser",
    "Outer vest", "Overall", "Overshirt", "Parka", "Pichi", "Pillow Case", "Plaid",
    "Poloshirt", "Poncho", "Puffer coat", "Purse", "Pyjama", "Pyjama Cardigan",
    "Pyjama Shirt", "Pyjama Shorts", "Pyjama Sweatshirt", "Pyjama T-Shirt", "Pyjama Top",
    "Pyjama Trousers", "Pyjiama Sweater", "Quilt", "Ring", "Sandals", "Scarf", "Shape",
    "Shirt", "Shoes", "Shorts", "Shoulder bag", "Skirt", "Skort", "Slippers", "Sock (Pack)",
    "Socks", "Sunglasses", "Sweater", "Sweater Vest", "Sweatshirt", "Swimsuit", "T-Shirt",
    "Tie", "Tights", "Top", "Totes bag", "Trainers", "Trenchcoat", "Trousers", "Tumblers",
    "Turban", "Umbrella", "Vest", "Wallet"]

    # Check if the input type is valid
    if type in valid_tipes:
        # Return the position of the type in the list (0-based index)
        return valid_tipes.index(type)
    else:
        print(f"Invalid type: {type}")
        return null  # Return null for an invalid type