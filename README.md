# 🏎️ RaceCraft NG

**Analyze. Understand. Dominate.**  
_A professional-grade motorsport analytics platform for amateur and semi-pro drivers to analyze and improve their performance using telemetry data and session insights._

---

## 📌 Vision

RaceCraft NG is built for passionate drivers who want to **unleash their full potential** on track.  
Whether you're karting at your local circuit or lapping the Nürburgring in a sim — RaceCraft NG gives you the **data-driven insights** to improve.

No noise. No guesswork. Just precision.

---

## ✨ Features

- 🔄 Upload & analyze real-world or sim racing sessions
- 📊 Interactive telemetry visualization
- 🏁 Lap time comparison and sector analysis
- 📈 Performance trends and consistency metrics
- 🛠️ Setup tracking and comparison
- 🔍 Granular telemetry analysis
- 🧠 AI-assisted insights (coming soon)
- 🔐 Privacy-focused architecture (only you can see your data)

---

## 🛠 Tech Stack

| Layer       | Stack                                      |
|-------------|--------------------------------------------|
| Frontend    | React, TypeScript, Vite, TailwindCSS, ShadCN UI |
| Backend     | Python, FastAPI, SQLAlchemy, Pydantic      |
| Database    | PostgreSQL (with TimescaleDB extension for time-series) |
| AI Engine   | OpenAI GPT-4 (planned)                     |
| Deployment  | Docker, Docker Compose                     |

---

## 🚀 Quick Start

### Prerequisites

- Docker & Docker Compose
- Node.js 18+
- Python 3.10+

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/RaceCraftNG.git
cd RaceCraftNG
```

### 2. Set up environment

```bash
# Copy example environment file
cp .env.example .env

# Start services
docker-compose -f infra/docker-compose.yml up -d
```

### 3. Set up backend

```bash
cd apps/backend
python -m venv .venv
.\\.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # macOS/Linux

pip install -r requirements.txt
alembic upgrade head
uvicorn src.main:app --reload
```

### 4. Set up frontend

```bash
cd ../frontend
npm install
npm run dev
```

Visit http://localhost:3000 to see the app in action! 🎉

---

## 🧪 Project Status

> **Status:** 🚧 In Development  
This is an early-stage project currently under active development. Expect breaking changes and rapid iteration.

---

## 📂 Project Structure

```
RaceCraftNG/
├── apps/
│   ├── frontend/       # React + TypeScript + Vite + Tailwind
│   └── backend/        # FastAPI + SQLAlchemy + PostgreSQL
└── infra/              # Docker, CI/CD, and infrastructure
```

### Frontend Structure
```
frontend/
├── src/
│   ├── components/     # Reusable UI components
│   ├── pages/          # Page components
│   ├── hooks/          # Custom React hooks
│   ├── styles/         # Global styles and themes
│   ├── utils/          # Utility functions
│   ├── api/            # API client and services
│   └── types/          # TypeScript type definitions
```

### Backend Structure
```
backend/
├── src/
│   ├── api/            # API routes and endpoints
│   ├── core/           # Core configuration and utilities
│   ├── models/         # Database models
│   ├── schemas/        # Pydantic models
│   ├── services/       # Business logic
│   └── utils/          # Helper functions
```

---

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Inspired by professional motorsport telemetry tools
- Built with the help of amazing open source projects
- Special thanks to all contributors and early testers
