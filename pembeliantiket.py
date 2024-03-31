print("Selamat datang di Cinema XXI")
print("Daftar Genre:")
print("1. Action")
print("2. Comedy")
print("3. Romance")
print("4. Horror")

genre = input("Pilih genre film yang ingin ditonton (masukkan nomor): ")

genres = {
    '1': 'Action',
    '2': 'Comedy',
    '3': 'Romance',
    '4': 'Horror'
}

genre_name = genres.get(genre)

if genre_name:
    films = {
        'Action': ['Avengers: Endgame', 'Mad Max: Fury Road', 'Mission Impossible: Fallout'],
        'Comedy': ['Deadpool', 'Superbad', 'The Hangover'],
        'Romance': ['The Notebook', 'Pride and Prejudice', 'Titanic'],
        'Horror': ['The Conjuring', 'Get Out', 'IT']
    }
    prices = {
        'Action': [40, 40, 40],
        'Comedy': [40, 35, 40],
        'Romance': [40, 40, 40],
        'Horror': [40, 40, 40]
    }
    days = {
        'Action': ['Jumat', 'Sabtu', 'Minggu'],
        'Comedy': ['Jumat', 'Sabtu', 'Minggu'],
        'Romance': ['Jumat', 'Sabtu', 'Minggu'],
        'Horror': ['Jumat', 'Sabtu', 'Minggu']
    }
    
    film = films[genre_name]
    price = prices[genre_name]
    day = days[genre_name]
    
    print(f"Genre: {genre_name}")
    print("Jenis Film:")
    for i in range(len(film)):
        print(f"{i+1}. {film[i]} - Harga: {price[i]} - Hari: {day[i]}")
    
    film_choice = int(input("Pilih film yang ingin ditonton (masukkan nomor): "))
    film_name = film[film_choice - 1]
    ticket_count = int(input("Masukkan jumlah tiket yang ingin dibeli: "))
    total_price = price[film_choice - 1] * ticket_count
    print(f"Total Price: {total_price}")
    
    confirm = input("Apakah Anda ingin membeli tiket (y/n)? ")
    if confirm.lower() == 'y':
        nama = input("Nama: ")
        umur = input("Umur: ")
        print("Detail Pembelian:")
        print("1. Nama:", nama)
        print("2. Umur:", umur)
        print("3. Genre:", genre_name)
        print("4. Film:", film_name)
        print("5. Jumlah Tiket:", ticket_count)
        print("6. Total Price:", total_price)
    else:
        print("Terima kasih telah mengunjungi Cinema XXI")
else:
    print("Terima kasih telah mengunjungi Cinema XXI")