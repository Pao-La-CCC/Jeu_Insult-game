import random
import copy

from player import Player
from ninja import Ninja
from chipeur import Chipeur
from inspector_gadget import Inspector
from greatMother import GreatMother



var_groupe_sujet =  ["Ta mère", "Les corbeaux ", "Tes shurikens", "Tes enfants", "leur maman", "Je", "l’ère médiévale",
                     "les films", "les taupes", "tu", "toi", "un aimant", "ils"]

var_groupe_verbale =["ne sait pas", "ressemble", "te prennent", "ressemblent", "ne connaissent pas", "n’a jamais vu",
                      "crois", "t'es trompé", "est", "terminée", "peux", "enlever", "sont", "passés", "agissent", "es",
                      "n'es", "tu t'es habillé", "allais à", "es", "tu te lève", "vois", "ont pitié", "il faut",
                      "trouver", "trouver", "devais parier", "mettrais", "laisses", "c'est", "as essayé", "n'as",
                      "réussi", "n'es pas", "est", "faudrait", "fasses", "sont" ]


var_groupe_nominale_adjetif  = ["futé", "habits noirs", "normal", "rapide", "efficace", "le pire", "ninjas",
                                "ni rapide", "ni discret", "si lente", "suffisante", "tellement mal", "la tortue",
                                "le petit poucet", "le pire", "nouveau", "Pokémon", "mi-homme", "mi-objet",
                                "un renard", "Suisse", "Multifonction", "mi-homme", "mi-tirebouchon", "humoriste",
                                "inspecteur", "efficace", "une arme", "tes gadgets", "technologies", "Antique"]

var_comp_cod_coi = ["de ton masque", "son propre enfant", "mes décorations de noël", "leur père", "ton visage",
                     "d’époque", "ton costume", "de Jackie Chan", "Les ninjas", "tout le contraire", "de toi",
                     "tes rides", "une carte", "tes yeux", "ta bouche", "entre toi", "une tortue", "mon argent",
                     "les voleurs", "une mise à jour", "des traces", "les qualités"]

var_preposition = ["à quoi", "pour", "à", "sur", "parmi", "que d'un", "de", "dans", "avec", "en", "par","jusque","jusqu’à","pendant"]

var_conjonction = ["mais", "où", "et", "donc", "or", "ni", "car", "à cause", "que", "à cause de", "comme si",
                    "pour que", "comme", "si", "avec", "plus"]

big_dictionnary = {

    "groupe_sujet": var_groupe_sujet,
   
    "groupe_verbale": var_groupe_verbale,

    "groupe_nominale_adjetif": var_groupe_nominale_adjetif ,

    "comp_cod_coi": var_comp_cod_coi,

    "preposition": var_preposition ,

    "conjonction": var_conjonction,

}

list_choice_player1 = { }
list_stocker = { }
phrase_final1 = [ ]
phrase_final2 = [ ]
check_position = [ ]
check_position2 = [ ]


def Menu():
    print("_____________________________________________________________________________________________\n"
          "                 ---------------------Insult Game--------------------\n"
          "                 1: Create new game\n"
          "                 2: About\n"
          "                 3: Exit\n"
          "                 _____________________________________________________\n"
          "_____________________________________________________________________________________________")
    choice_menu = str(input("                 |   Appuyer sur 1 pour commencer la partie.    |\n"
                      "                 |   Appuyer sur 2 pour en savoir plus.         |\n"
                      "                 |   Appuyer sur 3 pour quitter.                |\n"
                      "_____________________________________________________________________________________________\n"
                     " |C'est à vous de choisir:"))
    if choice_menu == "1":
        step1game()
    elif choice_menu == "2":
        about()
    else:
        exit()

def step1game():
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------\n"
          "--------------->Bienvenue dans Insult Game. Le but du Jeu mettre K.O votre adversaire en sortant des insultes les percutantes possibles. <---------------\n"
          "----------------------------------------------------------------------------------------------------------------------------------------------------------")
    player1 = str(input("  -----------------------------------------------------\n "
                        "|Premier compétiteur, Votre Prénom s'il vous plait : "))
    player2 = str(input(" |Second compétiteur, Votre Prénom s'il vous plait : "))
    print("  -----------------------------------------------------")
    print("                                     |Attention", player1, " &", player2,"|\n"
          " |le jeu va commencer et rien de vous sera épagné. Prenez vos mouchoirs et vos anti-dépresseurs. \n"
          " |Prévenez votre Mama car ça va faire mal.\n"
          "-----------------------------------------------------")

    fist_to_choice(player1, player2)

