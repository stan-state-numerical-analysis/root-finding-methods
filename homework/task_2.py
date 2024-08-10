# Task: Apply the Central Difference Method for Newton's Method and visualize the output.

# 1. Define a function called central_difference that outputs the central difference method approximation of
# the derivative of a function using the h value 1e-5.
#    - Parameters: 
#      - f: The function whose derivative is to be approximated.
#      - x: The point at which to approximate the derivative.



# 2. Import the matplotlib.pyplot, numpy, and the newtons_method function from the task_1.py file.



# 3. Define a new function called plot_newtons_method that applies Newton's method to find the root
#    of any function and plots the results.
#    - Parameters:
#      - f: The function whose root is being found.
#      - x_interval: A tuple specifying the interval of x values containing the root.



  # Inside plot_newtons_method, do the following...

  # 4. Use the central_difference function to create a function called f_prime which takes in an x-value
  # and returns an approximation of the derivative of the function f (a parameter of plot_newtons_method).



  # 5. Initialize a variable called x0 which is the midpoint of the interval defined by x_interval.



  # 5. Initialize a variable called root_approx which is the approximation of a root of f near x0
  # returned by newtons_method with a tolerance of 1e-5 and a maximum of 1000 iterations.



  # 6. Initialize a variable called x_values containing 1000 equally spaced values spanning x_interval.



  # 7. Initialize a variable called y_values which is a list of the evaluations of the input function f
  # at each value in x_values.


    
  fig, ax = plt.subplots(figsize=(14, 8))
  
  # 8. Use x_values and y_values to plot the function f over the given x-interval.



  # 9. Use ax.scatter to plot the point (root_approx, f(root_approx)) in the color red with size 200. Set the label so it
  # gives the x and y coordinates of the root estimate like so: (estimate, f(estimate))



  ax.set_xlabel("x")
  ax.set_ylabel("f(x)")
  ax.set_title(f"Approximation of the Root of f(x) in [{x_interval[0]}, {x_interval[1]}]")
  ax.legend(scatterpoints=1)
  ax.grid(True)

  return fig
