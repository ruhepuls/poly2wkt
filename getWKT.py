import os

from poly2wkt import parse_poly

dir = 'C:\\Users\\flori\\Documents\\Github\\poly2wkt\\poly\\'
stmt="insert into poly(name, geom) select '{name}',st_geomfromtext('{geojson}');"

f = open("poly.sql", "a")
f.write("create table poly(id serial, name text, geom geometry(MULTIPOLYGON,4326));")
f.write("create index idx_poly on poly using gist(geom);")

for filename in os.listdir(dir):
    if filename.endswith(".poly"):
        file = open(os.path.join(dir, filename))
        geojson = parse_poly(file)
        f.write(stmt.format(name=filename.replace('.poly',''),geojson=geojson))
        continue
    else:
        continue

f.close()