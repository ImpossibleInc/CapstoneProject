from Setup.backbone import *

print('\nHELLO! Welcome to the easiest to use fantasy football machine learning model.\n'
      'To start we need to go through some basic setup then you can view the results \n\
of the model and if you want to change the data size collected and retrain the model.\n')
start_year, end_year = setup()
print("\nYour model is all set up! You can now type 'view' to look at the rankings based \n\
on your model, 'stats' to see the MAE, MSE and RMSE of your model, 'setup' to run the \n\
setup again and plug in new years, or 'exit' to close the program.")
while True:
      usrInput = input('\nWhat would you like to do? ')
      if usrInput == 'view':
            view(start_year, end_year)
      elif usrInput == 'stats':
            stats(start_year, end_year)
      elif usrInput == 'setup':
            setup()
      elif usrInput == 'exit':
            break
      else :
            print('\nInvalid option. Please try again.')
print('\nThank you for using fantasy football machine.')