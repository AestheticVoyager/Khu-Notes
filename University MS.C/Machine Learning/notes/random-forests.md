# Random Forest

Random Forest Steps:
1. Create a "bootstrapped" dataset.
  To create a bootstrapped dataset that is the same size as the original, we just randomly select samples from the original dataset.
  The important detail is that we're allowed to pick the same sample more than once.   
2. Create a decision tree using the bootstrapped dataset, but only use a random susbset of variables (or columns) at each step.
  Just build the tree as usual, but only considering a random subset of variables at each step.
3. Now go back to step 1 and repeat: Make a new bootstrapped dataset and build a tree considering a subset of variables at each step.
  ideally, you'd do this 100's of times, but we only have space to show 6...but you get the idea.
Using a bootstrapped sample and considering only a subset of the variables at each step results in a wide variety of tree.
The variety is what makes random forests more effective than individual decision trees.
Now that we have random forests, what now?!
Get a new data entry point, track whether the boolean answer like for example, (does the patient have heart disease?), is yes or no in multiple trees that we have created.
After running the data down all of the trees in the random forest, we see which option recieved more votes.

## Bagging
Bootstrapping the data plus using the aggregate to make decision is called "Bagging".

NOTE: Typically, about 1/3 of the original data does not end up in the bootstrapped dataset.
The entries that don't end up in the bootstrapped dataset, are called "Out-of-Bag Dataset".

Then run all the entries in the random forest trees, to check the accuracy.
We then do the same thing for all of the other Out-Of-Bag samples for all of the trees.
Ultimately, we can measure how accurate our random forest is by the proportion of out-of-Bag samples that were correctly classified by the Random Forest.

### Out-of-Bag Error
The proportion of Out-Of-Bag samples that were incorrectly classified is the "Out-Of-Bag Error".

Ok, we now know how to:
1. Build a Random Forest.
2. Use a Random Forest.
3. Estimate the accuracy of a Random Forest.

Now that we know how to estimate the accuracy, and since we chose only 2 random variables fromt the dataset to create the random forest trees;
We can do this:
1. Build a Random Forest
2. Estimate the accuracy of a Random Forest.(Change the number of variables used per step.)
Do this a bunch of times and then choose the one that is most accurate.
Typically, we start by using the square number of variables and then try a few settings above and below that value.

--------

## Missing Data & Sample Clustering
Random Forests consider 2 types of missing data:
1. Missing data in the original dataset used to create the random forest.
2. Missing data in a new sample that you want to categorize.

We'll start with the first one.
The general idea for dealing with missing data in this context is to make an initial guess that could be bad, then gradually refine the guess unitl it is(hopefully) a good guess.
We guess the missing values based on similar data from the dataset.
Now we want to refine these guesses.
We do this by first determining which samples are similar to the on with missing data.
Steps:
1. Build a random forest
2. Run all of the data down all of the trees.
  Sample x and sample y both ended up at the same leaf node. That means they are similar. At least that's how similarity is defined in the random forests.
  We keep track of similar samples using a "Proximity Matrix".
  The proximity matrix has a row for each sample and it has a column for each sample.
  Becase sample x and sample y ended up in the same leaf, we put 1 at their intersection.
  Because no other pair of samples ended in the same leaf node, our proximity matrix looks like this after running the samples down the first tree.
  Now we run all of the data down the second tree.
  After the second tree, we add 1 to any pair of samples that ended up in the same leaf node.(Updating the proximity Matrix.)
  Now we run all of the data down the third tree.
  Ultimately, we run the data down all the trees and the proximity matrix fills in.
  Then we devide each proximity value by the total number of trees.
3. Use the proximity matrix to refine the missing values.
4. Now that we have revised our guesses a little bit, we do the whole thing over again.

We build a random forest, run the data through the trees, recalculate the proximities and recalculate the missing values.
We do this 6 or 7 times until the missing values converge(i.e. no longer change each time we recalculate.)

## Cool Trick with Proximity Matrix
1 - (the proximity values) = distance.
So we can create a "distance matrix" using the "proximity matrix".
And that means we can draw a heatmap with it.
We can also draw an MDS plot with it.
This is super cool because it means that no matter what the data are(ranks, multiple choices, numeric, etc) if we can use it to make a tree, we can draw a heatmap or an MDS plot to show how the samples are related to each other.

Now let's go back to the second method, 2) Missing data in a new sample that you want to categorize.
Imagine we had already built a Random Forest with existing data and wanted to classify this new patient.
We want to know if the patient has heart disease or not, but we don't know if the patient has blocked arteries or not.
First thing we do is create two copies of the data, one that has heart disease and one that doesn't have heart disease.
Then we use the iterative method we just talked about to make a good guess about the missing values.
Then we run the two samples down the trees in the forest and we see which of the two is correctly labeled by the random forest the most times.

FIN.
