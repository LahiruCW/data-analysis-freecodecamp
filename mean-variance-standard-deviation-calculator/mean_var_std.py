import numpy as np

def calculate(list):

  if len(list) >= 9:

    calculations = {}
  
    #Convert to a matrix;
    raw_array = np.asarray(list)
    shaped_array = np.reshape(raw_array, (3,3))

    #Calculate the mean;
    calculations["mean"] = [np.mean(shaped_array, axis = 0).tolist(), np.mean(shaped_array, axis = 1).tolist(),np.mean(shaped_array).tolist()]
    
    #Calculate the variance;
    calculations["variance"] = [np.var(shaped_array, axis = 0).tolist(), np.var(shaped_array, axis = 1).tolist(),np.var(shaped_array).tolist()]

    #Calculate the standard deviation;
    calculations["standard deviation"] = [np.std(shaped_array, axis = 0).tolist(), np.std(shaped_array, axis = 1).tolist(),np.std(shaped_array).tolist()]

    #Calculate the max;
    calculations["max"] = [np.max(shaped_array, axis = 0).tolist(), np.max(shaped_array, axis = 1).tolist(),np.max(shaped_array).tolist()]

    #Calculate the min;
    calculations["min"] = [np.min(shaped_array, axis = 0).tolist(), np.min(shaped_array, axis = 1).tolist(),np.min(shaped_array).tolist()]

    #Calculate the sum;
    calculations["sum"] = [np.sum(shaped_array, axis = 0).tolist(), np.sum(shaped_array, axis = 1).tolist(),np.sum(shaped_array).tolist()]

    return calculations
  
  else:
    raise ValueError("List must contain nine numbers.")