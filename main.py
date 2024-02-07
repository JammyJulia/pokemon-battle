
print("")
print("                                  ,'\\")
print("    _.----.        ____         ,'  _\   ___    ___     ____")
print("_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.")
print("\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |")
print(" \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |")
print("   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |")
print("    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |")
print("     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |")
print("      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |")
print("       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |")
print("        \_.-'       |__|    `-._ |              '-.|     '-.| |   |")
print("                                `'                            '-._|")
print("")
print("Pokemon Battle")
print("")

import json
import random

# read Pokemon file into dictionary
pokemons_file = open('pokemons.json') # opening JSON file
pokemons = json.load(pokemons_file) # returns JSON object as a dictionary
pokemons_file.close() # Closing file

print(pokemons[0])

def strength(pokemon):
    return (int(pokemon['hp']) + int(pokemon['defense']) + int(pokemon['attack']))/3


while True:
    print("1. Show pokemon by index")
    print("2. Top 10 strongest pokemons")
    print("3. Top 10 weakest pokemons")
    print("4. Battle of 2 pokemons")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        index = int(input("Index: "))
        pokemon = pokemons[index-1]
        print('name:', pokemon.get('name'))
        print('type 1:', pokemon.get('type_1'))
        if pokemon.get('type_2') != '':
            print('type 2:', pokemon.get('type_2'))
        print('total:', pokemon.get('total'))
        print('hp:', pokemon.get('hp'))
        print('attack:', pokemon.get('attack'))
        print('defense:', pokemon.get('defense'))
        # https://www.w3schools.com/python/python_dictionaries_access.asp

    elif choice == '2':
        # https://www.w3schools.com/python/python_lists_sort.asp
        pokemons.sort(key = strength, reverse=True)
        for i in range(10):
            print(f'============{i+1}============')
            print('Index:', pokemons[i].get('number'))
            print('name:', pokemons[i].get('name'))
            print('type 1:', pokemons[i].get('type_1'))
            if pokemons[i].get('type_2') != '':
                print('type 2:', pokemons[i].get('type_2'))
            print('total:', pokemons[i].get('total'))
            print('hp:', pokemons[i].get('hp'))
            print('attack:', pokemons[i].get('attack'))
            print('defense:', pokemons[i].get('defense'))
    elif choice == '3':
        pokemons.sort(key = strength)
        for i in range(10):
            print(f'============{i+1}============')
            print('Index:', pokemons[i].get('number'))
            print('name:', pokemons[i].get('name'))
            print('type 1:', pokemons[i].get('type_1'))
            if pokemons[i].get('type_2') != '':
                print('type 2:', pokemons[i].get('type_2'))
            print('total:', pokemons[i].get('total'))
            print('hp:', pokemons[i].get('hp'))
            print('attack:', pokemons[i].get('attack'))
            print('defense:', pokemons[i].get('defense'))
        # https://www.w3schools.com/python/python_lists_sort.asp
        pass
    elif choice == '4':
        computerPokemon = random.choice(pokemons)
        index = int(input("Choose pokemon(index): "))
        playerPokemon = pokemons[index-1]
        # while (playerPokemon['hp'] > 0) or (computerPokemon['hp'] > 0):
        while True:
            damageToPlayer = int(computerPokemon['attack']) - int(playerPokemon['defense']) + random.randint(5, 20)
            damageToComputer = int(playerPokemon['attack']) - int(computerPokemon['defense']) + random.randint(5, 20)
            if damageToPlayer > 0:
                playerPokemon['hp'] = int(playerPokemon['hp']) - damageToPlayer
            if damageToComputer > 0:
                computerPokemon['hp'] = int(computerPokemon['hp']) - damageToComputer
            if playerPokemon['hp'] <= 0:
                print("You lost!")
                break
            elif computerPokemon['hp'] <= 0:
                print("You won!")
                break

        # Battle
        # https://www.w3schools.com/python/ref_random_choice.asp - random choice
        # Computer choosing one random Pokemon from list
        # Player choosing by entering Pokemon index
        # Damage is calculated by: (attack of Pokemon 2) - (defense of Pokemon 1) + (random from 5 to 20), and vice-versa
        # Player reaching 0 health - lost

    elif choice == '5':
        print("Exiting")
        break
    else:
        print("Invalid choice, choose from 1 to 5")

    print("==========================")


