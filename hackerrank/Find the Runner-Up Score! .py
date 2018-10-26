if __name__ == '__main__':
    #n = int(raw_input())
    #arr = map(int, raw_input().split())
    N=int(input())
    list=list(set(map(int,input().strip().split(" "))))
    list.sort(reverse=True)
    print(list[1])

    
