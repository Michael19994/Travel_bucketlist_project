from db.run_sql import run_sql
from models.countries import Country
import repositories.countries_repository as countries_repository
from models.destinations import Destination

def save(destinations):
    sql = "INSERT INTO destinations (name, country_id) VALUES (%s, %s) RETURNING *"
    values = [destinations.name, destinations.country.id]
    results = run_sql(sql, values)
    destinations.id = results[0]['id']
    return destinations 

def select_all():
    destinations = []

    sql = "SELECT * FROM destinations"
    results = run_sql(sql)

    for row in results:
        destination = Destination(row['name'], row['country_id'], row['id'] )
        destinations.append(destination)
    return destinations

def select(id):
    destinations = None
    sql = "SELECT * FROM destinations WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        country = countries_repository.select(result["country_id"])
        destinations = Destination(result['name'], country, result['id'] )
    return destinations

def delete_all():
    sql = "DELETE FROM destinations"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM destinations WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(destinations):
    sql = "UPDATE destinations SET (name, country_id) = (%s, %s) WHERE id = %s"
    values = [destinations.name, destinations.country.id, destinations.id]
    print(values)
    run_sql(sql, values)