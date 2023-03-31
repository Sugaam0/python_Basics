
weight = float(input("ENter your weight : "))
choice =  input("(K)gs or (L)bs? ")

if choice.upper() == "K":
    pound  = weight * 2.20
    print("Weight in kg is : " + str(pound))
elif choice.upper() == "L":
    kg = weight/2.20
    print("weight in pounds  is : "+ str(kg))

    
