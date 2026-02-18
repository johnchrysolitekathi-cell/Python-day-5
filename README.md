This program analyzes emergency resource requests collected during a disaster drill. Each request may contain invalid values, zero demand, low demand, moderate demand, or high demand. The goal is to classify these requests properly and then apply a personalized filtering rule to generate the final dispatch report.

Approach Used

First, I entered my full name and removed the spaces to calculate its length (L). Then I calculated the Personalized Logic Index (PLI) using the formula:

PLI = L % 3

Next, I stored all resource requests in a list using a for loop. Each request was processed using conditional statements and classified as:

Invalid Request (< 0)

No Demand (0)

Low Demand (1–20)

Moderate Demand (21–50)

High Demand (> 50)

I also counted the total number of valid requests (values greater than 0).

After classification, I applied the PLI rule:

PLI = 0 → Removed all Low Demand requests

PLI = 1 → Removed all High Demand requests

PLI = 2 → Kept only Moderate Demand requests

Finally, the program displays the filtered lists, total valid requests, number of removed requests, and the values of L and PLI.

Personalization Applied

Length of my name (L): 21
PLI value: 0
Applied Rule: Rule A – Removed Low Demand requests

Learning Outcome

Through this challenge, I improved my understanding of lists, loops, and conditional statements in Python. I also learned how to apply personalized logic dynamically and how to structure a program step by step based on a real-world scenario.
