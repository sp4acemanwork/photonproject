import psycopg2


class database_handler:
    def __init__(self) -> None:
        self.__conn = psycopg2.connect(dbname="photon", user="postgres",password="1234", host="localhost", port="5432")
        self.cur = self.__conn.cursor()

    # add a player
    def add_player(self, player_tuple) -> None:
        if not self.player_exists(player_tuple[0]):
            self.cur.execute("""
                INSERT INTO players (id, codename)
                VALUES (%s, %s);
                """, (player_tuple[0], player_tuple[1]))
            self.__conn.commit()
        else:
            self.update_player(player_tuple[0], player_tuple[1])

    def get_player(self, player_id: int) -> tuple[int, str]:
        self.cur.execute(f"select * from players where id = {player_id}")
        row = self.cur.fetchall()
        player = (row[0][0], row[0][1])
        return player

    # delete a player
    def delete_player(self, del_id: int) -> None:
        self.cur.execute(f"delete from players where id = {del_id}")
        self.__conn.commit()
    # Commit the transaction (this is necessary to save the changes)

    # print database
    def print_table(self) -> None:
        print("{:10.10} {:20.20}".format("PLayer ID", "Username"))
        self.cur.execute("SELECT * FROM players ;")
        rows = self.cur.fetchall()

        for row in rows:
            print(f"{row[0]: <10} {row[1]:<20} \n")

    # print database
    def __str__(self) -> None:
        print("{:10.10} {:20.20}".format("Player ID", "Username"))
        output = ""
        self.cur.execute("SELECT * FROM players LIMIT 5;")
        rows = self.cur.fetchall()
        for row in rows:
            output += f"{row[0]: <10} {row[1]:<20} \n"
        return output

    def close(self) -> None:
        # Close the connection
        self.cur.close()
        self.__conn.close()

    def __len__(self) -> int:
        self.cur.execute("select count(*) from players")
        rows = self.cur.fetchall()
        return (rows[0][0])
    
    def clear(self):
        self.cur.execute("DELETE FROM players")
        self.__conn.commit()

    def player_exists(self, player_id: int) -> bool:
        self.cur.execute("SELECT COUNT(*) FROM players WHERE id = %s;", (player_id,))
        count = self.cur.fetchone()[0]
        return count > 0
    
    def update_player(self, player_id: int, new_codename: str) -> None:
        self.cur.execute("""
            UPDATE players 
            SET codename = %s 
            WHERE id = %s;
        """, (new_codename, player_id))
        self.__conn.commit()

   
test = database_handler()
test.clear()
test.print_table()
# test.get_player(1)
# test.close()
