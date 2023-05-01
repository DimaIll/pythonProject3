import json
def load_candidates_from_json(path):
    """
    JSON Data loader
    :param path: data-file path
    :return data
    """
    with open("path", "r", encoding="utf-8") as file:
        data = json.load(file)
        candidates = {}
        for i in data:
            candidates[i["id"]] = i
        return candidates


def get_candidate(id):
    return candidates[id]


def get_candidates_by_name(name):
    return candidates[name]


def get_candidates_by_skill(skill):
    return candidates[skill]