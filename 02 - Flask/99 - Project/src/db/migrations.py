import os
import shutil
from src.db.config import sqlite_path
from src.models.user import User
from src.models.category import Category
from src.models.product import Product
from src.models.product_info import ProductInfo
from src.models.product_picture import ProductPicture

def create_db(app, db):
    with app.app_context():
        if not os.path.isfile(sqlite_path):
            
            db.drop_all()
            db.create_all()

            add_user(db)
            add_category(db) 
            add_product(db)
           
            db.session.commit()

            
def add_user(db):
    db.session.add(User("David"))
    db.session.add(User("Renata"))    
    
def add_category(db):
    db.session.add(Category("Bebidas"))
    
def add_product(db):
    db.session.add(Product(1, "Heineken Lata 350ml", "Heineken International é uma cervejaria holandesa, fundada em 1863 por Gerard Adriaan Heineken na cidade de Amsterdã.", 100, 4.39, 0))
    db.session.add(ProductInfo(1, "Observação", "A venda e o consumo de bebidas alcoólicas são proibidos para menores de 18 anos. Beba com moderação. Se for dirigir, não beba!"))
    db.session.add(ProductInfo(1, "País de Origem", "Holanda"))
    db.session.add(ProductInfo(1, "Embalagem", "Lata verde"))
    db.session.add(ProductPicture(1, "heineken.png"))
    
    db.session.add(Product(1, "Original Lata 350ml", "Cerveja Pilsen Antarctica Original, harmonize suas comemorações com um sabor mais suave e refrescante!", 100, 3.49, 0))           
    db.session.add(ProductInfo(2, "Observação", "A venda e o consumo de bebidas alcoólicas são proibidos para menores de 18 anos. Beba com moderação. Se for dirigir, não beba!"))
    db.session.add(ProductInfo(2, "País de Origem", "Brasil"))
    db.session.add(ProductInfo(2, "Embalagem", "Lata branca"))
    db.session.add(ProductPicture(2, "original.png"))
    
    db.session.add(Product(1, "Budweiser Long Neck 350ml", "Budweiser, também conhecida popularmente como Bud, é uma cerveja do tipo long americana, fabricada pela AB InBev, fundada em 1876", 100, 3.49, 0))           
    db.session.add(ProductInfo(3, "Observação", "A venda e o consumo de bebidas alcoólicas são proibidos para menores de 18 anos. Beba com moderação. Se for dirigir, não beba!"))
    db.session.add(ProductInfo(3, "País de Origem", "Brasil"))
    db.session.add(ProductInfo(3, "Embalagem", "Lata branca"))
    db.session.add(ProductPicture(3, "budweiser.png"))
    
    db.session.add(Product(1, "Imperial Garrafa 600ml", "Cerveja ouro imperial garrafa 600ml, harmonize suas comemorações com um sabor mais suave e refrescante!", 100, 3.49, 0))           
    db.session.add(ProductInfo(4, "Observação", "A venda e o consumo de bebidas alcoólicas são proibidos para menores de 18 anos. Beba com moderação. Se for dirigir, não beba!"))
    db.session.add(ProductInfo(4, "País de Origem", "Brasil"))
    db.session.add(ProductInfo(4, "Embalagem", "Lata branca"))
    db.session.add(ProductPicture(4, "imperial.png"))