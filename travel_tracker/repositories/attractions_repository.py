from db.run_sql import run_sql

from models.attractions import Attraction
from models.countries import Country
import repositories.destinations_repository as destination_repository

def save(attractions):    
    sql = "INSERT INTO attractions (name, description, destination_id, date, visited) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [attractions.name, attractions.description, attractions.destination.id, attractions.date, attractions.visited]
    results = run_sql(sql, values)
    attractions.id = results[0]['id']
    return attractions 

def select_all():
    attractions = []

    sql = "SELECT * FROM attractions"
    results = run_sql(sql)
# talk about passing destination_id from the database which is stored as number and converted into a object by using a variable to store as a result
    for row in results:
        destination = destination_repository.select(row['destination_id'])
        attraction = Attraction(row['name'], row['description'], destination, row['date'], row['id'], row['visited'])
        attractions.append(attraction)
    return attractions

def select(id):
    attractions = None
    sql = "SELECT * FROM attractions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        destination = destination_repository.select(result["destination_id"])
        attractions = Attraction(result['name'], result['description'], destination, result['date'], result['id'], result['visited'])
    return attractions

def delete_all():
    sql = "DELETE FROM attractions"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM attractions WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(attractions):
    sql = "UPDATE attractions SET (name, description, destination_id, date, visited) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [attractions.name, attractions.description, attractions.destination.id, attractions.date, attractions.visited, attractions.id]
    print(values)
    run_sql(sql, values)