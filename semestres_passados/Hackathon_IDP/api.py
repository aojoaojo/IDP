from sqlalchemy import create_engine, Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship, backref, declarative_base
from sqlalchemy.orm import sessionmaker

# create SQLite engine
engine = create_engine('sqlite:///weather.db', echo=False)

# create declarative base
Base = declarative_base()

# define classes for each table
class City(Base):
    __tablename__ = 'city'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    lat = Column(String)
    long = Column(String)

    weather = relationship("Weather", backref="city")


class Weather(Base):
    __tablename__ = 'weather'
    id = Column(Integer, primary_key=True)
    date = Column(String)
    city_id = Column(Integer, ForeignKey('city.id'))
    temperature = Column(String)
    wind_speed = Column(String)
    wind_direction = Column(String)

# create tables
Base.metadata.create_all(engine)

# create session
Session = sessionmaker(bind=engine)
session = Session()

# add customers
city1 = City(name='Brasília', lat='-15.77972', long='-47.92972')
session.add_all([city1])

# add orders
weather1 = Weather(date='2022-03-30', city=city1, temperature='25.1',wind_speed='0.5',wind_direction='180')
weather2 = Weather(date='2022-04-30', city=city1, temperature='19.1',wind_speed='2.5',wind_direction='180')
session.add_all([weather1, weather2])

# commit changes
session.commit()

cidades = session.query(City).all()

for cidade in cidades:
    print(f'Cidade: {cidade.name}')
    for weather in cidade.weather:
        print(f'\tWeather: {weather.id} ({weather.date})')
        print(f'{weather.temperature}')

import requests
url = 'https://api.open-meteo.com/v1/forecast?latitude=-15.77972&longitude=-47.92972&current_weather=true'
res = requests.get(url)

res.json()