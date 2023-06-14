import pytest

from classes.operations import Operations


def test_date_revers(operation):
    assert Operations.date_revers(operation[0]['date']) == '26.08.2019'


# def test_repr(operation):
#     operation = Operations(operation[0])
#     assert operation.__repr__() == f'Operations({"id": 1,"state": "EXECUTED","date": "2019-08-26T10:50:58.294041"})'

def test_hide_information_to(operation):
    info_to = Operations(operation)
    _to = operation[0]["to"]
    assert info_to.hide_information_to(_to) == 'Счет  **9589'

def test_hide_information_from(operation):
    info_from = Operations(operation)
    _from = operation[0]['from']
    _from_2 = operation[2]['from']
    assert info_from.hide_information_from(_from) == 'Maestro 1596 37** **** 5199'
    assert info_from.hide_information_from(_from_2) == 'Счет **6952'

def test_last_five_operations(operation, capsys):
    operation = Operations(operation)
    operation.last_five_operations()
    captured = capsys.readouterr()
    assert 'Номер операции: 3' in captured.out





@pytest.fixture
def operation():
    new_operation = [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
        {
            "id": 2,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        },
        {
            "id": 3,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 4,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {
                "amount": "48223.05",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431"
        }, {}]
    return new_operation
