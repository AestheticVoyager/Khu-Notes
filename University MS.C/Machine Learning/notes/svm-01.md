# Support Vector Machines part 1 of 3
#ML
[link to video](https://www.youtube.com/watch?v=efR1C6CvhmE&ab_channel=StatQuestwithJoshStarmer)

**Maximal Margin Classifiers** are super sensitive to outliers in the training data and that makes them pretty lame.

To make a threshold that is not so sensitive to outliers we must **allow misclassifications.**

Choosing a threshold that allows misclassifications is an example of the **Bias/Variance Tradeoff** that plagues all of machine learning.

In other words, before we allowed misclassifications, we picked a threshold that was very sensitive to the training data (low bias); and it performed poorly when we got new data(high variance).
In contrast when we picked a threshold that was less sensitive to the training data and allowed misclassifications(higher bias) it performed better when we got new data(low variance).

## Soft Margin
When we allow misclassifications, the distance between the observations and the threshold is called a **Soft Margin**.

So the questions is "How do we know that this **soft margin** is better than this **Soft Margin**?" 
The answer is simple:
We use **Cross Validation** to determine how many misclassifications and observations to allow inside of the **Soft Margin** to get the best classification.
For example, if **Cross Validation** determined that this was the best **Soft Margin** then we would allow one misclassification and two observations, that are correctly classified, to be within the **Soft Margin**.

When we use a **Soft Margin** to determine the location of a threshold, then we are using **Soft Margin Classifier** aka a **Support Vector Classifier** to classify observations.
The name **Support Vector Classifier** comes from the fact that the observations on the edge and within the **Soft Margin** are called **Support Vectors**.

**NOTE:** if each observation had a **mass** measurement and a **height** mesurement then the data would be **2-Dimensional**.
When the data are **2-Dimensional**, a **Support Vector Classifier** is a line and, in this case, the **Soft Margin** is measured from these two points.
The blue parallel lines gives us a sense of where all other points are in relation to the **Soft Margin**.
![image1]()
These observations are outside of the **Soft Margin**
![image2]()
![image3]()
And this observation is inside the **Soft Margin** and misclassified.
Just like before, we used **Cross Validation** to determine that allowing this misclassification results in better classification in the long run. 

Now, if each observation had a **mass**, a **height** and an **age** then the data would be **3-Dimensional**.

**NOTE:**The axis that **age** is on is supposed to represent **depth** and these circles are larger in order to appear closer, and thus younger, and these circles are smaller in order to look further away, and thus, older.
![image4]()

When the data are **3-Dimensional**, the **Support Vector Classifier** forms a plane, instead of a line and we classify new observations by determining which side of the plane they are on.

**NOTE:** if we measured **mass**, **height**, **age** and **blood pressure**, then the data would be in **4-Dimensions** and I don't know how to draw a **4-Dimensional** graph.

But we know that when the data are **1-Dimensional**, the **Support Vector Classifier** is a single point on a **1-Dimensional** number line.
**NOTE:** In Mathematical jargon, a point is a "flat affine **0-Dimesional** subspace".

And when the data are in **2-Dimensions**, the **Support Vector Classifier** is a **1-Dimensional** line in a **2-Dimensional** space.
**NOTE:** In Mathematical jargon, a line is a "flat affine **1-Dimensional** subspace".

And when the data are in **3-Dimensions**, the **Support Vector Classifier** is a **2-Dimensional** line in a **3-Dimensional** space.
**NOTE:** In Mathematical jargon, a plane is a "flat affine **2-Dimensional** subspace".

And when the data are in **4 or more Dimensions**, the **Support Vector Classifier** is a hyperplane.
**NOTE:** In Mathematical jargon, a hyperplane is a "flat affine subspace".
**NOTE:** Technically speaking, all flat affine subspaces are called **hyperplanes**. So technically speaking, this **1-Dimensional** line is a **hyperplane**; BUT we generally use the term when we can'd draw it on paper.


**Support Vector Classifiers** seem pretty cool because they can handle outliers and, because they allow misclassifications, they can handle overlapping classifications but what if this was our training data and we had tons of overlap?
Now, no matter where we put the classifier, we will make a lot of misclassifications.
So **Support Vector Classifiers** are only semi-cool, since they don't perform well with this type of data.

Can we do better than **Maximal Margin Classifiers** and **Support Vector Classifiers**?
**YES!**
Since **Maximal Margin Classifiers** and **Support Vector Classifiers** can't handle this data, it's high time we talked about **Support Vector Machines**

## Support Vector Machines
So let's start by getting an intuitive sense of the main ideas behind **Support Vector Machines**.
We start by adding **y-axis** so we can draw a graph.
The **x-axis** coordinates in this graph will be the dosages that we have already observed and the **y-axis** coordinates will be the square of the dosages.
![image5]()
So, for this observation, with **Dosage=0.5** on the **x-axis** the **y-axis** value = **Dosage^2** = (0.5)^2.
Now we use **Dosage^2** for this **y-axis** coordinate and then we use **Dosage^2** for the **y-axis** coordinates for the remaining observations.
Since each observation has **x and y axis** coordinates, the data are now **2-Dimensional**.
![image6]()
And now that the data are **2-Dimensional**, we can draw a **Support Vector Classifier** that separates the people who were *cured* from the people who were *not cured* and the **Support Vector Classifier** can be used to classify new observations.

-----

13:36 of video.