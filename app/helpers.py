from models import db, Plant, Garden, Gardener

def menu_selection( gardens, plants, gardeners): #gardener_name missing as first positonal
      exit_loop = False
      while exit_loop == False:
                choice = input("Type 'gardens' to see the gardens, type 'plants' to see our available plants, not already a gardener? Type 'join', or type 'exit' to end session: ")
                print(' ')
                if choice.lower() == "gardens":
                     view_gardens(gardens, plants, gardeners)
                elif choice.lower() == "plants":
                     view_plants(plants)
                elif choice.lower() == "join":
                     add_gardener(gardener_name)
                elif choice.lower() == "exit":
                    exit_loop = True #write an exit
                else:
                    error_message()

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

def view_plants(plants):
    print("-" * 100)
    print(
        f'| {"ID":<0} | {"Name":<15} | {"Species":<20} | {"Season":<10} | {"Harvest Time":<21} | {"Quantity":<10} |'
    )
    print("-" * 100)
    for plant in plants:
        id_spaces = 3- len(str(plant.id))
        name_spaces = 15 - len(plant.name)
        species_spaces = 20 - len(plant.species)
        season_spaces = 10 - len(plant.season)
        harvest_spaces = 15 - len(str(plant.harvest_time))
        quantity_spaces = 10 - len(str(plant.quantity))
        
        print(
            f'|{" "}{plant.id}{" " * id_spaces}| {plant.name}{" " * name_spaces} | {plant.species}{" " * species_spaces} | {plant.season}{" " * season_spaces} | {plant.harvest_time} weeks{" " * harvest_spaces} | {plant.quantity}{" " * quantity_spaces} |'
        )
    print("-" * 100)

    # id = db.Column(db.Integer, primary_key=True)
    # name = db.Column(db.String)
    # species = db.Column(db.String)
    # season = db.Column(db.String)
    # harvest_time = db.Column(db.Integer)
    # #harvest_time is in weeks
    # quantity = db.Column(db.Integer)



def add_garden():
    garden_input = input("What would you like to call your garden?")
    location_input = input("City, State: ")
    exp_input = input("Years of experience: ")

    new_garden = Garden(
        name = garden_input,
        location = location_input,
        experience = exp_input
    )

    db.session.add(new_garden)
    db.session.commit()
    print(f"Congratulations! You've successfully created community garden, would you like to get planting in {new_garden.name}? Type Y to continue to your garden and plant, or L to see the list of gardens!")

def error_message():
        print("The input you've made is invalid, please try again.")

    # id = db.Column(db.Integer, primary_key=True)
    # name = db.Column(db.String)
    # location = db.Column(db.String)
    # experience_req = db.Column(db.Integer)

    # plant_id = db.Column(db.Integer, db.ForeignKey('plants.id'))
    # gardener_id = db.Column(db.Integer, db.ForeignKey('gardeners.id'))
