import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    personA = record[0]
    personB = record[1]
    mr.emit_intermediate(personA, record)
    mr.emit_intermediate(personB, record)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    for value in list_of_values:
        personA = value[0]
        personB = value[1]
        count = 0
        for value2 in list_of_values:
            if value2[0] == personB and value2[1] == personA:
                count += 1
        if count == 0:
            if key == personA:
                mr.emit((key, personB))
            elif key == personB:
                mr.emit((key, personA))
            else:
                pass

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)