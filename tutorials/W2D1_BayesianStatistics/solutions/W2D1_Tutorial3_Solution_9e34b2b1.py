x = np.arange(-10, 10, 0.1)
hypothetical_stim = np.linspace(-8, 8, 1000)

def compute_likelihood_array(x_points, stim_array, sigma=1.):

    # initializing likelihood_array
    likelihood_array = np.zeros((len(stim_array), len(x_points)))

    # looping over stimulus array 
    for i in range(len(stim_array)):
        likelihood_array[i, :] = my_gaussian(x_points, stim_array[i], sigma)
        likelihood_array[i, :] /= likelihood_array[i, :].sum()

    return likelihood_array

likelihood_array = compute_likelihood_array(x, hypothetical_stim)

with plt.xkcd():
  plot_myarray(likelihood_array,
               '$\~x$ : Brain representation of $x$',
               'Hypothetical True Stimulus $x$',
               'Sample Likelihood Array : $p(\~x | x)$')