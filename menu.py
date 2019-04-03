import budget_Formula
import pcpp_Scrape
import pcpp_Filter
import sys


def drawline():
    '''
    Draws Line, used mostly for TUI formatting
    '''
    ln_Symbol = "*"  # Symbol for line drawing
    ln_Length = 134  # Length of symbol drawing
    print(ln_Symbol * ln_Length)


def exposition():
    '''
    Prints exposition of project
    '''
    symbol_Length = int(48 / 2)
    print(
        " _______                       __          __                      " +
        "          _______             __  __        __                       "
    )
    print(
        "|       \                     |  \        |  \                     " +
        "         |       \           |  \|  \      |  \                    ")
    print(
        "| $$$$$$$\  ______    _______ | $$   __  _| $$_     ______    _____" +
        "_        | $$$$$$$\ __    __  \$$| $$  ____| $$  ______    ______  ")
    print(
        "| $$  | $$ /      \  /       \| $$  /  \|   $$ \   /      \  /     " +
        " \       | $$__/ $$|  \  |  \|  \| $$ /      $$ /      \  /      \ ")
    print(
        "| $$  | $$|  $$$$$$\|  $$$$$$$| $$_/  $$ \$$$$$$  |  $$$$$$\|  $$$$" +
        "$$\      | $$    $$| $$  | $$| $$| $$|  $$$$$$$|  $$$$$$\|  $$$$$$\\")
    print(
        "| $$  | $$| $$    $$ \$$    \ | $$   $$   | $$ __ | $$  | $$| $$  |" +
        " $$      | $$$$$$$\| $$  | $$| $$| $$| $$  | $$| $$    $$| $$   \$$")
    print(
        "| $$__/ $$| $$$$$$$$ _\$$$$$$\| $$$$$$\   | $$|  \| $$__/ $$| $$__/" +
        " $$      | $$__/ $$| $$__/ $$| $$| $$| $$__| $$| $$$$$$$$| $$      ")
    print(
        "| $$    $$ \$$     \|       $$| $$  \$$\   \$$  $$ \$$    $$| $$   " +
        " $$      | $$    $$ \$$    $$| $$| $$ \$$    $$ \$$     \| $$      ")
    print(
        " \$$$$$$$   \$$$$$$$ \$$$$$$$  \$$   \$$    \$$$$   \$$$$$$ | $$$$$" +
        "$$        \$$$$$$$   \$$$$$$  \$$ \$$  \$$$$$$$  \$$$$$$$ \$$      ")
    print(
        "                                                            | $$  " +
        "                                                                    ")
    print(
        "                                                            | $$   " +
        "                                                                   ")
    print(
        "                                                             \$$   " +
        "                                                                   ")
    print("\n\nCreated By: Jimmy Ho, Bryan Yuen, Charles Harold Llanto")
    drawline()
    print("Welcome to Desktop Builder")
    print("The purpose of this program is to:")
    print("---Assist those that are either novices or veterans at computer" +
          " building and provide useful tools that can be applicable at a" +
          " lower and higher level of understanding.")
    print("\nThis is why we decided to do this ASDKAJSLDKAJSDLKAJSDLJKASD")
    drawline()
    print("-" * symbol_Length + "Menu" + "-" * symbol_Length)


def startMenu():
    '''
    Menu for program, allows user to start program or update/store local files
    Return:
    -   User-based parameter List(Desktop Type, User Budget)
    '''
    exposition()  # Load Exposition of TUI
    print("At anytime in the program, enter \"q\" or \"Q\" to quit...")
    print("---Option 1: Start Creating Custom Desktop with Guided Parameters")
    print("---Option 2: Create Desktop Based on Type")
    print("---Option 3: Update Local Files")
    menuSelect = input("Select an option: ")
    while menuSelect.lower() != "q":
        # Parses and validates user menu option, entering q quits program
        try:
            if menuSelect == "1":
                return menu_parameter(0)  # Returns Parameter List
            elif menuSelect == "2":
                return menu_parameter(1)  # Returns Parameter List
            elif menuSelect == "3":
                input("Press enter to update...")
                print("Please wait for program to finish scraping data")
                print("This will take several minutes...")
                pcpp_Scrape.update()
            else:
                raise ValueError("***Error: Invalid Option***")
        except ValueError as error:
            print(error)
            menuSelect = input("Select an option: ")  # Prompt user for input
    exit()


def menu_parameter(userOption):
    '''
    Filler description
    '''
    drawline()
    user_Para = []
    para_Option = {
        "p1": ["General Usage", "Gaming Desktop", "Media Editing Workstation"],
        "p2": ["AMD", "Intel", "Doesn't Matter"],  # Brand of CPU
        "p3": ["Yes", "No",
               "Doesn't Matter"],  # Option for Overclock enabled CPU
        "p4": ["Small", "Regular", "Doesn't Matter"],  # Size of Case and MB
        "p5": ["Nvidia", "Radeon", "Doesn't Matter"]  # Video Card Parameter
    }
    para_Q = {
        "Q1": "What type of desktop do you want?",
        "Q2": "What brand of CPU do you want?",
        "Q3": "Do you want an Overclock enabled CPU?",
        "Q4": "What size of the computer tower do you want?",
        "Q5": "What brand of GPU do you want?"
    }
    skip = 0
    for num in range(1, 7):
        if num + skip < 6:
            print(para_Q["Q" + str(num + skip)])
            for index, items in enumerate(para_Option["p" + str(num + skip)]):
                print("---Option", str(index + 1) + ":", items)
            userInput = input("Please choose an option: ")
        while userInput.lower() != "q":
            try:
                if int(userInput) > 0 and int(userInput) < 4:
                    drawline()
                    if userOption == 1:
                        user_Para = [
                            userInput,
                            userBudget(int(userInput)), 3, 3, 3, 3
                        ]  # 3 is default/doesn't matter
                        return user_Para
                    else:
                        if len(user_Para) < 6:
                            drawline()
                            user_Para.append(int(userInput))
                            if len(user_Para) == 3 and int(
                                    userInput) == 1:  # AMD
                                user_Para.append(3)  # Append Default Overclock
                                skip += 1
                            if num == 1:
                                user_Para.append(userBudget(int(userInput)))
                            break
                        else:
                            return user_Para
                else:
                    raise ValueError("***Error: Invalid Option***")
            except ValueError as error:
                print(error)
                userInput = input("Please choose an option: ")


