import cc_dat_utils
import cc_data
import json
def make_level_from_dat(example_data):
    #Initialize a new GameLibrary
    with open(example_data) as reader:

        #data = json.load(reader)
        test = open(example_data)


        json_library = json.load(test)
    game_library = cc_data.CCDataFile()
    for game_json in json_library:
            new_game = cc_data.CCLevel()
            new_game.level_number = game_json["level_number"]
            new_game.time = game_json["time"]
            new_game.num_chips = game_json["num_chips"]
            new_game.upper_layer = game_json["upper_layer"]
            new_game.lower_layer = game_json["lower_layer"]
            result = game_json["optional_fields"]
            result = []
            for optional_fields_json in game_json["optional_fields"]:
                if optional_fields_json["id"] == 1:
                    cc_data.CCMapHintField(optional_fields_json["hint_text"])

                if optional_fields_json["id"] == 2:
                    cc_data.CCEncodedPasswordField(optional_fields_json["password_data"])

                if optional_fields_json["id"] == 3:
                    cc_data.CCMapTitleField(optional_fields_json["title"])

                if optional_fields_json["id"] == 6:
                    cords = optional_fields_json["monsters"]
                    cords = []
                    for cords in optional_fields_json["monsters"]:
                        optional_fields_json["monsters"].x = cords["x"]
                        optional_fields_json["monsters"].y = cords["y"]
                        optional_fields_json.add_field(cords)
                new_game.add_field(optional_fields_json)

            game_library.add_level(new_game)

    return game_library

    cc_dat_utils.write_cc_data_to_dat(game_library, "data/new_game.dat")

    pfgd_test_data = cc_dat_utils.make_cc_data_from_dat("data/new_game.dat")
    cc_dat_utils.write_cc_data_to_dat(pfgd_test_data, "data/copy_of_new_game.dat")
    print (pfgd_test_data)
example_data = "data/example_data.json"

game_library = make_level_from_dat(example_data)

print(game_library)




    #Part 3
#Load your custom JSON file
#Convert JSON data to cc_data
#Save converted data to DAT file



