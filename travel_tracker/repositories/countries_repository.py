from db.run_sql import run_sql

from models.countries import Country

def save(countries):    
    sql = "INSERT INTO countries (name, region) VALUES (%s, %s) RETURNING *"
    values = [countries.name, countries.region]
    results = run_sql(sql, values)
    countries.id = results[0]['id']
    return countries 

def select_all():
    countries = []

    sql = "SELECT * FROM countries"
    results = run_sql(sql)

    for row in results:
        country = Country(row['name'], row['region'], row['id'] )
        countries.append(country)
    return countries

def select(id):
    countries = None
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        country = Country(result['name'], result['region'], result['id'] )
    return country

def delete(id):
    sql = "DELETE FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM countries"
    run_sql(sql)

def update(countries):
    sql = "UPDATE countries SET (name, region) = (%s, %s) WHERE id = %s"
    values = [countries.name, countries.region, countries.id]
    print(values)
    run_sql(sql, values)

