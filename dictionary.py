###ICS 311 Assignment 2
###
###Authors: Evan Rau, Yuzuki Fujimoto

import bisect

###  Evan Rau
# For this assignment, we chose to use a python dictionary to implement the database, which itself is an implementation of a hash table.
# Hash tables are extremely efficient for single-entry lookups, and there are imports, such as bisect that allow you to sort entries in the database.
# In this context, bisect is using a kind of binary sort so that sorted order is maintained with each insertion into the list.
# See https://docs.python.org/3/library/bisect.html for full documentation on the bisect import
###

class HawaiianDictionary:
    def __init__(self):
        self.sayings = []

    ### find_index creates a list of keys from all of the sayings present in the dict. bisect.bisect_left performs a binary search on the sorted list of keys
    ### in order to find an index such that the list remains sorted alphabetically. It specifically returns the index for the leftmost occurance of 'saying'
    def find_index(self, saying):
        keys = [s['saying'] for s in self.sayings]
        index = bisect.bisect_left(keys, saying)
        return index
    
    def member(self, saying):
        index = self.find_index(saying)
        if index < len(self.sayings) and self.sayings[index]['saying'] == saying:
            return self.sayings[index]
        return "Saying not in Dictionary"
    
    def first(self):
        if self.sayings:            #returns first saying in dictionarty so long as there is at least 1 entry
            return self.sayings[0]
        return "Dictionary Empty"
    
    def last(self):
        if self.sayings:            #returns last saying in dictionarty so long as there is at least 1 entry
            return self.sayings[-1]
        return "Dictionary empty"
    
    def predecessor(self, saying):
        index = self.find_index(saying) #finds index for saying
        if index == -1: #saying is not in dict
            return "Saying not in dictionary"
        elif index > 0: #saying in dictionary with predecessor
            return self.sayings[index - 1]
        else: #saying in dictionary but no predecessor
            return "First entry in dictionary; no predecessor"

    def successor(self, saying):
        index = self.find_index(saying)
        if index == -1: #saying is not in dict
            return "Saying not in dictionary"
        elif index < len(self.sayings) - 1: #saying in dictionary with successor
            return self.sayings[index + 1]
        else: #saying in dictionary but no successor
            return "Last entry in dictionary; no successor"
    
    def insert(self, saying, translation, explanation_non_english, explanation_english):
        new_saying = { #sort components of new dictionary entry for insertion into list
            'saying': saying,
            'translation': translation,
            'explanation_non_english': explanation_non_english,
            'explanation_english': explanation_english
        }
        index = self.find_index(saying) #find sorted index for new entry
        if index < len(self.sayings) and self.sayings[index]['saying'] == saying:
            # Update existing saying
            self.sayings[index] = new_saying
        else:
            # Insert new saying
            self.sayings.insert(index, new_saying)

    def list_all_sayings(self):
        if not self.sayings:
            print("No sayings found in the dictionary.")
            return
        
        print("===== Hawaiian Sayings Dictionary =====")
        for index, saying in enumerate(self.sayings, start=1): #Iterate through dictionary
            print(f"   Saying: {saying['saying']}")
            print(f"   Translation: {saying['translation']}")
            print(f"   Explanation (Hawaiian): {saying['explanation_non_english']}")
            print(f"   Explanation (English): {saying['explanation_english']}")
            print()


      ### MeHua and WithWord programmed by Yuzuki Fujimoto
       ### @todo complete code with explanations
       # This function searches through all sayings in the dictionary and returns those containing the given non-English word.
       #It iterates through each saying and checks if the word is present in the saying field of each entry.
       # If a saying contains the word, it is added to the sayings_containing_word list, which is then returned.
       def MeHua(self, word):
               sayings_containing_word = []
               for saying in self.sayings:
                   if word in saying['saying']:
                       sayings_containing_word.append(saying)
               return sayings_containing_word
       #This function searches through all sayings in the dictionary and returns those containing the given English word in either the translation or the English explanation.
           def WithWord(self, word):
               sayings_containing_word = []
               for saying in self.sayings:
                   if word in saying['translation'] or word in saying['explanation_english']:
                       sayings_containing_word.append(saying)
               return sayings_containing_word


