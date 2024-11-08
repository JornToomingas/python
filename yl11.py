#08.11.24 Toomingas
#Ülesanne 11

def pikim_sona(*sonad):
    pikim = 0
    for i in sonad:
        if len(i)>pikim:
            pikim=len(i)
    print(f"Pikim sõna on {pikim} märki!")





pikim_sona("Üks", "Kaks", "Kolmkümmend", "abc123def456ghi789j0")