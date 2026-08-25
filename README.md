# SE-Labs-PES1UG24CS550\
PROBLEM STATEMENT #33 | Retail, E-Commerce & Finance
Micro-Lending & Peer Credit Risk Assessor
1. Problem Context & Overview
A peer-to-peer micro-finance platform calculating borrower risk scores using heuristic rules, generating
structured repayment schedules, and triggering automated default warnings.
Target Stakeholders / Actors: Borrower, Peer Lender
2. Sample Functional Requirement (FR) Guideline
Sample Requirement: FR-001 [Priority: High]
Description: The system shall compute borrower credit risk ratings based on debt-to-income ratio, repayment
history, and employment stability indicators.
Sample Acceptance Criteria: Pass: Risk tier (Low/Med/High) accurately assigned; Fail: Incomplete financial profile
generates credit approval.
3. Sample Non-Functional Requirement (NFR) Guideline
Sample Requirement: NFR-001 [Type: Performance & Security]
Description: Loan repayment transactions and EMI distribution must execute inside database ACID
transactions to prevent double-spending.
Sample Acceptance Criteria: Pass: Benchmarking tests confirm target latency and security standards under
simulated peak load.
