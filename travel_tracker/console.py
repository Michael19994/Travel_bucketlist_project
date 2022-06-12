import pdb

from models.attractions import Attraction
from models.destinations import Destination
from models.countries import Country

import repositories.attractions_repository as attractions_repository
import repositories.destinations_repository as destinations_repository
import repositories.countries_repository as countries_repository

countries_repository.delete_all()
destinations_repository.delete_all()
attractions_repository.delete_all()


country1 = Country("Norway", "Europe")
countries_repository.save(country1)

destination1 = Destination("Tromso", country1)
destinations_repository.save(destination1)

attraction1 = Attraction("Whale Watching", "description", destination1, "20/12/2020")
attractions_repository.save(attraction1)

country2 = Country("Canada", "North America")
countries_repository.save(country2)

destination2 = Destination("Vancouver Island", country2)
destinations_repository.save(destination2)

attraction2 = Attraction("Nature Walk", "description2", destination2, "22/02/2021")
attractions_repository.save(attraction2)


countries_repository.delete(country2.id)
destinations_repository.delete(destination2.id)
attractions_repository.delete(attraction2.id)

countries = countries_repository.select_all()
destinations = destinations_repository.select_all()
attractions = attractions_repository.select_all()

country1 = countries_repository.select(country1.id)
destination_1 = destinations_repository.select(destination1.id)
attraction_1 = attractions_repository.select(attraction1.id)

destination_update = Destination("Svalbard", country1, destination_1.id)
destinations_repository.update(destination_update)
destination_updated = destinations_repository.select(destination_1.id)

attraction_update = Attraction("Polar Bear Tour", "bus tour", destination_updated, "02/02/2021", attraction_1.id)
attractions_repository.update(attraction_update)
attraction_updated = attractions_repository.select(attraction_1.id)

pdb.set_trace()