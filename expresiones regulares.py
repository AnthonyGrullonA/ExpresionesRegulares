import re

#Coincidir con un patron especifico en cadena

pattern = r"apple"
text = "I have an apple"
match = re.search(pattern, text)
if match:
    print("Se encontró una coincidencia.")

#Coincidir con varias ocurrencias de un patron en cadena

pattern = r"apple"
text = "I have an apple, an apple pie, and an apple juice"
matches = re.findall(pattern, text)
print(matches)  # Salida: ['apple', 'apple', 'apple']


#coincidir con un patron al incio de una cadena

pattern = r"^I"
text = "I have an apple"
match = re.search(pattern, text)
if match:
    print("El patrón coincide al inicio de la cadena.")

#Coincidir con un patron al final de una cadena

pattern = r"apple$"
text = "I have an apple"
match = re.search(pattern, text)
if match:
    print("El patrón coincide al final de la cadena.")


#Utilizar caracteres especiales en expresiones regulares

pattern = r"\d+"  # Coincide con uno o más dígitos
text = "I have 123 apples"
match = re.search(pattern, text)
if match:
    print("Se encontró una coincidencia de dígitos.")

