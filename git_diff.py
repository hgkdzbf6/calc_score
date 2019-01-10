import numpy as np
import math

class DiffBlock:
    def __init__(self):
        self.lost_index = []
        self.more_index = []
        self.diag_index = []
        pass
            
    def calc(self,a, b):
        Xs = []
        X = {}
        X[1] = 0
        go_ahead = True
        d = 0
        the_max = len(a)+len(b)
        while d <= the_max and go_ahead:
            k=-d
            while k<=d:
                down = (k==-d or (k!=d and X[k-1]<X[k+1]))
                if down:
                    k_prev = k+1
                else:
                    k_prev = k-1
                # 起始位置
                x_start = X[k_prev]
                y_start = x_start - k_prev
                # mid位置
                if down:
                    x_temp = x_start
                else:
                    x_temp = x_start + 1
                y_temp = x_temp-k

                x_end = x_temp
                y_end = y_temp
                
                while x_end < len(a) and y_end < len(b) and a[x_end] == b[y_end] :
                    x_end=x_end+1
                    y_end=y_end+1
                X[k] = x_end

                # 到终点，找到了最终路线
                if x_end>=len(a) and y_end >=len(b):
                    go_ahead = False
                    break
                k=k+2
            # 如果有8个以上错误就抛弃，返回结果是0
            Xs.append(X)
            d=d+1
        print(Xs)
        # 回溯
        path =[]
        pt = [len(a),len(b)]
        path.append(pt)
        d = len(Xs)-1
        while (pt[0]>0 or pt[1]>0) :
            X = Xs[d]
            k = pt[0] - pt[1]
            x_end = X[k]
            y_end = pt[0] - k
            while x_end>0 and y_end>0 and x_end <= len(a) and y_end <= len(b) and a[x_end-1]==b[y_end-1]:
                x_end = x_end - 1
                y_end = y_end - 1
                path.append([x_end, y_end])
            down = (k==-d or (k!=d and X[k-1]<X[k+1]))
            if down:
                k_prev = k+1
            else:
                k_prev = k-1
            print("hello")
            print(path)
            if k_prev == 2:
                pass
                print(path)
                print(X)
            x_start = X[k_prev]
            y_start = x_start - k_prev
            # path.append([x_start, y_start])
            pt[0] = x_start
            pt[1] = y_start
            d=d-1

        path = path[1:len(path)]
        if len(path)>=2:
            size = len(path)
            i = size-2
            while i>=0:
                prev_point = path[i+1]
                point = path[i]
                res = self.calc2point(prev_point,point)
                if res == "right":
                    print("-{}".format(a[prev_point[0]]))
                elif res == "down":
                    print("+{}".format(b[prev_point[1]]))
                elif res == "diag":
                    print("={}".format(a[prev_point[0]]))
                i=i-1
        print(self.lost_index)
        print(self.more_index)
        print(self.diag_index)
        print(path)
        

    def calc2point(self, p1, p2):
        if p1[0] == p2[0] and p1[1]+1 == p2[1]:
            # 如果少了字符的话，向下移动
            self.lost_index.append(p1[0])
            return "down"
        elif p1[1] == p2[1] and p1[0]+1 == p2[0]:
            # 如果多了字符，向右移动
            self.more_index.append(p2[1])
            return "right"
        elif p1[0]+1 == p2[0] and p1[1]+1 == p2[1]:
            self.diag_index.append(p1[0])
            return "diag"

def main():
    # a = 'GS150415232'
    # b = 'GS150415234'
    a = 'ABCDEFG'
    b = 'BBCDEFG'
    # b = 'hello world'
    diff_block = DiffBlock()
    diff_block.calc(a,b)
    # diff_block.score()

if __name__ == '__main__':
    main()