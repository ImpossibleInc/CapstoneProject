from . import rankings, databaseManipulation, dataScrape, regressionModel

def setup():
    print('\nPlease input the starting year you would like to use (data in README.md uses 1970, 1970 is also the earliest date possible)')
    while True:
        try:
            num1 = input("Starting Year: ")
            if num1.isdigit():
                num1 = int(num1)
            else:
                raise ValueError()
            if 1970 <= num1 <= 2023:
                break
            raise ValueError()
        except ValueError:
            print('\nSorry. The year must be between 1970 and 2023 for the starting data')
    print('\nPlease input the end year you would like to use (data in README.md uses 2024, 2024 is also the latest date possible)')
    while True:
        try:
            num2 = input('Ending Year: ')
            if num2.isdigit():
                num2 = int(num2)
            else:
                raise ValueError()
            if num1 <= num2 <= 2024:
                break
            raise ValueError()
        except ValueError:
            print('\nSorry. The year must be between ' + str(num1) + ' and 2024 for the ending data')
    print('\nData collection starting! (This may take a while)')
    dataScrape.get_data(num1, num2)
    print('\nData collection finished!')
    print('\nBeginning to train model!')
    regressionModel.train_model()
    print('\nTraining finished!')
    print('\nFormulating rankings')
    rankings.create_rankings(num2)
    print('\nRankings created!')
    return num1, num2

def view(num1, num2):
    print('Here are the rankings for the ' + str(num2) + ' season based off the model trained from ' + str(num1) + ' and ' + str(num2) + '!\n')
    rankings.print_rankings()

def stats(num1, num2):
    print('Here are the accuracy stats for the model trained from ' + str(num1) + ' and ' + str(num2) + '!\n')
    regressionModel.lm_stats()

def closeDatabase():
    print('\nClosing database!')
    databaseManipulation.db_close()