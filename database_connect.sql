CREATE DATABASE supplier;
conn = psycopg2.connect("dbname=supplier user=postgres password=123456")
conn = psycopg2.connect(
    host="localhost"
    database="supplier"
    user="postgres"
    password="123456"
)