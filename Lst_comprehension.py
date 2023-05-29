#1
for i in range(1,7):
    print([i*i*i],end=' ')
print("\n")
for i in range(0,10):
    if i%2!=0:
        print([i*i],end=' ')
print("\n")
#2
movies = ["Sky high","Predator","Avengers","Johnny English","John Wick","jojo Rabbit"]
for movie in movies:
    if movie.startswith('J'):
        print([movie],end=' ')
print("\n")
#3
jamesBondMovies = [('Dr.No','1962'),('From Russia with love', '1963'),('Goldfinger', '1964'),('Thunderball','1965'),('You only Live Twice','1967'),('On her Majesty s Secret service','1969'),('Diamonds are forever','1971'),('Live and Let die','1973'),('The man wiht the Golden Gun','1974'),
                   ('Moonraker','1979'),('For your eyes only','1981'),('Octopussy','1983'),('A view to kill','1985'),('the living daylights','1987'),('License to kill','1989'),
                   ('Goldeneye','1995'),('tomorrow Never dies','1997'),('the world is not enough','1999'),('die another day','2002'),('casino royale','2006'),('quantum of solace','2008'),
                   ('Skyfall','2012'),('Spectre','2015'),('No time to die','2021')]

print([movie for movie in jamesBondMovies if '1990' <= movie[1][0:] <= '2000'])
print("\n")
#4
matrix = [1,2,3,4,5]
for i in range(len(matrix)):
    matrix[i] *= 5
print(matrix)
print("\n")
#5
presidents = ['Clinton', 'Obama', 'Trump']
presidents = ['Mr ' + name for name in presidents]
print(presidents)
print("\n")
#6
A = [1,2,3]
B = [4,5]
C = A + B
print(C)
print("\n")
#7
users = ['Customer', 'Admin', 'Analyst']
loginCredentials = ['Valid', 'Invalid','Empty','Empty ']
print([(user,credential) for user in users for credential in loginCredentials])
print("\n")