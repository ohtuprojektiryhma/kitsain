import csv
import json


class FileHandler:
    def read_from_csv(self, filename):
        rows = []
        with open(filename, newline="", encoding="utf-8") as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=",", quotechar="|")
            for row in csv_reader:
                rows.append(row)
        return rows

    def write_to_csv(self, filename, line_list):
        with open(filename, "w", newline="", encoding="utf-8") as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=",", quotechar="|")
            for line in line_list:
                csv_writer.writerow(line)

    def write_to_txt(self, filename, string):
        with open(filename, "a", encoding="utf-8") as file:
            file.write(f"{string}\n")

    def read_json_objects_recipe_txt(self):
        recipe_list = []
        with open("recipes.txt", encoding="utf-8") as f:
            for jsonObj in f:
                recipeDict = json.loads(jsonObj)
                recipeDict["ingredients"] = list(recipeDict["ingredients"].items())
                recipe_list.append(recipeDict)
        return recipe_list
