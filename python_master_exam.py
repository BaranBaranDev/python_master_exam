'''
Python Sınav Hazırlık Notları (Vize & Final Formatı)
Bu dosyada Python'un temel konularını içeren sorular ve çözümleri bulunmaktadır.
'''

# 1. Print Çıktı Sorusu
print("Hello, World!")  # Çıktı: Hello, World!
print(5 + 3)  # Çıktı: 8
print("5" + "3")  # Çıktı: 53
print("Python" * 2)  # Çıktı: PythonPython
print("10 / 2 =", 10 / 2)  # Çıktı: 10 / 2 = 5.0

# 2. Veri Tipleri Sorusu
a = 10  # int
b = "Python"  # str
c = 3.14  # float
d = True  # bool
print(type(a), type(b), type(c), type(d))  # Çıktı: <class 'int'> <class 'str'> <class 'float'> <class 'bool'>

# 3. If-Else Kontrol Yapısı
num = 7
if num % 2 == 0:
    print("Çift sayı")  # Çıktı: (Bu çalışmaz çünkü num tek)
else:
    print("Tek sayı")  # Çıktı: Tek sayı


# 4. While Döngüsü ile Faktöriyel Hesaplama
def factorial(n):
    '''Bu fonksiyon verilen sayının faktöriyelini hesaplar.'''
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result


print("5! =", factorial(5))  # Çıktı: 5! = 120


# 5. Fibonacci Algoritması (Detaylı Açıklama)
def fibonacci(n):
    '''
    Fibonacci serisini hesaplayan fonksiyon.
    Fibonacci serisi, her sayının kendinden önceki iki sayının toplamı olduğu bir dizidir.
    Örnek: [0, 1, 1, 2, 3, 5, 8, 13, ...]
    '''
    if n <= 0:
        return "Hata: Pozitif bir sayı giriniz."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    series = [0, 1]  # İlk iki eleman 0 ve 1 olarak başlatılır.
    for i in range(2, n):  # Döngü, serinin devamını hesaplar.
        next_value = series[-1] + series[-2]  # Son iki elemanın toplamı yeni elemanı oluşturur.
        series.append(next_value)  # Yeni eleman listeye eklenir.
    return series


print(fibonacci(10))  # Çıktı: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# 6. Dictionary Kullanımı
student = {"name": "Ali", "age": 20, "grade": "A"}
print(f"Öğrenci Adı: {student['name']}")  # Çıktı: Öğrenci Adı: Ali

# 7. Try-Except ile Hata Yönetimi
try:
    x = int("ABC")
except ValueError:
    print("Hata: Geçersiz giriş!")  # Çıktı: Hata: Geçersiz giriş!


# 8. Not Sistemi
def grade_system(score):
    '''Bu fonksiyon alınan nota göre geçme veya kalma durumunu belirler.'''
    if score >= 90:
        return "AA (Geçti)"
    elif score >= 80:
        return "BB (Geçti)"
    elif score >= 70:
        return "CC (Geçti)"
    elif score >= 60:
        return "DD (Geçti)"
    else:
        return "FF (Kaldı)"


print(grade_system(85))  # Çıktı: BB (Geçti)
print(grade_system(45))  # Çıktı: FF (Kaldı)

# 9. Profesyonel Yazım Kuralları
'''
- Değişken ve fonksiyon isimleri İngilizce ve anlamlı olmalıdır.
- Yorum satırları kodun amacını açıklamalıdır.
- Kod okunabilirliği için girintileme kurallarına uyulmalıdır.
- Python'da snake_case isimlendirme tercih edilmelidir.
- Fonksiyonlar tek bir sorumluluğa sahip olmalıdır (Single Responsibility Principle).
- Hata yönetimi (try-except) ile beklenmeyen hatalar ele alınmalıdır.
'''
