#Movies

#---
#Global
#---

movies = {
    "Dune": 12.5,
    "Barbie": 11.0,
    "Oppenheimer": 13.0,
    "Spirited Away": 10.0
}

purchases = []  # list of (title, qty, price_each)

#---
#Function
#---

# Title, Tickets, Ticket Cost
def total_cost(item):
    total = 0
    recipt = {}
    
    for i in range(len(item)):
        x = item[i]
        calc= x[1] * x[2]
        rc = {item[0]: calc}
        recipt.append(rc)
        total += calc    
    return total,recipt


def available_movies():
    print("Available movies:")
    for title, price in movies.items():
        print(f"{title:14s} ${price:.2f}")
    


#---
#MAIN
#---


available_movies()

tickets = 0
while True:
    title = input(f"What movie would you like?, or done: ")
    if title.lower() == 'done':
        break
    if title in movies:
        tickets = int(input(f"How many would you like tickets?: "))
    else:
        print('Thats not avalible!')
        available_movies()
        continue
    q = (title, tickets, movies[title])
    purchases.append(q)

total = total_cost(purchases)


#---
#Recipt
#---

print(total)



        
    

    
        
    
    
        
        
        



# TODO: use a while loop that continues until the user enters 'done'
# 1) ask for movie title (case sensitive is fine)
# 2) if title not in movies, print the available keys and continue
# 3) ask for quantity (int)
# 4) append (title, qty, movies[title]) to purchases
# 5) optional: track running subtotal