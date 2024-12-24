if __name__ == '__main__':

    from sys import version

    if version[0] == "3":
        raw_input = input

    print('quel est le type de calcul que vous voulez faire : ')
    print('1. +')
    print('2. -')
    print('3. *')
    print('4. /')

    while 1:
        reponse = raw_input("Choisissez de 1 à 4 : ")
        if reponse in ['1', '2', '3', '4']:
            break
        else:
            print("Choix incorrect !")

if reponse == "1":
    note1 = int(input('nombre 1 : '))
    note2 = int(input('nombre 2 : '))
    note3 = note1 + note2
    print(str(note3))

if reponse == "2":
    note1 = int(input('nombre 1 : '))
    note2 = int(input('nombre 2 : '))
    note3 = note1 - note2
    print(str(note3))

if reponse == "3":
    note1 = int(input('nombre 1 : '))
    note2 = int(input('nombre 2 : '))
    note3 = note1 * note2
    print(str(note3))
if reponse == '4':
    note1 = int(input('nombre 1 : '))
    note2 = int(input('nombre 2 : '))
    note3 = note1 / note2
    print(str(note3))