def about():
    print("Insult Game, Le Jeu de l'année 2020/2021 développé par les étudiants Paola,Abdullah,Ibrahim et Tania et de l'Ecole HETIC")

def exit():
    quit()


def fist_to_choice(base1, base2):
    print("Nous allons définir quel joueur va commencer par un système de dés à 6 faces. Si le nombre est pair c'est",
          base1, "qui commence. Au contraire si c'est impair c'est ", base2, " qui débute la partie.")
    print("Commençons  ! ")
    print("")
    hazard = random.randint(1, 10)
        #Tirage au sort du joueur qui débute la partie
    if hazard % 2 == 0:
        print("---", base1, "c'est vous qui commencez en tant que Joueur 1")
        beginner_player = base1  # -- Prenom joueur 1
        second_player = base2  # -- Prenom joueur 2
        select_caractere_part1(beginner_player, second_player)
        while (player_one.Life > 0) and (player_two.Life > 0):
            first(big_dictionnary, phrase_final1, beginner_player, second_player, player_one, player_two)
            second(big_dictionnary, phrase_final1, beginner_player, second_player, player_one, player_two)

    else:
        print("---", base2, "c'est vous qui commencez en tant que Joueur 2 ")
        beginner_player = base2  # -- Prenom joueur 1
        second_player = base1  # -- Prenom joueur 2
        select_caractere_part1(beginner_player, second_player)
        while (player_one.Life > 0) and (player_two.Life > 0):
            first(big_dictionnary, phrase_final1, beginner_player, second_player, player_one, player_two)
            second(big_dictionnary, phrase_final1, beginner_player, second_player, player_one, player_two)




#Fonction pour supprimer les élements séléctionnés par les joueurs du dictionnaire
def delete_from_big_dictionnary(value):
    for key in big_dictionnary:
        if value in big_dictionnary[key]:
            big_dictionnary[key].remove(value)



#Fonction pour le choix du personnage du joueur 1
def select_caractere_part1(base_player, second_player):
    global player_one
    second_player = second_player
    dict_object = [Ninja("Ninja Ryouk", 100, 0), Chipeur("Chipeur Roukin", 100, 0), GreatMother("Grand-mère", 100, 0),
                   Inspector("L'inspecteur gadget", 100, 0)]
    list = ["Le Ninja", "Chiffeur le Renard ", "Pour La Grand-Mère", "Pour Inspecteur Gadget", ]
    list_choice = [1, 2, 3, 4]

    for x, y in enumerate(list):
        plus = x + 1
        print("Pour :", plus, ":", y)
    print("--->",base_player, ",Merci de choisir un personnage en sélectionnant l'indice associé à ce dernier : ")
    choice = int(input())
    if choice in list_choice:
        for i in range(len(list)):  # Sélection du personnage selon choix affiché
            more = i + 1
            if choice == more:
                for y in range(len(dict_object)):  # Attribution
                    more_two = y + 1
                    if choice == more_two:
                        player_one = base_player
                        player_one = dict_object[y]  # ---- Nom de la variable qui contient ma class
                        print("=== === === === === === === === === === === === ===\n"
                            "=== === === ",player_one.personality,"=== === === \n"
                                "=== === === === === === === === === === === === ===")
                        list.remove(list[choice - 1])
                        list_choice.remove(list_choice[choice - 1])
                        dict_object.remove(dict_object[choice - 1])
                        select_caractere_part2(second_player, dict_object, list)

    else:
        print("Vous avez choisi un élément en dehors de la liste. Merci de bien vouloir recommencer")

            

