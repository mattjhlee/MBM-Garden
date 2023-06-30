from models import db, Plant, Garden, Gardener

def add_gardener(gardener_name):
    location_input = input("City, State: ")
    exp_input = input("Years of experience: ")

    new_gardener = Gardener(
        name = gardener_name,
        location = location_input,
        experience = exp_input
    )

    db.session.add(new_gardener)
    db.session.commit()
    print(f"Welcome to MBM Gardens, {gardener_name}. You've been added to our list of gardeners.")

def view_gardens(gardens, plants, gardeners):
    print("-" * 112)
    print(
        f'| {"ID":<3} | {"Name":<20} | {"Location":<20} | {"XP LVL":<10} | {"Plant":<20} | {"Gardener":<20} |'
    )
    print("-" * 112)
    for garden in gardens:
        id_spaces = 3 - len(str(garden.id))
        name_spaces = 20 - len(garden.name)
        location_spaces = 20 - len(garden.location)
        experience_spaces = 10 - len(str(garden.experience_req))
        plant_name = garden.plant.name
        plant_spaces = 20 - len(plant_name)
        gardener_name = garden.gardener.name
        gardener_spaces = 20 - len(gardener_name)
        print(
            f'| {garden.id}{" " * id_spaces} | {garden.name}{" " * name_spaces} | {garden.location}{" " * location_spaces} | {garden.experience_req}{" " * experience_spaces} | {plant_name}{" " * plant_spaces} | {gardener_name}{" " * gardener_spaces} |'
        )
    print("-" * 112)

# def plant_existing_garden(gardner_name): #Should gardner_name be an argument
#     print("Would you like to grow a new plant?")
#     choice = input("Type 'Yes' or 'No'") #This goes in the CLI and choice will become an attribute

#     if choice.lower() == 'Yes'.lower():
#         # db.session.add(gardener) This was commented out prior
#         print("Great!")
#         new_plant_name = input("What type of plant do you want to grow? ")
#         # new_plant_species = input("What species is the plant? If you don't know type 'N/A")
#         # new_plant_season = input("What season does this plant bloom/flower?")
#         new_plant_quantity = input("Using numbers, how many plants will you be planting? ")
#         new_plant_gardener = [gardner_name] 
#         new_plant_garden = None
        


#         new_plant = Plant(
#             name = new_plant_name,
#             quantity = new_plant_quantity,
#             gardeners = new_plant_gardener,
#             garden = new_plant_garden
#         )

#         print(new_plant)

        
#         db.session.add(new_plant)
#         db.session.commit()
#         print("success!")
#     elif choice.lower() == 'No'.lower():
#         print("Alright, no problem!")
#     else:
#         print("Must type 'Yes' or 'No'")

def plant_existing_garden(gardener_name):
    print("Would you like to grow a new plant?")
    choice = input("Type 'Yes' or 'No': ")

    if choice.lower() == 'yes':
        print("Great!")
        new_plant_name = input("What type of plant do you want to grow? ")
        new_plant_quantity = input("Using numbers, how many plants will you be planting? ")

        gardener = Gardener.query.filter_by(name=gardener_name).first()  # Fetch the gardener object from the database

        if gardener:
            new_plant_gardener = [gardener]
            garden_name = input("In which garden do you want to plant? ")
            garden = Garden.query.filter_by(name=garden_name).first()  # Fetch the garden object from the database

            if garden:
                new_plant = Plant(
                    name=new_plant_name,
                    quantity=new_plant_quantity,
                    gardeners=new_plant_gardener,
                    gardens=[garden]
                )

                db.session.add(new_plant)
                db.session.commit()
                print("Success!")
            else:
                print(f"No garden found with the name: {garden_name}")
        else:
            print(f"No gardener found with the name: {gardener_name}")
    elif choice.lower() == 'no':
        print("Alright, no problem!")
    else:
        print("Please type 'Yes' or 'No'")


    
        