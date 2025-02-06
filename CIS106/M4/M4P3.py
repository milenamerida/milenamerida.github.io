'''Formating is not working with Total variable - talked about it in class 2/6/25'''
total = float(input('Enter the total for your meal $'))
tip15 = total * 0.15
tt15 = total + tip15
tip18 = total * 0.18
tt18 = total + tip18
tip20 = total * 0.20
tt20 = total + tip20
print('\nWith 15% Tip: \n\nTotal:'.ljust(20),'','{:10.2f}'.format(total), '\nTip:'.ljust(20),'','{:10.2f}'.format(tip15), '\nTotal with Tip:'.ljust(20),'','{:10.2f}'.format(tt15))
print('\nWith 18% Tip: \n\nTotal:'.ljust(20),'','{:10.2f}'.format(total), '\nTip:'.ljust(20),'','{:10.2f}'.format(tip18), '\nTotal with Tip:'.ljust(20),'','{:10.2f}'.format(tt18))
print('\nWith 20% Tip: \n\nTotal:'.ljust(20),'','{:10.2f}'.format(total), '\nTip:'.ljust(20),'','{:10.2f}'.format(tip20), '\nTotal with Tip:'.ljust(20),'','{:10.2f}'.format(tt20))
