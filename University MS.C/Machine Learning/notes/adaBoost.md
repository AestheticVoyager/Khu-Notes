# AdaBoost
Let's start by using **Decision Trees** and **Random Forests** to explain the 3 main concepts behind **AdaBoost**.

In a **Random Forest**, each time you make a tree, you make a full sized tree.
Some trees might be bigger than others, but there's no predetermined maximum depth.
In contrast, in a **Forest of Trees** made with **AdaBoost**, the trees are usually just a **node** and two **leaves**.

NOTE: A tree with just one node and 2 leaves is called a **stump**. So this is really a forest of stumps rather than forest of trees.
**Strumps** are not great at making accurate classifications.
**Stumps** are technically "Weak Learners". However, that's the way **AdaBoost** likes it, and it's one of the reasons why they are so commonly combined.

In a **Random Forest**, each tree has an equal vote on the final classification.
In contrast, in a **Forest of Stumps** made with **AdaBoost**, some stumps get more say in the final classification than others.

Lastly, in a **Random Forest**, each decision tree is made independently of the othres.
In contrast, in a **Forest of Stumps** made with **AdaBoost**, order is important.
The errors that the first stump makes, influences how the second stump is made, and the errors that the second stump makes, influences how the third stump is made, etc.

To review, the three ideas behind **AdaBoost** are:
1. AdaBoost combines a lot of "weak learners" to make classifications. The weak learners are almost always **stumps**.
2. Some **stumps** get more say in the classification than others.
3. Each **stump** is made by taking the previous **stump's** mistakes into account.

# Details of Forest of Stumps
Now let's dive into the nitty gritty detail of how to create a **Forest of Stumps** using **AdaBoost**.
[Honestly watch the video lol](https://www.youtube.com/watch?v=LsK-xG1cLYA&ab_channel=StatQuestwithJoshStarmer)
