def generate_name(city, pet):
    return city + ' ' + pet

def main():
    city = input("What's the name of the city you grew up in? ", )
    pet = input("What's your pet's name? ")
    print(generate_name(city, pet))


if __name__ == "__main__":
    main()