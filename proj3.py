





#INSURANCE POLICY INFORMATION LISTS

Policy_Number_List=[4739,2511,4608,8921,4700,9676,3251,5091,2567,5298,8463,9066,5881,7968,6308,2335,4468,4395,6504]

Name_List=['Simpson, Homer','Flanders, Ned','Seinfeld, Jerry','Tanner, Danny','Banks, Phillip','Brady, Marcia','Flintstone, Wilma','Bradshaw, Carrie','Griffith, Andy','Cleaver, June','Fletcher, Jessica','McGee, Fibber','Brown, Doc','Summers, Buffy','Halliwell, Prue','Malone, Sam','Barone, Debra','Tanner, Stephanie','Taylor, Tim']

Address_List=['742 Evergreen Terrace, Springfield, IL 62704-4913','744 Evergreen Terrace, Springfield, MA 01119-2800','129 W 81st St, #5A, New York, NY 10024-7207','1882 Gerard Street, San Francisco, CA 94134-1259','508 Saint Cloud Road, Los Angeles, CA 90077-3427','4222 Clinton Way, Los Angeles, CA 90026-4164','342 Gravelpit Terrace, Boulder, CO 80305-2341','245 East 73rd Street, Manhattan, NY 10023-2702','322 Maple Drive, Mount Airy, NC 27030-3406','485 Maple Drive, Kennebunkport, ME 04046-6711','698 Candlewood Lane, East Lansin, MI 48823-1234','79 Wistful Vista, Lynbrook, NY 11563-3045','1640 Riverside Drive, Elizabeth City, NC 27909','1630 Revello Drive, Tuskegee, AL 36088-6088','1329 Carroll Ave, Auburn, AL 94134-1259','83 Beacon St, Detroit, MI 48211-1068','320 Fowler Street, Fowler, KY 11563-3045','1882 Gerard Street, Des Moines, IA 50310-5565','510 Glenview, Hill Valley, CA 93706-4735']

Gender_List=['M','F','M','M','F','M','F','M','F','M','M','F','F','M','F','M','M','M','M']

Beneficiaries_List=[3,2,3,1,2,1,2,1,4,2,3,4,3,3,2,1,5,1,1]

Policy_Amount_List=[664500,505011,301064,709890,80026,1006082,280000,680107,804042,1028006,603008,700145,504083,73005,32098,10799,500123,600016,101100]

#### NOT CHANGE THE INCLUDED LISTS #####


# add all of your function definitions here

def getMenuOption():
    val = input("\n1. Address Change\n2. Beneficary Change\n3. Remove a Policy\n4. Print Modified Polices by Policy Number\n5. Display all Data\n6. Exit\n\n")
    if   (val == '1' or val.split()[0].lower() == "address"):
        return 1
    elif (val == '2' or val.split()[0].lower() == "beneficiary"):
        return 2
    elif (val == '3' or val.split()[0].lower() == "remove"):
        return 3
    elif (val == '4' or val.split()[0].lower() == "print"):
        return 4
    elif (val == '5' or val.split()[0].lower() == "display"):
        return 5
    elif (val == '6' or val.split()[0].lower() == "exit"):
        return 6
    else:
        return 0


"""
Determines if the policy is in the given policy list
input   -- policyNumber - the policy number to be checked
        -- policyList   - the list containing all policies
Returns -- true if policy is in list, false otherwise
"""
def isValidPolicy(policyNumber, policyList):
    if (policyNumber in policyList):
        return True
    else:
        return False
"""
Prints the policies in a given list
input -- changed policy list
"""
def printChangedPolicies(policy_list):
    i = 0
    print("\nChanged or deleted:")
    for policy in policy_list:
        print(policy)
    count = countPolicies(policy_list)
    if count == 1:
        print("1 policy has been changed or deleted.")
    else:
        print("%d policies have been changed or deleted." % count)

"""
Counts the number of policies in given list
input   -- a list
returns -- the size of the list
"""
def countPolicies(aList):
    i = 0
    for policy in aList:
        i = i + 1
    return i

