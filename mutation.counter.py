#Ill generate a list of mutations randomly
# A234G means Adenine mutated to Guanine at position 234

mutations = ["A234G", "A234G", "C144T", "G789A", "A234G", "C144T"]

#now ill create a dictionary to store contents 
#key: mutation name and the value: how many time the mutation occurs
#starts empty {} because nothing is counted yet

mutation_counter = {}

for mutation in mutations:
    if mutation in mutation_counter:
        mutation_counter[mutation] += 1
    else:
        mutation_counter[mutation] = 1

#This checks if mutation is already in the dictionary
#If it is, it adds 1 to the count if not, it adds the mutation to the dictionary with a count of 1``
# E.g. after first A234G, the dictionary looks like this: {"A234G": 1}
# After second A234G, it looks like this: {"A234G": 2}
# After C144T, it looks like this: {"A234G": 2, "C144T": 1}            

print("Mutation frequencies:")
for mutation, count in mutation_counter.items():
    print(f"{mutation}: {count}")

# suppose the dictionary looks like this: mutation_counter = {"A234G": 3, "C144T": 2, "G789A": 1}
#.items turn the dictionary into pairs so it becomes like this: [("A234G", 3), ("C144T", 2), ("G789A", 1)]
#loop through each pair; each time, mutation takes the first value in the pair and count takes the second value in the pair``(splitting)
#Then it prints them out in a formatted way``