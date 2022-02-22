scores = eval(input())
p1=scores[0]
p2=0
for score in range(0,len(scores)-1):
    if(scores[score]%2 == 1):
        p2=p2+scores[score+1]
    else:
        p1=p1+scores[score+1]

if(len(scores)>2):
    print(f"p1: {p2}, p2: {p1}")
else:
    print(f"p1: {p1}, p2: {p2}")