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

def plant_existing_garden():

    print("Would you like to grow a new plant?")
    choice = input("Type 'Yes' or 'No'")

    if choice.lower() == 'Yes'.lower():
        # db.session.add(gardener)
        print("Great!")
        print("What type of plant do you want to grow?")
        new_plant_name = input("What type of plant do you want to grow? ")
        # new_plant_species = input("What species is the plant? If you don't know type 'N/A")
        # new_plant_season = input("What season does this plant bloom/flower?")
        new_plant_quantity = input("Using numbers, how many plants will you be planting?")
        new_plant_gardener = Gardener.name
        new_plant_garden = Garden.name


        new_plant = Plant(
            name = new_plant_name,
            quantity = new_plant_quantity,
            gardener = new_plant_gardener,
            garden = new_plant_garden
        )

        db.session.add(new_plant)
        db.session.commit()
    elif choice.lower() == 'No'.lower():
        print("Alright, no problem!")
    else:
        print("Must type 'Yes' or 'No'")
    
        