import pandas as pd
from faker import Faker
import random

fake = Faker()

def generate_clients(n=100):
    clients = []
    for i in range(n):
        client_id = i + 1
        age = random.randint(18, 70)
        income = random.randint(1000, 5000)
        charges = random.randint(200, 2000)
        clients.append([client_id, age, income, charges])
    df_clients = pd.DataFrame(clients, columns=["client_id", "age", "income", "charges"])
    df_clients.to_csv("../data/clients.csv", index=False)

def generate_loans(n=100):
    loans = []
    for i in range(n):
        client_id = random.randint(1, 100)
        amount = random.randint(1000, 20000)
        duration_months = random.choice([12, 24, 36, 48, 60])
        loans.append([client_id, amount, duration_months])
    df_loans = pd.DataFrame(loans, columns=["client_id", "amount", "duration_months"])
    df_loans.to_csv("../data/loans.csv", index=False)

if __name__ == "__main__":
    generate_clients()
    generate_loans()
    print("Fake data generated ✅")
