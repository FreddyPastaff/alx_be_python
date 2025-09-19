# Weather Recommendation Program
weather = input("What's the weather like today? (sunny/rainy/cold): ")
# Normalize input to lowercase
weather = weather.lower()

# clothing recommendations

if  weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf")
else:
    print("Sorry, I dont have recommendations for this weather")