"""
Prints the data contained the the 6 given lists
"""
def printAllData():
    print(Policy_Number_List)
    print(Name_List)
    print(Address_List)
    print(Gender_List)
    print(Beneficiaries_List)
    print(Policy_Amount_List)
"""
deletes items from all list coresponding to the index
input -- Index of policy
"""
def deleteByIndex(Index):
    del Policy_Number_List[Index]
    del Name_List[Index]
    del Address_List[Index]
    del Gender_List[Index]
    del Beneficiaries_List[Index]
    del Policy_Amount_List[Index]


def changBeneficiary(bAmount, bNumber, policyNumber):
    #TODO
    Index = Policy_Number_List.index(policyNumber)
    if bAmount > int(Policy_Amount_List[Index]):
        aChange = "Change in Policy Amount: Increase"
    elif bAmount == int(Policy_Amount_List[Index]):
        aChange = "Change in Policy Amount: None"
    else:
        aChange = "Change in Policy Amount: Reduction"

    if bNumber > int(Beneficiaries_List[Index]):
        bChange = "Change in Beneficiaries: Increase"
    elif bAmount == int(Beneficiaries_List[Index]):
        bChange = "Change in Beneficiaries: None"
    else:
        bChange = "Change in Beneficiaries: Reduction"
    Policy_Amount_List[Index] = bAmount
    Beneficiaries_List[Index] = bNumber
    policyPercent = (1 / bNumber) * 100
    policyAmount  = (bAmount / bNumber)
    print("%78s Policy #%d\n%s" % (" ",policyNumber, Address_List[Index]))
    print("%-15s %-15s %-15s %-15s %-15s %-15s" % ("Name","Gender","Policy Amount", "Beneficiaries", "Payout %", "Payout $"))
    print("%-15s %-15s %-15s %-15s %-15.2f %-15.2f" % (Name_List[Index], Gender_List[Index], Policy_Amount_List[Index], Beneficiaries_List[Index], policyPercent, policyAmount))
    print(aChange)
    print(bChange)

# This is where your main program starts
if __name__ == '__main__':
    # put all of your main program code here;
    # all of it indented to this level
    Modified_Policies = []
    while True:
        option = getMenuOption()
        if (option == 0):
           print("\nUnknown menu option")

##Address Change
        elif (option == 1):
            Policy_Number = int(input("\nWhat is the policy number?"))
            if (isValidPolicy(Policy_Number, Policy_Number_List)):
                if Policy_Number not in Modified_Policies:
                    Modified_Policies.append(Policy_Number)
                New_Address = input("\nWhat is the new Address")
                Index = Policy_Number_List.index(Policy_Number)
                Address_List[Index] = New_Address
            else:
                print("\nThat policy does not exist.")


##Beneficaiary Change
        elif (option == 2):
            Policy_Number = int(input("\nWhat is the policy number?"))
            if (isValidPolicy(Policy_Number, Policy_Number_List)):
                if Policy_Number not in Modified_Policies:
                    Modified_Policies.append(Policy_Number)
                Amount = input("What is the new policy amount?")
                Number = input("What is the new number of beneficiaries?")
                changBeneficiary(int(Amount), int(Number), Policy_Number)
            else:
                print("\nThat policy does not exist.")


##Remove Policy
        elif (option == 3):
            Policy_Number = int(input("\nWhat is the policy number?"))
            if (isValidPolicy(Policy_Number, Policy_Number_List)):
                if Policy_Number not in Modified_Policies:
                    Modified_Policies.append(Policy_Number)
                Index = Policy_Number_List.index(Policy_Number)
                Name = Name_List[Index]
                deleteByIndex(Index)
                print("Policy #%d for %s has been removed" % (Policy_Number, Name))
            else:
                print("\nThat policy does not exist.")


##Print Modified Policies by Policy Number
        elif (option == 4):
            printChangedPolicies(Modified_Policies)


##Display all data
        elif (option == 5):
            printAllData()


##Exit
        else:
            break
