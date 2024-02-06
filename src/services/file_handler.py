import csv
import json


class FileHandler:
    def read_from_csv(self, filename):
        rows = []
        with open(filename, "a+", newline="", encoding="utf-8") as csvfile:
            csvfile.seek(0)
            csv_reader = csv.reader(csvfile, delimiter=",", quotechar="|")
            for row in csv_reader:
                rows.append(row)
        return rows

    def write_to_csv(self, filename, line_list):
        with open(filename, "w+", newline="", encoding="utf-8") as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=",", quotechar="|")
            for line in line_list:
                csv_writer.writerow(line)

    def write_to_txt(self, filename, string):
        with open(filename, "a", encoding="utf-8") as file:
            file.write(f"{string}\n")

    def overwrite_latest_recipe(self, filename, updated_recipe):
        with open(filename, "r+") as file:
            lines = file.readlines()
            if lines:
                lines[-1] = updated_recipe + "\n"  # Replace the last line
                file.seek(0)  # Go back to the start of the file
                file.writelines(lines)  # Write the modified lines
                file.truncate()  # Truncate the file to the new size
            else:
                file.write(updated_recipe + "\n")  # Write the line if file is empty

    def read_json_objects_recipe_txt(self):
        recipe_list = []
        with open("recipes.txt", "a+", encoding="utf-8") as f:
            f.seek(0)
            for jsonObj in f:
                recipeDict = json.loads(jsonObj)
                recipeDict["ingredients"] = list(recipeDict["ingredients"].items())
                recipe_list.append(recipeDict)
        return recipe_list

    def read_json_objects_mock_recipe(self):
        with open("mock_recipe.json", encoding="utf-8") as file:
            mock_recipe = json.load(file)
        return mock_recipe
