```python
# quantum.py

import qiskit
from qiskit import QuantumCircuit, transpile, assemble, Aer, execute
from qiskit.visualization import plot_bloch_multivector, plot_histogram
from qiskit.extensions import Initialize
from qiskit.ignis.verification import marginal_counts
from qiskit.quantum_info import random_statevector

from config import OPEN_API_KEY

# Set your API Token.
# You can get it from https://quantum-computing.ibm.com
qiskit.IBMQ.save_account(OPEN_API_KEY)

# Load Account and Choose Backend
provider = qiskit.IBMQ.load_account()
device = provider.get_backend('ibmq_qasm_simulator')

def create_quantum_circuit():
    # Create a Quantum Circuit
    qc = QuantumCircuit(2, 2)

    # Initialize the 0th qubit in state `psi` using a rotation
    qc.h(0)

    # Add a CX (CNOT) gate on control qubit 0 and target qubit 1
    qc.cx(0, 1)

    # Map the quantum measurement to the classical bits
    qc.measure([0,1], [0,1])

    return qc

def execute_quantum_circuit(qc):
    # Execute the circuit on the qasm simulator
    job = execute(qc, device, shots=1000)

    # Grab results from the job
    result = job.result()

    # Returns counts
    counts = result.get_counts(qc)
    print("\nTotal count for 00 and 11 are:",counts)

    return counts
```
