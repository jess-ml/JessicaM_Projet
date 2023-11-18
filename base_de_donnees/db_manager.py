import sqlite3

class DatabaseManager:
    def _init_(self, db_file="bibliotheque.db"):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def creer_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS livres (
                id INTEGER PRIMARY KEY,
                titre TEXT,
                auteur TEXT,
                genre TEXT,
                isbn TEXT
            )
        """)
        

    def sauvegarder_livre(self, livre):
        self.cursor.execute("INSERT INTO livres VALUES (?, ?, ?, ?, ?)", (livre.id, livre.titre, livre.auteur, livre.genre, livre.isbn))
        self.conn.commit()

db_manager = DatabaseManager()
db_manager.creer_tables()
