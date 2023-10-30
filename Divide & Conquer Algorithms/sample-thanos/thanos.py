n_p = int(input())
people = list(map(int, (input()).strip().split(" ")))

amoches = set()
n_amoches = int(input())

list(map(lambda x : amoches.add(int(x)), (input()).strip().split(" ")))

n_comp = int(input())

# result = list(map(lambda x : ":_(" if int(x) in amoches else ":)", (input()).strip().split(" ")))

check = list(map(int, input().strip().split()))
for i in range(n_comp):
    if check[i] in amoches:
        print(":_(")
    else:
        print(":)")


#for i in result:
    #print(i)