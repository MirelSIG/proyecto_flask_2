import sqlite3

con=sqlite3.connect("weather.db")
cur =con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS cities(id, name, temperature, rain_probability)")
con.close()

def _city_from_row(row):
    if row is None:
        return None
    return {"id": row[0], "name": row[1], "temperature": row[2], "rain_probability": row[3]}

def read(city_id):
    con=sqlite3.connect("weather.db")
    try:
        cur =con.cursor()
        res=cur.execute("SELECT id, name, temperature, rain_probability FROM cities WHERE id=?", [city_id])
        city_sql=res.fetchone()

        return _city_from_row(city_sql)
    except sqlite3.Error:
        return None
    finally:
        con.close()

def read_all():
    con=sqlite3.connect("weather.db")
    try:
        cur =con.cursor()
        res=cur.execute("SELECT id, name, temperature, rain_probability FROM cities")
        cities=res.fetchall()
        citi_list=[]
        for city_SQL in cities:
            city = _city_from_row(city_SQL)
            citi_list.append(city)
        return citi_list
    except sqlite3.Error:
        return []
    finally:
        con.close()


def create(new_city):
    con = sqlite3.connect("weather.db")
    try:
        cur = con.cursor()
        values = (new_city['id'], new_city['name'], new_city['temperature'], new_city['rain_probability'])
        cur.execute("INSERT INTO cities (id, name, temperature, rain_probability) VALUES (?, ?, ?, ?)", values)
        con.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    except sqlite3.Error:
        return False
    finally:
        con.close()

def update(city_id, update_city_data):
    con = sqlite3.connect("weather.db")
    try:
        cur = con.cursor()
        values = (update_city_data['name'], update_city_data['temperature'], update_city_data['rain_probability'], city_id)
        cur.execute("UPDATE cities SET name = ?, temperature = ?, rain_probability = ? WHERE id = ?", values)
        con.commit()
        return cur.rowcount > 0
    except sqlite3.Error:
        return False
    finally:
        con.close()

def delete(city_id):
    con = sqlite3.connect("weather.db")
    try:
        cur = con.cursor()
        cur.execute("DELETE FROM cities WHERE id=?", (city_id,))
        con.commit()
        return cur.rowcount > 0
    except sqlite3.Error:
        return False
    finally:
        con.close()
