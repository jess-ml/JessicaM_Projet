class Utilisateur:
    def _init_(self, nom, prenom, categorie):
        self.nom = nom
        self.prenom = prenom
        self.categorie = categorie

    def _str_(self):
        return f"{self.prenom} {self.nom} ({self.categorie})"
