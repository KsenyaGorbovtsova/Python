class Unique(object):

    def __init__(self, items, **kwargs):

        assert len(items) > 0

        ignor_case = False
        for key in kwargs:
            ignor_case = kwargs[key]

        self.lst = list(map(str, items))

        if ignor_case is False:
            self.lst.sort(key=lambda x: x.lower())
        else:
            self.lst.sort()

        self.newlst = []
        counter = 0
        self.newlst.append(self.lst[0])
        for i in self.lst:
            if ignor_case is False:
                if i.lower() != self.newlst[counter].lower():
                    self.newlst.append(i)
                    counter += 1
            elif ignor_case is True:
                if i != self.newlst[counter]:
                    self.newlst.append(i)
                    counter += 1

        self.index = -1

    def __next__(self):
        if self.index >= len(self.newlst) - 1:
            raise StopIteration
        self.index += 1
        return self.newlst[self.index]

    def __iter__(self):
        return self
