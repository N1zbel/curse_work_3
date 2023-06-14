class Operations:
    def __init__(self, user_operations):
        """инициализация всех операций"""
        self.user_operations = user_operations
        self.last_operations = self.set_last_operations()

    def __repr__(self):
        """Возращает строку Operations"""

        return f"Operations({self.user_operations})"


    def set_last_operations(self):
        """Возвращает последние 5 операций, отсортированных по дате"""
        operations = filter(
            lambda item: item.get("date") and item["state"] == "EXECUTED",
            self.user_operations)
        operations = sorted(operations, key=lambda item: item["date"])[-5:]
        return operations


    @staticmethod
    def date_revers(date):
        """Возвращает дату в формате ДД.ММ.ГГГГ """
        revert_date1 = date[:10]
        day, month, year = revert_date1[-2:], revert_date1[-5:-3], revert_date1[:4]
        return f"{day}.{month}.{year}"

    def hide_information_from(self, _from):
        """частично скрывает информацию о счете отправки"""
        check = _from.split()
        check_number = check[-1]
        if len(check_number) == 16:
            return f"{' '.join(check[:-1])} {check_number[:4]} {check_number[5:7]}** **** {check_number[-4:]}"
        else:
            return f"{' '.join(check[:-1])} **{check_number[-4:]}"

    def hide_information_to(self, _to):
        """частично скрывает информацию о счете получения"""
        check = _to.split()
        check_number = check[-1]
        return f"{check[0]}  **{check_number[-4:]}"

    def last_five_operations(self):
        """выводит инфу о последних 5 операциях"""
        for operation in self.last_operations:
            if operation == {}:
                continue
            if operation.get('from'):
                print(f'Номер операции: {operation["id"]}')
                print(f"Дата перевода: {Operations.date_revers(operation['date'])} \nОперация -> {operation['description']}")
                print(f"{self.hide_information_from(operation['from'])} -> {self.hide_information_to(operation['to'])}")
                print(f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}")
                print()
            else:
                print(f'Номер операции: {operation["id"]}')
                print(f"Дата перевода: {Operations.date_revers(operation['date'])} \nОперация -> {operation['description']}")
                print(f"Пополнение счета -> {self.hide_information_to(operation['to'])}")
                print(f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}")
                print()
