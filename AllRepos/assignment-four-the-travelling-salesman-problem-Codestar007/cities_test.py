"""cities_test.py

Test coverage includes the following:
    All functions that return a value.
    Checking for correct algorithms and output
    Also checking for error handling

    Functions tested:
     - def compute_total_distance
     - swap_adjacent_cities
     - swap_cities
     - next_nearest_city
     - find_best_cycle
     

    Functions not tested:
     - main
     - read_cities
     - print_cities
     - print_map

"""

# Import Statements
import pytest
import sys
import random
import cities


def test_compute_total_distance():
    epsilon = 0.0000000000001
    road_map1 = [ ('Alabama', 'Montgomery', '32.361538', '-86.279118'),
                  ('Alaska', 'Juneau', '58.301935', '-134.41974'),
                  ('Arizona', 'Phoenix', '33.448457', '-112.073844'),
                  ('Arkansas', 'Little Rock', '34.736009', '-92.331122'),
                  ('California', 'Sacramento', '38.555605', '-121.468926') ]

    road_map2 = [ ('Kentucky', 'Frankfort', '38.197274', '-84.86311'),
                  ('Louisiana', 'Baton Rouge', '30.45809', '-91.140229'),
                  ('Maine', 'Augusta', '44.323535', '-69.765261'),
                  ('Maryland', 'Annapolis', '38.972945', '-76.501157') ]

    road_map3 = [ ('Maryland', 'Annapolis', '38.972945', '-76.501157') ]

    road_map4 = [ ('Alabama', 'Montgomery', '32.361538', '-86.279118'),
                  ('Alaska', 'Juneau', '58.301935', '-134.41974'),
                  ('Arizona', 'Phoenix', '33.448457', '-112.073844'),
                  ('Arkansas', 'Little Rock', '34.736009', '-92.331122'),
                  ('California', 'Sacramento', '38.555605', '-121.468926'),
                  ('Colorado', 'Denver', '39.7391667', '-104.984167'),
                  ('Connecticut', 'Hartford', '41.767', '-72.677'),
                  ('Delaware', 'Dover', '39.161921', '-75.526755'),
                  ('Florida', 'Tallahassee', '30.4518', '-84.27277'),
                  ('Georgia', 'Atlanta', '33.76', '-84.39'),
                  ('Hawaii', 'Honolulu', '21.30895', '-157.826182'),
                  ('Idaho', 'Boise', '43.613739', '-116.237651'),
                  ('Illinois', 'Springfield', '39.78325', '-89.650373'),
                  ('Indiana', 'Indianapolis', '39.790942', '-86.147685'),
                  ('Iowa', 'Des Moines', '41.590939', '-93.620866'),
                  ('Kansas', 'Topeka', '39.04', '-95.69'),
                  ('Kentucky', 'Frankfort', '38.197274', '-84.86311'),
                  ('Louisiana', 'Baton Rouge', '30.45809', '-91.140229'),
                  ('Maine', 'Augusta', '44.323535', '-69.765261'),
                  ('Maryland', 'Annapolis', '38.972945', '-76.501157'),
                  ('Massachusetts', 'Boston', '42.2352', '-71.0275'),
                  ('Michigan', 'Lansing', '42.7335', '-84.5467'),
                  ('Minnesota', 'Saint Paul', '44.95', '-93.094'),
                  ('Mississippi', 'Jackson', '32.32', '-90.207'),
                  ('Missouri', 'Jefferson City', '38.572954', '-92.189283'),
                  ('Montana', 'Helana', '46.595805', '-112.027031'),
                  ('Nebraska', 'Lincoln', '40.809868', '-96.675345'),
                  ('Nevada', 'Carson City', '39.160949', '-119.753877'),
                  ('New Hampshire', 'Concord', '43.220093', '-71.549127'),
                  ('New Jersey', 'Trenton', '40.221741', '-74.756138'),
                  ('New Mexico', 'Santa Fe', '35.667231', '-105.964575'),
                  ('New York', 'Albany', '42.659829', '-73.781339'),
                  ('North Carolina', 'Raleigh', '35.771', '-78.638'),
                  ('North Dakota', 'Bismarck', '48.813343', '-100.779004'),
                  ('Ohio', 'Columbus', '39.962245', '-83.000647'),
                  ('Oklahoma', 'Oklahoma City', '35.482309', '-97.534994'),
                  ('Oregon', 'Salem', '44.931109', '-123.029159'),
                  ('Pennsylvania', 'Harrisburg', '40.269789', '-76.875613'),
                  ('Rhode Island', 'Providence', '41.82355', '-71.422132'),
                  ('South Carolina', 'Columbia', '34', '-81.035'),
                  ('South Dakota', 'Pierre', '44.367966', '-100.336378'),
                  ('Tennessee', 'Nashville', '36.165', '-86.784'),
                  ('Texas', 'Austin', '30.266667', '-97.75'),
                  ('Utah', 'Salt Lake City', '40.7547', '-111.892622'),
                  ('Vermont', 'Montpelier', '44.26639', '-72.57194'),
                  ('Virginia', 'Richmond', '37.54', '-77.46'),
                  ('Washington', 'Olympia', '47.042418', '-122.893077'),
                  ('West Virginia', 'Charleston', '38.349497', '-81.633294'),
                  ('Wisconsin', 'Madison', '43.074722', '-89.384444'),
                  ('Wyoming', 'Cheyenne', '41.145548', '-104.802042') ]

    total = cities.compute_total_distance(road_map1)
    expected = 9624.208366999157
    assert abs(expected - total) < epsilon

    total = cities.compute_total_distance(road_map2)
    expected = 3109.553973937813
    assert abs(expected - total) < epsilon

    total = cities.compute_total_distance(road_map3)
    expected = 0.0
    assert abs(expected - total) < epsilon

    total = cities.compute_total_distance(road_map4)
    expected = 58803.51773575106
    assert abs(expected - total) < epsilon


