import random
import string

def randomString(stringLength):

    test = ""
    for i in range(stringLength):
        x = random.randint(32, 122)
        letter = chr(x)
        test =test + letter

    return test




def createPopulation(number,strlen):
    pop = {}
    for i in range(number):
        temp = randomString(strlen)
        tempDict = {temp:0}
        pop.update(tempDict)
    # print(pop)
    return pop


def fitness(pop, ft, strlen):
    # popText = pop.keys()
    # print(popText)

    # print("fitness",pop)
    cn=0
    for text in pop:
        cn += 1
        count = pop[text]
        # print("count",count)
        # print("this is ",text,"count",cn)
        for i in range(0,strlen):
            # print("i:", i)

            # try:
            #     if(text[i] == ft[i]):
            #         count = count+1
            # except:
            #     print("error",text)

            if (text[i] == ft[i]):
                count = count+1
                # print(pop[text])
        pop[text] = count * count
        # print("c:",cn)
    # print(len(pop))
    # print(pop)
    return pop




def genePool(pop):
    pool = []
    for text in pop:
        num = pop[text]*50
        pool.append(text)
        for i in range(num):
            pool.append(text)
    print("totalpool: ",len(pool))
    return pool

def selectParent(pool):
    total = len(pool)
    # print("total ",total)
    x=random.randint(0,total-1)
    y = random.randint(0, total-1)
    firstParent = pool[x]
    secondParent = pool[y]
    return firstParent,secondParent




def crossover(first, second,strlen):
    cp1 = random.randint(0,strlen) #cp = crossover point
    # cp2 = random.randint(0, strlen)  # cp = crossover point
    firstChild = first[0:cp1] + second[cp1:strlen]
    # if len(firstChild)!= 5:
    #     print("error here in fc b m")

    # if len(secondChild) != 5:
    #     print("error here in sc b m")
    firstChild = mutation(0.02,firstChild)
    # if len(firstChild) != 5:
    #     print("error here in fc a m",firstChild)

    # if len(secondChild) != 5:
    #     print("error here in sc a m",secondChild)
    return firstChild


def mutation(n, text):
    memberSize = len(text)
    # if(memberSize != 5):
    #     print("error inside mutation before 1111")
    finalText=""
    if(n<=random.random()):
        mp = random.randint(0,memberSize-1) #mp = Mutation Point
        x = random.randint(32, 122)
        letter = chr(x)
        finalText = text[0:mp]+ letter + text[mp+1:memberSize]
        # if (len(finalText) != 5):
        #     print("error inside mutation after 2222222")
    else:
        finalText = text
        # if (len(finalText) != 5):
        #     print("error inside mutation after 3333333")
    return finalText


if __name__ == '__main__':
    popSize = 500
    text = "hello shubham"
    strlen = len(text)
    pop = createPopulation(popSize, strlen)

    print(pop)
    pop = fitness(pop, text, strlen)
    # print(pop.values())
    j = 1
    while (True):

        print("\n\tGeneration: ",j,"\n")

        pool = genePool(pop)
        pop.clear()

        for i in range(round(popSize)):
            first, second = selectParent(pool)
            firstChild= crossover(first, second, strlen)
            temp = {firstChild:0}
            pop.update(temp)
        pop = fitness(pop, text, strlen)
        m = max(pop.values())
        for x in pop.keys():
            if m == pop[x]:
                print("fittest ", x, " fitness value ",(m/(strlen*strlen))*100)
                break
        if(text in pop.keys()):
            print("found in ", j, " generation")
            break
        j += 1
        # print(len(pop))