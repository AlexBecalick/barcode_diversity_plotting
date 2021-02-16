#Load libraries
import pandas as pd
import numpy as np
from IPython.display import display
import matplotlib.pyplot as plt
import math as math

#Creates array to hold amounts of each barcode
def my_data(barcode_amount = 5000, broadness = 100, exponentiality = 1):
    data = np.zeros((barcode_amount, 2))

    num = 1
    for row in range(barcode_amount):
        data[row][0] = num
        num += 1

    for row in range(barcode_amount):
        data[row][1] = math.exp(exponentiality/broadness*(data[row][0]))
    
    return data

def generate_data(barcode_amount = 5000, broadness = 100, exponentiality = 1):
    plt.figure(figsize=(15,7))
    plt.scatter(my_data(barcode_amount, broadness, exponentiality)[:,0], 
        my_data(barcode_amount, broadness, exponentiality)[:,1], marker=".")
    plt.title('Barcode diversity')
    plt.xlabel('Barcode index')
    plt.ylabel('Barcode frequency')
    plt.xlim(0)
    plt.grid(True)
    global barcode_distribution
    barcode_distribution = my_data(barcode_amount, broadness, exponentiality)

#Calculates the fraction of uniquely labelled cells, given the barcode distribution and number of infected cells
def probability_distribution():
    barcode_amount = 5000
    broadness = 100
    exponentiality = 1
    barcode_distribution = np.zeros((barcode_amount, 2))
    num = 1
    for row in range(barcode_amount):
        barcode_distribution[row][0] = num
        num += 1
    for row in range(barcode_amount):
        barcode_distribution[row][1] = math.exp(exponentiality/broadness*(barcode_distribution[row][0]))


    #The probability of picking a given barcode 
    barcode_probability = np.zeros(len(barcode_distribution))
    counter = 0
    for barcode in barcode_distribution[:,1]:
        probability = barcode_distribution[counter,1] / sum(barcode_distribution[:,1])
        barcode_probability[counter] = probability
        counter += 1
    return barcode_probability


def fraction_unique(cell_num = 5000):
    barcode_amount = 5000
    broadness = 100
    exponentiality = 1
    barcode_distribution = np.zeros((barcode_amount, 2))
    num = 1
    for row in range(barcode_amount):
        barcode_distribution[row][0] = num
        num += 1
    for row in range(barcode_amount):
        barcode_distribution[row][1] = math.exp(exponentiality/broadness*(barcode_distribution[row][0]))


    #The probability of picking a given barcode 
    barcode_probability = np.zeros(len(barcode_distribution))
    counter = 0
    for barcode in barcode_distribution[:,1]:
        probability = barcode_distribution[counter,1] / sum(barcode_distribution[:,1])
        barcode_probability[counter] = probability
        counter += 1    
    barcode_contribution = barcode_probability * (1 - (1 - barcode_probability)**(cell_num - 1))
    unique = 1 - sum(barcode_contribution)
    return unique

def plot_unique_barcoded_cells(max_cells = 5000, plotted_points = 5000):
    barcode_amount = 5000
    broadness = 100
    exponentiality = 1
    barcode_distribution = np.zeros((barcode_amount, 2))
    num = 1
    for row in range(barcode_amount):
        barcode_distribution[row][0] = num
        num += 1
    for row in range(barcode_amount):
        barcode_distribution[row][1] = math.exp(exponentiality/broadness*(barcode_distribution[row][0]))

    barcode_probability = np.zeros(len(barcode_distribution))
    counter = 0
    for barcode in barcode_distribution[:,1]:
        probability = barcode_distribution[counter,1] / sum(barcode_distribution[:,1])
        barcode_probability[counter] = probability
        counter += 1 

    def fraction_unique(cell_num):
        #The probability of picking a given barcode 
        barcode_contribution = barcode_probability * (1 - (1 - barcode_probability)**(cell_num - 1))
        unique = 1 - sum(barcode_contribution)    
        return unique
    

    plt.figure(figsize=(15,7))
    cell_num_array = np.arange(1, plotted_points, dtype = float)
    print(cell_num_array)

    for num in cell_num_array:
        cell_num_array[int(num)-1] = fraction_unique(int(num))
        print(num)
    plt.plot(np.arange(1, max_cells, max_cells//plotted_points), cell_num_array)
    plt.title('Barcode diversity')
    plt.xlabel('Number of infected starter cells')
    plt.ylabel('Fraction of uniquely labeled cells')
    plt.xlim(0)
    plt.ylim(0, 1)