# Import necessary libraries
from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
import matplotlib.pyplot as plt

def generate_quantum_random_numbers(num_bits=10):
    """Generates quantum random numbers using a quantum circuit."""
    # Create a quantum circuit with 'num_bits' qubits
    qc = QuantumCircuit(num_bits, num_bits)
    
    # Apply Hadamard gate to put qubits into superposition
    qc.h(range(num_bits))
    
    # Measure the qubits
    qc.measure(range(num_bits), range(num_bits))
    
    # Use the Qiskit AerSimulator
    simulator = Aer.get_backend('aer_simulator')  # Correct backend
    transpiled_qc = transpile(qc, simulator)
    
    # Run the circuit directly without using assemble()
    result = simulator.run(transpiled_qc).result()
    
    # Get the measurement results
    counts = result.get_counts()
    
    # Convert results into a list of random binary numbers
    random_numbers = [int(key, 2) for key in counts.keys()]
    
    return random_numbers, counts

def plot_results(counts):
    """Plots the quantum random number distribution."""
    plt.bar(counts.keys(), counts.values(), color='royalblue')
    plt.xlabel('Quantum Random Numbers')
    plt.ylabel('Frequency')
    plt.title('Quantum Random Number Distribution')
    plt.show()

# Run the quantum random number generator
if __name__ == "__main__":
    num_bits = 10  # Number of quantum bits
    random_numbers, counts = generate_quantum_random_numbers(num_bits)
    
    print(f"Generated Quantum Random Numbers: {random_numbers}")
    plot_results(counts)