#Fonction pour le choix du personnage du joueur 2
def select_caractere_part2(second_player,dict_object,list):
    global player_two
    print ("--->",second_player,",Merci de choisir un personnage en sélectionnant l'indice associé à ce dernier : ")
    list_choice =[]
    for x, y in enumerate(list):
        plus_bis = x + 1 
        list_choice.append(plus_bis)
        print ("Pour :", plus_bis , ":", y)
    choice = int(input()) 
    if choice in list_choice :
        for i in range(len(list)): # Sélection du personnage selon choix affiché
            more = i + 1
            if choice == more :
                for y in range(len(dict_object)): # Attribution 
                    more_two = y + 1 
                    if choice == more_two :
                        player_two = second_player
                        player_two = dict_object[y]  # ---- Nom de la variable qui contient ma class 
                        print("=== === === === === === === === === === === === ===\n"
                              "=== === === ", player_two.personality, "=== === === \n"
                                "=== === === === === === === === === === === === ===")
                        list.remove(list[choice - 1])
                        list_choice.remove(list_choice[choice - 1]) 
                        dict_object.remove(dict_object[choice -1])
        

    else : 
        print("Vous avez choisi un élément en dehors de la liste. Merci de bien vouloir recommencer")


#Fonction pour l'application des malus
def points_player_one(beginner_player,check_position,second_player):
    
    print(beginner_player,"Votre insulte a généré des dégats chez votre adversaire")
    print("La longeur de la phrase :", len(check_position))

    if len(check_position) > 1  and len(check_position) < 6 :
        player_two.X_malus = 2
        print(second_player, "Vous venez d'être touché par un Malus de ",player_two.X_malus, "vos points de vie sont maintenant à ", player_two.malus_action(player_two.X_malus))
        
    
    elif len(check_position) > 7 and len(check_position) < 9 :
        player_two.X_malus = 2
        print(second_player, "Vous venez d'être touché par un Malus de ",player_two.X_malus, "vos points de vie sont maintenant à ", player_two.malus_action(player_two.X_malus))
    
    elif len(check_position) > 10 and len(check_position) <13 :
        player_two.X_malus = 15
        print(second_player, "Vous venez d'être touché par un Malus de ",player_two.X_malus, "vos points de vie sont maintenant à ", player_two.malus_action(player_two.X_malus))



def points_player_two(second_player,check_position2,beginner_player):
    
    print(second_player,"Votre insulte a généré des dégats chez votre Adversaire")
    print("La longeur de la phrase :", len(check_position2))


    if len(check_position2) > 1  and len(check_position2) < 6 :
        player_one.X_malus = 2
        print(beginner_player, "Vous venez d'être touché par un Malus de ",player_one.X_malus, "vos points de vie sont maintenant à ", player_one.malus_action(player_one.X_malus))
        
    elif len(check_position2) > 7 and len(check_position2) < 9 :
        player_one.X_malus = 2
        print(beginner_player, "Vous venez d'être touché par un Malus de ",player_one.X_malus, "vos points de vie sont maintenant à ", player_one.malus_action(player_one.X_malus))
    
    elif len(check_position2) > 10 and len(check_position2) <13 :
        player_one.X_malus = 15
        print(beginner_player, "Vous venez d'être touché par un Malus de ",player_one.X_malus, "vos points de vie sont maintenant à ", player_one.malus_action(player_one.X_malus))




