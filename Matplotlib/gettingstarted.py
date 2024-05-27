from matplotlib import pyplot as plt

ages_x = [25,26,27,28,29,30,31,32]

devsalary_y = [12234,34351,52335,56700,57324,58432,59233,60455]

py_dev_y = [13202,57324,58432,59233,60455,62454,63000,66000]

plt.plot(ages_x,py_dev_y , label ='Alldevs')

plt.plot(ages_x,devsalary_y , label = 'Pydev')

plt.xlabel('Ages')
plt.ylabel('Median salary')
plt.title('Median salary (in INR) by ages')
plt.legend() #(['Alldevs','Python'])




plt.show()