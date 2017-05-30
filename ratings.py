def restaurant_rating(file_name):
    """Restaurant rating lister."""

    restaurant_ratings = {}

    with open(file_name) as open_file:
        for line in open_file:
            line = line.strip()
            data = line.split(":")
            restaurant, rating = data
            restaurant_ratings[restaurant] = rating

    while True:
        new_restaurant = (raw_input("Enter a restaurant name: ")).capitalize()
        new_rating = raw_input("Enter a restaurant rating: ")

        try:
            float(new_rating)
        except ValueError or False or AttributeError or SyntaxError:  
            print "Invalid input. Please enter an integer between 1 and 5."
            continue

        if "." in new_rating:
            print "Invalid input. Please enter an integer between 1 and 5."
            continue

        if int(new_rating) < 1 or int(new_rating) > 5:
            print "Invalid input. Please enter an integer between 1 and 5."    
            continue
        else:
            restaurant_ratings[new_restaurant] = int(new_rating)
            break

    for restaurant, rating in sorted(restaurant_ratings.items()):
        print "{} is rated at {}.".format(restaurant, rating)

restaurant_rating("scores.txt")


# put your code here
