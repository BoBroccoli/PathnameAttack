def restaurant_rating(file_name):
    """Restaurant rating lister."""

    restaurant_ratings = {}

    with open(file_name) as open_file:
        for line in open_file:
            line = line.strip()
            data = line.split(":")
            restaurant_ratings[data[0]] = int(data[1])

    new_restaurant = (raw_input("Enter a restaurant name: ")).capitalize()
    new_rating = raw_input("Enter a restaurant rating: ")
    restaurant_ratings[new_restaurant] = int(new_rating)

    for restaurant, rating in sorted(restaurant_ratings.items()):
        print "{} is rated at {}.".format(restaurant, rating)

restaurant_rating("scores.txt")


# put your code here
