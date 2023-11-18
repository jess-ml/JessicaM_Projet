# gestionnaire_prets.py
from datetime import datetime, timedelta

class GestionnairePrets:
    def __init__(self):
        self.prets = []

    def enregistrer_pret(self, livre, utilisateur):
        date_pret = datetime.now()
        date_retour_prevue = date_pret + timedelta(days=14)  # Exemple : Retour prévu dans 14 jours
        pret = {'livre': {'titre': livre}, 'utilisateur': utilisateur, 'date_pret': date_pret, 'date_retour_prevue': date_retour_prevue}
        self.prets.append(pret)
        return pret


    def retour_livre(self, livre, utilisateur):
        for pret in self.prets:
            if pret['livre'] == livre and pret['utilisateur'] == utilisateur:
                pret['date_retour'] = datetime.now()
                return pret
        return None

    def lister_prets_en_cours(self):
        return [pret for pret in self.prets if 'date_retour' not in pret]

    def lister_retards(self):
        date_actuelle = datetime.now()
        retards = [pret for pret in self.prets if 'date_retour' not in pret and date_actuelle > pret['date_retour_prevue']]
        return retards

    def lister_prets(self):
        return self.prets

    def livre_deja_emprunte(self, titre):
        for pret in self.prets:
            if pret['titre'] == titre:
                return True
        return False

    def livre_emprunte(self, titre):
        for pret in self.prets:
            if pret['livre']['titre'] == titre and 'date_retour' not in pret:
                return True
        return False