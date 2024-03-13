import csv
import json


class FileHandler:
    """Class that handles changes to files"""

    def read_from_csv(self, filename):
        rows = []
        with open(filename, "a+", newline="", encoding="utf-8") as csvfile:
            csvfile.seek(0)
            csv_reader = csv.reader(csvfile, delimiter=",", quotechar="|")
            for row in csv_reader:
                rows.append(row)
        return rows

    def write_to_csv(self, filename, line_list):
        """Writes new lines to a csv file

        Args:
            filename (string): name of the file
            line_list (list): new lines to be added to the file
        """

        with open(filename, "w+", newline="", encoding="utf-8") as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=",", quotechar="|")
            for line in line_list:
                csv_writer.writerow(line)

    def write_to_txt(self, filename, line):
        """Writes a new line to the txt file

        Args:
            filename (string): name of the file
            line (string): line to be added to the file
        """

        with open(filename, "a", encoding="utf-8") as file:
            file.write(f"{line}\n")

    def overwrite_latest_recipe(self, filename, updated_recipe):
        """Overwrites the latest recipe with the new updated recipe

        Args:
            filename (string): name of the file
            updated_recipe (string): the updated recipe which replaces the latest recipe
        """
        with open(filename, "r+", encoding="utf-8") as file:
            lines = file.readlines()
            if lines:
                lines[-1] = updated_recipe + "\n"
                file.seek(0)
                file.writelines(lines)
                file.truncate()
            else:
                file.write(updated_recipe + "\n")

    def read_json_objects_recipe_txt(self):
        """Reads json objects from txt file into a list

        Returns:
            list: List containing all json objects from the file
        """
        recipe_list = []
        with open("recipes.txt", "a+", encoding="utf-8") as f:
            f.seek(0)
            for json_obj in f:
                recipe_dict = json.loads(json_obj)
                recipe_dict["ingredients"] = list(recipe_dict["ingredients"].items())
                recipe_list.append(recipe_dict)
        return recipe_list

    def read_json_objects_mock_recipe(self):
        """Reads json objects to be used as a mock recipe for testing

        Returns:
            JSON object: the mock recipe
        """
        with open("mock_recipe.json", encoding="utf-8") as file:
            mock_recipe = json.load(file)
        return mock_recipe
