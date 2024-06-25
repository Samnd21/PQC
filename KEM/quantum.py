from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, depolarizing_error
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler, Session

# Create a Quantum Circuit for Kyber (simplified example)
kyber_circuit = QuantumCircuit(3)
kyber_circuit.h(0)
kyber_circuit.cx(0, 1)
kyber_circuit.cx(1, 2)
kyber_circuit.measure_all()

# Create a Quantum Circuit for RSA (simplified example)
rsa_circuit = QuantumCircuit(3)
rsa_circuit.h(0)
rsa_circuit.cx(0, 1)
rsa_circuit.cx(0, 2)
rsa_circuit.measure_all()

# Create a noise model with depolarizing error
noise_model = NoiseModel()
depolarizing_prob = 0.02
noise_model.add_all_qubit_quantum_error(depolarizing_error(depolarizing_prob, 1), ['u1', 'u2', 'u3'])
noise_model.add_all_qubit_quantum_error(depolarizing_error(depolarizing_prob, 2), ['cx'])

# Simulate Kyber Circuit
simulator = AerSimulator(noise_model = noise_model)
compiled_kyber = transpile(kyber_circuit, simulator)
result_kyber = simulator.run(compiled_kyber).result()
counts_kyber = result_kyber.get_counts()

# Simulate RSA Circuit
compiled_rsa = transpile(rsa_circuit, simulator)
result_rsa = simulator.run(compiled_rsa).result()
counts_rsa = result_rsa.get_counts()

print("Kyber simulation result:", counts_kyber)
print("RSA simulation result:", counts_rsa)




service = QiskitRuntimeService()

# Specify the backend
backend = service.backend("ibmq_qasm_simulator")

# Run Kyber circuit
with Session(service=service, backend=backend) as session:
    sampler = Sampler(session=session)
    job_kyber = sampler.run(circuits=kyber_circuit)
    result_kyber = job_kyber.result()

# Run RSA circuit
with Session(service=service, backend=backend) as session:
    sampler = Sampler(session=session)
    job_rsa = sampler.run(circuits=rsa_circuit)
    result_rsa = job_rsa.result()

print("Kyber on IBM Q:", result_kyber)
print("RSA on IBM Q:", result_rsa)
