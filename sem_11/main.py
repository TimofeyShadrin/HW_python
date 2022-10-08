class Person:

    def __init__(self, f_name, s_name, l_name, tels):
        self.f_name = f_name
        self.s_name = s_name
        self.l_name = l_name
        self.tels = tels

    def get_phone(self):
        return self.tels.get('private')

    def get_name(self):
        return f'{self.f_name} {self.s_name} {self.l_name}'.title()

    def get_work_phone(self):
        return self.tels.get('work')

    def get_sms_text(self):
        return f'Уважаемый {self.f_name} {self.s_name}! Примите участие ' \
               f'в нашем беспроигрышном конкурсе для физических лиц.'


class Company:

    def __init__(self, company_name, type_company, tels_company, *persons):
        self.company_name = company_name
        self.type_company = type_company
        self.tels_company = tels_company
        self.persons = persons

    def get_phone(self):
        if self.tels_company.get('contact'):
            return self.tels_company.get('contact')
        else:
            return self.persons[0].get_work_phone()

    def get_name(self):
        return self.company_name

    def get_sms_text(self):
        return f'Для компании {self.company_name} есть супер предложение! ' \
               f'Примите участие в нашем беспроигрышном конкурсе для {self.type_company}.'


def send_sms(*args):
    for item in args:
        if item.get_phone():
            print(f'Отправлено СМС на номер {item.get_phone()} с текстом: {item.get_sms_text()}')
        else:
            print(f'Не удалось отправить сообщение абоненту: {item.get_name()}')


# Example 1:
# person1 = Person('Ivan', 'Ivanovich', 'Ivanov', {'private': 123, 'work': 456})
# person2 = Person('Ivan', 'Petrovich', 'Petrov', {'private': 789})
# person3 = Person('Ivan', 'Petrovich', 'Sidorov', {'work': 789})
# person4 = Person('John', 'Unknown', 'Doe', {})
# company1 = Company('Bell', 'OOO', {'contact': 111}, person3, person4)
# company2 = Company('Cell', 'AO', {'non_contact': 222}, person2, person3)
# company3 = Company('Dell', 'Ltd', {'non_contact': 333}, person2, person4)
# send_sms(person1, person2, person3, person4, company1, company2, company3)

# Example 2:
person1 = Person('Степан', 'Петрович', 'Джобсов', {'private': 555})
person2 = Person('Боря', 'Иванович', 'Гейтсов', {'private': 777, 'work': 888})
person3 = Person('Семен', 'Робертович', 'Возняцкий', {'work': 789})
person4 = Person('Леонид', 'Арсенович', 'Тордвальсон', {})
company1 = Company('Яблочный комбинат', 'OOO', {'contact': 111}, person1, person3)
company2 = Company('ПластОкно', 'AO', {'non_contact': 222}, person2)
company3 = Company('Пингвинья ферма', 'Ltd', {'non_contact': 333}, person4)
send_sms(person1, person2, person3, person4, company1, company2, company3)
