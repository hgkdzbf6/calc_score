import numpy as np
import math

class DiffBlock:
    def __init__(self):
        pass
            
    def calc(self,str, pattern):
        # 5

        # a = 'abcabc'
        # b = 'bcbd'
        # 4

        # a = 'abcabc'
        # b = 'abc'
        # 3

        N = len(str)
        M = len(pattern)

        MAX = max(0, M+N)
        V = np.zeros((2*MAX+1), np.int)

        dist = -1

        for D in range(MAX):
            for k in range(-D, D+1, 2):
                if k == -D or k != D and V[k-1] < V[k+1]:
                    x = V[k+1]
                else:
                    x = V[k-1] + 1

                y = x - k

                while x < N and y < M and (y < 0 or str[x] == pattern[y]):
                    x += 1
                    y += 1

                V[k] = x

                if x >= N and y >= M:
                    dist = D
                    break

            if dist != -1:
                break
        self.dist = dist
        self.V = V
        self.str_len = len(str)
        self.max_len = MAX
        self.pattern_len = len(pattern)

    def score(self):
        print(self.dist)
        print(self.V)
        print(len(self.V))
        print(self.str_len)
        print(self.pattern_len)
        the_sum = np.sum(np.array(self.V))
        self.score = 1- math.exp(-self.str_len / (the_sum - self.str_len) - (the_sum - self.str_len)/self.str_len)
        self.score = self.score - math.fabs(self.str_len - self.pattern_len)/ self.str_len
        print(self.score)

def main():
    
    a = 'abcabca'
    b = 'abcabca'
    diff_block = DiffBlock()
    diff_block.calc(a,b)
    diff_block.score()

if __name__ == '__main__':
    main()