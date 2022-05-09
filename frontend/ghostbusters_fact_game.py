list_cast = [
    "carrie coon", "paul rudd", "finn wolfhand", "mckenna grace", "logan kim", "celeste o'connor", "bill murray", "dan aykroyd", "ernie hudson", "annie potts", "sigourney weaver", "bob gunton", "j.k. simmons", "shawn seward", "billie bryk", "sydney mae diaz", "hannah duke", "bokeem woodbine", "paulina alexis"
]
 list_quotes = [
     "Why’d you bring me up here? – Trevor", "Entertainment value? Do you juggle? – Lucky", "What are you doing here in Summerville? – Lucky", "Honestly, my mom won’t say it, but we’re completely broke. And the only thing that’s left in our name is this creepy old farmhouse my grandfather left us in the middle of nowhere. – Trevor", "Somehow, a town that isn’t anywhere near a tectonic plate, has no volcanic activity, that has no faultlines no fracking, no loud music even- is shaking on a daily basis. – Mr. Grooberson", "Under the dining table- now! – Mom", "Hey remember that summer, when we all died under a table? – Trevor"
 ]



print("Welcome to the ghostbuster info game")

def game_start():
    print("welcome")

    answer = input ("would you like to play (yes/no)?....")

    if answer.lower().strip() == "yes":
        name = input("enter you name.....")
        print(f"welcome to ghost busters {name} procede for knowlege!")
        

    if answer.lower().strip() == "no":
        print("well go home then!")

game_start()        