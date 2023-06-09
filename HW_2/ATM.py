class ATM:
    limit_ATM = 1_000_000_000
    start_limit = 0
#     text = int(input("""Добрый день! Какую операцию хотите провести?
# 1.Снятие
# 2.Пополнение
# 3.Выход
#  """))

    def pull_money(self, sum):
        if sum % 50 == 0:
            self.start_limit += sum
            print(f'Баланс успешно пополнен. Ваш баланс: {self.start_limit}')
        else:
            print('Сумма должна быть кратна 50')

    def get_money(self, sum):
        # проверям что бы сумма снятия была меньше суммы баланса и кратна 50
        if sum < self.start_limit and sum % 50 == 0:
            procent = (0.015 * sum) / 100
            min_procent = 30
            max_procent = 600
            if sum < 2000:
                # если процент от суммы меньше минимально процента, то комиссия 30
                self.start_limit -= sum + min_procent
                print(f'Снятие прошло успешно. Ваш баланс: {self.start_limit}. Комиссия {min_procent} у.е.')
            # если процент от суммы больше максимального процента, то комиссия 600
            elif sum > 40000:
                self.start_limit -= sum + max_procent
                print(f'Снятие прошло успешно. Ваш баланс: {self.start_limit}. Комиссия {max_procent} у.е.')
            else:
                self.start_limit -= sum + procent * 100
                print(f'Снятие прошло успешно. Ваш баланс: {self.start_limit}. Комиссия {procent * 100}')
        else:
            print(f'Недостаточно денежных средств. Ваш баланс: {self.start_limit}')

    def exit_ATM(self):
        print('До новых встреч!')


bank = ATM()
print(bank.start_limit)
bank.pull_money(50000000)
bank.get_money(200000)

