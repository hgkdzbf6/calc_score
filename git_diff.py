import difflib

class MyDiff:
    def __init__(self):
        self.len_a = 0
        self.len_b = 0
        self.lost_list = []
        self.more_list = []
        self.diag_list = []
        self.modi_list = []
        pass
    
    def run(self,a,b):
        self.calc(a,b)
        return self.score()

    def calc(self,a,b):
        d = difflib.Differ()    
        diff = d.compare(a,b)
        self.len_a = len(a)
        self.len_b = len(b)
        s = ''.join(diff)
        index = 0
        for i in range(0,len(s),3):
            if s[i]==' ':
                self.diag_list.append(index)
                index = index+1
            elif s[i]=='-':
                self.lost_list.append(index)
                # index 不变
            elif s[i]=='+':
                self.more_list.append(index)
                index = index+1
            pass
        
        for item in self.lost_list:
            for it in self.more_list:
                if it==item:
                    self.modi_list.append(it)
                    # lost_list.remove(it)
                    # more_list.remove(it)
                    break
        
        for item in self.modi_list:
            self.lost_list.remove(item)
            self.more_list.remove(item)

    def score(self):
        base_score = 0
        for i in range(self.len_a):
            base_score=base_score+i*i
        diag_score = 0

        for i in self.diag_list:
            diag_score=diag_score+i*i
        
        score = diag_score / base_score
        return score
        

def main():
    a='GS150415234'
    b='GS150415234'
    d = MyDiff()
    print(d.run(a,b))

if __name__ == "__main__":
    main()
