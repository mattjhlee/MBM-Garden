from app import app
from models import db, Plant, Gardener, Garden

if __name__ == '__main__':
    with app.app_context():


        #SQLAlchemy seeding

        #Clear out models
        Plant.query.delete()
        Gardener.query.delete()
        Garden.query.delete()

        plants = [
        Plant(
            name = "tomato",
            species = "Solanum lycopersicum",
            season = "Spring",
            harvest_time = 10
        ),
        Plant (
            name = "Bush Beans",
            species = "Phaseolus vulgaris",
            season = "Summer",
            harvest_time = 6
        ),
        Plant (
            name = "Watermelon",
            species = "Citrullus lanatus",
            season = "Summer",
            harvest_time = 11
        ),
        Plant (
            name = "Pumpkin",
            species = "Cucurbita pepo",
            season = "Fall",
            harvest_time = 15
        ),
        Plant(
            name = "Strawberries",
            species = "Fragaria ananassa",
            season = "Spring",
            harvest_time = 5
        )]

        # print(plants) #some reason there is no closing >

        db.session.add_all(plants)

        gardeners = [
        Gardener(
            name = "Emily Johnson",
            location = "Seattle, WA",
            experience = 3
        ),

        Gardener (
            name = "Michael Thompson",
            location = "Austin, TX",
            experience = 2
        ),

        Gardener (
            name = "Luisa Rodriguez",
            location = "Chicago, IL",
            experience = 1
        ),

        Gardener (
            name = "Sophie Clark",
            location = "San Francisco, CA",
            experience = 4
        ),

        Gardener (
            name = "Juan Hernandez",
            location = "Miami, FL",
            experience = 0
        )]

        db.session.add_all(gardeners)

        gardens = [
        Garden(
            name = "Sunshine Paradise",
            location = "Seattle, WA",
            experience_req = 3,
            plant_id = 1,
            gardener_id = 1
        ),

            Garden (
            name = "Breezy Meadows",
            location = "Austin, TX",
            experience_req = 2,
            plant_id = 2,
            gardener_id = 2
        ),

            Garden (
            name = "City Retreat",
            location = "Chicago, IL",
            experience_req = 1,
            plant_id = 3,
            gardener_id = 3
        ),

            Garden (
            name = "Serene Haven",
            location = "San Francisco, CA",
            experience_req = 4,
            plant_id = 4,
            gardener_id = 4
        ),

            Garden (
            name = "Tropical Oasis",
            location = "Miami, FL",
            experience_req = 0,
            plant_id = 5,
            gardener_id = 5
        )]
        
        db.session.add_all(gardens)

        db.session.commit()
        

    # name = db.Column(db.String)
    # species = db.Column(db.String)
    # season = db.Column(db.String)
    # harvest_time = db.Column(db.Integer)

