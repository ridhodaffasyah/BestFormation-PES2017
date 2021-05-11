def bacaDataPemain(inputFile):
    #Input file txt berisikan database pemain di PES 2017
    f = open(inputFile, 'r')
    print("Input Squad Success!")
    #List daftar pemain
    list_pemain = []

    for x in f:
        list_pemain.append(x.strip().split(','))
    
    #List Pemain Penyerang (CF,LWF,RWF,SS)
    list_penyerang = []
    for i in range(len(list_pemain)):
        if list_pemain[i][1] == "CF" or list_pemain[i][1] == "LWF" or list_pemain[i][1] == "RWF" or list_pemain[i][1] == "SS" :
            list_penyerang.append(list_pemain[i])
            
    #sort pemain dari yg punya rating terbesar
    list_penyerang = sorted(list_penyerang, key=lambda l: (l[2],l[3]), reverse = True)

    #hapus pemain yang memiliki kondisi 1
    k = 0
    for i in list_penyerang:
        if (i[3] < '2'):
            list_penyerang.remove(list_penyerang[k])
        else:
            k+=1
    
    #List Pemain Tengah Serang(AMF,LMF,RMF)

    list_tengah_serang = []
    for i in range(len(list_pemain)):
        if list_pemain[i][1] == "LMF" or list_pemain[i][1] == "RMF" or list_pemain[i][1] == "AMF":
            list_tengah_serang.append(list_pemain[i])

    #sort pemain dari yg punya rating terbesar
    list_tengah_serang = sorted(list_tengah_serang, key=lambda l: (l[2],l[3]), reverse = True)

    #hapus pemain yang memiliki kondisi 1
    k = 0
    for i in list_tengah_serang:
        if (i[3] < '2'):
            list_tengah_serang.remove(list_tengah_serang[k])
        else:
            k+=1


    #List Pemain Tengah Bertahan (DMF,CMF)
    list_tengah_bertahan = []
    list_tengah = []
    for i in range(len(list_pemain)):
        if list_pemain[i][1] == "DMF" or list_pemain[i][1] == "CMF":
            list_tengah_bertahan.append(list_pemain[i])

    #sort pemain dari yg punya rating terbesar
    list_tengah_bertahan = sorted(list_tengah_bertahan, key=lambda l:l[2], reverse = True)

    #hapus pemain yang memiliki kondisi 1
    k = 0
    for i in list_tengah_bertahan:
        if (i[3] < '2'):
            list_tengah_bertahan.remove(list_tengah_bertahan[k])
        else:
            k+=1
            
    #List Pemain Belakang (CB,RB,LB)
    list_belakang = []

    for i in range(len(list_pemain)):
        if list_pemain[i][1] == "RB" or list_pemain[i][1] == "CB" or list_pemain[i][1] == "LB" :
            list_belakang.append(list_pemain[i])

    #sort pemain dari yg punya rating terbesar
    list_belakang = sorted(list_belakang, key=lambda l:l[2], reverse = True)

    #hapus pemain yang memiliki kondisi 1
    k = 0
    for i in list_belakang:
        if (i[3] < '2'):
            list_belakang.remove(list_belakang[k])
        else:
            k+=1
    
    #List Pemain Kiper (GK)
    list_kiper = []

    for i in range(len(list_pemain)):
        if list_pemain[i][1] == "GK" :
            list_kiper.append(list_pemain[i])

    #hapus pemain yang memiliki kondisi 1  
    k = 0
    for i in list_kiper:
        if (i[3] < '2'):
            list_kiper.remove(list_kiper[k])
        else:
            k+=1


    #Deskripsi masing-masing formasi
    #1. 4-2-3-1 : formasi yang fleksibel dimana jumlah pemain tengah ini memungkinkan untuk bermain ball possession atau menyerang dari luar lebar lapangan
    #2. 4-1-4-1 : formasi dengan pemain yang memiliki daya pikir menyerang diletakkan di posisi tinggi tengah dan membutuhkan pemain berkaliber tinggi untuk diposisikan sebagai jangkar menembus defense.
    #3. 4-3-2-1 : formasi yang diarahkan untuk melakukan penyerangan balik dengan kedalaman di lini tengah. Kualitas di lini tengah sangatlah penting.
    #4. 4-2-2-2 : formasi serbaguna dan seimbang, cocok untuk serangan balik melalui lini tengah maupun dari lebar lapangan.
    #5. 4-3-1-2 : formasi yang cocok untuk menyerang melalui tengah dengan ukuran yang besar tapi dibutuhkan konsentrasi yang tinggi dari pemain lini tengah.
    #6. 4-2-1-3 : formasi dengan fokus lebih besar pada pertahanan daripada 4-1-2-3. Membutuhkan gelandang offensif berkaliber tinggi agar bisa bekerja.
    #7. 4-1-2-3 : formasi menyerang dengan mengorbankan kekuatan lini tengah.
    #8. 3-2-4-1 : formasi dengan kedalaman lini tengah yang luar biasa yang membuatnya cocok untuk penguasaan bola serta menyerang dari lebar lapangan.
    #9. 3-2-3-2 : formasi serbaguna yang seimbang dan paling cocok untuk menyerang dari lebar lapangan.
    #10. 3-3-2-2 : formasi yang menempatkan lebih banyak pemain di tengah daripada pemain sayap.
    #11. 3-2-2-3 : formasi dimana pemain ditempatkan secara merata di lapangan.
    #12. 5-2-2-1 : formasi ini menempatkan pemain pada posisi bertahan.
    #13. 5-2-1-2 : formasi ini menempatkan pemain pada posisi bertahan juga tetapi ada 2 pemain penyerang yang siap menyerang.
    #14. 5-3-2 : formasi ini lebih berbobot ditengah harus banyak playmaker untuk posisi ini agar efektif.

    list_formasi = [[4,2,3,1],[4,1,4,1],[4,3,2,1],[4,2,2,2],[4,3,1,2],[4,2,1,3],[4,1,2,3],[3,2,4,1],[3,2,3,2],[3,3,2,2],[3,2,2,3],[5,2,2,1],[5,2,1,2],[5,3,2]]

    #Cek apakah jumlah pemain di masing-masing posisi memenuhi salah satu atau lebih dari formasi yang ada di list formasi
    print("\nFormasi yang bisa dipakai : ")
    list_rekomen_formasi = []
    for i in range(len(list_formasi)):
        if (len(list_penyerang) >= list_formasi[i][0]):
            if (len(list_tengah_serang) >= list_formasi[i][1]):
                if (len(list_tengah_bertahan) >= list_formasi[i][2]):
                    if (len(list_belakang) >= list_formasi[i][3]):
                        print(list_formasi[i])
                        list_rekomen_formasi.append(list_formasi[i])

    count_sum_rating_penyerang = []
    full_get_serang = []
    count_sum_rating_tengah_serang = []
    full_get_tengah_serang = []
    count_sum_rating_tengah_bertahan = []
    full_get_tengah_bertahan = []
    count_sum_rating_belakang = []
    full_get_belakang = []
    count_sum_rating_kiper = []
    
    for k in range(len(list_rekomen_formasi)):
        i = 0
        sum_rating_serang = 0
        get_serang = []
        for m in range(list_rekomen_formasi[k][3]):
            for j in range(i,len(list_penyerang)):
                if (i <= m and list_penyerang[j][3] >= '2'):
                    sum_rating_serang += int(list_penyerang[j][2])
                    get_serang.append(list_penyerang[j][0])
                    i += 1
        count_sum_rating_penyerang.append(sum_rating_serang)
        full_get_serang.append(get_serang)

        i = 0
        sum_rating_tengah_serang = 0
        get_tengah_serang = []
        for m in range(list_rekomen_formasi[k][2]):
            for j in range(i,len(list_tengah_serang)):
                if (i <= m  and list_tengah_serang[j][3] >= '2'):
                    sum_rating_tengah_serang += int(list_tengah_serang[j][2])
                    get_tengah_serang.append(list_tengah_serang[j][0])
                    i += 1
        count_sum_rating_tengah_serang.append(sum_rating_tengah_serang)
        full_get_tengah_serang.append(get_tengah_serang)

        i = 0
        sum_rating_tengah_bertahan = 0
        get_tengah_bertahan = []
        for m in range(list_rekomen_formasi[k][1]):
            for j in range(i,len(list_tengah_bertahan)):
                if (i <= m and list_tengah_bertahan[j][3] >= '2'):
                    sum_rating_tengah_bertahan += int(list_tengah_bertahan[j][2])
                    get_tengah_bertahan.append(list_tengah_bertahan[j][0])
                    i += 1
        count_sum_rating_tengah_bertahan.append(sum_rating_tengah_bertahan)
        full_get_tengah_bertahan.append(get_tengah_bertahan)

        i = 0
        sum_rating_belakang = 0
        get_belakang = []
        for m in range(list_rekomen_formasi[k][0]):
            for j in range(i,len(list_belakang)):
                if (i <= m and list_belakang[j][3] >= '2'):
                    sum_rating_belakang += int(list_belakang[j][2])
                    get_belakang.append(list_belakang[j][0])
                    i += 1
        count_sum_rating_belakang.append(sum_rating_belakang)
        full_get_belakang.append(get_belakang)

        get_kiper = []
        for j in range(len(list_kiper)):
            if (list_kiper[j][3] >= '2'):
                get_kiper.append(list_kiper[j])
        
        best_formasi = []
        best_player_serang = []
        best_player_tengah_serang = []
        best_player_tengah_bertahan = []
        best_player_belakang = []
        best_player_kiper = []
        sum_total = count_sum_rating_penyerang[0] + count_sum_rating_tengah_serang[0] + count_sum_rating_tengah_bertahan[0] + count_sum_rating_belakang[0] + int(get_kiper[0][2])
        for i in range(len(count_sum_rating_penyerang)):
            if ((count_sum_rating_penyerang[i] + count_sum_rating_tengah_serang[i] + count_sum_rating_tengah_bertahan[i] + count_sum_rating_belakang[i] + int(get_kiper[0][2])) > sum_total):
                sum_total = count_sum_rating_penyerang[i] + count_sum_rating_tengah_serang[i] + count_sum_rating_tengah_bertahan[i] + count_sum_rating_belakang[i] + int(get_kiper[0][2])
                best_formasi.append(list_rekomen_formasi[i])
                best_player_serang.append(full_get_serang[i])
                best_player_tengah_serang.append(full_get_tengah_serang[i])
                best_player_tengah_bertahan.append(full_get_tengah_bertahan[i])
                best_player_belakang.append(full_get_belakang[i])
                best_player_kiper.append(get_kiper[0][0])
                
                best_formasi = best_formasi.pop()
                best_player_serang = best_player_serang.pop()
                best_player_tengah_serang = best_player_tengah_serang.pop()
                best_player_tengah_bertahan = best_player_tengah_bertahan.pop()
                best_player_belakang = best_player_belakang.pop()
    
    print("\nRekomendasi formasi : ")
    print((str)(best_formasi[0]) + "-" + (str)(best_formasi[1]) + "-" + (str)(best_formasi[2]) + "-" + (str)(best_formasi[3]))

    print("\nSusunan pemain untuk formasi : ", best_formasi)
    print("Penyerang (CF/RWF/LWF) : ")
    for j in range(len(best_player_serang)):
        print((j+1),end="")
        print(". " + best_player_serang[j])

    print("Pemain Tengah Serang (AMF/LMF/RMF) : ")
    for j in range(len(best_player_tengah_serang)):
        print((j+1),end="")
        print(". " + best_player_tengah_serang[j])

    print("Pemain Tengah Bertahan (CMF/DMF) : ")
    for j in range(len(best_player_tengah_bertahan)):
        print((j+1),end="")
        print(". " + best_player_tengah_bertahan[j])

    print("Pemain Belakang (CB/LB/RB) : ")
    for j in range(len(best_player_belakang)):
        print((j+1),end="")
        print(". " + best_player_belakang[j])        

    print("Kiper (GK) : ")
    print("1. " + best_player_kiper[0])
            
bacaDataPemain("dataManCity.txt")
