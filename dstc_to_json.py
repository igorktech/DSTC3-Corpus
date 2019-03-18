import json
import spacy
import os

nlp = spacy.load('en')

dataset_name = "train"
dataset_path = "data/dstc3/"
output_path = "data/output/"

# Get a list of all the dialogues
dataset_list = os.listdir(dataset_path + dataset_name)

out_data = dict()
dialogues = []
num_dialogues = 0

# For each dialogue
# for folder in dataset_list:

for i in range(3,4):
    folder = dataset_list[i]
    print(folder)
    # Read JSON files
    with open(dataset_path + dataset_name + "/" + folder + "/" + "log.json") as file:
        sys_data = json.load(file)

    with open(dataset_path + dataset_name + "/" + folder + "/" + "label.json") as file:
        usr_data = json.load(file)

    # print(sys_data)
    # print(usr_data)

    dialogue = dict()
    utterances = []
    num_utterances = 0

    for j in range(len(usr_data['turns'])):

        sys_turn = sys_data['turns'][j]
        usr_turn = usr_data['turns'][j]
        # print(sys_turn['turn-index'])
        # print(usr_turn['turn-index'])
        sys_utts = nlp(sys_turn['output']['transcript'])
        print(sys_utts)
        usr_utts = nlp(usr_turn['transcription'])
        print(usr_utts)

        slots = dict()
        # Get the user slots for this turn
        for data in usr_turn['semantics']['json']:

            for slot in data['slots']:
                slots[slot[0]] = slot[1]
        print(slots)
        # Get systems utterances (it always starts)
        for sent in sys_utts.sents:

            utterance = dict()

            utterance['speaker'] = "SYS"
