```python
# quantum_utils.py

import qiskit
from qiskit import QuantumCircuit, transpile, assemble, Aer, execute
from qiskit.visualization import plot_bloch_multivector, plot_histogram
from qiskit.extensions import Initialize
from qiskit.ignis.mitigation.measurement import (complete_meas_cal, CompleteMeasFitter)
from config import OPEN_API_KEY

# Set your API Key
qiskit.IBMQ.save_account(OPEN_API_KEY)

# Load your account
qiskit.IBMQ.load_account()

def create_quantum_circuit(num_qubits):
    """
    Function to create a quantum circuit with the specified number of qubits
    """
    qc = QuantumCircuit(num_qubits)
    return qc

def apply_gate(qc, gate, qubit):
    """
    Function to apply a gate to a specific qubit in a quantum circuit
    """
    if gate.lower() == 'h':
        qc.h(qubit)
    elif gate.lower() == 'x':
        qc.x(qubit)
    elif gate.lower() == 'y':
        qc.y(qubit)
    elif gate.lower() == 'z':
        qc.z(qubit)
    else:
        print("Invalid gate. Please enter 'h', 'x', 'y', or 'z'.")

def run_circuit(qc):
    """
    Function to run a quantum circuit and return the result
    """
    backend = Aer.get_backend('qasm_simulator')
    job = execute(qc, backend, shots=1000)
    result = job.result()
    counts = result.get_counts(qc)
    return counts
```
