print("Ufak Yazı Bazlı Maacera Oyunuma Hoş Geldiniz")
print("İki seçenek ile karşılaşacaksınız. 'seçiminiz:' yazan bölümün yanına '1' ve ya '2' yazarak ilerleyeceksiniz")
print("haydı başlayalım")
print(" ")
while True:
    print("bir mağranın önünde uyandınız. Gözleriniz büyükçe açıldı. Nefesinizin altından 'hayır...'diye fısıldadınız.\nTek yön ileri.")
    print("1. dar yol \n2. geniş yol")
    a = input("sseçiminiz:")
    if a == "2":
        print("Önünüzde devasa bir uçurum buldunuz. Arkanızdaki yol sizden sonra çökmüştü. Odayı 4 meşale aydınlatıyordu. Şansınıza karşıda gidilebilecek bir yer var. aşağı baktınız. inilebileceğe benzemiyor. Ama bu tek olasılığı çok ince, düz bir köprü bırakıyor.")
        print("1. yinede aşağı inmeye çalış \n2. köprüden karşıya geç")
        b = input("seçiminiz:")
        if b == "1":
            print("Aşağı inerken ayağınız kaydı. Düşerken artık herşeyin burada biteceğini umit ettiniz. etrafınızdaki zaman yavaşladı ve her şey karanlığa büründü")
            continue
        elif b == "2":
            print("köprünün yarısına geldiğinizde ağayınızın altından bir çıtırtı duydunuz. sonsuz karanlığa doğru düserken bunun son olması için yalvardınız. Önce zaman yavaşladı ardından her şey siyaha büründü ")
            continue
        else:
            print(
                "1 veya 2 yi seçmemeye (yazmamaya) karar verdiniz. Ama maalesef bu cehennemden çıkmanın tek yolu onu bulmaktı. Birden üzerinize bir uyku çöktü... ")
            continue
    elif a == "1":
        print("Sürünerek başka bir odaya geçtiniz. Oda küçüktü ve mükemmel bir küreydi. İki meşale aydınlatmaya yetiyordu. Önünüzde iki yol belirdi")
        print("1. ışık gelen oda\n2. karanlık oda")
        c = input("seçiminiz:")
        if c == "1":
            print(" odanın ortasında biri duruyordu. Elindeki meşale anormal derecede parlaktı. yardım istemek için yanına yaklaştınız. Ölü bir cesete benziyen vücüdunu görünce anladınız ama artık çok geçti.")
            print("Ona teslim olanlar yeni birini daha tuzağa düşürmüştü. Meşalenin hala yanık olmasına rağmen odayı bir karanlık kapladı.")
            continue
        elif c == "2":
            print("Odaya girdiğinizde bir meşale yandı ve arkanızdaki yol sanki hiç bağlı olmamış gibi diğer odadan ayrıldı, tünel gizemli bir şekilde düz bir duvar oldu. Meşalenin ışığında demir bir kapı ve bir kombinasyon kilidi vardı.")
            print("kilitte iki sembol vardı. Sırasıyla: 'I' ve 'O'. bu sembollerin bir ip ucu olabileceğini düşündünüz. ")
            try:
                sifre = int(input("iki basamaklı şifreyi giriniz:"))
                if sifre == 42:
                    print("kapı açılır...")
                    print("Odaya atım attınığınızda odadaki bütün meşaleler aynanda yandı. Ortada altın bir küre duruyordu. Küreye yaklaştıkça onun sesini daha çok duyuyordunuz.")
                    print("Sizin en zayıf olduğunuz yerleri hedefliyordu ama durmadınız. Küreyi elinize aldınız ve olabldiğince hızlı bir şekilde yere attınız. Küre yere deydiği anda parçalandı.")
                    print("Kürenin içinden kör edici bir ışık patlaması yayıldı. Sonunda huzurluydunuz... Sonunda bir sona ulaştınız...")
                    break
                else:
                    print("Etrafınız kararırken bir ses duydunuz: Bırakın Işıklarım yardımcı olsun.")
                    continue
            except:
                print("İmkansızı denediniz ve başarısız oldunuz. Bir dahakine tam sayı girmeliyim diye düşündünüz...")
        else:
            print("1 veya 2 yi seçmemeye (yazmamaya) karar verdiniz. Ama maalesef bu cehennemden çıkmanın tek yolu onu bulmaktı. Birden üzerinize bir uyku çöktü... ")
            continue
    else:
        print("1 veya 2 yi seçmemeye (yazmamaya) karar verdiniz. Ama maalesef bu cehennemden çıkmanın tek yolu onu bulmaktı. Birden üzerinize bir uyku çöktü... ")
        continue