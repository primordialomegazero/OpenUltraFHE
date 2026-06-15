# OpenUltraFHE — φ-Bootstrapping FHE Engine

**OpenUltraFHE** is a post-quantum, self-bootstrapping Fully Homomorphic Encryption engine based on BFV. It integrates golden ratio (φ) noise management, Lyapunov stability, and NIST Level-5 post-quantum cryptography.

## 🔥 Key Features

| Feature | Description |
|---------|-------------|
| **φ-Noise Bootstrap** | Self-stabilizing noise with 40-bit divine anchor |
| **Lyapunov Stability** | Exponential noise decay with λ = -0.4812 |
| **PQC ML-KEM-1024** | NIST Level-5 post-quantum key encapsulation |
| **Serialization** | Save/load ciphertexts to/from files |
| **BFV FHE** | Full homomorphic encryption (addition) |

## 🚀 Quick Start

```bash
git clone https://github.com/primordialomegazero/OpenUltraFHE.git
cd OpenUltraFHE
make
./openultrafhe
📦 Dependencies
Microsoft SEAL 4.3

liboqs (for ML-KEM-1024)

OpenSSL (SHA-256)

C++17 compiler

📜 License
Apache 2.0

ΦΩ0 — I AM THAT I AM
