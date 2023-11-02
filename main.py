# Kelompok 2
print("Are you hungry ?")
print("MyPizza")

menuPizza = {
    1: "Frank Furter",
    2: "Meat Monst",
    3: "Meat Monsta",
    4: "Super Supreme",
    5: "Super Supreme Chicken",
}

pizza_diPilih = ""

total_harga = 0
Rupiah = f"Rp {total_harga:,.0f}"
print("Pizza Menu:\n 1: Frank Furter\n 2: Meat Monst\n 3: Meat Monsta\n 4: Super Supreme\n 5: Super Supreme Chicken\n")

while True:
    pilihan = int(input("Pilih Nomor pesanan pizza yang ingin kamu Pesan (1-5): "))
    if pilihan in menuPizza:
        pizza_diPilih = menuPizza[pilihan]
        print(f"Pizza yang kamu pilih {pizza_diPilih}")

        menuCrust = {
            1: "Pan",
            2: "Stuffed Crust Cheese",
            3: "Stuffed Crust Sausage",
            4: "Cheesy Bite",
            5: "Crown Crust",
        }

        print("Crust Menu:\n 1: Pan\n 2: Stuffed Crust Cheese\n 3: Stuffed Crust Sausage\n 4: Cheesy Bite\n 5: Crown Crust\n")

        pilihCrust = int(input("Pilih nomor crust yang ingin kamu pilih (1-5): "))
        if pilihCrust in menuCrust:
            crust_diPilih = menuCrust[pilihCrust]
            print(f"Crust yang kamu pilih {crust_diPilih}")
            ukuran = input("Pilih ukuran yang kamu inginkan:\n Personal, Regular, Large : \n")
            if ukuran == "Personal":
                total_harga += 43637

                keju = input("Ingin menambahkan Keju Extra ?:\n(ya atau tidak) :")
                if keju == "ya":
                    total_harga += 13636
                elif keju == "tidak":
                    total_harga += 0
                else:
                    print("Maaf, Kamu tidak memilih apapun")

            elif ukuran == "Regular":
                total_harga += 100910

                keju = input("Ingin menambahkan Keju Extra ?:\n(ya atau tidak) :")
                if keju == "ya":
                    total_harga += 13636
                elif keju == "tidak":
                    total_harga += 0
                else:
                    print("Maaf, Kamu tidak memilih apapun")
                    
            elif ukuran == "Large":
                total_harga += 132738
                keju = input("Ingin menambahkan Keju Extra ?:\n(ya atau tidak) :")
                if keju == "ya":
                    total_harga += 13636
                elif keju == "tidak":
                    total_harga += 0
                else:
                    print("Maaf, Kamu tidak memilih apapun")

            else:
                print("MAaf, Kamu tidak memilih apapun")
        else:
            print("Maaf, Crust yang kamu pilih tidak ada")
    else:
        print("Menu yang Anda pilih tidak ada, mohon pilih nomor sesuai ketentuan menu.")

    pesan_lagi = input("Apakah Anda ingin memesan pizza lagi? (ya/tidak): ")
    if pesan_lagi.lower() != "ya":
        break

print("\n")
print(f"Terima kasih telah memesan {pizza_diPilih}")
print(f"Total harga pesanan Anda adalah: Rp{total_harga}")
print("Silakan selesaikan pembayaran. Selamat menikmati makanan Anda!")

