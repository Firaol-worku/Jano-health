# Jano Health — Full System Architecture

This architecture combines everything we discussed:

- MVP-first execution
- Enterprise scalability
- AI-ready infrastructure
- Healthcare compliance
- Microservices evolution path
- Multi-platform ecosystem

---

## 1. High-Level System Architecture

```text
                    ┌─────────────────────┐
                    │     Patients        │
                    └─────────┬───────────┘
                              │
                    ┌─────────▼───────────┐
                    │  Web & Mobile Apps  │
                    │ React / ReactNative │
                    └─────────┬───────────┘
                              │
                    ┌─────────▼───────────┐
                    │     API Gateway     │
                    │ Auth + Routing      │
                    └─────────┬───────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
┌───────▼────────┐ ┌──────────▼─────────┐ ┌────────▼────────┐
│ Auth Service   │ │ Clinical Services  │ │ Billing Service │
│ Users / Roles  │ │ EHR / Appointments │ │ Payments        │
└───────┬────────┘ └──────────┬─────────┘ └────────┬────────┘
        │                     │                    │
        └────────────┬────────┴───────────┬────────┘
                     │                    │
             ┌───────▼────────┐  ┌────────▼────────┐
             │ PostgreSQL DB  │  │ Redis / Queue   │
             └───────┬────────┘  └────────┬────────┘
                     │                    │
            ┌────────▼────────┐ ┌────────▼────────┐
            │ AI Services     │ │ NotificationSvc │
            │ LLM + RAG       │ │ SMS/Email/Push  │
            └─────────────────┘ └─────────────────┘
```

## 2. Repository Architecture

```text
jano/
├── docs/
│   ├── blueprint/
│   ├── technical/
│   ├── api/
│   ├── legal/
│   └── branding/
│
├── frontend/
│   ├── web/
│   └── admin/
│
├── backend/
│   ├── apps/
│   ├── common/
│   ├── integrations/
│   ├── config/
│   └── tests/
│
├── mobile/
│   ├── patient-app/
│   └── provider-app/
│
├── infrastructure/
│   ├── docker/
│   ├── kubernetes/
│   ├── nginx/
│   ├── terraform/
│   └── monitoring/
│
├── ai/
│   ├── rag/
│   ├── embeddings/
│   ├── prompts/
│   ├── models/
│   └── pipelines/
│
├── scripts/
├── .github/
├── docker-compose.yml
├── README.md
└── .env
```

## 3. Frontend Architecture

### Tech Stack

- React
- TypeScript
- Tailwind CSS
- React Query
- Zustand or Redux
- Axios
- React Router

### Frontend Structure

```text
frontend/web/src/
├── api/
├── assets/
├── auth/
├── components/
│   ├── ui/
│   ├── forms/
│   ├── charts/
│   └── layouts/
│
├── features/
│   ├── patients/
│   ├── appointments/
│   ├── ehr/
│   ├── billing/
│   └── dashboard/
│
├── hooks/
├── pages/
├── routes/
├── services/
├── store/
├── types/
├── utils/
└── main.tsx
```

## 4. Backend Architecture

### Tech Stack

- Django
- Django REST Framework
- PostgreSQL
- Redis
- Celery
- JWT
- Swagger/OpenAPI

## 5. Backend Structure

```text
backend/
├── apps/
│   ├── users/
│   ├── patients/
│   ├── appointments/
│   ├── ehr/
│   ├── pharmacy/
│   ├── laboratory/
│   ├── billing/
│   ├── telemedicine/
│   ├── analytics/
│   └── notifications/
│
├── common/
│   ├── permissions/
│   ├── middleware/
│   ├── pagination/
│   ├── exceptions/
│   ├── audit/
│   ├── logging/
│   └── utils/
│
├── integrations/
│   ├── chapa/
│   ├── telebirr/
│   ├── email/
│   ├── sms/
│   ├── fhir/
│   └── insurance/
│
├── config/
│   ├── settings/
│   │   ├── base.py
│   │   ├── development.py
│   │   ├── production.py
│   │   └── testing.py
│   │
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── tests/
```

## 6. Authentication Architecture

### Authentication Flow

```text
User Login
   │
   ▼
JWT Access Token
   │
   ▼
Refresh Token
   │
   ▼
RBAC Permission Check
   │
   ▼
Protected APIs
```

### User Roles

- Admin
- Doctor
- Nurse
- Receptionist
- Pharmacist
- Lab Technician
- Radiologist
- Patient

