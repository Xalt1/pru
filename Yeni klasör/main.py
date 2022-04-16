import random
sans = "rastgele"
kategori = "kategori"
user = "tanju"
password = "123456"
cevapbir = "evet"
cevapiki = "hayir"

while True:
    kullanici = input("kullanıcı adınızı giriniz:")
    parola = input("Şifrenizi Giriniz:")
    if kullanici == user and parola == password:
        print("Hoşgeldiniz")
        break
    elif kullanici == user and parola != password:
        print("Şifreniz yanlış \n")
    elif kullanici != user and parola == password:
        print("Kullanıcı adınız yanlış \n")
    else:
        print("Kullanıcı adı ve şifre hatalı \n")

while True:
    kategorisec = input("kategori sec veya rastgele dene ")
    if kategorisec == sans :
        line = random.choice(open('all.txt').readlines())
        print(line)
        break
    elif kategorisec == kategori :
        import pandas as pd

        X = input("Kategoriler:\nDrama\nCrime\nAction\nAdventure\nBiography\nHistory\nSci-Fi\nWestern\nFamily\nThriller\nRomance\nComedy\nFantasy\nMusic\nAnimation\nWar\nHorror\nFilm-Noir\nLutfen bir kategori seciniz: ")
        df = pd.read_csv('imdb_listee.csv')
        df = df.dropna()
        result = df[df["genre"].str.contains(X.lower())]
        print(result.head(1000))

        filmsirasi = input("lütfen film sırasını giriniz:")
        filmsirasi2 = int(filmsirasi)
        data = []
        with open("all.txt", "r") as f:
            data = f.readlines()

        print(data[filmsirasi2])

        izledinizmi = input("Filme yorum yapmak, puan vermek ve size yeni bir film onerisinde bulunmamizi ister misiniz ")


    if izledinizmi == cevapbir :
        yorumdosyasi = open(filmsirasi, "a")
        yorum = input("film hakkindaki yorumlarinizi yaziniz: ")
        yorumdosyasi.write("\n"+yorum)
        yorumdosyasi.close()
        puanlama = input("Lutfen 0 ile 10 arasinda bir puan giriniz:")
        puanlama2 = int(puanlama)
        if puanlama2 > 5 :
            result = df[df["genre"].str.contains(X)]
            print(result.sample(3))
            print("Sistemimizi kullandiginiz icin tesekkur eder iyi gunler dileriz")
            input()
            break
        else:
            basadonmekistermisiniz = input("Basa donerek rastgele bir film veya yeni bir kategori secmek ister misiniz?: ")

            if basadonmekistermisiniz == cevapiki :
                print("Sistemimizi kullandiginiz icin tesekkur eder iyi gunler dileriz")
                input()
                break
    elif izledinizmi == cevapiki :
            print("Sistemimizi kullandiginiz icin tesekkur eder iyi gunler dileriz")
            input()
            break




