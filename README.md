# Expresiones regulares

Esta es una breve documentación de ejemplo que explica algunas funcionalidades de expresiones regulares en Python utilizando la biblioteca `re`.

## Coincidir con un patrón específico en una cadena

```python
import re

pattern = r"apple"
text = "I have an apple"
match = re.search(pattern, text)
if match:
    print("Se encontró una coincidencia.")

En este ejemplo, utilizamos re.search() para buscar el patrón "apple" dentro de la cadena "I have an apple". Si se encuentra una coincidencia, se imprime "Se encontró una coincidencia". ```

## Coincidir con varias ocurrencias de un patrón en una cadena

```python
import re

pattern = r"apple"
text = "I have an apple, an apple pie, and an apple juice"
matches = re.findall(pattern, text)
print(matches)  # Salida: ['apple', 'apple', 'apple']
```

En este ejemplo, utilizamos re.search() para buscar el patrón "apple" dentro de la cadena "I have an apple". Si se encuentra una coincidencia, se imprime "Se encontró una coincidencia".

## Coincidir con varias ocurrencias de un patrón en una cadena

```python
import re

pattern = r"apple"
text = "I have an apple, an apple pie, and an apple juice"
matches = re.findall(pattern, text)
print(matches)  # Salida: ['apple', 'apple', 'apple']```

Aquí utilizamos re.findall() para encontrar todas las ocurrencias del patrón "apple" dentro de la cadena "I have an apple, an apple pie, and an apple juice". Las coincidencias encontradas se almacenan en una lista llamada matches y se imprime su contenido.

## Coincidir con un patrón al inicio de una cadena

```python
import re

pattern = r"apple$"
text = "I have an apple"
match = re.search(pattern, text)
if match:
    print("El patrón coincide al final de la cadena.")```
    


En este ejemplo, utilizamos el carácter especial $ en el patrón para indicar que la coincidencia debe estar al final de la cadena. Si el patrón "apple" coincide al final de la cadena "I have an apple", se imprime "El patrón coincide al final de la cadena".

## Utilizar caracteres especiales en expresiones regulares

```python
import re

pattern = r"\d+"  # Coincide con uno o más dígitos
text = "I have 123 apples"
match = re.search(pattern, text)
if match:
    print("Se encontró una coincidencia de dígitos.")```

En este último ejemplo, utilizamos el carácter especial \d+ en el patrón para coincidir con uno o más dígitos en la cadena. Si se encuentra una coincidencia de dígitos en la cadena "I have 123 apples", se imprime "Se encontró una coincidencia de dígitos".

Espero que esta documentación te ayude a comprender y utilizar estas funcionalidades de expresiones regulares en Python con la biblioteca `re
