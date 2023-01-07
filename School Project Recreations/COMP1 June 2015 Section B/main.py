#From AQA AS Computing June 2015 COMP1 Paper - psuedocode about printing prime numbers up to 50.
print("The first few prime numbers are: ")
for Count1 in range(2, 50):
  Count2 = 2
  Prime = "Yes"
  while Count2 * Count2 <= Count1:
    if Count1 % Count2 == 0:
      Prime = "No"
    Count2 += 1
  if Prime == "Yes":
    print(Count1)
