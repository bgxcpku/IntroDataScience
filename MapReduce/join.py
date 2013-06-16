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
    datatype = record[0]
    orderid = record[1]
    mr.emit_intermediate(orderid, record)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    first_part = None
    for value in list_of_values:
        if value[0] == 'order':
            first_part = value
    
    for value in list_of_values:
        if value[0] == 'line_item':
            mr.emit(first_part + value)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)