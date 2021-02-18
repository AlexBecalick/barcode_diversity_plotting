#Load libraries
import numpy as np
import matplotlib.pyplot as plt

def my_data(barcode_amount, n_coefficient, e_coefficient, all_unique):
    '''Create array holding the frequency of each barcode in the library.
    
    Keyword arguments: 
    barcode_amount -- number of unique barcode sequences.
    n_coefficient -- parameter for adjusting skew steepness.
    e_coefficient -- parameter for adjusting skew strength.
    all_unique -- toggle for skew.
    '''
    data = np.zeros((barcode_amount, 2))
    data[:,0] = np.arange(1, barcode_amount+1)
    data[:,1] = e_coefficient*np.exp(all_unique/n_coefficient*data[:,0])
    #Zador paper equation?
    #data[:,1] = e_coefficient*np.exp(all_unique/(barcode_amount*data[:,0]))
    
    return data

def probability_distribution(barcode_distribution):
    '''Calculate the probability of picking each barcode.''' 
    total_barcodes = sum(barcode_distribution[:,1])
    barcode_probability = barcode_distribution[:,1] / total_barcodes 

    return barcode_probability

def fraction_unique(barcode_probability, cell_num):
    '''Calculate the fraction of uniquely labelled cells.

    Keyword arguments: 
    barcode_probability -- an array of probabilites for picking each barcode.
    cell_num -- number of infected cells.
    '''
    barcode_contribution = barcode_probability * (1 - (1 - barcode_probability)**(cell_num - 1))
    unique = 1 - sum(barcode_contribution)

    return unique

def generate_plots(n_bins, stride, barcode_amount, n_coefficient, e_coefficient, max_cells, all_unique):
    '''Plot barcode distribution, CDF and fraction of uniquely labeled cells'''
    #Create subplots
    fig = plt.figure(figsize=(30,7))
    coord1, coord2, coord3 = 131, 132, 133

    #Plot barcode distribution
    plt.subplot(coord1)
    plt.plot(my_data(barcode_amount, n_coefficient, e_coefficient, all_unique)[:,0], 
             my_data(barcode_amount, n_coefficient, e_coefficient, all_unique)[:,1], c='b', linewidth=4.0)
    plt.title('Barcode distribution', fontsize=20, pad=20)
    plt.xlabel('Barcode index', fontsize=16, labelpad=10)
    plt.ylabel('Barcode abundance', fontsize=16, labelpad=10)
    plt.xlim(0)
    plt.grid(True)

    #Plot cumulative fraction
    plt.subplot(coord2)
    n, bins, patches = plt.hist(my_data(barcode_amount, n_coefficient, e_coefficient, all_unique)[:,1],
         n_bins, density=True, histtype='step', cumulative=True, label='Empirical', color = 'b', linewidth=4.0)
    #Remove rightmost vertical line from histogram CDF
    patches[0].set_xy(patches[0].get_xy()[:-1])
    plt.title('Cumulative barcode distribution', fontsize=20, pad=20)
    plt.xlabel('Barcode abundance group', fontsize=16, labelpad=10)
    plt.ylabel('Cumulative fraction', fontsize=16, labelpad=10)
    plt.xlim(0)
    plt.ylim(0,1)
    plt.grid(True)
    
    #Select the number of points to plot and create an array of cell numbers based on this
    num_points = stride
    strided_array = np.zeros(num_points)
    evaluation_point = np.array(np.linspace(1, max_cells, num_points), dtype=int)
    #First, calculate the barcode probability distribution
    global barcode_distribution
    barcode_distribution = my_data(barcode_amount, n_coefficient, e_coefficient, all_unique)
    barcode_probability = probability_distribution(barcode_distribution)
    #Then, for each cell number in the evaluation array, calculate the fraction of uniquely labeled cells
    for index, num in enumerate(evaluation_point):
        strided_array[index] = fraction_unique(barcode_probability, num)

    #plot_unique_barcoded_cells
    plt.subplot(coord3)
    plt.plot(evaluation_point, strided_array, c='b', linewidth=4.0)
    plt.title('Uniquely labeled cells', fontsize=20, pad=20)
    plt.xlabel('Number of infected starter cells', fontsize=16, labelpad=10)
    plt.ylabel('Fraction of uniquely labeled cells', fontsize=16, labelpad=10)
    #plt.xscale("log")
    plt.xlim(0)
    plt.ylim(0,1)
    plt.grid(True)