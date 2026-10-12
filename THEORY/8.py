scores = {"Aliceji": 88, "Bobokkkkkk": 95, "Charlie": 92}
topscorer = max(scores, key=scores.get)
print("The top scorer is:", topscorer, "with a score of", scores[topscorer])