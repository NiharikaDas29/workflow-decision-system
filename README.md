# Configurable Workflow Decision System

## Overview

This project implements a **Configurable Workflow Decision Platform** that processes incoming requests, evaluates configurable rules, executes workflow stages, maintains state, records audit logs, and handles failures and retries.

The system is designed to simulate real-world business workflows such as:

- Application approval workflow
- Claim processing workflow
- Employee onboarding workflow
- Vendor approval workflow
- Document verification workflow

The design emphasizes **modularity, configurability, explainability, and robustness** so that business rules can change without major code modifications.

# System Architecture

The system follows a **modular architecture** where each component has a specific responsibility.

### Components

1. **API Layer**
   - Accepts incoming structured requests
   - Validates inputs
   - Triggers workflow execution

2. **Workflow Engine**
   - Orchestrates workflow processing
   - Handles rule evaluation and decision making
   - Manages retry logic when dependencies fail

3. **Rule Engine**
   - Evaluates rules defined in configuration
   - Supports conditional decision logic

4. **State Manager**
   - Tracks lifecycle of each request
   - Ensures idempotency and prevents duplicate processing

5. **Audit Logger**
   - Records rule evaluation results
   - Provides traceability for decision explanations

6. **Dependency Service**
   - Simulates external service dependencies
   - Example: credit score API


# Architecture Diagram
  +-------------------+
                |       Client      |
                +---------+---------+
                          |
                          v
                +-------------------+
                |      API Layer    |
                |      (FastAPI)    |
                +---------+---------+
                          |
                          v
                +-------------------+
                |   Workflow Engine |
                +---------+---------+
                          |
        +-----------------+------------------+
        |                                    |
        v                                    v
+---------------+                     +---------------+
|  Rule Engine  |                     | Dependency    |
|               |                     | Service       |
| Evaluate      |                     | (Simulated)   |
| Config Rules  |                     +---------------+
+-------+-------+
        |
        v
+---------------+
|  Decision     |
| Approve /     |
| Reject /      |
| Retry /       |
| Manual Review |
+-------+-------+
        |
        v
+---------------+
| State Manager |
| Track Request |
| Lifecycle     |
+-------+-------+
        |
        v
+---------------+
|  Audit Logger |
| Rule Traces   |
+---------------+
---
# System Workflow
Client Request
↓
API Endpoint
↓
Workflow Engine
↓
External Dependency Check
↓
Rule Engine Evaluation
↓
Decision (Approve / Reject / Retry / Manual Review)
↓
State Storage
↓
Audit Logging

---
# Project Structure
workflow-decision-system/

main.py # API entry point
workflow_engine.py # Workflow orchestration logic
rule_engine.py # Rule evaluation logic
state_manager.py # Request state tracking
audit.py # Audit logging
dependency_service.py # External dependency simulation

configs/
workflow.json # Configurable workflow rules

README.md
---

---

# Configuration Model

The system allows workflows and rules to be modified through configuration files rather than changing application code.

Example configuration:

```json
{
  "workflow_name": "application_approval",
  "rules": [
    {
      "name": "income_check",
      "field": "income",
      "operator": ">=",
      "value": 30000,
      "on_fail": "reject"
    },
    {
      "name": "age_check",
      "field": "age",
      "operator": ">=",
      "value": 18,
      "on_fail": "manual_review"
    }
  ]
}

API Interface

The system exposes a REST API using FastAPI.

Endpoint
POST /process
Example Request
{
  "request_id": "123",
  "age": 25,
  "income": 40000
}
Example Response


