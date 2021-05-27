class Commands:
    def __init__(self, status='Off', volume=20, channel=0):
        self.status = status
        self.volume = volume
        self.channel = channel
    def on_off(self):
        if self.status == 'Off':
            self.status = 'On'
            print(f'The TV is turning {self.status}.')
        elif self.status == 'On':
            self.status = 'Off'
            print(f'The TV is turning {self.status}.')
        else:
            print(f'Critical error, please reboot.')
    
    def volume_status(self):
        print(f'Volume: {self.volume}')
    

    def channel_status(self):
        print(f'Channel: {self.channel}')


    def control(self):
        if self.status == 'On':
            while True:  #onde n é o input recebido
                n = str(input('''
                
                    [ 1 ] Increase Volume
                    [ 2 ] Lower Volume
                    [ 3 ] Next Channel
                    [ 4 ] Prev. Channel
                    [ 5 ] Type Channel
                    [ 6 ] Exit Control UI
                
                    Digite a opção desejada:  '''))
                if n == '1':
                    if 0 <= self.volume <= 99:
                        self.volume += 1
                elif n == '2':
                    if 0 < self.volume <= 100:
                        self.volume -= 1
                elif n == '3':
                    self.channel += 1
                elif n == '4':
                    self.channel -= 1
                elif n == '5':
                    self.channel = int(input('Digite o canal: '))
                else:
                    break   

    
    