def first(big_dictionnary, phrase_final1,beginner_player,second_player,player_one,player_two) :
    inter = []
    restriction_one ="groupe_verbale"
    restriction_two = "groupe_nominale_adjetif"
    restric_one = "preposition"
    restric_two = "conjonction"
    print("-----------------------", beginner_player, "-----------------------")
    print("A vous de jouer! Saisissez l'indice du mot que vous voulez employer.\n"
          "Pour arreter de composer votre phrase et céder le tour à votre adversaire appuyer sur 404\n"
          "Pour quitter appuyez sur la touche O.")

    # tiré au sort 2 valeurs de chaque clé du dictionnaire
    for key, value in big_dictionnary.items():
        random_entry = random.sample(big_dictionnary[key], 2)
        inter.extend(random_entry)
    # inserer ces valeurs à inter(la liste intermédiaire) puis les mélanger et les proposer au joueur
    random.shuffle(inter)
    for key, value in enumerate(inter):
        key += 1
        print(key, value)


    #print("La liste après mélange :", inter)
    for i in range(len(inter)):
        choix = int(input("C'est à vous :")) - 1
        if choix != -1 and choix in range(len(inter)):
            print("ce qui a été choisi :", inter[choix])
            phrase_final1.append(inter[choix])
            print("------------->", " ".join(phrase_final1), "<------------------")
            print(check_position)
            for index in range(len(phrase_final1)):
                for i, val in big_dictionnary.items():
                    if phrase_final1[index] in val :
                        if phrase_final1[-1] in player_two.insult_  :
                            print(beginner_player," Vous venez de toucher un points sensible de votre adversaire : ")
                            print(" Votre adversaire ")
                            player_two.X_malus = 25
                            print(second_player, " Vous venez d'être touché par un Malus de ",player_two.X_malus, " . Vos points de vie sont maintenant à ", player_two.malus_action(player_two.X_malus))

                        check_position.append(i)
                        if len(check_position) == 1 :
                            if check_position[0] == restriction_one :
                                print(restriction_one,"Ne peut se trouver en début de phrase")
                                print("Vous avez généré un Malus : ")
                                player_one.X_malus = 10
                                print("Vous venez d'être touché par un Malus de ",player_one.X_malus, "vos points de vie sont maintenant à ", player_one.malus_action(player_one.X_malus))

                            elif check_position[0] == restriction_two :
                                print(restriction_two,"Ne peut se trouver en début de phrase")
                                print("Vous avez généré un Malus : ")
                                player_one.X_malus = 10
                                print("Vous venez d'être touché par un Malus de ",player_one.X_malus, "vos points de vie sont maintenant à ", player_one.malus_action(player_one.X_malus))
                            else :
                                pass
                        elif len(check_position) > 1 :

                            if check_position[-1] == check_position[-2] :
                                print("Le type de mot :", check_position[-1],"Le type de mots avant  est ",check_position[-2],"or deux types de mots ne peuvent venir à la suite" )
                                player_one.X_malus = 10
                                print("Vous venez d'être touché par un Malus de ",player_one.X_malus, " . Vos points de vie sont maintenant à ", player_one.malus_action(player_one.X_malus))


        # supprimer les valeurs choisies du dictionnaire
            value_to_delete = inter.pop(choix)
            delete_from_big_dictionnary(value_to_delete)
            # supprimer les valeurs choisies de la liste des propositions
            # prposer de nouveau la novelle liste pour que le joueur effectue un choix
            #print("Ensuite:", inter)

            for key, value in enumerate(inter):
                key += 1
                print(key, value)
            print("**********************************")

        elif choix == 403:
            print("----------------------------->", " ".join(phrase_final1), "<----------------------------------")
            points_player_one(beginner_player,check_position, second_player)

            print("Votre score est de:",player_one.Life)
            if check_position[-1] == restric_one :
                print(restric_one,"Ne peut se trouver en fin de phrase")
                print("Vous venez d'être touché par un Malus de ",player_one.X_malus, "vos points de vie sont maintenant à ", player_one.malus_action(player_one.X_malus))
                print('')


            elif check_position[-1] == restric_two :
                print(restric_two,"Ne peut se trouver en fin de phrase")
                player_one.X_malus = 10
                print("Vous venez d'être touché par un Malus de ",player_one.X_malus, "vos points de vie sont maintenant à ", player_one.malus_action(player_one.X_malus))
                print('')

            else:
                print(check_position[-1], "Peut être en fin de phrase")
                print('')
            second(big_dictionnary, phrase_final2, player_two, second_player, beginner_player)
        else:

            print("------------->", " ".join(phrase_final1), "<------------------")
            print("Votre score est de:", player_one.Life)
            print('Vous vous êtes trompé de touche, Au revoir ')
            exit()




