import requests
def create_datastructure(data_list):
  new_dict = {}
  for d in data_list:
    new_dict[ d['_id'] ] = {
      'city': d['city'],
      'state': d['state'],
      'longitude': d['loc'][0],
      'latitude': d['loc'][1]
    }
  return new_dict
def find_city(data, city_name):
  lst = []
  for key, value in data.items():
    if value['city'].lower() == city_name.lower():
      lst.append({
        'zip_code': key,
        **value
      })
  return lst
from utils import create_datastructure, find_city
data = requests.get('https://assets.breatheco.de/apis/fake/zips.php').json()
zipcode = {
  '01001': {
    'state': 'MA',
    'city': 'AGAWAM',
    'longitude': -72.622739,
    'latitude': 42.070206,
    'loc': [2345,234],
    'pop': 15338
  }
}
data = create_datastructure(data)
def get_info_by_zip(zip):
  return data[zip]
# DIFFERENT WAY OF WRITING THE SAME THING
# def find_city(city_name):
#   for key in data.keys():
#     if data[key]['city'] == city_name:
#       print(key)
# def find_city(city_name):
#   for key, value in data.items():
#     if value['city'] == city_name:
#       print(key)
for x in find_city(data, 'miami'):
  print(x)
# print( zipcode['01001']['loc'][0] )
# zipcode['44567']
# print(data[0]['_id'])
# def find_zip():
#   a = input('Enter zip code: ')
#   for d in data:
#     if d['_id'] == a:
#       return d
#   return 'not found 404'
# result = find_zip()
# print(result)
# def find_zip(a):
#   for d in data:
#     if d['_id'] == a:
#       return d
#   return 'not found 404'
# inp = input('Enter zip code: ')
# result = find_zip(inp)
# print(result)
# first_zip = data[0]['_id']
# print( find_zip(first_zip) )
# print( find_zip('33186'))
# def printing():
#   return '1 + 1'
# result = printing()
# print( result )