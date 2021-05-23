import json
import yaml

def readFile(**kwargs):
    filename = kwargs.get("filename")
    filetype = kwargs.get("filetype")

    if (filetype == "json"):
        try:
            with open(filename) as f:
                print("got json: "+ filename)
                data = json.load(f)
                return (data)
        except:
            #didnt find file
            raise Exception("failed to read file "+filename)
    elif (filetype == "yaml"):
        try:
            with open(filename) as f:
                print("got json: "+ filename)
                data = yaml.safe_load(f)
                return (data)
        except:
            #didnt find file
            raise Exception("failed to read file "+filename)

def getCreds(**kwargs):
    filename = kwargs.get("filename")
    return readFile(filename=filename, filetype="json")