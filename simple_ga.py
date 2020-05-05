import random


def randomString(stringLength):
    """

    :param stringLength: Required Length of each string in the population
    :return: test : each string
    """

    test = ""
    for i in range(stringLength):
        x = random.randint(32, 122)
        letter = chr(x)
        test = test + letter

    return test




def createPopulation(number,strlen):
    """

    :param number: Number of members in a population
    :param strlen: Length of each string in the population
    :return: list of population
    """
    pop = {}
    for i in range(number):
        temp = randomString(strlen)
        tempDict = {temp: 0}
        pop.update(tempDict)
    return pop


def fitness(pop, ft, strlen):
    """

    :param pop:
    :param ft:
    :param strlen:
    :return:
    """

    cn = 0
    for text in pop:
        cn += 1
        count = pop[text]

        for i in range(0,strlen):

            if (text[i] == ft[i]):
                count = count+1

        pop[text] = round(((count * count * count) / (strlen * strlen * strlen)) * 100)
    return pop




def genePool(pop):
    """

    :param pop:
    :return:
    """
    pool = []
    for text in pop:
        num = pop[text]*50
        pool.append(text)
        for i in range(num):
            pool.append(text)
    print("totalpool: ", len(pool))
    return pool

def selectParent(pool):
    """

    :param pool:
    :return:
    """
    total = len(pool)
    x = random.randint(0,total-1)
    y = random.randint(0, total-1)
    firstParent = pool[x]
    secondParent = pool[y]
    return firstParent, secondParent




def crossover(first,second,strlen):
    """

    :param first:
    :param second:
    :param strlen:
    :return:
    """
    cp1 = random.randint(0,strlen) #cp = crossover point
    firstChild = first[0:cp1] + second[cp1:strlen]
    firstChild = mutation(0.02,firstChild)
    return firstChild


def mutation(n, text):
    """

    :param n:
    :param text:
    :return:
    """
    memberSize = len(text)
    if(n<=random.random()):
        mp = random.randint(0,memberSize-1) #mp = Mutation Point
        x = random.randint(32, 122)
        letter = chr(x)
        finalText = text[0:mp] + letter + text[mp+1:memberSize]

    else:
        finalText = text

    return finalText


if __name__ == '__main__':

    popSize = 500
    text = "hello"
    strlen = len(text)
    pop = createPopulation(popSize, strlen)

    print(pop)
    pop = fitness(pop, text, strlen)
    j = 1
    while True:

        print("\n\tGeneration: ", j, "\n")

        pool = genePool(pop)
        pop.clear()

        for i in range(round(popSize)):
            first, second = selectParent(pool)
            firstChild = crossover(first, second, strlen)

            temp = {firstChild: 0}
            pop.update(temp)
        pop = fitness(pop, text, strlen)
        m = max(pop.values())
        for x in pop.keys():
            if m == pop[x]:
                print("fittest ", x, " fitness value ", m)
                break
        if text in pop.keys():
            print("found in ", j, " generation")
            break
        j += 1

