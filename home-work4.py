##################################### Function #######################################
def get_temperature_type():
    temperature_type = input("""Selectati tipul pentru convertare a temperaturi:
1. Grade celsius
2. Farenheit
Introduceti valoare: """)

    if (not temperature_type.isdigit()):
        print("Valoare introdusa nu este numar!\n")
        return get_temperature_type();
        
    temperature_type = int(temperature_type)

    if (temperature_type not in [1, 2]):
        print("Valoare introdusa nu este in lista propusa de variante!\n")
        return get_temperature_type();
    
    return temperature_type;

def get_temperature():
    temperature = input("\nIntroduceti temperatura: ")

    if (not temperature.isdigit() ):
        print("Valoare introdusa nu este numar!\n")
        return get_temperature();

    return int(temperature);

######################################################################################


print("##############################################################################")
print("################################ Exercitiul 1 ################################")
print("##############################################################################")
print("------------------------------------------------------------------------------")
print("Calculati suma numerelor pare mai mici decit 100.\n")
a = sum = 0
while (a <= 100):
    if (a % 2 == 0):
        sum += a
    a += 1
print("Suma numerelor pare mai mici decit 100 este: " + str(sum))
print("------------------------------------------------------------------------------\n")

print("##############################################################################")
print("################################ Exercitiul 2 ################################")
print("##############################################################################")
print("------------------------------------------------------------------------------")
print("Scrieti un program care converteste temperatura din grade celsius in farenheit")
print("si invers (formula: c/5 = f-32/9)\n")

type_selected = ""
temperature_type = get_temperature_type()
temperature = get_temperature()

if (temperature_type == 1):
    type_selected = "Grade celsius"
    temperature = (temperature - 32) * (5 / 9)
elif (temperature_type == 2):
    type_selected = "Farenheit"
    temperature = (temperature * (9 / 5)) + 32

if (type_selected):
    print("Temperatura este converata in " + type_selected  + ": " + str(temperature))
print("------------------------------------------------------------------------------\n")

print("##############################################################################")
print("################################ Exercitiul 3 ################################")
print("##############################################################################")
print("------------------------------------------------------------------------------")
print("Scrieti un program determina daca un text este palindrom (caiac,capac,minim)\n")

text = input("\nIntroduceti textul: ")
lenght = len(text) - 1
i = 0
is_palindrom = ""
while i <= lenght:
    if (text[i] != text[lenght - i]):
        is_palindrom = "nu "
        break

    i += 1
# is_palindrom = ""
# reversed_string = text[::-1]
# if (text != reversed_string):
#     is_palindrom = "nu "

print("Cuvintul " + text + " " + is_palindrom + "este palindrom!")

print("------------------------------------------------------------------------------")
