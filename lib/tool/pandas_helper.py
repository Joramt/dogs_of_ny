class PandaHelper():
    def generateConditionsFromDict(condition_dict):
        if not condition_dict:
            raise ValueError("You must provide a non empty dict")
        else:
            return " and ".join("{} == '{}'".format(key.lower(), val.lower())
                                for key, val in condition_dict)

    def generateConditionsFromList(condition_list):
        # TODO : implement this function
        return False
