#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []
    import numpy as np
    predictions = np.array(predictions)
    ages = np.array(ages)
    net_worths = np.array(net_worths)

    for y_hat, x, y in zip(predictions, ages, net_worths):
        error = abs((y - y_hat)**2)
        val = (x, y, error)
        cleaned_data.append(val)

    array = np.array(cleaned_data)
    array = array.reshape((len(array), 3))

    ### your code goes here

    a = np.array([[1, 2, 3], [4, 5, 6], [0, 0, 1]])
    array = array[array[:,2].argsort()]
    array = array[:][:int(len(array) * 0.9)]
    cleaned_data = array


    return cleaned_data

