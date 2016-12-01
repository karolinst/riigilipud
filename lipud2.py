from PIL import Image
import random
import numpy as np
import matplotlib.pyplot as plt

#eesti = Image.open("Estonia.jpg")
#eesti.show()
counter = 0
while counter < 10:
    
    riigid = ['albaania = "albania.png"', 'andorra = "andorra.png"', 'armeenia = "armeenia.png"', 'aserbaidžaan = "aserbaidžaan.png"',
              'austria = "austria.png"', 'belgia = "belgia.png"', 'bosnia ja hertsegoviina = "bosniajahertsegoviina.png"',
              'bulgaaria = "bulgaaria.png"', 'eesti = "eesti.jpg"']
    arv = random.randint(0,len(riigid)-1)
    riiksplit = (riigid[arv].split("="))
    riiginimi = riiksplit[0].strip()
    lipufail = riiksplit[1].strip()[1:-1]
    #print(riiginimi)

    def näita_lippu(riik):
        lipp = Image.open(riik)
        lippNumphyFormat = np.asarray(lipp)
        plt.imshow(lippNumphyFormat)
        plt.draw()
        plt.pause(5)
        plt.close()

    def arvamine(pakkumine):
        if pakkumine == riiginimi:
           return "Õige!"
        else:
            return "Vale, õige oli " + riiginimi.title()
    counter += 1
    

    

    näita_lippu(lipufail)
    pakkumine = input("Sisesta riigi nimi: ")
    print(arvamine(pakkumine))

