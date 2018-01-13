# Report - Nerual Network on Handwritten Digits Recognition

### Preparation
- Data has size (5000, 400). 5000 samples, each has 400 features. Output into 10 classes.
- Using architecture [400, 25, 10]. Input layer 400 elements; one hidden layer with 25 elements; output layer 10 elements
- Plan 3 runs. Run 1: optimize sample number, decide bias vs. variance. Run 2: optimize regulating rate. Run 3: compute Theta and test on test data set

---

### Analysis Before Run 1
- Each data has 400 features, which is absolutely enough for human beings to classify the data, thus we consider this is a feature-rich data set and we have high chance running into high-variance (overfitting) result. High regulating rate (lambda) might help.
- If it's a high-variance case, the best option for us is to use more samples and apply high regulating rate (lambda).
- We firstly run sample number [2000, 3000], if we see converge, we take the most optimized sample number in that range. Otherwise, we need to run sample number [1, 1000] to make sure of converge.
- If it's a high-variance case, we hope to see the plot like below. 
	- Cross validation curve and training curve never go across. 
	- Difference between cv and train is getting smaller as sample increases
	- Relatively high cross validation cost and low train cost  	
	- ![high_variance](https://github.com/TrentaIcedCoffee/algo-ml/blob/master/readme_resource/high_variance.png)

### Run 1 
#### sample number [2000, 3000] (max iteration 400, 1001 runs, takes 2.23 hours)
![run1_2000_3000](https://github.com/TrentaIcedCoffee/algo-ml/blob/master/readme_resource/run1_2000_3000.jpg) 
- Most optimized sample number is 2989.
- We see cross validation and train doesn't cross
- We fail to see convergence.
- Cross validation and train have similar and low cost.
- We need to run sample number [1, 1000] to see if cross validation and train converge.  
#### sample number [1, 1000] (max iteration 400, 1001 runs, takes 0.84 hour)  
![run1_1_1000](https://github.com/TrentaIcedCoffee/algo-ml/blob/ali/readme_resource/run1_1_1000.jpg)  
- We see cross validation and train converge, thus we infer they also converge on [2000, 3000].

### Analysis After Run 1
- High-variance case.
- Acceptable, relatively low cross validation cost means that we don't need to collect more train data.
- We obtained the most optimized sample number, 2989  

---

### Analysis Before Run 2
- Since this is a high variance case, we might need high regulating rate (lambda) to avoid overfitting.
- We hope to see a convex curve and find the lowest point.
- We firstly try [0, 10], then find the lowest point with precision tolerance 0.01.

### Run 2
#### lambda [0, 10] (max iteration 400, 11 runs, takes less than 1 minute)
![run2_0_10](https://github.com/TrentaIcedCoffee/algo-ml/blob/master/readme_resource/run2_0_10.jpg)  
- We see a convex lambda curve.
- The lambda curve has minimum in range [0, 2].
- We can run [0, 2] with precision 0.01 to find accurate minimum.  
#### lambda [0, 2] (max iteration 400, 201 runs, takes 0.56 hour)
![run2_0_2](https://github.com/TrentaIcedCoffee/algo-ml/blob/master/readme_resource/run2_0_2.jpg)
- Above curves follow the same routine.
- We find minimum lambda 0.88.

---

### Analysis Before Run 3
- We obtained two most optimized value, sample number 2989 and lambda 0.88, we just need to use these values to train learning model. Since we've already did everything to optimize this model, if we don't find a high accuracy, we may want to try different architectures.

### Run 3 (sample number 2989, lambda 0.88, max iteration 4000, 4000 runs, takes less than 3 minutes)
- Train accuracy 99.90
- Cross validation accuracy 93.60
- Test accuracy 93.60

---

## Summary
- We boosted the accuracy of the training model to the top. And 93.60 is the what we got.
- If we want higher accuracy, we have to try different architectures.
