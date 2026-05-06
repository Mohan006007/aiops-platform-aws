# 🚀 AI-Driven Self-Healing AIOps Platform on AWS

Production-grade cloud-native AIOps platform built on AWS using Kubernetes (EKS), Prometheus, Grafana, Alertmanager, GitHub Actions, and AWS Lambda for automated monitoring, alerting, CI/CD, and self-healing remediation workflows.

---

# 📌 Project Overview

This project simulates a real-world AIOps/DevOps environment with:

- Kubernetes-based application deployment on Amazon EKS
- Real-time observability using Prometheus + Grafana
- Automated CI/CD pipeline with GitHub Actions
- Alert-driven incident response using Alertmanager
- AWS Lambda webhook integration for automated remediation
- Self-healing deployment rollback and recovery workflows

The platform demonstrates how modern SRE/DevOps systems can automatically detect, analyze, and respond to infrastructure and application failures in real time.

---

# 🏗️ Architecture

```text
GitHub Actions
        ↓
Docker Build & Push
        ↓
Amazon ECR
        ↓
Amazon EKS (Kubernetes)
        ↓
Prometheus Metrics Collection
        ↓
Alertmanager
        ↓
AWS Lambda Webhook
        ↓
Automated Remediation / Incident Response
