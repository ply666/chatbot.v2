madText1 = ["", "", "", "", ""]
madText2 = ["", "", "", "", ""]
madText3 = ["", "", "", "", ""]
madText4 = ["", "", "", "", ""]
madText5 = ["", "", "", "", ""]

def pirmaiSpeletajs():
    speletajs1 = input("Ka sauc 1 speletajs?")
    speletajs1 = speletajs1.title()
    print(speletajs1 + ", atbildi uz 5 jautājumiem")

    madText1[0] = input("KĀDS")
    madText5[1] = input("KAS?")
    madText4[2] = input("KUR?")
    madText3[3] = input("KO DARĪJA?")
    madText2[4] = input("KAS SANĀCA?")


def otraiSpeletajs():
    speletajs2 = input("Ka sauc 2 speletajs?")
    speletajs2 = speletajs2.title()
    print(speletajs2 + ", atbildi uz 5 jautājumiem")

    madText2[0] = input("KĀDS")
    madText1[1] = input("KAS?")
    madText5[2] = input("KUR?")
    madText4[3] = input("KO DARĪJA?")
    madText3[4] = input("KAS SANĀCA?")


def tresaiSpeletajs():
    speletajs3 = input("Ka sauc 3 speletajs?")
    speletajs3 = speletajs3.title()
    print(speletajs3 + ", atbildi uz 5 jautājumiem")

    madText3[0] = input("KĀDS")
    madText2[1] = input("KAS?")
    madText1[2] = input("KUR?")
    madText5[3] = input("KO DARĪJA?")
    madText4[4] = input("KAS SANĀCA?")


def ceturtaiSpeletajs():
    speletajs4 = input("Ka sauc 4 speletajs?")
    speletajs4 = speletajs4.title()
    print(speletajs4 + ", atbildi uz 5 jautājumiem")

    madText4[0] = input("KĀDS")
    madText3[1] = input("KAS?")
    madText2[2] = input("KUR?")
    madText1[3] = input("KO DARĪJA?")
    madText5[4] = input("KAS SANĀCA?")


def piektaiSpeletajs():
    speletajs5 = input("Ka sauc 5 speletajs?")
    speletajs5 = speletajs5.title()
    print(speletajs5 + ", atbildi uz 5 jautājumiem")

    madText5[0] = input("KĀDS")
    madText4[1] = input("KAS?")
    madText3[2] = input("KUR?")
    madText2[3] = input("KO DARĪJA?")
    madText1[4] = input("KAS SANĀCA?")

if __name__ == '__main__':
  print("MadText. Katrs spēlētājs atbild uz jautājumu,"
        " un nākamajam spēlētājam līdz ir atbildēts uz visiem jautājumiem."
        " Spēles beigās tiek nolasīti teikumi, kas izveidojušies spēles rezultātā.")
  pirmaiSpeletajs()
  otraiSpeletajs()
  tresaiSpeletajs()
  ceturtaiSpeletajs()
  piektaiSpeletajs()
  print(madText1)
  print(madText2)
  print(madText3)
  print(madText4)
  print(madText5)




