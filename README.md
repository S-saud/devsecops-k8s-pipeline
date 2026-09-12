# 🛡️ Zero-Trust DevSecOps & Kubernetes CI/CD Pipeline

A production-grade, automated **DevSecOps Pipeline** built with GitHub Actions that enforces security gates at every stage of the software development lifecycle (SDLC) before deploying workloads securely to a local Kubernetes cluster using Minikube.

---

## 🚀 Architecture & Workflow Flow

1. **Code Commit / Pull Request:** Triggers the automated GitHub Actions pipeline on the `main` branch.
2. **Security Linting (Hadolint):** Scans the `Dockerfile` for best practices and security misconfigurations.
3. **Container Build & Local Transfer:** Builds the Docker image locally and loads it securely into the Minikube cluster environment.
4. **Vulnerability Scanning (Trivy):** Deep-scans the container image for Common Vulnerabilities and Exposures (CVEs).
5. **Custom Security Gate (Python):** Evaluates scan thresholds via an automated script to pass or fail the build.
6. **Kubernetes Deployment & Self-Healing:** Automatically provisions manifests (`k8s/`), applies deployments with active Liveness and Readiness Probes, and verifies rollouts.

---

## 📂 Repository Structure

- `.github/workflows/devsecops-pipeline.yml` : Main automated CI/CD pipeline configuration
- `app/` : Application source code and secured `Dockerfile`
- `k8s/` : Kubernetes Deployment, Service, and Probes manifests
- `scripts/` : Custom Python-based security gate validation script
- `.hadolint.yaml` : Container linter configurations

---

## 🛠️ Tech Stack Used

- **CI/CD:** GitHub Actions
- **Containerization & Security:** Docker, Hadolint, Aqua Security Trivy, Cosign (Simulated)
- **Orchestration & Resilience:** Kubernetes (Minikube), Liveness/Readiness Probes
- **Validation:** Python Custom Security Gate