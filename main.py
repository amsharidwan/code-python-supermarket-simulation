#input all items
all_items = [{
    'item': 'susu',
    'harga': 50000
    }, {
    'item': 'daging',
    'harga': 20000
    }, {
    'item': 'lampu',
    'harga': 15000
    }, {
    'item': 'masker',
    'harga': 25000
    }, {
    'item': 'apel',
    'harga': 30000
    }]

#input promotional items
promotional_items = [all_items[0], all_items[3]]

def print_all_items():
    print('*' * 25)
    number = 1
    for itemx in all_items:
        print_itemx = str(number) + '. ' + itemx['item'] + ' = ' + str(itemx['harga'])
        number += 1
        print(print_itemx)
    print('*' * 25)

def print_promotional_items():
    print('*' * 25)
    number = 1
    for itemy in promotional_items:
        print_itemy = str(number) + '. ' + itemy['item'] + ' = ' + str(itemy['harga'])
        number += 1
        print(print_itemy)
    print('*' * 25)

#greeting
greeting = "Hallo selamat datang di IndoApril, saat ini kami menyediakan beberapa produk diskon:"
print(greeting)
print_promotional_items()

proceed_shopping = input("Apakah anda akan lanjut belanja? (yes or no)")
if proceed_shopping == "yes":
    print("Ketik yes untuk meilhat semua produk")
    print("Ketik promo untuk tetap melihat produk yang sedang diskon")
    print("Ketik stop untuk mengakhiri transaksi")
    
    shopping_list = []
    while True:
        show_items = input("Pilih menu (all, promo, stop): ")
        if show_items.lower() == "all":
            print_all_items()
            add_item = input('Tambahkan produk ke kerangjang (ketik angka): ')
            add_item_number = int(add_item) - 1
            if int(add_item) <= len(all_items):
                qty_item = int(input("Jumlah produk yang akan dibeli: "))
                selectedItem = all_items[add_item_number]
                shopping_list.append({
                'quantity': qty_item,
                'item': selectedItem['item'],
                'total': qty_item * selectedItem['harga']
                })

            else:
                print("tidak bisa menambahkan produk yang tidak tersedia")
            show_items = input("Apakah anda ingin menambahkan lagi produk ke keranjang? (yes/stop) ")

        if show_items == "promo":
            print_promotional_items()
            add_item = input('Tambahkan produk ke kerangjang (ketik angka): ')
            add_item_number = int(add_item) - 1
            if int(add_item) <= len(all_items):
                qty_item = int(input("Jumlah produk yang akan dibeli: "))
                selected_item = all_items[add_item_number]
                shopping_list.append({
                'quantity': qty_item,
                'item': selected_item['item'],
                'total': qty_item * selected_item['harga']
                })
            else:
                print("tidak bisa menambahkan produk yang tidak tersedia")
            show_items = input("Apakah anda ingin menambahkan lagi produk ke keranjang? (yes/stop) ")
        
        if show_items == "stop":
            print("\n\n")
            print("*****Struk Belanja*****")
            print("\n")
            print(" Produk    Qty   SubTotal")
            number = 1
            for bill in shopping_list:
                print_bill = str(number) + '. ' + bill['item'] + " " + str(bill['quantity']) + "pcs " + ' = ' + str(bill['total'])
                number += 1
                print(print_bill)

            grandTotal = 0
            for totalbill in shopping_list:
                grandTotal += totalbill['total']
        
            print("Total harga belanja anda = ", grandTotal)
            print("\n")
            print("**********Thank You**********")
            break
