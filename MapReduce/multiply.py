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
    matrix = record[0]
    if matrix == 'a':
        i = record[1]
        j = record[2]
        value = record[3]
        for k in range(5):
            mr.emit_intermediate((i, k), (j, value))
    else:
        j = record[1]
        k = record[2]
        value = record[3]
        for i in range(5):
            mr.emit_intermediate((i, k), (j, value))

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    i = key[0]
    k = key[1]
    d_sum = {}
    for value in list_of_values:
        j = value[0]
        v1 = value[1]
        if j not in d_sum:
            d_sum[j] = [v1]
        else: 
            d_sum[j].append(v1)
    sum_total = 0
    print d_sum
    for j in d_sum:
        try:
            sum_total += d_sum[j][0]*d_sum[j][1]
        except IndexError:
            sum_total += 0
    mr.emit((i, k, sum_total))   

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)