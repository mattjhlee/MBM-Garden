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

def view_gardens(gardens):
    print("-" * 50)
    print(
        f'| {"ID":<3} | {"Name":<45} | {"Location":<12} | {"Experience LVL":<20} | {"":<15} | {"Contact":<17} |'
    )