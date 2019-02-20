import test_data
import json

#Creates and returns a GameLibrary
# object(defined in test_data) from loaded json_data
def make_game_library_from_json( json_data ):
    #Initialize a new GameLibrary
    with open(json_data) as reader:
        data = json.load(reader)

    test = open(json_data)
    #print(test.read())
    #use data object to build a new game library
    game_library = test_data.GameLibrary()
    a = json.load(test)
    for game_json in json_data:
        new_game = test_data.Game()
        new_game.title = game_json["title"]
        new_game.year = game_json[-1]

        platform_json = game_json["platform"]
        new_platform = test_data.Platform()
        new_platform.launch_year = platform_json[-1]
        new_platform.name = platform_json["name"]

        new_game.platform = new_platform
        game_library.add_game(new_game)

    #print(game_library.games)

    ### Begin Add Code Here ###
    #Loop through the json_data
        #Create a new Game object from the json_data by reading
        #  title
        #  year
        #  platform (which requires reading name and launch_year)
        #Add that Game object to the game_library
    ### End Add Code Here ###



    return game_library

    json_data = "data/test_data.json"

    game_library = make_game_library_from_json(a)

    print(game_library)



#Part 2
input_json_file = "data/test_data.json"



### Begin Add Code Here ###
#Open the file specified by input_json_file
#Use the json module to load the data from the file
#Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
#Print out the resulting GameLibrary data using print()
### End Add Code Here ###
