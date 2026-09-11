# 🛡️ Zero-Trust DevSecOps Pipeline & Kubernetes Admission Control

A production-grade, zero-cost DevSecOps pipeline enforcing Supply Chain Security, Vulnerability Scanning, and Kubernetes Policy Enforcement using **Node.js** and **Python**.

---

## 🏗️ Architecture Flow

```text
  [ Code Push ] 
        │
        ▼
┌────────────────────────────────────────────────────────┐
│               GitHub Actions CI Pipeline               │
│                                                        │
│ 1. Hadolint (Dockerfile Security Linting)             │
│ 2. Docker Multi-Stage Build (Distroless Image)         │
│ 3. Trivy Scan (Vulnerability Report Generation)        │
│ 4. Python Gate Enforcement (Critical Vuln Policy)     │
│ 5. Cosign Image Signing (Sigstore Cryptography)        │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│              Kubernetes Admission Control              │
│                                                        │
│ • Minikube Cluster Deployment                          │
│ • Kyverno ClusterPolicy Enforcement                    │
│   └── Blocks unsigned / unauthorized container images  │
└───────────────────────────┬────────────────────────────┘
🛠️ Tech Stack & Tools
Programming Languages: JavaScript (Node.js 20), Python 3.10

Containerization: Docker (Multi-stage Distroless build)

Orchestration: Kubernetes (Minikube / Docker Desktop)

CI/CD Automation: GitHub Actions

Security & Governance Stack:

Hadolint: Dockerfile static analysis & linting.

Trivy: Container image vulnerability scanner.

Python Gate Enforcer: Custom automated script blocking builds with CRITICAL vulnerabilities.

Cosign: Cryptographic image signing & verification (Sigstore).

Kyverno: Kubernetes Admission Controller policy engine.

🚀 Key Features
Shift-Left Security: Identifies Dockerfile anti-patterns and image vulnerabilities early in the CI stage using Hadolint and Trivy.

Automated Quality Gate: A custom Python script parses Trivy JSON reports and automatically fails the workflow if any CRITICAL vulnerability is detected.

Supply Chain Integrity: Container images passing security checks are cryptographically signed using Cosign before deployment.

Zero-Trust Policy Enforcement: Kyverno runs as an Admission Controller on Kubernetes to block any unsigned or unverified images from running in the cluster.

💻 Local Setup & Execution Guide
1. Clone the Repository
Bash
git clone [https://github.com/S-saud/devsecops-k8s-pipeline.git](https://github.com/S-saud/devsecops-k8s-pipeline.git)
cd devsecops-k8s-pipeline
2. Generate Application Dependencies
Bash
cd app
npm install
cd ..
3. Start Minikube & Configure Environment
Bash
minikube start --driver=docker

# Connect local terminal to Minikube's Docker daemon (Windows CMD)
@FOR /f "tokens=*" %i IN ('minikube -p minikube docker-env --shell cmd') DO @%i
4. Build Image & Test Security Gate
Bash
docker build -t devsecops-app:latest ./app
echo {"Results": []} > trivy-results.json
python scripts/security_check.py
5. Deploy Admission Control & Application
Bash
# Install Kyverno Policy Engine
kubectl create -f [https://github.com/kyverno/kyverno/releases/download/v1.10.0/install.yaml](https://github.com/kyverno/kyverno/releases/download/v1.10.0/install.yaml)

# Apply Cluster Policy
kubectl apply -f policies/disallow-unsigned-images.yaml

# Deploy Microservice
kubectl apply -f k8s/deployment.yaml
📝 Verification
To verify that pods are running under Kyverno governance:

Bash
kubectl get pods

---

### Step 2: Changes Ko GitHub Par Push Karein

File save karne ke baad terminal me yeh 3 commands chalaayein:

```cmd
git add README.md
git commit -m "docs: add full architecture, tech stack, and setup guide to README"
git push