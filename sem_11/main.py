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
            return self.persons[0].get('work')