def userBudget(option):
    '''
    Filler Description
    '''
    budgetFloor = [500, 700, 1000, 0]
    budgetStatus = True
    budget = input("Enter your budget: ")
    while str(budget).lower() != "q":
        # Parses and validates user budget
        budget = float(budget)
        try:
            while budgetStatus:
                if budget < budgetFloor[option - 1]:
                    print("Please make sure your input is more than $%.2f" %
                          budgetFloor[option - 1])
                    budget = float(input("Enter your budget: "))
                else:
                    budgetStatus = False
            break
        except:
            print("***Error: Invalid Value***")
            budget = input("Enter your budget: ")
    print("Budget = $%.2f" % budget)
    drawline()
    return budget


def help_parameter():
    helpDirectory = []
    with open("HELPMENU.txt", "r") as textFile:
        helpDirectory.append(textFile.readlines())
    print(helpDirectory)


def printparts(compList, parameter_List):
    cpu_returns = pcpp_Filter.getCPU(compList, MASTER_LIST[0], parameter_List)
    chosen_cpu = cpu_returns[0]
    cooler_option = cpu_returns[1]
    chosen_motherboard = pcpp_Filter.getmobo(compList, MASTER_LIST[1],
                                             chosen_cpu, parameter_List[4])
    chosen_ram = pcpp_Filter.getram(compList, MASTER_LIST[2],
                                    chosen_motherboard)
    storage_list = pcpp_Filter.getstor(compList, MASTER_LIST[3])
    chosen_ssd = storage_list[0]
    chosen_hdd = storage_list[1]
    chosen_psu = pcpp_Filter.getpsu(compList, MASTER_LIST[6])
    chosen_case = pcpp_Filter.getcase(compList, MASTER_LIST[5], chosen_motherboard)
    extra_budget = (compList['cpu'] - chosen_cpu['price']) + (
            compList['motherboard'] - chosen_motherboard['price']) + (
                               compList['memory'] - chosen_ram['price']) + (
                           compList['storage'] - storage_list[2]) + (
                           compList['psu'] - chosen_psu['price'])

    chosen_gpu = pcpp_Filter.getgpu(compList, MASTER_LIST[4], extra_budget, parameter_List[5])
    chosen_cooler = pcpp_Filter.getcooler(compList, MASTER_LIST[7], extra_budget, cooler_option, chosen_gpu)

    print(parameter_List)
    print(compList)
    print(chosen_cpu)
    print(chosen_cooler)
    print(chosen_motherboard)
    print(chosen_ram)
    print(chosen_ssd)
    print(chosen_hdd)
    print(chosen_psu)
    print(chosen_gpu)
    print(chosen_case)



MASTER_LIST = pcpp_Scrape.read_JSON()
# (CPU, Motherboard, Memory, Storage, GPU, Case, PSU)
#testvalues = [(1, 500), (1, 1000), (2, 700), (2, 1500), (2, 2000), (2, 2500),
#              (2, 3000), (3, 1000), (3, 1500), (3, 2000), (3, 3000)]
#testvalues = [['1', 500, 3, 3, 3, 3], ['1', 1000, 3, 3, 3, 3], ['2', 700, 3, 3, 3, 3],
#              ['2', 1500, 3, 3, 3, 3], ['2', 2000, 3, 3, 3, 3], ['2', 2500, 3, 3, 3, 3],
#              ['2', 3000, 3, 3, 3, 3], ['3', 1000, 3, 3, 3, 3], ['3', 2000, 3, 3, 3, 3],
#              ['3', 3000, 3, 3, 3, 3]]
testvalues = [['2', 1500, 1, 1, 3, 3],['2', 1500, 1, 2, 3, 3],['2', 1500, 1, 3, 3, 3],
              ['2', 1500, 2, 1, 3, 3], ['2', 1500, 2, 2, 3, 3], ['2', 1500, 2, 3, 3, 3],
              ['2', 1500, 3, 1, 1, 3], ['2', 1500, 3, 2, 1, 3], ['2', 1500, 3, 3, 1, 3]]
choice = input("Test option (1 = menu) (2 = test): ")
if choice == "1":
    parameter_List = startMenu()
    compList = budget_Formula.giveFormula(parameter_List[0], parameter_List[1])
    printparts(compList, parameter_List)

if choice == "2":
    for testsubject in testvalues:
        compList = budget_Formula.giveFormula(testsubject[0], testsubject[1])
        printparts(compList, testsubject)
