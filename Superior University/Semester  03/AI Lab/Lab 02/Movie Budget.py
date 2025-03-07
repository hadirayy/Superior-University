class movies:
    def __init__(self):
        self.movies = [
            ("Eternal Sunshine of the Spotless Mind", 20000000),
            ("Memento", 9000000),
            ("Requiem for a Dream", 4500000),
            ("Pirates of the Caribbean: On Stranger Tides", 379000000),
            ("Avengers: Age of Ultron", 365000000),
            ("Avengers: Endgame", 356000000),
            ("Incredibles 2", 200000000)
        ]
    
    def add_movie(self):
        n = int(input("\nHow many movies do you want to add? "))
        for j in range(n):
            name = input("\nEnter the name of the movie: ")
            budget = int(input("\nEnter the budget of the movie: "))
            self.movies.append((name, budget))
    
    def average_budget(self):
        total = 0
        for movie in self.movies:
            total += movie[1]
        avg = total / len(self.movies)
        return (f"{format(avg)}")
    
    def higest_budget(self):
        avg =float( self.average_budget())
        count = 0
        for movie in self.movies:
            if movie[1] > avg:
                count += 1
        print(f"\n{count} movies had higher budget than average.")
    
    def display_movies(self):
        for movie in self.movies:
            print(f"{movie[0]}: {movie[1]}\n")
movies = movies()
def main():
    while True:
        print(f"\n----------Menu----------\n")
        print(f"1. Add movie")
        print(f"2. Calculate average budget")
        print(f"3. Display movies")
        print(f"4. Display high budget movies")
        print(f"5. Exit")
        user_input = int(input("Enter the number: "))
        if user_input == 1:
            movies.add_movie()
        elif user_input == 2:
            print(f"\nThe average budget is {movies.average_budget()}")
        elif user_input == 3:
            movies.display_movies()
        elif user_input == 4:
            movies.higest_budget()
        elif user_input == 5:
            break
        else:
            print("Invalid input.")
main()