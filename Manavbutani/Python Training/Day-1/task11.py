

def ATM(amount):
    pink=0
    blue=0
    yellow=0
    while(amount!=0):
        if amount>=2000:
            amount-=2000
            pink+=1
        if amount>=500:
            amount-=500
            yellow+=1
        if amount>=100:
            amount-=100
            blue+=1
        if amount<100 and amount!=0:
            print(f"{amount} will be not full filled")
            break
    print("2000 notes frequency is ",pink)
    print("500 notes frequency is ",yellow)
    print("100 notes frequency is ",blue)

if __name__=="__main__":
    amount=int(input())
    # pink=0
    # yellow=0
    # blue=0
    
    ATM(amount)