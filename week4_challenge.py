# Group Name : ALPHA

# Team members
# Ayush Gupta (202251025)
# Dhruv Sachdeva (202251040)
# Vedant Agawane (202251005)
# Hitarth Thakkar (202251056)


import random
# Define Raag Bhairav notes for Aroha and Avaroha
aroha = ['S', 'r', 'G', 'M', 'P', 'd', 'N', 'S\'']
avaroha = ['S\'', 'N', 'd', 'P', 'M', 'G', 'r', 'S']

# Define fundamental phrases (Pakad)
phrases = [
    ['N', 'r', 'S'],  # Ni ra Sa
    ['S', 'r', 'G'],  # Sa ra Ge
    ['P', 'M', 'G', 'r', 'S'],  # P M G r S
    ['d', 'N', 'S\'']  # dhi Ni Sa'
]

# Define the probability distribution for notes
note_probabilities = {
    'S': 0.1, 'r': 0.2, 'G': 0.15, 'M': 0.1, 'P': 0.1, 
    'd': 0.15, 'N': 0.1, 'S\'': 0.1
}

# Function to generate a random note based on probabilities
def choose_note():
    notes = list(note_probabilities.keys())
    probabilities = list(note_probabilities.values())
    return random.choices(notes, probabilities)[0]

# Generate a melody by combining fundamental phrases and random notes
def generate_melody(length=16):
    melody = []

    # Start with a phrase
    melody.extend(random.choice(phrases))
    
    # Generate the remaining melody
    while len(melody) < length:
        if random.random() < 0.3:  # 30% chance to add a pakad (phrase)
            melody.extend(random.choice(phrases))
        else:  # 70% chance to add a random note
            melody.append(choose_note())
    
    return melody

# Generate a 16-note melody
melody = generate_melody()
print("Generated a 16-note melody (Raag Bhairav):")
print(" - ".join(melody))






























# import random
# import math

# # Melody and cost function

# def generate_initial_melody(length, scale):
#     """Generate a random initial melody with notes from the given scale."""
#     return [(random.choice(scale), 1) for _ in range(length)]  # Random pitch, uniform duration

# def melody_cost(melody):
#     """Evaluate how pleasing the melody is (lower cost means better)."""
#     cost = 0
#     # Example: penalize large jumps between notes
#     for i in range(1, len(melody)):
#         cost += abs(melody[i][0] - melody[i-1][0])  # Penalize large intervals
#     return cost

# def generate_neighbor_melody(melody, scale):
#     """Generate a slightly different melody by modifying one note."""
#     new_melody = melody[:]
#     idx = random.randint(0, len(melody) - 1)  # Pick random note to modify
#     new_melody[idx] = (random.choice(scale), 1)  # Change pitch
#     return new_melody

# def simulated_annealing_melody(scale, melody_length=8, initial_temp=100, cooling_rate=0.95, min_temp=1):
#     current_melody = generate_initial_melody(melody_length, scale)
#     current_cost = melody_cost(current_melody)
#     temp = initial_temp

#     while temp > min_temp:
#         new_melody = generate_neighbor_melody(current_melody, scale)
#         new_cost = melody_cost(new_melody)
#         delta_cost = new_cost - current_cost
        
#         if delta_cost < 0 or random.random() < math.exp(-delta_cost / temp):
#             current_melody, current_cost = new_melody, new_cost

#         temp *= cooling_rate  # Decrease temperature
    
#     return current_melody

# # Example usage
# scale = [60, 62, 64, 65, 67, 69, 71]  # C major scale
# final_melody = simulated_annealing_melody(scale)
# print("Generated Melody:", final_melody)