from collections import Counter

class GenerateurRapports:
    def _init_(self, gestionnaire_prets):
        self.gestionnaire_prets = gestionnaire_prets

    def generer_rapport_emprunts(self):
        emprunts = self.gestionnaire_prets.prets
        livres_empruntes = [pret.livre for pret in emprunts]
        livres_populaires = [livre for livre, count in Counter(livres_empruntes).items() if count > 1]
        return livres_populaires
