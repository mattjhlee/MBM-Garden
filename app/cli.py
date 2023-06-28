from app import app
from models import db, Plant, Garden, Gardener
from helpers import (
    add_gardener
)

if __name__ == "__main__":
    with app.app_context():
        print(
            """
,---.    ,---. _______   ,---.    ,---.          .-_'''-.      ____    .-------.     ______         .-''-.  ,---.   .--. 
|    \  /    |\  ____  \ |    \  /    |         '_( )_   \   .'  __ `. |  _ _   \   |    _ `''.   .'_ _   \ |    \  |  | 
|  ,  \/  ,  || |    \ | |  ,  \/  ,  |        |(_ o _)|  ' /   '  \  \| ( ' )  |   | _ | ) _  \ / ( ` )   '|  ,  \ |  | 
|  |\_   /|  || |____/ / |  |\_   /|  |        . (_,_)/___| |___|  /  ||(_ o _) /   |( ''_'  ) |. (_ o _)  ||  |\_ \|  | 
|  _( )_/ |  ||   _ _ '. |  _( )_/ |  |        |  |  .-----.   _.-`   || (_,_).' __ | . (_) `. ||  (_,_)___||  _( )_\  | 
| (_ o _) |  ||  ( ' )  \| (_ o _) |  |        '  \  '-   .'.'   _    ||  |\ \  |  ||(_    ._) ''  \   .---.| (_ o _)  | 
|  (_,_)  |  || (_{;}_) ||  (_,_)  |  |         \  `-'`   | |  _( )_  ||  | \ `'   /|  (_.\.' /  \  `-'    /|  (_,_)\  | 
|  |      |  ||  (_,_)  /|  |      |  |          \        / \ (_ o _) /|  |  \    / |       .'    \       / |  |    |  | 
'--'      '--'/_______.' '--'      '--'           `'-...-'   '.(_,_).' ''-'   `'-'  '-----'`       `'-..-'  '--'    '--' 
                                                                                                                        
            """)
        print("Hello, gardener! Welcome to the MBM Garden CLI.")
        plants = db.session.query(Plant)
        gardeners = db.session.query(Gardener)
        gardens = db.session.query(Garden)

        gardener_name = input("Name: ")
        for gardener in gardeners:
            if gardener.name.lower() == gardener_name.lower():
                print(f"Welcome back, {gardener.name}.")
                break
            else:
                add_gardener(gardener_name)

        
        