### Main code to prove functionality

db = HawaiianDictionary()

db.insert(
    saying="A‘ea‘e mōhala i luna o ke kukui.",
    translation="Whiteness unfolds on the kukui trees.",
    explanation_non_english="Hoʻohana ʻia e pili ana i ke kanaka hina hina, me ka hoʻohālikelike ʻana iā ia me ka lāʻau kukui mohala piha i nā pua keʻokeʻo",
    explanation_english="Used in reference to a person who grays, comparing him to a blooming kukui tree laden with white flowers."
)

db.insert(
    saying="E mālama i ka makua, he mea laha ‘ole; ‘o ke kāne he loa‘a i ka lā ho‘okahi.",
    translation="Take care of parents for they are choice; a husband can be found in a day.",
    explanation_non_english="Pono e mālama ʻia nā mākua, no ka mea, ke hala lākou, ʻaʻohe mea nāna e pani.",
    explanation_english="Parents should be cared for, for when they are gone, there are none to replace them."
)

db.insert(
    saying="I pa‘a i kona kupuna ‘a‘ole kākou e puka.",
    translation="Had our ancestress died in bearing our grandparent, we would not have come forth.",
    explanation_non_english="Ua ʻōlelo ʻia e hoʻomanaʻo i kekahi lālā o ka ʻohana e mahalo i ka laina kiʻekiʻe, no ka mea ua hele mai lākou ka mua.",
    explanation_english="Said to remind a member of the family to respect the senior line, because they came first."
)

db.insert(
    saying="Kālina ka pona, ‘a‘ohe hua o ka pu‘e, aia ka hua i ka lālā.",
    translation="The potato hill is bare of tubers for the plant no longer bears; it is the vines that are now bearing.",
    explanation_non_english="ʻAʻole hānau hou ka makuahine, akā ʻo kāna mau keiki.",
    explanation_english="The mother is no longer bearing, but her children are."
)

db.insert(
    saying="Ola ka inoa.",
    translation="The name lives.",
    explanation_non_english="Ua ʻōlelo ʻia ke hāʻawi ʻia ka inoa o kahi hoahānau aloha i make i kahi keiki.",
    explanation_english="Said when the name of a beloved deceased relative is given to a child."
)

db.insert(
    saying="Ola nā iwi.",
    translation="The bones live.",
    explanation_non_english="Wahi a kekahi ʻelemakule hanohano i mālama maikaʻi ʻia e kona ʻohana.",
    explanation_english="Said of a respected oldster who is well cared for by his family."
)

db.list_all_sayings()

### Out-of-order insert to prove alphabetical sorting is maintained

db.insert(
    saying="Ha‘a ka pelehū i ka haka; ha‘a ka ‘elemakule i ke ala; ha‘a ka luahine i ka hale.",
    translation="The turkey struts on the roost; the old man struts on the highway; the old woman struts in the house.",
    explanation_non_english="ʻAʻole i kaupalena ʻia nā wahi hōʻike i hoʻokahi wahi",
    explanation_english="Show places are not confined to a single locality."
)

db.list_all_sayings()

print(db.predecessor('Ola ka inoa.')) # Output should be 'Kālina ka pona, ‘a‘ohe hua o ka pu‘e, aia ka hua i ka lālā.'
print()
print(db.successor('Kālina ka pona, ‘a‘ohe hua o ka pu‘e, aia ka hua i ka lālā.')) # output should be 'Ola ka inoa.'
print()
print(db.first()) #output should be 'A‘ea‘e mōhala i luna o ke kukui.'
print()
print(db.last()) #output should be 'Ola nā iwi.'
print()
