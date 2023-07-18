# IPv4 Validation
# Author: Sandro Zappulla
# Github: @SandroZappulla
# version: v1.0

# IMPORT
# RegEx
import re

# Variables # TestOnly
#my_ip = "192.168.178.177"
#test = ""
#short_ip = "1.1.1.1"
#not_valid_ip = "256.-1.1000.532"

# Eintrag # TestOnly
#IPv4_entry = my_ip

# checks
check_empty_input = False
check_length = False
check_valid_chars = True
check_first_char_is_digit = False
check_amount_dots = False
check_regex_pattern = True
check_number_range = False



# MAIN
print("IPv4 Validierung by Sandro Zappulla")
IPv4_entry = input("Bitte Geben Sie eine gültige IPv4-Adresse ein: ") # Eingabe

# Überprüfe: Nicht leer
if IPv4_entry == '':
    check_empty_input = True



# Überprüfe: Länge (Mind. 7 Max. 15 Zeichen)
length = len(IPv4_entry)
if length >= 7 and length <= 15:
    check_length = True 



# Überprüfe: Ob NUR Ziffern und Punkte enthalten sind
char_counter = 0
valid_chars = 0
unvalid_chars = 0

while char_counter < length:
    # Überprüfung ob beim index von der Eingabe eine Zahl vorhanden ist oder ein "."
    if IPv4_entry[char_counter].isdigit() or IPv4_entry[char_counter] == '.':
        valid_chars+=1
    else:
        unvalid_chars+=1
    char_counter+=1

if unvalid_chars != 0:
    check_valid_chars = False



# Überprüfe: Erstes Zeichen Zahl
first = IPv4_entry[0]

if first.isdigit():
    check_first_char_is_digit = True



# Überprüfe: Anzahl der Punkte
dot_count = IPv4_entry.count('.')

if dot_count == 3:
    check_amount_dots = True
elif dot_count != 3:
    check_amount_dots = False



# Überprüfe: Keine Punkte hintereinander
# RegEx Überprüfung: Vorgabe(1-3 Zahlen, dann darauffolgender ".") (^ = Beginn, $ = Ende)
pattern = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
if pattern.match(IPv4_entry) == None:
    check_regex_pattern = False


# Oktett Bildung: Unterteilung von Punkt in einer Liste
digit_split = IPv4_entry.split(".")



# Überprüfung: Validierung einer einzelnen Zahl (Zwischen 0-255)
correct_number_counter = 0

# Bevor jede Zahl einzelnd Validiert wird erwarten wir das erst die Überprüfung "Keine Punkte Hintereinander (RexEx)" richtig ist
if check_regex_pattern == True:
    for digit in digit_split:
        int_digit = int(digit)
        #print(int_digit)

        if int_digit >= 0 and int_digit <= 255:
            correct_number_counter+=1
    
        if correct_number_counter == 4:
            check_number_range = True

# AUSGABE
print("------------------------------------- EINTRAG ----------------------------------------")
print("\n")
print(f"Eintrag: {IPv4_entry}")
print("\n")
print("------------------------------------- ÜBERPRÜFUNG ----------------------------------------")
print(f"check_empty_input: {check_empty_input}")
print(f"check_length: {check_length} : length: {length}")
print(f"check_valid_chars: {check_valid_chars} : valid_chars: {valid_chars} : unvalid_chars: {unvalid_chars}")
print(f"check_first_char_is_digit: {check_first_char_is_digit} : first: '{first}',")
print(f"check_amount_dots: {check_amount_dots} : dot_count: '{dot_count}',")
print(f"check_regex_pattern: {check_regex_pattern}")
print(f"check_number_range: {check_number_range} : correct_number_counter: {correct_number_counter}")