def test_swap_adjacent_cities():
    epsilon = 0.0000000000001
    road_map1 = [ ('Alabama', 'Montgomery', '32.361538', '-86.279118'),
                  ('Alaska', 'Juneau', '58.301935', '-134.41974'),
                  ('Arizona', 'Phoenix', '33.448457', '-112.073844'),
                  ('Arkansas', 'Little Rock', '34.736009', '-92.331122'),
                  ('California', 'Sacramento', '38.555605', '-121.468926') ]

    expected_map1 = [ ('Alaska', 'Juneau', '58.301935', '-134.41974'),
                      ('Alabama', 'Montgomery', '32.361538', '-86.279118'),
                      ('Arizona', 'Phoenix', '33.448457', '-112.073844'),
                      ('Arkansas', 'Little Rock', '34.736009', '-92.331122'),
                      ('California', 'Sacramento', '38.555605', '-121.468926') ]

    expected_map2 = [ ('California', 'Sacramento', '38.555605', '-121.468926'),
                      ('Alaska', 'Juneau', '58.301935', '-134.41974'),
                      ('Arizona', 'Phoenix', '33.448457', '-112.073844'),
                      ('Arkansas', 'Little Rock', '34.736009', '-92.331122'),
                      ('Alabama', 'Montgomery', '32.361538', '-86.279118') ]

    returned = cities.swap_adjacent_cities(road_map1, 0)
    new_road_map = returned[ 0 ]
    new_total_distance = returned[ 1 ]
    expected_total_distance = 8583.007779472131
    assert expected_map1 == new_road_map
    assert abs(expected_total_distance - new_total_distance) < epsilon

    returned = cities.swap_adjacent_cities(road_map1, 4)
    new_road_map = returned[ 0 ]
    new_total_distance = returned[ 1 ]
    expected_total_distance = 7011.754031768182
    assert expected_map2 == new_road_map
    assert abs(expected_total_distance - new_total_distance) < epsilon


