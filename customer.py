import time

def get_current_date():
    return time.strftime("%Y-%m-%d", time.localtime())  # Doğrudan "YYYY-MM-DD" formatında alıyoruz

# Musteri veritabanı
database = {
    "Ahmet": [3000, 1800, "2024-10-10"],
    "Joe": [12345, 9876, "2021-10-28"]
}

def update_customer(database, customer_name, purchase_amount, payment_amount):
    if customer_name in database:
        # Müşteri zaten varsa, değerleri güncelle
        database[customer_name][0] += purchase_amount
        database[customer_name][1] += payment_amount
        database[customer_name][2] = get_current_date()  # son işlem tarihini güncelle
        print(f"{customer_name} has been updated: {database[customer_name]}")
    else:
        # Yeni müşteri ekle
        database[customer_name] = [purchase_amount, payment_amount, get_current_date()]
        print(f"New customer added: {customer_name} = {database[customer_name]}")

while True:
    customer_name = input("Müşteri adını girin veya çıkmak için EOT yazın: ")
    if customer_name == "EOT":
        print("Program sonlandırılıyor...")
        break
    try:
        purchase_amount = int(input("Satın alım tutarını girin: "))
        payment_amount = int(input("Ödeme tutarını girin: "))
        update_customer(database, customer_name, purchase_amount, payment_amount)
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")

print("\nGüncel müşteri veritabanı: ")
for customer in database:
    print(customer, ":", database[customer])

