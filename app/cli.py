from app import app
from models import db, Plant, Garden, Gardener

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
            