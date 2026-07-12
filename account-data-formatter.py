with open("AccountList.txt", "r") as f:
    accounts = f.readlines()
with open("bind.txt", "w") as f:
    for account in accounts:
        account = account.strip().replace(":", " ")
        logpass = account.replace(" ", ":")
        f.write(f"/bind {account}\n")
print("Успешно!")
