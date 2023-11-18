class Utilisateur:
    def __init__(self, nom, prenom, categorie):
        self.nom = nom
        self.prenom = prenom
        self.categorie = categorie

    def __str__(self):
        return f"{self.prenom} {self.nom} ({self.categorie})"


class GestionnaireUtilisateurs:
    def __init__(self):
        self.utilisateurs = []

    def ajouter_utilisateur(self, nom, prenom, categorie):
        nouvel_utilisateur = Utilisateur(nom, prenom, categorie)
        self.utilisateurs.append(nouvel_utilisateur)

    def lister_utilisateurs(self):
        return [str(utilisateur) for utilisateur in self.utilisateurs]


