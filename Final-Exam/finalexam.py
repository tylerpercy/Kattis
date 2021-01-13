# Tyler Percy
# 1/13/21

n = int(input())

correct_ans = []
shifted_ans = []

for i in range(0, n):
    correct_ans.append(input())

for i in range(0, n-1):
    shifted_ans.append(correct_ans[i+1])

final_grade = 0

for i in range(0, n):
    try:
        if shifted_ans[i] == correct_ans[i]:
            final_grade+=1
    except:
        pass

print(final_grade)
    
#print(correct_ans)
#print(shifted_ans)