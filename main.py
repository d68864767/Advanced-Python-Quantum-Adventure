```python
# main.py

from quantum_utils import create_quantum_circuit, apply_gate, run_circuit
from api_utils import get_quantum_data

def main():
    # Get quantum data from API
    quantum_data = get_quantum_data()

    if quantum_data is not None:
        # Create a quantum circuit with the number of qubits specified in the quantum data
        qc = create_quantum_circuit(quantum_data['num_qubits'])

        # Apply the gates specified in the quantum data to the quantum circuit
        for gate_data in quantum_data['gates']:
            apply_gate(qc, gate_data['gate'], gate_data['qubit'])

        # Run the quantum circuit and get the result
        result = run_circuit(qc)

        # Print the result
        print(result)
    else:
        print("No quantum data received.")

if __name__ == "__main__":
    main()
```
