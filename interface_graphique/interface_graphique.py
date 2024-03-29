import tkinter as tk
from tkinter import ttk
from gestion_livres.gestionnaire_livres import GestionnaireLivres
from gestion_utilisateurs.gestionnaire_utilisateurs import GestionnaireUtilisateurs
from pret_retour.gestionnaire_prets import GestionnairePrets

class InterfaceGraphique:
    def __init__(self, master, gestionnaire_livres, gestionnaire_utilisateurs, gestionnaire_prets):
        self.master = master
        self.gestionnaire_livres = gestionnaire_livres
        self.gestionnaire_utilisateurs = gestionnaire_utilisateurs
        self.gestionnaire_prets = gestionnaire_prets

        self.master.title("Application de Gestion de Bibliothèque")
        self.master.geometry("900x700")  # Taille de la fenêtre


        self.listbox_prets = tk.Listbox(self.master, height=1, width=200)
        self.listbox_prets.pack(pady=5)


        self.actualiser_liste_prets()

        # Couleurs
        couleur_principale = "#3b5998"  # Bleu foncé
        couleur_texte = "#FFFFFF"  # Blanc
        couleur_bouton_texte = "#2d4262"  # Bleu plus foncé pour le texte des boutons
        couleur_bouton_fond = "#4a6fa5"  # Bleu un peu plus clair pour le fond des boutons

        # Style
        style = ttk.Style()
        style.configure("TFrame", background=couleur_principale)
        style.configure("TButton", background=couleur_bouton_fond, foreground=couleur_bouton_texte, font=("Helvetica", 12, "bold"))
        style.configure("TLabel", background=couleur_principale, foreground=couleur_texte, font=("Helvetica", 12, "italic bold"))
        style.map("TButton", background=[("active", "#335080")])

        # Titre en haut de l'interface
        label_titre = ttk.Label(self.master, text="BIBLIOTHEQUE EN LIGNE EPSI", style="TLabel")
        label_titre.pack(pady=10)

        # Listebox pour afficher les livres
        self.listbox_livres = tk.Listbox(self.master, height=10, width=50)
        self.listbox_livres.pack(pady=10)

        # Boutons pour les différentes fonctionnalités
        self.bouton_ajouter_livre = ttk.Button(self.master, text="Ajouter un livre", command=self.afficher_fenetre_ajout_livre)
        self.bouton_ajouter_livre.pack(pady=3)

        self.bouton_supprimer_livre = ttk.Button(self.master, text="Supprimer un livre", command=self.afficher_fenetre_suppression_livre)
        self.bouton_supprimer_livre.pack(pady=3)

        self.bouton_modifier_livre = ttk.Button(self.master, text="Modifier un livre", command=self.afficher_fenetre_modification_livre)
        self.bouton_modifier_livre.pack(pady=3)

        self.bouton_rechercher_livres = ttk.Button(self.master, text="Rechercher des livres", command=self.rechercher_livres)
        self.bouton_rechercher_livres.pack(pady=3)

        self.bouton_lister_livres = ttk.Button(self.master, text="Lister les livres", command=self.lister_livres)
        self.bouton_lister_livres.pack(pady=3)

        # Boutons pour les fonctionnalités de gestion des utilisateurs
        self.bouton_ajouter_utilisateur = ttk.Button(self.master, text="Ajouter un utilisateur", command=self.afficher_fenetre_ajout_utilisateur)
        self.bouton_ajouter_utilisateur.pack(pady=3)

        self.bouton_modifier_utilisateur = ttk.Button(self.master, text="Modifier un utilisateur", command=self.afficher_fenetre_modification_utilisateur)
        self.bouton_modifier_utilisateur.pack(pady=3)

        self.bouton_lister_utilisateurs = ttk.Button(self.master, text="Lister les utilisateurs", command=self.lister_utilisateurs)
        self.bouton_lister_utilisateurs.pack(pady=3)

        # Affiche initialement la liste des livres
        self.afficher_liste_livres_initiale()

        self.bouton_effectuer_pret = ttk.Button(self.master, text="Effectuer un prêt",
                                                command=self.afficher_fenetre_pret)
        self.bouton_effectuer_pret.pack(pady=3)

        self.bouton_effectuer_retour = ttk.Button(self.master, text="Effectuer un retour",
                                                  command=self.afficher_fenetre_retour)
        self.bouton_effectuer_retour.pack(pady=3)

        self.bouton_lister_prets = ttk.Button(self.master, text="Lister les prêts", command=self.lister_prets)
        self.bouton_lister_prets.pack(pady=3)

    def afficher_liste_livres_initiale(self):
        livres_initiaux = [
            "LE MARBRE",
            "LE PLEURER RIRE",
            "AGOSTINO NETO",
            "LES FABLES",
            "MATHEMATIQUES SCIENCES",
            "ALGORITHME",
            "DEVELOPPEMENT WEB"
        ]

        for livre in livres_initiaux:
            self.gestionnaire_livres.ajouter_livre(livre, "", "", "")  # Ajoute les livres au gestionnaire
            self.listbox_livres.insert(tk.END, livre)  # Ajoute les livres à la Listbox

    def afficher_fenetre_ajout_livre(self):
        fenetre_ajout = tk.Toplevel(self.master)
        fenetre_ajout.title("Ajouter un livre")

        tk.Label(fenetre_ajout, text="Titre :").pack(pady=5)
        entry_titre = tk.Entry(fenetre_ajout, width=30)
        entry_titre.pack(pady=5)

        tk.Label(fenetre_ajout, text="Auteur :").pack(pady=5)
        entry_auteur = tk.Entry(fenetre_ajout, width=30)
        entry_auteur.pack(pady=5)

        tk.Label(fenetre_ajout, text="Genre :").pack(pady=5)
        entry_genre = tk.Entry(fenetre_ajout, width=30)
        entry_genre.pack(pady=5)

        tk.Label(fenetre_ajout, text="ISBN :").pack(pady=5)
        entry_isbn = tk.Entry(fenetre_ajout, width=30)
        entry_isbn.pack(pady=5)

        bouton_enregistrer = ttk.Button(fenetre_ajout, text="Enregistrer", command=lambda: self.ajouter_livre_saisie(entry_titre.get(), entry_auteur.get(), entry_genre.get(), entry_isbn.get(), fenetre_ajout))
        bouton_enregistrer.pack(pady=10)

    def ajouter_livre_saisie(self, titre, auteur, genre, isbn, fenetre):
        self.gestionnaire_livres.ajouter_livre(titre, auteur, genre, isbn)
        self.actualiser_liste_livres()
        fenetre.destroy()
        print("Livre ajouté avec succès!")

    def afficher_fenetre_modification_livre(self):
        fenetre_modification = tk.Toplevel(self.master)
        fenetre_modification.title("Modifier un livre")

        tk.Label(fenetre_modification, text="Ancien Titre :").pack(pady=5)
        entry_ancien_titre = tk.Entry(fenetre_modification, width=30)
        entry_ancien_titre.pack(pady=5)

        tk.Label(fenetre_modification, text="Nouveau Titre :").pack(pady=5)
        entry_nouveau_titre = tk.Entry(fenetre_modification, width=30)
        entry_nouveau_titre.pack(pady=5)

        tk.Label(fenetre_modification, text="Auteur :").pack(pady=5)
        entry_auteur = tk.Entry(fenetre_modification, width=30)
        entry_auteur.pack(pady=5)

        tk.Label(fenetre_modification, text="Genre :").pack(pady=5)
        entry_genre = tk.Entry(fenetre_modification, width=30)
        entry_genre.pack(pady=5)

        tk.Label(fenetre_modification, text="ISBN :").pack(pady=5)
        entry_isbn = tk.Entry(fenetre_modification, width=30)
        entry_isbn.pack(pady=5)

        bouton_enregistrer_modification = ttk.Button(fenetre_modification, text="Enregistrer", command=lambda: self.modifier_livre_saisie(entry_ancien_titre.get(), entry_nouveau_titre.get(), entry_auteur.get(), entry_genre.get(), entry_isbn.get(), fenetre_modification))
        bouton_enregistrer_modification.pack(pady=10)

    def modifier_livre_saisie(self, ancien_titre, nouveau_titre, auteur, genre, isbn, fenetre):
        self.gestionnaire_livres.modifier_livre(ancien_titre, nouveau_titre, auteur, genre, isbn)
        self.actualiser_liste_livres()
        fenetre.destroy()
        print("Livre modifié avec succès!")

    def afficher_fenetre_suppression_livre(self):
        fenetre_suppression = tk.Toplevel(self.master)
        fenetre_suppression.title("Supprimer un livre")

        tk.Label(fenetre_suppression, text="Titre :").pack(pady=5)
        entry_titre = tk.Entry(fenetre_suppression, width=30)
        entry_titre.pack(pady=5)

        bouton_supprimer = ttk.Button(fenetre_suppression, text="Supprimer", command=lambda: self.supprimer_livre_saisie(entry_titre.get(), fenetre_suppression))
        bouton_supprimer.pack(pady=10)

    def supprimer_livre_saisie(self, titre, fenetre):
        self.gestionnaire_livres.supprimer_livre(titre)
        self.actualiser_liste_livres()
        fenetre.destroy()
        print("Livre supprimé avec succès!")

    def afficher_fenetre_ajout_utilisateur(self):
        fenetre_ajout_utilisateur = tk.Toplevel(self.master)
        fenetre_ajout_utilisateur.title("Ajouter un utilisateur")

        tk.Label(fenetre_ajout_utilisateur, text="Nom :").pack(pady=5)
        entry_nom = tk.Entry(fenetre_ajout_utilisateur, width=30)
        entry_nom.pack(pady=5)

        tk.Label(fenetre_ajout_utilisateur, text="Prénom :").pack(pady=5)
        entry_prenom = tk.Entry(fenetre_ajout_utilisateur, width=30)
        entry_prenom.pack(pady=5)

        tk.Label(fenetre_ajout_utilisateur, text="Catégorie :").pack(pady=5)
        entry_categorie = tk.Entry(fenetre_ajout_utilisateur, width=30)
        entry_categorie.pack(pady=5)

        bouton_enregistrer_utilisateur = ttk.Button(fenetre_ajout_utilisateur, text="Enregistrer", command=lambda: self.ajouter_utilisateur_saisie(entry_nom.get(), entry_prenom.get(), entry_categorie.get(), fenetre_ajout_utilisateur))
        bouton_enregistrer_utilisateur.pack(pady=10)

    def ajouter_utilisateur_saisie(self, nom, prenom, categorie, fenetre):
        self.gestionnaire_utilisateurs.ajouter_utilisateur(nom, prenom, categorie)
        self.actualiser_liste_utilisateurs()
        fenetre.destroy()
        print("Utilisateur ajouté avec succès!")

    def afficher_fenetre_modification_utilisateur(self):
        # Code pour afficher une fenêtre permettant de modifier un utilisateur
        pass

    def lister_utilisateurs(self):
        liste_des_utilisateurs = self.gestionnaire_utilisateurs.lister_utilisateurs()
        self.afficher_resultats(liste_des_utilisateurs)

    def actualiser_liste_utilisateurs(self):
        # Code pour actualiser la liste des utilisateurs dans l'interface
        pass

    def rechercher_livres(self):
        critere = input("Critère de recherche (titre/auteur/isbn) : ").lower()
        valeur = input("Valeur de recherche : ")

        resultats = self.gestionnaire_livres.rechercher_livres(critere, valeur)
        self.afficher_resultats(resultats)

    def lister_livres(self):
        liste_des_livres = self.gestionnaire_livres.lister_livres()
        self.afficher_resultats(liste_des_livres)

    def afficher_resultats(self, resultats):
        self.listbox_livres.delete(0, tk.END)  # Efface les anciens résultats

        if not resultats:
            self.listbox_livres.insert(tk.END, "Aucun résultat trouvé.")
        else:
            for livre in resultats:
                self.listbox_livres.insert(tk.END, livre)

    #####

    def afficher_fenetre_pret(self):
        fenetre_pret = tk.Toplevel(self.master)
        fenetre_pret.title("Prêt de Livre")

        tk.Label(fenetre_pret, text="Titre du livre :").pack(pady=5)
        entry_titre = tk.Entry(fenetre_pret, width=30)
        entry_titre.pack(pady=5)

        tk.Label(fenetre_pret, text="Nom de l'emprunteur :").pack(pady=5)
        entry_emprunteur = tk.Entry(fenetre_pret, width=30)
        entry_emprunteur.pack(pady=5)

        bouton_pret = ttk.Button(fenetre_pret, text="Prêter",
                                 command=lambda: self.effectuer_pret(entry_titre.get(), entry_emprunteur.get(),
                                                                     fenetre_pret))
        bouton_pret.pack(pady=10)

    def effectuer_pret(self, titre, emprunteur, fenetre):
        if self.gestionnaire_prets.livre_deja_emprunte(titre):
            print("Ce livre est déjà emprunté.")
        else:
            # Utilisez la méthode correcte du gestionnaire de prêts (enregistrer_pret)
            self.gestionnaire_prets.enregistrer_pret(titre, emprunteur)
            self.actualiser_liste_prets()
            fenetre.destroy()
            print("Prêt effectué avec succès!")

    def afficher_fenetre_retour(self):
        fenetre_retour = tk.Toplevel(self.master)
        fenetre_retour.title("Retour de Livre")

        tk.Label(fenetre_retour, text="Titre du livre :").pack(pady=5)
        entry_titre = tk.Entry(fenetre_retour, width=30)
        entry_titre.pack(pady=5)

        tk.Label(fenetre_retour, text="Nom de l'emprunteur :").pack(pady=5)
        entry_utilisateur = tk.Entry(fenetre_retour, width=30)  # Ajoutez cette ligne pour le nom de l'utilisateur
        entry_utilisateur.pack(pady=5)

        bouton_retour = ttk.Button(fenetre_retour, text="Retourner",
                                   command=lambda: self.effectuer_retour(entry_titre.get(), entry_utilisateur.get(),
                                                                         fenetre_retour))
        bouton_retour.pack(pady=10)

    def effectuer_retour(self, titre, utilisateur, fenetre):
        if self.gestionnaire_prets.livre_emprunte(titre):
            self.gestionnaire_prets.retour_livre(titre, utilisateur)
            self.actualiser_liste_prets()
            fenetre.destroy()
            print("Retour effectué avec succès!")
        else:
            print("Ce livre n'est pas actuellement emprunté.")
    def lister_prets(self):
        liste_des_prets = self.gestionnaire_prets.lister_prets()
        self.afficher_resultats(liste_des_prets)


    def actualiser_liste_prets(self):
        # Efface les anciens résultats
        self.listbox_prets.delete(0, tk.END)

        # Récupère la liste des prêts en utilisant la méthode appropriée
        liste_des_prets = self.gestionnaire_prets.lister_prets()

        # Affiche la liste des prêts dans la Listbox
        for pret in liste_des_prets:
            self.listbox_prets.insert(tk.END, pret)

    def actualiser_liste_livres(self):
        pass


def main():
    root = tk.Tk()
    gestionnaire_livres = GestionnaireLivres()
    gestionnaire_utilisateurs = GestionnaireUtilisateurs()
    gestionnaire_prets = GestionnairePrets()

    app = InterfaceGraphique(root, gestionnaire_livres, gestionnaire_utilisateurs, gestionnaire_prets)
    root.mainloop()

if __name__ == "__main__":
    main()
