def undoom_dice(dieA, dieB):
    sums=range(2, 13)
    total=len(dieA)*len(dieB) 

    t=generate_combo([2,3,2,3,2,3,2,3], 4)
    ComboA=list()
    for x in t:
        lst=[1]+list(x)+[4]
        ComboA.append(lst)
    ComboB=generate_combo([1,2,3,4,5,6,7,8], 6)

    for A in ComboA:
        for B in ComboB:
            if same_prob(A, B,total,sums):
                return A,B

    return None, None  
    
def generate_combo(items, r):
    combinations = []

    def f(l, left, k):
        if k == 0:
            combinations.append(l[:])
            return
        for i in range(len(left)):
            l.append(left[i])
            f(l, left[i + 1:], k - 1)
            l.pop()

    f([], items, r)
    return combinations

def same_prob(A, B,outcomes,sums):
    original_prob=cal_prob(dieA, dieB)
    new_prob=cal_prob(A, B)
    orig_probs=list(original_prob.values())
    new_probs=list(new_prob.values())

    for orig, new in zip(orig_probs, new_probs):
        if abs(orig-new)>0:
            return False
    
    return True
    
def cal_prob(dieA, dieB):
    toutcomes=len(dieA)*len(dieB)  
    probabilities={}
    for outcome in range(2, 13):
        c=0
        for numA in dieA:
            for numB in dieB:
                if numA+numB==outcome:
                    c+= 1
        
        probability=c/toutcomes
        probabilities[outcome]=probability
    return probabilities


dieA=[1,2,3,4,5,6]
dieB=[1,2,3,4,5,6]
newdieA, newdieB=undoom_dice(dieA, dieB)

print("New_Die_A = ", newdieA)
print("New_Die_B = ", newdieB)
