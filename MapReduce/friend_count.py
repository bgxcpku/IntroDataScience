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
    mr.emit_intermediate(personA, personB)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    mr.emit((key, len(list(set(list_of_values)))))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)