class A(object):
    def __init__(self):
        self.unit=int(input('Enter unit:'))


class B(A):
    def __init__(self):
        super().__init__()
        print('Unit is:',self.unit)
if __name__ == "__main__":
    B()
    pass