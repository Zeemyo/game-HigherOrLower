import random
from game_data import data
from art import logo, vs
from replit import clear


def get_random_data():
    """Data berikut merupakan data game yang di ambil secara random"""
    return random.choice(data)


def format_data(account):
    """Format data diambil untuk dapat di print dengan format: name, description, dan country"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, {description}, dari {country}"


def check_jawaban(tebakan, a_answer, b_answer):
    """Memeriksa jawaban folower dari pemain dengan data game, jika mengembalikan true maka benar dan jika mengembalikan false maka salah"""
    if a_answer > a_answer:
        return tebakan == "a"
    else:
        return tebakan == "b"


def game():
    print(logo)
    skor = 0
    status_game = True
    account_a = get_random_data()
    account_b = get_random_data()

    while status_game:
        account_a = account_b
        account_b = get_random_data()

        while account_a == account_b:
            account_b == get_random_data()

        print(f"Membandingkan A: {format_data(account_a)}")
        print(vs)
        print(f"Membandingkan B: {format_data(account_b)}")

        guess = input("Siapa yang memiiki lebih banyak follower? ketika 'A' atau 'B' ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        apakah_benar = check_jawaban(guess, a_follower_count, b_follower_count)

        clear()
        print(logo)
        if apakah_benar:
            skor += 1
            print(f"Kamu benar! skor kamu sekarang adalah {skor}.")
        else:
            status_game = False
            print(f"Kamu salah, skor terakhirmu adalah {skor}.")

game()

"""Di game ini, kamu hanya perlu meebak antara kepopuleran dari dua data yang berbeda, jika kamu menjawab pertanyaan yang benar maka kamu akan dapat 1 poin, jika salah maka game akan berakhir"""