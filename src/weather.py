from .weather_repository_sqlite import *

def get_city_by(city_id):
    return read(city_id)

def get_all_cities():
    return read_all()

def post_city(new_city):
    return create(new_city)

def update_city(city_id, update_city_data):
    return update(city_id, update_city_data)

def del_city(city_id):
    return delete(city_id)
    
