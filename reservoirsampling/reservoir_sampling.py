import random

def reservoir_sampling_online(item, _id, samples, final_len):
    """
    Performs an online sampling. Given an item, the number item it
    is (1-based), and the desired final length of the final samples
    list, determines if it should be saved within a given array
    """
    if len(samples) < final_len:
        samples.append(item)

    pos = random.randrange(0, _id)
    if pos < final_len:
        samples[pos] = item

def reservoir_sampling_offline(items, num_samples):
    """
    Performs the sampling offline. Receives a list of all items
    to be sampled from (in order of arrival) and the number of
    samples to take. Returns a list of samples
    """
    if num_samples > len(items):
        return items[:]

    samples = []
    for i in range(num_samples):
        samples.append(items[i])

    for i in range(num_samples, len(items)):
        pos = random.randrange(0, i)
        # Probability you save an item: num_samples / len(items)
        # Probability you choose a specific position in samples: 1/num_samples
        # Probability to replace any item in samples becomes:
        #   1/num_samples * num_samples/len(items) = 1/len(items)
        if pos < num_samples:
            samples[pos] = items[i]

    return samples

def test_reservoir_sampling_offline():
    samples = reservoir_sampling_offline([1,2,3,4,5,6,7,8,9,10], 2)

def test_reservoir_sampling_online():
    samples = []
    for i in range(100):
        reservoir_sampling_online(i, i+1, samples, 25)

def main():
    test_reservoir_sampling_offline()
    test_reservoir_sampling_online()

if __name__ == '__main__':
    main()
