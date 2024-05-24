import psycopg2
import yaml
import pandas as pd
import psycopg2.extras as extras
from io import StringIO
import sys


def test_connection():

	with open('config.yml') as file:
		config = yaml.safe_load(file)

	try:
		conn = psycopg2.connect(database=config['default']['DB_NAME'],
								user=config['default']['DB_USER'],
								password=config['default']['DB_PASS'],
								host=config['default']['DB_HOST'],
								port=config['default']['DB_PORT'],
								options=f'-c search_path=pokebase')

		print("Database connected successfully")

		return conn
	except:
		print("Database not connected successfully")



def create(conn, table):
	print("Attempting to create table(s)...")
	# table name also equals the column name
	# api suggests two columns per connection: id, column_name
	# order is not guaranteed

	t = list(table.columns)
	t.remove("id")

	cur = conn.cursor()
	query = """SELECT EXISTS (
		SELECT 1
			FROM information_schema.tables
		WHERE table_name = '{}'
	) AS table_existence;""".format(t[0])

	cur.execute(query)

	if bool(cur.fetchone()[0]):
		print("pokebase.{} table exists in postgreSQL. Moving on...".format(t[0]))

	else:
		print('pokebase.{} does not exist in postgreSQL. Attempting to create this table now...'.format(t[0]))

		query ="""CREATE TABLE IF NOT EXISTS pokebase.{tbl}(
		ID INT PRIMARY KEY NOT NULL, 
		{col} VARCHAR ( 255 ) NOT NULL
		);""".format(tbl = t[0], col = t[0])

		try:
			cur = conn.cursor()
			cur.execute(query)
			# commit the changes
			conn.commit()

		except (Exception, psycopg2.DatabaseError) as error:
			print(error)

	return t


def insert_pre_check(conn, col):
	print("Confirm if table is empty or not.")
	query = """select exists(select 1 from pokebase.{});""".format(col[0])

	try:
		cur = conn.cursor()
		cur.execute(query)
		check = cur.fetchone()[0]
		if check is True:
			print("pokebase.{} is already populated. No need to insert.".format(col[0]))

	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
		conn.close() 

	return check



def insert(conn, table, col):

    check = insert_pre_check(conn, col)
    if check is False:
        """
        Using cursor.executemany() to insert the dataframe.
        Find a way to update current timestamp
        """
        print("Attempting to populate the tables...")
        c = col[0]
        #can i create a new col here with current_timestamp
        df = table[["id",c]]

        buffer = StringIO()
        df.to_csv(buffer, header=False, index = False)
        buffer.seek(0)
    
        cur = conn.cursor()
        #cur.execute("""TRUNCATE pokebase.{};""".format(c))
        try:
            cur.copy_from(buffer, c, sep=",")
            print("Data inserted using copy_from_datafile_StringIO() successfully....")
            cur.close()
            conn.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            print("Error: %s" % error)
            conn.rollback()
            cur.close()
            return 1

    cur.close()

    insert_post_check(conn, col)

def insert_post_check(conn, col):
	print("Validate the insert statements.")


	query = """select exists(select 1 from pokebase.{});""".format(col[0])

	try:
		cur = conn.cursor()
		cur.execute(query)
		check = cur.fetchone()[0]
		if check is True:
			print("pokebase.{} is good to go".format(col[0]))
		else:
			print("Something went wrong with pokebase.{} You'll need to investigate further...".format(col[0]))

	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
		conn.close() 
#def update():

if __name__ == "__main__":
	test_connection()
	set_globals()
	print(globals())
