import psycopg2


class Database:
    def __init__(self) -> None:
        self.__conn = psycopg2.connect(dbname="photon", user="postgres", host="localhost",  port="5432")
        self.cur = self.__conn.cursor()

        
    # add a player 
    def add_player(self, player_tuple: tuple[int, str]) -> None:
        self.cur.execute("""
            INSERT INTO players (id, codename) 
            VALUES (%s, %s);
            """, ( player_tuple[0], player_tuple[1]))
        self.__conn.commit()
        

    # delete a player
    def delete_player(self,del_id: int) -> None:
        self.cur.execute(f"delete from players where id = {del_id}")
        self.__conn.commit()
    # Commit the transaction (this is necessary to save the changes)

    # print database
    def print_table(self) -> None:
        self.cur.execute("SELECT * FROM players LIMIT 5;")
        rows = self.cur.fetchall()

        for row in rows:
            print(row)


    def close(self) -> None:
        # Close the connection
        self.cur.close()
        self.__conn.close()

#player = (4, 'james')
# test = Database()
# test.delete_player(4)
# test.print_table()
# test.close()