def test_swap_cities():
    epsilon = 0.0000000000001
    road_map1 = [ ('Alabama', 'Montgomery', '32.361538', '-86.279118'),
                  ('Alaska', 'Juneau', '58.301935', '-134.41974'),
                  ('Arizona', 'Phoenix', '33.448457', '-112.073844'),
                  ('Arkansas', 'Little Rock', '34.736009', '-92.331122'),
                  ('California', 'Sacramento', '38.555605', '-121.468926') ]

    expected_map1 = [ ('Arkansas', 'Little Rock', '34.736009', '-92.331122'),
                      ('Alaska', 'Juneau', '58.301935', '-134.41974'),
                      ('Arizona', 'Phoenix', '33.448457', '-112.073844'),
                      ('Alabama', 'Montgomery', '32.361538', '-86.279118'),
                      ('California', 'Sacramento', '38.555605', '-121.468926') ]

    expected_map2 = [ ('Alabama', 'Montgomery', '32.361538', '-86.279118'),
                      ('Alaska', 'Juneau', '58.301935', '-134.41974'),
                      ('California', 'Sacramento', '38.555605', '-121.468926'),
                      ('Arkansas', 'Little Rock', '34.736009', '-92.331122'),
                      ('Arizona', 'Phoenix', '33.448457', '-112.073844') ]

    expected_map3 = [ ('Alabama', 'Montgomery', '32.361538', '-86.279118'),
                      ('Alaska', 'Juneau', '58.301935', '-134.41974'),
                      ('Arizona', 'Phoenix', '33.448457', '-112.073844'),
                      ('Arkansas', 'Little Rock', '34.736009', '-92.331122'),
                      ('California', 'Sacramento', '38.555605', '-121.468926') ]

    # Test case 1
    returned = cities.swap_cities(road_map1, 0, 3)
    new_road_map = returned[ 0 ]
    new_total_distance = returned[ 1 ]
    expected_total_distance = 9648.295805724285
    assert expected_map1 == new_road_map
    assert abs(expected_total_distance - new_total_distance) < epsilon

    # Test case 2
    returned = cities.swap_cities(road_map1, 2, 4)
    new_road_map = returned[ 0 ]
    new_total_distance = returned[ 1 ]
    expected_total_distance = 8583.007779472131
    assert expected_map2 == new_road_map
    assert abs(expected_total_distance - new_total_distance) < epsilon

    # Test case 3 (if index1==index2)
    returned = cities.swap_cities(road_map1, 3, 3)
    new_road_map = returned[ 0 ]
    new_total_distance = returned[ 1 ]
    expected_total_distance = 9624.208366999157
    assert expected_map3 == new_road_map
    assert abs(expected_total_distance - new_total_distance) < epsilon


def test_shortest_city_to_city_map():
    # epsilon = 0.0000000000001
    road_map1 = [ ('Alabama', 'Montgomery', '32.361538', '-86.279118'),
                  ('Alaska', 'Juneau', '58.301935', '-134.41974'),
                  ('Arizona', 'Phoenix', '33.448457', '-112.073844'),
                  ('Arkansas', 'Little Rock', '34.736009', '-92.331122'),
                  ('California', 'Sacramento', '38.555605', '-121.468926') ]

    road_map1_total_distance = cities.compute_total_distance(road_map1)
    new_road_map = cities.shortest_city_to_city_map(road_map1)[ 0 ]
    new_total_distance = cities.compute_total_distance(new_road_map)

    # Checks that the return value is an improvement.
    assert (road_map1_total_distance >= new_total_distance)


def test_find_best_cycle():
    # epsilon = 0.0000000000001
    road_map1 = [ ('Alabama', 'Montgomery', '32.361538', '-86.279118'),
                  ('Alaska', 'Juneau', '58.301935', '-134.41974'),
                  ('Arizona', 'Phoenix', '33.448457', '-112.073844'),
                  ('Arkansas', 'Little Rock', '34.736009', '-92.331122'),
                  ('California', 'Sacramento', '38.555605', '-121.468926') ]

    road_map1_total_distance = 9624.208366999157
    new_road_map = cities.find_best_cycle(road_map1)
    new_total_distance = cities.compute_total_distance(new_road_map)

    # Checks that `new_road_map` is different.
    assert road_map1 != new_road_map
    # Checks that the return value is an improvement.
    assert (road_map1_total_distance > new_total_distance)
    # Checks that the `new_total_distance` value is less than the original.
    assert new_total_distance < road_map1_total_distance