def second(big_dictionnary, phrase_final1,beginner_player,second_player,player_one,player_two):
    inter = []
    restriction_one ="groupe_verbale" 
    restriction_two = "groupe_nominale_adjetif"
    restric_one = "preposition"
    restric_two = "conjonction"

    print("-----------------------", second_player, "-----------------------")
    print("A vous de jouer!Saisissez l'indice du mot que vous voulez employer.\n"
          "Pour arreter de composer votre phrase et céder le tour à votre adversaire appuyer sur 404\n"
          "Pour quitter appuyez sur la touche O.")

    # tiré au sort 2 valeurs de chaque clé du dictionnaire
    for key, value in big_dictionnary.items():
        random_entry = random.sample(big_dictionnary[key], 2)
        inter.extend(random_entry)
    # inserer ces valeurs à inter puis les mélanger et les proposer au joueur
    random.shuffle(inter)
    #print("La liste après mélange", inter)

    for key, value in enumerate(inter):
        key += 1
        print(key, value)

        for i in range(len(inter)):
            choix = int(input("C'est à vous :")) - 1
            if choix != -1 and choix in range(len(inter)):
                phrase_final2.append(inter[choix])
                print("")
                print("------------->", " ".join(phrase_final2), "<------------------")
                print("")
                print(check_position2)
                for index in range(len(phrase_final2)):
                    for i, val in big_dictionnary.items():
                        if phrase_final2[index] in val :
                            if phrase_final2[-1] in player_one.insult_ :
                                print(second_player," Vous venez de toucher un points sensible de votre adversaire : ")
                                player_one.X_malus = 25
                                print(beginner_player, " Vous venez d'être touché par un Malus de ",player_one.malus_action(player_one.X_malus), " . Vos points de vie sont maintenant à ", player_one.malus_action(player_one.X_malus))

                            check_position2.append(i)
                            if len(check_position2) == 1 :
                                if check_position2[0] == restriction_one :
                                    print(restriction_one,"Ne peut se trouver en début de phrase")
                                    print("Vous avez généré un Malus : ")
                                    player_two.X_malus = 10
                                    print("Vous venez d'être touché par un Malus de ",player_two.X_malus, "vos points de vie sont maintenant à ", player_two.malus_action(player_two.X_malus))

                                elif check_position2[0] == restriction_two :
                                    print(restriction_two,"Ne peut se trouver en début de phrase")
                                    print("Vous avez généré un Malus : ")
                                    player_two.X_malus = 10
                                    print("Vous venez d'être touché par un Malus de ",player_two.X_malus, "vos points de vie sont maintenant à ", player_two.malus_action(player_two.X_malus))

                                else :
                                    pass
                            elif len(check_position2) > 1 :
                                if check_position2[-1] == check_position2[-2] :
                                    print("Le type de mot :", check_position2[-1],"Le type de mots avant  est ",check_position2[-2],"or deux types de mots ne peuvent venir à la suite" )
                                    player_two.X_malus = 10
                                    print("Vous venez d'être touché par un Malus de ",player_two.X_malus, "vos points de vie sont maintenant à ", player_two.malus_action(player_two.X_malus))

                                else :
                                    pass

                # supprimer les valeurs choisies du dictionnaire
                value_to_delete = inter.pop(choix)
                delete_from_big_dictionnary(value_to_delete)
                # supprimer les valeurs choisies de la liste des propositions
                # prposer de nouveau la novelle liste pour que le joueur effectue un choix
                #print("Ensuite:", inter)
                for key, value in enumerate(inter):
                    key += 1
                    print(key, value)
                    print('')

                print("**********************************")

            elif choix == 403:
                print("Votre score est de:",player_two.Life)
                points_player_two(second_player,check_position2,beginner_player)
                
                if check_position2[-1] == restric_one :
                    print(restric_one,"Ne peut se trouver en fin de phrase")
                    player_two.X_malus = 10
                    print("Vous venez d'être touché par un Malus de ",player_two.X_malus, "vos points de vie sont maintenant à ", player_two.malus_action(player_two.X_malus))


                elif check_position2[-1] == restric_two :
                    print(restric_two,"Ne peut se trouver en fin de phrase")
                    player_two.X_malus = 10
                    print("Vous venez d'être touché par un Malus de ",player_two.X_malus, "vos points de vie sont maintenant à ", player_two.malus_action(player_two.X_malus))

                else:
                    print(check_position2[-1], "Peut être en fin de phrase")
                
                first(big_dictionnary, phrase_final1, player_one, beginner_player, second_player)
                
            else:
                print("------------->", " ".join(phrase_final2), "<------------------")
                print("Votre score est de:", player_two.Life)
                print('Vous vous êtes trompé de touche, Au revoir ')
                exit()



Menu()