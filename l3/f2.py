# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
#1 Write a function that takes a single movie and returns True if its IMDB score is above 5.5

def imdb(movie):
    for i in movies:
        if i["name"] == movie:
            if i["imdb"] >= 5.5:
                return True
    return False

movie = str(input("movie's name: "))
print(imdb(movie))

#2 Write a function that returns a sublist of movies with an IMDB score above 5.5.
mylist = []
def checking():
    for i in movies:
        if i["imdb"] >= 5.5:
            mylist.append(i["name"])
    return mylist
print(*checking(), sep = ", ")

#3 Write a function that takes a category name and returns just those movies under that category.
l = []
def cat(nam):
    for i in movies:
        if i["category"] == nam:
            l.append(i["name"])
    return l
nam = input("Which Category?? ")
print(*cat(nam), sep = ", ")

#4 Write a function that takes a list of movies and computes the average IMDB score. 
def avg(movies):
    total = 0
    
    for i in movies:
        total += i["imdb"]
    
    return total / len(movies)

print(f"Average IMDB score: {round(avg(movies), 4)}")

#5 Write a function that takes a category and computes the average IMDB score.

def avg2(cat):
    count = 0
    total = 0
    for i in movies:
        if i["category"] == cat:
            count += 1
            total += i["imdb"]
    return total / count

cat = input("Categoryyy: ")
print("Avg IMDB score for" ,cat,"is", round(avg2(cat), 4))