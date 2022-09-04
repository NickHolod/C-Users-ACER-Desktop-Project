from pandas.io import excel
from utils import check_email, number_check
import pandas


def is_correct2(email, number):
    assert type(email) == str, 'email must be string type'
    assert type(number) == str, 'number must be string type'
    if number_check(number) is False:
        return False
    if check_email(email) is False:
        return False
    return True


class PhoneBook:
    def __init__(self, path=None):
        if path is None:
            self.df = pandas.DataFrame({"name": [], "email": [], "number": []})
        else:
            self.df = pandas.read_csv(path)

    def add(self, un_name, un_email, un_number):
        assert type(un_email) == str, 'email must be string type'
        assert type(un_name) == str, 'name must be string type'
        assert type(un_number) == str, 'number must be string type'
        if is_correct2(un_email, un_number) is True:
            new_row = {'name': un_name, 'email': un_email, 'number': un_number}
            self.df = self.df.append(new_row, ignore_index=True)

    def info(self):
        return self.df

    def save(self, path, format='excel'):
        print(path)
        assert type(format) == str, 'format must be string type'
        assert type(path) == str, 'path must be string type'
        if format == 'excel':
            self.df.to_excel(path, index=False)
        elif format == 'csv':
            self.df.to_csv(path, index=False)
        else:
            print('ERR: unknown format')

    def change_email(self, name, new_email):
        assert type(name) == str, 'name must be string type'
        self.df.loc[self.df.isin([name]).any(axis=1), 'email'] = new_email
        return self.df

    def change_number(self, name, new_number):
        assert type(name) == str, 'name must be string type'
        self.df.loc[self.df.isin([name]).any(axis=1), 'number'] = new_number
        return self.df

    def read(self, path):
        assert type(path) == str, 'path must be string type'
        if path.endswith('xlsx') is True:
            self.df = pandas.read_excel(path)
        if path.endswith('csv') is True:
            self.df = pandas.read_csv(path)
        else:
            print('ERR: unknown path')

    def delete(self, contact):
        assert type(contact) == str, 'contact must be string type'
        buffer = []
        for i in self.df['name'].index:
            if self.df['name'][i] == contact:
                buffer.append(self.df['number'][i])
                if len(buffer) == 1:
                    self.df.drop(labels=[i], axis=0, inplace=True)
                    print('bla')
                if len(buffer) > 1:
                    print('Which number do you want to delete?', buffer)
