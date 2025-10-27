from collections import defaultdict

text = "HDFS is a storage unit of Hadoop Mapreduce is a processing tool of Hadoop"

def mapper(text):
    mapped = []
    for line in text.strip().split("\n"):
        for word in line.strip().split():
            mapped.append((word.lower(), 1))
    return mapped

def shuffle_and_sort(mapped):
    grouped = defaultdict(list)
    for word, count in mapped:
        grouped[word].append(count)
    return grouped

def reducer(grouped):
    reduced = {}
    for word, counts in grouped.items():
        reduced[word] = sum(counts)
    return reduced

# Map step
mapped_data = mapper(text)

# Shuffle and sort step
grouped_data = shuffle_and_sort(mapped_data)

# Reduce step
reduced_data = reducer(grouped_data)

# Output
print("Word count output is:\n")
for word, count in sorted(reduced_data.items()):
    print(f"{word}\t{count}")



python wordcount.py input.txt

HADOOP  2
MAPREDUCE       1
EXAMPLE 2