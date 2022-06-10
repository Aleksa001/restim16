class Electricity:
    def __init__(self, personal_id, monthly_value, month):
        self.personal_id = personal_id
        self.monthly_value = monthly_value
        self.month = month

    def __str__(self):
        return str(self.__class__) + '\n' + '\n'.join(
            (str(item) + ' = ' + str(self.__dict__[item]) for item in self.__dict__))

class Option:
    def __init__(self, opt, parametar):
        self.opt = opt
        self.parametar = parametar