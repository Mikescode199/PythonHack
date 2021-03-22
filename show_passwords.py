import subprocess
import re
import os
"""Hola a todos, he mejorado 
   el codigo, ya que el anterior no era muy legible, aqui tienen la version mejorada"""


#Creamos una funcion
def obtener_redes_guardadas():
    command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output = True).stdout.decode()

    profile_names = (re.findall("All User Profile     : (.*)\r", command_output))

    wifi_list = list()

    if len(profile_names) != 0:
        for name in profile_names:
             wifi_profile = dict()
             profile_info = subprocess.run(["netsh", "wlan", "show", "profile", name], capture_output = True).stdout.decode()
             if re.search("Security key           : Absent", profile_info):
                pass
             else:
                wifi_profile["ssid"] = name
                profile_info_pass = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output = True).stdout.decode()
                password = re.search("Key Content            : (.*)\r", profile_info_pass)
                if password == None:
                    wifi_profile["password"] = None
                else:
                    wifi_profile["password"] = password[1]
                wifi_list.append(wifi_profile)

    #Guardamos las contrasenas en un archivo de texto
    file = open("filename.txt", "w")
    file.write("Passwords by Mike " + os.linesep)
    for x in wifi_list:
        file.write(f"{str(x)}  {os.linesep}")
    file.close()

#Debemos de llamar a la funcion
obtener_redes_guardadas()