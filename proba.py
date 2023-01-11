import random

retries = 0
def randomNum():
    my_nums = []
    for i in range(4):
        my_nums.append(random.randint(1,10))
    
    
    if len(set(my_nums)) < len(my_nums):
        global retries
        retries+=1
        randomNum()
    else:
        lotto_number = 1
        for items in my_nums:
            print("Lotto number {}".format(lotto_number), items)
            lotto_number+=1
        print("The number of tries", retries)

def checkDistinct(random, nums):
    for i in range(0, len(nums)):
        if random == nums[i]:
            return False
    return True

def getLottoNums():
    nums = [random.randint(1, 10)] 
    for i in range(1, 4): # 1, 2, 3
        r = random.randint(1, 10)
        while not checkDistinct(r, nums):
            r = random.randint(1, 10) 
        nums.append(r)
    return nums 

def getLottoNums():
    global retries
    nums = [random.randint(1, 10)]
    r = random.randint(1, 10)
    
    while not checkDistinct(r, nums):
        retries += 1  
inp = 'y'
while(inp == 'y'):
    retries = 0
    nums = getLottoNums()
    for i in range(0, 4):
        print(f"Lotto number {i+1}  {nums[i]}")
    print(f"It took {retries} retries to get the four different numbers")
    inp = input("Do you want to play again? (y)")
getLottoNums()    
checkDistinct()
randomNum()