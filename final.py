import sys
import csv
import matplotlib.pyplot as plt

def main(argv):  #  python final.py transactions.csv 3

    valid_input(argv) #make sure that the input given is valid
    trans=get_month_spening(argv) #give me the tim's:-24
    
    #make the graphs interactive
    paid_off_cc(trans)
    show_location_spending(trans) 
     
def paid_off_cc(trans):
    #show me if i paid off my cc
    spent=0
    paid=0
    for item in trans:
        spening=trans[item]
        if spening<0:
            spent+=(spening)
        else:
            paid+=(spening)
            
    spent=round(spent,2)
    paid=round(paid,2)
    diffrence=round(paid+spent,2) #paid:+ & spent:-, need to add to cancel out
    
    #graph the data
    graph_apperance("$ Spent","$ Paid", "Did i pay off Credit Card?")
    plt.bar("Spent", spent,color='#DE3C3C')
    add_text("Spent",spent)
    
    plt.bar("Paid off", paid, color='black')
    add_text("Paid off",paid)
    
    plt.bar("I owe",diffrence,color='#133804')
    add_text("I owe",diffrence)
    
    plt.show()

def addlabels(x,y): #credit: https://bit.ly/31ECTkN
    for i in range(len(x)):
        plt.text(i, y[i], y[i], ha = 'center',rotation=45 ,Bbox = dict(facecolor = 'white', alpha =.6))
        
def add_text(x,y):
    plt.text(x,y,float(y)*-1,ha='center',Bbox=dict(facecolor="white", alpha=.8))         
                 
def graph_apperance(x,y,title):
    plt.figure(figsize=(10,8),facecolor='#C6CDCC')
    plt.xlabel(x,fontweight="bold")
    plt.ylabel(y,fontweight='bold')
    plt.tick_params(axis='x', rotation=35)
    plt.title(title)  
    
def show_location_spending(trans): 
    #how much did i spent where
    spent_where=[]
    amount_spent=[]
    for item in trans:
        if(item=="PAYMENT"): #i dont want to know how much i paid just yet
            continue
        amount_spent.append(float(round(trans[item],2)))
        spent_where.append(item)
       
    #make the bargraph
    graph_apperance("I spent $ at ", "I spent how much!?", "How much did I spend Where?")
    plt.bar(spent_where,amount_spent,color='#DE3C3C') #i want to hover over the bargraph and it tell me the amount spent
    addlabels(spent_where, amount_spent)
    
    plt.show()

def get_month_spening(argv):
    trans={}

    with open(argv[1],"r") as csvfile:
        reader =csv.DictReader(csvfile)
        for row in reader: #select the month chosen by the user
            #check the len on date
            if(len(row['Transaction Date'])==8):
                #print(row['Description 1'])

                if (int(row['Transaction Date'][0]) ==int(argv[2]) ): #match the month selected
                    new_descript=row['Description 1'].split() #give me the first word

                    #if the trans is empty add it's first item
                    if(len(trans)==0):
                        new_dict={
                            new_descript[0]:float(row["CAD$"])
                        }
                        trans.update(new_dict)
                        continue;

                    #if bob in trans update bob's new total
                    elif new_descript[0] in trans:
                        trans[new_descript[0]]+=float(row["CAD$"])

                    #if bob not in trans set bob:$4.20
                    elif new_descript[0] not in trans:
                        trans.update( {new_descript[0]:float(row["CAD$"]) } )


            elif(len(row['Transaction Date'])==9):
              
                if (int(row['Transaction Date'][:1]) ==int(argv[2]) ): #match the month selected
                    new_descript=row['Description 1'].split() #give me the first word

                    #if the trans is empty add it's first item
                    if(len(trans)==0):
                        new_dict={
                            new_descript[0]:float(row["CAD$"])
                        }
                        trans.update(new_dict)
                        continue;

                    #if bob not in trans set bob:$4.20
                    elif new_descript[0] not in trans:
                        trans.update( {new_descript[0]:float(row["CAD$"]) } )

                    #if bob in trans update bob's new total
                    elif new_descript[0] in trans:
                        trans[new_descript[0]]+=float(row["CAD$"])
                        
    
    trans_order= dict(sorted(trans.items(), key=lambda i:i[1]))
    return trans_order;

def valid_input(argv):
    if( len(argv)!=3): #if no csv given
        print("Usage: python final.py transactions.csv month(ex: 7) year(ex: 2020)")
        sys.exit()

    try:#try to open the csv
        open(argv[1],"r")

    except FileNotFoundError:
        print("The file input is invalid, try again :)")
        return 1;

main(sys.argv)