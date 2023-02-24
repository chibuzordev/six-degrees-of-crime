import csv
import sys

from util import Node, StackFrontier, QueueFrontier


# Maps names to a set of corresponding person_ids
names = {}
# Maps person_ids to a dictionary of: name, birth, detained, crime_scenes (a set of city_ids)
people = {}
# Maps city_ids to a dictionary of: title, appearances (a set of person_ids)
crime_scenes = {}


def load_data(directory):

    # Load people
    with open(f"{directory}/people.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "detained": row["detained"],
                "crime_scenes": set()
            }
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                names[row["name"].lower()].add(row["id"])
    # Load crime_scenes
    with open(f"{directory}/crime_scenes.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            crime_scenes[row["id"]] = {
                "name": row["name"],
                "appearances": set()
            }
    # Load appearances
    with open(f"{directory}/appearances.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                people[row["person_id"]]["crime_scenes"].add(row["city_id"])
                crime_scenes[row["city_id"]]["appearances"].add(row["person_id"])
            except KeyError:
                pass

def main():
    if len(sys.argv) > 2:
        sys.exit("Usage: python degrees.py [directory]")
    directory = "data"

    # Load data from files into memory
    print("Loading data...")
    load_data(directory)
    print("Data loaded.")

    source = person_id_for_name(input("Name: "))
    if source is None:
        sys.exit("Person not found.")
    target = person_id_for_name(input("Name: "))
    if target is None:
        sys.exit("Person not found.")

    path = shortest_path(source, target)

    if path is None:
        print("Not connected.")
    else:
        degrees = len(path)
        s = ""
        if degrees != 1:
            s = "s"
        print(f"{degrees} degree{s} of separation.")
        path = [(None, source)] + path
        for i in range(degrees):
            detained1 = people[path[i][1]]["detained"]
            detained2 = people[path[i + 1][1]]["detained"]
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            city = crime_scenes[path[i + 1][0]]["name"]
            status = "."
            if (detained1 == detained2) and (degrees == 1):
                status = "  *."
            print(f"{i + 1}: {person1} and {person2} were in {city}{status}")
            


def shortest_path(source, target):
    """
    Returns the shortest list of (city_id, person_id) pairs
    that connect the source to the target.

    If no possible path, returns None.
    """

    start = Node(state=source, parent=None, action= None)
    frontier = QueueFrontier()
    frontier.add(start)
    explored = set()

    while True:
        if frontier.empty():
            return None
        node = frontier.remove()
        explored.add(node.state)
        
        neighbors = neighbors_for_person(node.state)
        for city, person in neighbors:
            if person not in explored and not frontier.contains_state(person):
                child = Node(state=person, parent=node, action=city)
                if child.state == target:
                    path = []
                    node = child
                    while node.parent is not None:
                        path.append((node.action, node.state))
                        node = node.parent

                    path.reverse()
                    return path
                frontier.add(child)


def person_id_for_name(name):
    """
    Returns the state id for a person's name,
    resolving ambiguities as needed.
    """
    person_ids = list(names.get(name.lower(), set()))
    if len(person_ids) == 0:
        return None
    elif len(person_ids) > 1:
        print(f"Which '{name}'?")
        for person_id in person_ids:
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
        try:
            person_id = input("Intended Person ID: ")
            if person_id in person_ids:
                return person_id
        except ValueError:
            pass
        return None
    else:
        return person_ids[0]


def neighbors_for_person(person_id):
    """
    Returns (city_id, person_id) pairs for people
    who were in same city with a given person.
    """
    city_ids = people[person_id]["crime_scenes"]
    neighbors = set()
    for city_id in city_ids:
        for person_id in crime_scenes[city_id]["appearances"]:
            neighbors.add((city_id, person_id))
    return neighbors

if __name__ == "__main__":
    main()