## 7. Database Architecture

### Primary Database

PostgreSQL

### Main Tables

```text
users
patients
appointments
medical_records
prescriptions
laboratory_tests
billing
payments
audit_logs
notifications
```

## 8. EHR Architecture

### Core Components

#### Patient Profile

- Demographics
- Insurance
- Allergies
- Medical history

#### Clinical Notes

- SOAP notes
- Diagnosis
- Prescriptions

#### Medical Records

- Lab results
- Imaging reports
- Visit history

## 9. AI Architecture

### AI Stack

- OpenAI APIs
- LangChain
- Vector Database
- RAG Pipeline
- Embeddings
- Fine-tuned healthcare prompts

### AI Services

#### AI Assistant

- Symptom guidance
- Appointment assistance
- Medication reminders

#### Clinical AI

- AI documentation
- Medical summarization
- Clinical suggestions

#### Analytics AI

- Predictive healthcare analytics
- Risk scoring
- Operational insights

## 10. AI Infrastructure

```text
User Query
    │
    ▼
API Gateway
    │
    ▼
AI Service
    │
 ┌──┴──────────────┐
 │                 │
 ▼                 ▼
LLM            Vector DB
(OpenAI)       (Embeddings)
 │                 │
 └──────┬──────────┘
        ▼
  Final Response
```

## 11. Telemedicine Architecture

### Components

- Video consultations
- Messaging
- Call scheduling
- E-prescriptions
- Consultation recording

### Technology

- WebRTC
- Socket.IO
- Redis Pub/Sub

## 12. Billing Architecture

### Payment Integrations

- Telebirr
- Chapa
- Stripe
- Bank APIs

### Billing Features

- Invoices
- Wallets
- Insurance claims
- Payment tracking

## 13. Notification System

### Channels

- SMS
- Email
- Push notifications
- In-app notifications

### Event Triggers

- Appointment reminders
- Prescription updates
- Lab results
- Billing alerts

## 14. Security Architecture

### Security Layers

#### Authentication

- JWT
- MFA
- Refresh token rotation

#### Data Protection

- AES-256 encryption
- TLS

#### Compliance

- HIPAA
- GDPR
- ISO 27001

#### Monitoring

- Audit logs
- Threat detection
- Access monitoring

## 15. DevOps Architecture

### Infrastructure

- Docker
- Kubernetes
- NGINX
- Terraform

### CI/CD

- GitHub Actions
- Automated testing
- Automated deployment

## 16. Cloud Architecture

### AWS Services

```text
Route53
CloudFront
Load Balancer
EKS/Kubernetes
RDS PostgreSQL
Redis
S3
CloudWatch
IAM
Secrets Manager
```

## 17. API Architecture

### Standards

- REST APIs
- OpenAPI/Swagger
- HL7 FHIR compatibility

### Future

- GraphQL gateway
- Event-driven APIs
- gRPC microservices

## 18. Scalability Strategy

### MVP Stage

Monolith:

- Django modular monolith

### Growth Stage

Split into services:

- Auth service
- EHR service
- Billing service
- AI service

### Enterprise Stage

Full microservices:

- Kubernetes orchestration
- Event-driven architecture
- Multi-region deployment

## 19. Monitoring Architecture

### Tools

- Prometheus
- Grafana
- ELK Stack
- Sentry

## 20. Testing Architecture

### Testing Layers

- Unit tests
- Integration tests
- API tests
- End-to-end tests
- Security testing

## 21. Git Strategy

### Branches

```text
main
develop
feature/*
hotfix/*
release/*
```

## 22. Docker Architecture

### Containers

```text
frontend
backend
postgres
redis
nginx
celery
worker
```

## 23. MVP Development Order

### Phase 1

- Auth
- Roles
- PostgreSQL
- Docker

### Phase 2

- Patients
- Appointments

### Phase 3

- Basic EHR
- Dashboard

### Phase 4

- Notifications
- Billing basics

## 24. Future Expansion

### Future Modules

- Insurance
- AI diagnosis support
- Wearables integration
- Remote monitoring
- National healthcare exchange
- Multi-country infrastructure

## 25. Long-Term Vision (2030)

Jano Health evolves into:

- Healthcare operating system for Africa
- AI healthcare infrastructure platform
- Digital health fintech ecosystem
- Interoperable healthcare network
- Global healthcare intelligence platform
