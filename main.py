pip install colorama
pip show colorama   
from colorama import init
init()
from colorama import Fore, Back, Style
#Fore цвет текста Back цвет фона style становится ярче

print(Fore.GREEN + 'зеленый ')
print('обычный ')
#использование цветного текста
from colorama import init
init()
#инициализацияa