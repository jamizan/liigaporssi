import mysql.connector
import parseData


# Function to store statistics in MySQL
def store_statistics_in_mysql(stats):
    # Database connection
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="liiga"
    )
    cursor = db.cursor()

    # Create table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS pelaajat (
                    pelaajanNimi VARCHAR(255),
                    joukkue VARCHAR(255),
                    maali int,
                    syotto int,
                    plusmiinus int,
                    jaahymin int,
                    laukaukset int,
                    taklaukset int,
                    blokkaukset int,
                    aloitukset int
                      )''')

    # drop indexes 4,9,10,11,13,14

    realStats = [stats[0], stats[1], stats[2], stats[3], stats[5], stats[6], stats[7], stats[8], stats[9], stats[12]]

    # Insert data into the table
    for i in range(1):
        cursor.execute('''INSERT INTO pelaajat (pelaajanNimi, joukkue, maali, syotto, plusmiinus, jaahymin, laukaukset, taklaukset, blokkaukset, aloitukset) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''', realStats)

    # Commit and close
    db.commit()
    cursor.close()
    db.close()

def main():
    stats = parseData.main()

    x = 0
    length = len(stats)

    while x < length:
        store_statistics_in_mysql(stats[x])
        x += 1

if __name__ == '__main__':
    main()

