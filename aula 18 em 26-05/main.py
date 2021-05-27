#Faça um programa que simule um televisor criando-o como um objeto. ​
# O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume.​
# Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.​

from commands import Commands

#status='off', volume=20, channel=36
tv = Commands()


print(tv.status)
tv.on_off()
print(tv.status)
tv.control()
print(tv.status)
tv.channel_status()
tv.volume_status()

