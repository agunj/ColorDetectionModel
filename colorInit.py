import sqlite3

def initialize_database(db_path, sql_file):
    # Connect to the SQLite database (it will create the file if it doesn't exist)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Read and execute the SQL script
    with open(sql_file, 'r') as file:
        sql_script = file.read()

    cursor.executescript(sql_script)  # Execute the whole SQL script

    # Commit changes and close the connection
    conn.commit()
    conn.close()
    print(f"Database at '{db_path}' initialized and populated with data from '{sql_file}'.")

if __name__ == "__main__":
    # Initialize the original RGB colors database
    initialize_database('colors.db', 'colors.sql')

    # Initialize the new HSV colors database
    initialize_database('broad_colors.db', 'colorsHSV.sql')
