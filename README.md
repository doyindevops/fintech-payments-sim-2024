
# 💸 fintech-payments-sim-2024 – *AWS Serverless, CI/CD, Security, Real-World DevOps*
![CI/CD Pipeline](https://github.com/doyindevops/fintech-payments-sim-2024/actions/workflows/ci-cd.yml/badge.svg)


> **A true-to-life fintech payments API, fully serverless on AWS, built and shipped with CI/CD, real infrastructure-as-code, and shift-left security.
> This isn’t a demo. It’s the actual automation and reliability you’d expect from a cloud-native, production-grade system.**

---

## 🎯 Why I Built This & Why It Matters

I wanted to prove (to myself, to recruiters, to future teams) that I can own every part of the DevOps lifecycle—**not just code, but automation, security, troubleshooting, and real AWS infrastructure**.

This project simulates what a modern fintech system actually needs:

* *Everything in code* (no console clicking)
* *Real CI/CD, real monitoring*
* *Failures documented, not hidden*
* *Security and audit baked in, not bolted on*

**For recruiters:** This repo is proof I can ship, automate, secure, and support serious cloud software.

---

## ⚡️ Project Highlights

* **100% AWS Serverless** – Lambda, API Gateway, DynamoDB, S3, CloudFormation/SAM.
* **Push = Deploy** – GitHub Actions pipeline runs tests, deploys, and security scans automatically.
* **Security Baked In** – OWASP ZAP scan on every deploy (see screenshots—403 is a feature, not a bug).
* **Infra as Code** – All infra is reproducible and versioned.
* **Troubleshooting Shown** – Real AWS issues and errors included; you see what actually happens in production.

---

## 🏗️ Architecture

**Lambda (Python) ↔️ API Gateway ↔️ DynamoDB**
*All automated via SAM. Artifacts in S3. Monitoring with CloudWatch. Security in the CI/CD.*

---

## 📷 Screenshots & Walkthrough

**Every screenshot is shown in order (1–19) below, with clear explanations.**
Images are referenced as `./images/FILENAME.png`—just copy your images into the `images/` folder in your repo.

---

### 1. CI/CD Pipeline Overview

![CI/CD UI](images/CICD%20UI.png)
*Shows the whole GitHub Actions workflow with build-test, deploy, and security scan.*

---

### 2. CloudFormation Events

![CloudFormation Events](images/CLOUDFORMATION%20EVENTS.png)
*Proof of all AWS resource creations and status events.*

---

### 3. CloudFormation Stacks

![CloudFormation Stacks](images/CLOUFORMATION.png)
*All deployed stacks visible and trackable.*

---

### 4. CloudWatch Logging

![CloudWatch](images/cludwatch.png)
*Lambda logs are visible and searchable in CloudWatch for observability and debugging.*

---

### 5. Successful Deploy in CI/CD

![Deploy with SAM in CI](images/DEPLOY%20WITH%20SAM%20CICD%20SUCCESS.png)
*Deployment job completes; you see API endpoint outputs and stack info.*

---

### 6. DynamoDB Table

![DynamoDB Table](images/DYNAMODB.png)
*Table structure and status as provisioned for transactions.*

---

### 7. Lambda UI

![Lambda Function](images/lambda%20ui.png)
*Lambda payment handler function, as deployed in AWS.*

---

### 8. API Gateway Resource

![API Gateway](images/API%20GATEWAAY.png)
*API resource and endpoint for payments.*

---

### 9. API Gateway Stages

![API Gateway Stages](images/APIGATEWAY%20STAGES.png)
*Stage-level deployment, with live invoke URL.*

---

### 10. Build & Test Passing

![Build-Test Passing](images/BUILDTEST-CICD.png)
*Green check = tests pass before any deploy.*

---

### 11. SAM Build (Terminal Output)

![SAM Build 2](images/sam%20build%202.png)
*`sam build` shows Lambda and template packaged, ready to ship.*

---

### 12. SAM Build (Step View)

![SAM Build](images/SAM%20BUILD.png)
*Full build process with all resources and layers bundled.*

---

### 13. SAM Deploy (Guided)

![SAM Deploy Guided](images/sam-deploy-guided.png)
*Deploy parameters chosen step-by-step for reproducibility.*

---

### 14. Successful Transaction Output

![Successful Transaction](images/successful%20transaction.png)
*API call returns status and a unique transaction\_id.*

---

### 15. DynamoDB: Transaction Persisted

![DynamoDB Transaction Data](images/transaction%20data%20in%20DYNAMODB.png)
*You can see your API call resulted in a real DB write.*

---

### 16. OWASP ZAP Security Scan

![OWASP ZAP Scan](images/OWASP%20ZAP%20SCAN.png)
*Security scan as part of CI/CD.
403 error? That’s good—it means your API isn’t wide open to the world (API key required).*

---

### 17. Production API Output

![Prod Pay Output](images/PROD%20PAY%20OUTPUT.png)
*Shows real output (or error) from the deployed API in production.*

---

### 18. S3 Bucket: Deployed Templates

![S3 Templates](images/S3%20BUCKET%20TEMPLATES.png)
*SAM CLI manages all deployment artifacts for rollback, audit, and reproducibility.*

---

### 19. S3 Bucket: Artifact List

![S3 Bucket](images/S3%20BUCKET.png)
*Versioned artifacts in S3, fully managed by AWS SAM.*

---

## 💡 Troubleshooting & Lessons Learned

* **Stack in ROLLBACK\_COMPLETE:** Delete before redeploy or change the stack name in `sam deploy`.
* **Table Already Exists:** Use unique names or dynamic table names in your infra.
* **ZAP Scan 403:** Endpoint is secured (API key required). This is what you want for fintech APIs.
* **No Changes to Deploy:** All up to date. Edit the template or code to trigger a redeploy.

---

## 🏃‍♂️ How to Run This Project

1. **Clone repo, set AWS credentials.**
2. **Install Python, AWS CLI, AWS SAM CLI.**
3. **Run `sam build` and `sam deploy --guided`.**
4. **(Or) Use GitHub Actions for automated pipeline.**
5. **Run `pytest` for unit tests.**
6. **Check AWS for live API, Lambda, DynamoDB, S3, and logs.**

---

## 🤝 Connect

* [LinkedIn](https://www.linkedin.com/in/adedoyin-ekong/)
* [GitHub](https://github.com/doyindevops)

---

## 🏷️ Keywords

`#AWS #Serverless #DevOps #CI/CD #Fintech #Lambda #DynamoDB #APIGateway #SAM #OWASPZAP #Automation`

---

> ## This project is my proof:
> ## I don’t just write scripts—I deliver production automation, security, and results!!.🔥

