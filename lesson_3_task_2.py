from smartphone import Smartphone


catalog = [
    Smartphone("Apple", "iPhone 13", "+79123456789"),
    Smartphone("Samsung", "Galaxy S22", "+79098765432"),
    Smartphone("Xiaomi", "Redmi Note 10", "+79234567890"),
    Smartphone("Google", "Pixel 6", "+79345678901"),
    Smartphone("Huawei", "P50 Pro", "+79456789012"),
]


for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
