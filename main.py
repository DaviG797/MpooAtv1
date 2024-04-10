

class Televisao:
    def __init__(self):
        self.tvOn = False
        self.canal = 2
        self.volume = 1
        self.volumetemp = 0
        self.mute = False

    def turnOnOff(self):
        if not self.tvOn:
            self.tvOn = True
            print("TV Ligada!")
        else:
            self.tvOn = False
            print("TV Desligada!")
        return

    def aumentarVolume(self):
        if not self.tvOn:
            return
        else:
            if self.volume < 100:
                self.volume += 1
                print("Volume:", self.volume)
            return

    def diminuirVolume(self):
        if not self.tvOn:
            return
        else:
            if self.volume > 0:
                self.volume -= 1
                print("Volume:", self.volume)
            return

    def muteVol(self):
        if not self.tvOn:
            return
        else:
            if self.mute:
                self.mute = False
                self.volume = self.volumetemp
                print("Volume:", self.volume)
            else:
                self.volumetemp = self.volume
                self.mute = True
                self.volume = 0
                print("Volume:", self.volume)
            return

    def proxCanal(self):
        if not self.tvOn:
            return
        else:
            if self.canal < 12:
                self.canal += 1
                print("Canal:", self.canal)
            else:
                self.canal = 2
                print("Canal:", self.canal)
            return

    def prevCanal(self):
        if not self.tvOn:
            return
        else:
            if self.canal > 2:
                self.canal -= 1
                print("Canal:", self.canal)
            else:
                self.canal = 12
                print("Canal:", self.canal)
            return

    def getinfo(self):
        if not self.tvOn:
            return
        else:
            print(f'Canal Atual: {self.canal} \nVolume Atual: {self.volume}')
            return

    def selectCanal(self, canal):
        if not self.tvOn:
            return
        else:
            if canal < 2:
                return print(f'Canal não existe.')
            elif canal > 12:
                return print(f'Canal não existe.')
            else:
                self.canal = canal
                print("Canal:", self.canal)
            return

tv = Televisao()
tv.turnOnOff()
tv.aumentarVolume()
tv.aumentarVolume()
tv.diminuirVolume()
tv.muteVol()
tv.proxCanal()
tv.prevCanal()
tv.selectCanal(9)
tv.getinfo()
