from datetime import datetime, timedelta


class PretRetour:
    def _init_(self, livre, utilisateur, date_emprunt):
        self.livre = livre
        self.utilisateur = utilisateur
        self.date_emprunt = date_emprunt
        self.date_retour = None

    def retourner_livre(self):
        self.date_retour = datetime.now()

    def est_en_retard(self):
        if self.date_retour is None:
            return False
        date_limite_retour = self.date_emprunt + timedelta(days=14)  # Exemple : 14 jours pour retourner le livre
        return datetime.now() > date_limite_retour
