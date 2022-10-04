def sorting_hat(name):
    import random
    f=name
    name=random.randint(0,3)
    return name


name=input("Whats your name, young wizard or witch !! ")
a=sorting_hat(name)
if a==0:
    print(name," is A HUFFLEPUFF, YOU HAVE A STRONG SENSE OF JUSTICE, LOYALTY AND A NICHE FOR HARDWORK")
if a==1:
    print(name," is A GRYFFINDOR, YOU ARE A BRAVE SOUL WITH A CHIVALROUS HEART")
if a==2:
    print(name," IS A SLYTHERIN, YOU ARE AN AMBITIOUS BEING  WITH LOADS OF LEADERSHIP QUALITIES")
if a==3:
    print(name," IS A RAVENCLAW, YOU ARE A WISE SOUL WITH AN ABILITY TO CREATE AND INTELLECTUALLY PONDER ON THINGS")

x
