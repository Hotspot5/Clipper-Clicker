print('loading...')

import os
import time
import math

VERSION = '0.1.0'

starttime = time.time()

class Generator:
    def __init__(self, name, description, cost, costmult, click, time):
        self.name = name
        self.description = description
        self.cost = cost
        self.costmult = costmult
        self.click = click
        self.time = time
        self.number = 0

generators = [
    Generator('Machine', 'A Machine that makes Paperclips automatically', 10, 1.1, 0, 1), 
    Generator('Factory', 'A Factory that produces Machines on an industrial scale', 1000, 1.2, 1, 2), 
    Generator('Builder', 'A Builder to build all these Factories for you', 30000, 1.3, 3, 4), 
    Generator('Employer', 'An Employer to employ handy Builders', 10**6, 1.4, 10, 8), 
    Generator('Firm', 'A Firm to set up recruitment centers to get you more Employers', 10**9, 1.5, 100, 16), 
    Generator('Entrepreneur', 'An Entrepreneur to set up brand new Firms for you', 10**12, 1.6, 1000, 32), 
    Generator('Advert', 'Paid Advertisement to attract aspiring Entrepreneurs', 10**15, 1.7, 10000, 64)
]

paperclips = 0
perclick = 1

os.system('cls')
print(f'Version: {VERSION}')
print()
input('[enter] to continue')

while True:
    os.system('cls')

    paperclips += perclick
    dur = time.time() - starttime

    for x in range(len(generators)-1, -1, -1):
        if x == 0:
            paperclips += dur / generators[x].time * generators[x].number
            break
        generators[x-1].number += dur / generators[x].time * generators[x].number
        perclick += dur / generators[x].time * generators[x].number * generators[x-1].click

    starttime = time.time()

    print(f'Paperclips: {"{:,}".format(round(paperclips))}')
    print()
    print('-' * 10)
    print()
    print(f'Per Click: {"{:,}".format(round(perclick))}')
    print(f'Per Second: {"{:,}".format(round(generators[0].number))}')
    print()
    print('-' * 10)
    print()
    print('UPGRADES:')
    print()
    print('(coming soon)')
    print()
    print('GENERATORS:')
    print()

    unlocked = 1

    for x in range(len(generators)):

        generatorDisplay = f'{x+1} - {generators[x].name}: {"{:,}".format(round(generators[x].number))} (Costs {"{:,}".format(round(generators[x].cost))})'

        if x == 0:
            print(generatorDisplay)
            continue
        if generators[x-1].number > 0:
            unlocked += 1
            print(generatorDisplay)
        else:
            break

    print()
    print('-' * 10)
    print()
    print('[number] - View Generator')
    print('[blank] - Leave Blank to Update Paperclips')
    print()
    action = input('> ')

    try:
        action = int(action)
    except:
        pass

    if isinstance(action, int):
        if action <= unlocked:
            os.system('cls')

            print(generators[action-1].name.upper())
            print()
            print(f'Cost: {"{:,}".format(round(generators[action-1].cost))}')
            print(f'Owned: {"{:,}".format(round(generators[action-1].number))}')
            print()
            print(f'Paperclips: {"{:,}".format(round(paperclips))}')
            print()
            print('-' * 10)
            print()
            print(f'"{generators[action-1].description}"')
            print()
            print('-' * 10)
            print()
            print('c - Cancel')
            print('[enter] - Purchase 1')
            print('[number] - Purchase Custom Amount')
            print()

            action2 = input('> ')

            try:
                action2 = int(action2)
            except:
                pass

            if not isinstance(action2, int):
                if action2.lower() != 'c':
                    if paperclips >= generators[action-1].cost:
                        paperclips -= generators[action-1].cost
                        generators[action-1].cost *= generators[action-1].costmult
                        generators[action-1].number += 1
                        perclick += generators[action-1].click
            else:
                os.system('cls')
                print('loading...')
                sum = generators[action-1].cost
                cost = generators[action-1].cost
                
                for x in range(action2-1):
                    cost *= generators[action-1].costmult
                    sum += cost
                
                os.system('cls')
                print('Please Confirm:')
                print()
                try:
                    print(f'Cost: {"{:,}".format(round(sum))}')
                except:
                    pass
                else:
                    print(f'Paperclips: {"{:,}".format(round(paperclips))}')
                    print()
                    print('c - Cancel')
                    print('[enter] - Confirm and Pay')
                    print()
                    action3 = input('> ')

                    if action3.lower() != 'c':
                        if paperclips >= sum:
                            paperclips -= sum
                            generators[action-1].cost *= generators[action-1].costmult ** action2
                            generators[action-1].number += action2
                            perclick += generators[action-1].click * action2