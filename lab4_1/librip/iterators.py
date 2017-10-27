class Unique(object):
    def __init__(self, items, **kwargs):
        
        assert len(items) > 0
        
        self.ignor_case = kwargs.get('ignore_case', False)
        self.lst = (x for x in items)
        self.newlst = list()
    
    def __next__(self):
        try:
            buffer = next(self.lst)
            
            if isinstance(buffer, str) and self.ignor_case is False:
                if buffer.lower() not in self.newlst:
                    self.newlst.append(buffer.lower())
                    return buffer
            elif isinstance(buffer, str) and self.ignor_case is True:
                if buffer not in self.newlst:
                    self.newlst.append(buffer)
                    return buffer
            else:
                if buffer not in self.newlst:
                    self.newlst.append(buffer)
                    return buffer
            return next(self)
        
        except Exception:
            raise StopIteration

def __iter__(self):
    return self
