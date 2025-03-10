print('loading...')

import os
import time
import math

VERSION = '0.3.0'

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
    Generator('Machine', 'A Machine that makes Paperclips automatically', 10, 1.05, 0, 1), 
    Generator('Factory', 'A Factory that produces Machines on an industrial scale', 500, 1.1, 1, 2), 
    Generator('Builder', 'A Builder to build all these Factories for you', 30000, 1.15, 3, 4), 
    Generator('Employer', 'An Employer to employ handy Builders', 10**6, 1.2, 10, 8), 
    Generator('Firm', 'A Firm to set up recruitment centers to get you more Employers', 10**9, 1.25, 100, 16), 
    Generator('Entrepreneur', 'An Entrepreneur to set up brand new Firms for you', 10**12, 1.3, 10**3, 32), 
    Generator('Advert', 'Paid Advertisement to attract aspiring Entrepreneurs', 10**15, 1.35, 10**4, 64), 
    Generator('Quantum', 'Quantum Computers to mine crypto for Ads (let the transformation begin ;D)', 10**21, 1.4, 10**6, 128), 
    Generator('Rocket', 'A Rocket to ship Quantum Computers to other planets', 10**27, 1.45, 10**8, 256), 
    Generator('Planet', 'Manufacture planets for more space for Quantum Computers!', 10**36, 1.5, 10**11, 512), 
    Generator('Star', 'Manufacture Stars to attract Planets with gravity!', 10**45, 1.55, 10**14, 1024), 
    Generator('Galaxy', 'Collapse matter into a Supermassive Black Hole to form a Galaxy of Stars!', 10**57, 1.6, 10**18, 2048), 
    Generator('Universe', 'Break free of the 3rd Dimension and forge Universes of Paperclips!', 10**69, 1.65, 10**22, 3600), 
    Generator('Multiverse', 'Summon entire Multiverses by contorting spacetime to generate limitless realities!', 10**84, 1.7, 10**27, 3600), 
    Generator('Dimensions', 'Rip the fabric of reality into higher dimensions to summon... MORE... PAPERCLIPS!', 10**100, 1, 10**33, 3600)
]

savefile = open('save.txt', 'r')
savelines = savefile.readlines()
    
paperclips = float(savelines[savelines.index('paperclips\n')+1].strip('\n'))
perclick = float(savelines[savelines.index('perclick\n')+1].strip('\n'))

for x in range(len(generators)):
    generators[x].number = float(savelines[savelines.index('generators\n')+x+1].strip('\n'))
    
savefile.close()

os.system('cls')

print(f'Version: {VERSION}')
print('This game saves automatically with every input')
print()
input('[enter] to continue')

while True:
    os.system('cls')

    paperclips += perclick
    dur = time.time() - starttime

    for x in range(len(generators)):
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
    print('[R] - Reset Progress (w/ confirmation)')
    print()
    
    action = input('> ')
    
    savefile = open('save.txt', 'w')
    towrite = f'paperclips\n{paperclips}\n'
    towrite += f'perclick\n{perclick}\n'
    towrite += 'generators\n'
    
    for generator in generators:
        towrite += str(generator.number) + '\n'
        
    savefile.write(towrite)
    savefile.close()
    
    if action == 'R':
        
        os.system('cls')
        confirmation = input('Are you sure you want to reset all progress? (yes/no)\n> ')
        
        if confirmation.lower() == 'yes':
            savefile = open('save.txt', 'w')
            towrite = f'paperclips\n0.0\n'
            towrite += f'perclick\n1.0\n'
            towrite += 'generators\n'
            
            for generator in generators:
                towrite += '0.0\n'
                
            savefile.write(towrite)
            savelines = savefile.readlines()
            
            paperclips = float(savelines[savelines.index('paperclips\n')+1].strip('\n'))
            perclick = float(savelines[savelines.index('perclick\n')+1].strip('\n'))

            for x in range(len(generators)):
                generators[x].number = float(savelines[savelines.index('generators\n')+x+1].strip('\n'))
            
            savefile.close()

    try:
        action = int(action)
    except:
        pass

    if isinstance(action, int):
        
        if action <= unlocked:
            os.system('cls')

            print(generators[action-1].name.upper())
            print()
            print('-' * 10)
            print()
            print(f'"{generators[action-1].description}"')
            print()
            print('-' * 10)
            print()
            print(f'Cost: {"{:,}".format(round(generators[action-1].cost))}')
            print(f'(Paperclips: {"{:,}".format(round(paperclips))})')
            print()
            print(f'Owned: {"{:,}".format(round(generators[action-1].number))}')
            print()
            print(f'Production Time: {generators[action-1].time} second(s)')
            print(f'Cost Multiplier: x{generators[action-1].costmult}')
            print(f'Per Click: +{"{:,}".format(generators[action-1].click)}')
            print()
            print('-' * 10)
            print()
            print('[c] - Cancel')
            print('[enter] - Purchase 1')
            print('[number] - Purchase Custom Amount (no more than 1000)')
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
                if action2 <= 1000:
                    os.system('cls')
                    print('calculating...')
                    
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