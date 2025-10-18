import random
#spdps
l = ["taş", "kağıt", "makas"]
while True:
    a = random.choice(l)
    b = input("seçiminizi girin:")
    print(a)
    try:
        int(b)
        print("'taş','kağıt' ya da 'makas' yazın")
    except:
        if a == "makas":
            try:
                b = str(b)
                if a == b:
                    print("berabere")
                elif b == "taş":
                    print("kazandınız")
                elif b == "kağıt":
                    print("kaybettiniz")
                else:
                    print("'taş','kağıt' ya da 'makas' yazın")
            except:
                print("'taş','kağıt' ya da 'makas' yazın")

        elif a == "kağıt":
            try:
                b = str(b)
                if a == b:
                    print("berabere")
                elif b == "makas":
                    print("kazandınız")
                elif b == "taş":
                    print("kaybettiniz")
                else:
                    print("'taş','kağıt' ya da 'makas' yazın")
            except:
                print("'taş','kağıt' ya da 'makas' yazın")

        elif a == "taş":
            try:
                b = str(b)
                if a == b:
                    print("berabere")
                elif b == "kağıt":
                    print("kazandınız")
                elif b == "makas":
                    print("kaybettiniz")
                else:
                    print("'taş','kağıt' ya da 'makas' yazın")
            except:
                print("'taş','kağıt' ya da 'makas' yazın")
    c = input("bir tur daha?(e/h):")
    if c == "e":
        continue
    elif c == "h":
        print("oynadığınız için teşekkürler")
        break
    else:
        print("kapatılıyor. eğer oynamak istiyor olsaydınız e yazmalıydınız")
        break
