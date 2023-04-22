import subprocess

label1_es = "Perfil de todos los usuarios"
label1_en = "All User Profile"
label2_es = "Contenido de la clave"
label2_en = "Key Content"

label1 = label1_es
label2 = label2_es

cmd1 = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])
cmd1_decoded = cmd1.decode('utf-8')
cmd1_list = cmd1_decoded.split('\n')

profiles = []
for i in cmd1_list:
    if label1 in i:
        profiles.append(i.split(':')[1][1:-1])


for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('cp1252').split('\n')
    results = [j.split(":")[1][1:-1] for j in results if label2 in j]
    try:
        print("{:<30}|  {:<}".format(i, results[0]))
    except IndexError:
        print("{:<30}|  {:<}".format(i, ""))
