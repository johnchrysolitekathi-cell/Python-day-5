Name=input("Enter your name: ")
Name=Name.replace(" ","")
L=len(Name)
low_demand=[]
moderate_demand=[]
high_demand=[]
invalid_request=[]
no_demand=0
n=int(input("Enter the Number of Resource Request: "))
Resource_Request=[0]*n
valid=0
for i in range (n):
    Resource_Request[i]=int(input("Enter Resource Request: "))
    if Resource_Request[i] >= 0:
        valid = valid + 1

for i in range (n):
    if Resource_Request[i] < 0:
        invalid_request=invalid_request+[Resource_Request[i]]
    elif Resource_Request[i] == 0:
        no_demand=no_demand + 1
    elif 1 <= Resource_Request[i]<=20:
        low_demand=low_demand+[Resource_Request[i]]

    elif 21 <= Resource_Request[i]<=50:
        moderate_demand= moderate_demand + [Resource_Request[i]]

    elif Resource_Request[i]> 50:
        high_demand= high_demand + [Resource_Request[i]]

print("Resource Request= ",Resource_Request)
print("Low Demand= ",low_demand)
print("Moderate Demand= ",moderate_demand)
print("High Demand= ", high_demand)
print("Invalid Request=",invalid_request)
print(" ")


PLI= L%3
print("After using PLI: ")

if PLI==0:
    a=len(low_demand)
    low_demand=[]
    print("length of Name= ",L)
    print("PLI= ",PLI)
    print("Low Demand=",low_demand)
    print("Moderate Demand=",moderate_demand)
    print("High Demand=",high_demand)
    print("Invalid Request=",invalid_request)
    print(" ")
    print("Valid Entries=",valid)
    print("No. Entries removed due to PLI(i.e., low_demand)= ", a)

elif PLI==1:
    a=len(high_demand)
    high_demand=[]
    print("length of Name= ",L)
    print("PLI= ",PLI)
    print("Low Demand=",low_demand)
    print("Moderate Demand=",moderate_demand)
    print("High Demand=",high_demand)
    print("Invalid Request=",invalid_request)
    print(" ")
    print("Valid Entries=",valid)
    print("No. Entries removed due to PLI(i.e., high_demand)= ", a)

elif PLI==2:
    a=len(low_demand)
    b=len(high_demand)
    c=len(invalid_request)
    low_demand=[]
    high_demand=[]
    invalid_request=[]
    print("length of Name= ",L)
    print("PLI= ",PLI)
    print("Low Demand=",low_demand)
    print("Moderate Demand=",moderate_demand)
    print("High Demand=",high_demand)
    print("Invalid Request=",invalid_request)
    print(" ")
    print("Valid Entries=",valid)
    print("No. Entries removed due to PLI(i.e., low_demand, high_demand, invalid_demand)= ", a+b+c)






