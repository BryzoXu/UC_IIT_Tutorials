#Movies

#---
#Global
#---
tickets_by_movie = {}
revenue_by_movie = {}

purchases = []  

movies = {
    "Dune": 12.5,
    "Barbie": 11.0,
    "Oppenheimer": 13.0,
    "Spirited Away": 10.0
}



#---
#Functions
#---


def total_cost(items):
    total = 0
    recipt = {}
    discount = False  
     
    for x in items:
        name = x[0]
        qty = x[1]
        price = x[2]
        line_total = qty * price
        if qty > 4:
            line_total *= 0.9 # 10% discount
            discount = True
       
        if name in recipt:  # already purchased this movie
            old_qty, old_total = recipt[name]
            recipt[name] = (old_qty + qty, old_total + line_total)
        else:
            recipt[name] = (qty, line_total)
        
        total += line_total
    
    return total, recipt, discount


def available_movies():
    print("Available movies:")
    for title, price in movies.items():
        print(f"{title:14s} ${price:.2f}")

def analytics(tickets_by_movie, revenue_by_movie):
    
    
    
    return 

def sale_summary(recipt):
  
    for item, (qty, _) in recipt.items(): 
        tickets_by_movie[item] = tickets_by_movie.get(item, 0) + qty
    
    for item, (_, cost) in recipt.items():
        revenue_by_movie[item] = revenue_by_movie.get(item, 0) + cost
    
     

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
        tickets = int(input(f"How many tickets would you like?: "))
    else:
        print('Thats not avalible!')
        available_movies()
        continue
    q = (title, tickets, movies[title])
    purchases.append(q)

total, recipt, discount = total_cost(purchases)

sale_summary(recipt)
analytics(tickets_by_movie, revenue_by_movie)



#---
#OUT
#---

mem_code = input(f"\nAre you a memeber?: ").lower()
if "y" in mem_code:
    total *= 0.95

print("----------\n*Recipt* \n        ")

for item, (qty, cost) in recipt.items():
    print(f"{item:10s} {qty} @ ${movies[item]:.2f} = ${cost:.2f}")

print(f"Your Total: ${total:.2f}")
if discount == True:
    print(f"**INCLUDES GROUP 10% DISCOUNT**")


    

        

    
        
    
    
        
        
        


