from app import app
from models import db, Plant, Gardener, Garden

if __name__ == '__main__':
    with app.app_context():


        #SQLAlchemy seeding

        #Clear out models
        Plant.query.delete()

        plants = [Plant(
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

        db.session.commit()
        

    # name = db.Column(db.String)
    # species = db.Column(db.String)
    # season = db.Column(db.String)
    # harvest_time = db.Column(db.Integer)

