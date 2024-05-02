import pickle
import sys

sys.path.append('/data/courses/2024/class_cse59836295spring2024_rsenana1/group2/aayush/roadscene2vec')
print(sys.path)

with open('/data/courses/2024/class_cse59836295spring2024_rsenana1/group2/aayush/roadscene2vec/pickle_dump/temp2.pkl', 'rb') as f:
    data = pickle.load(f)
    print(data)