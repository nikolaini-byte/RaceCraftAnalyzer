# 🧭 RaceCraft NG Roadmap

_Last updated: July 30, 2025_  
This document serves as the master plan for RaceCraft NG development, organized by milestones and categories with clear status tracking.

## 🎯 Current Focus: MVP Development

### 🏗️ Core Infrastructure
| Task | Status | Priority | Dependencies |
|------|--------|----------|--------------|
| Frontend project setup | 🟢 Done | P0 | - |
| Backend API structure | 🟢 Done | P0 | - |
| Database schema design | 🟢 Done | P0 | Backend setup |
| **Authentication System** | **Status** | **Priority** | **Dependencies** |
| JWT Authentication Setup | 🔴 Open | P0 | - |
| - Configure JWT tokens | 🔴 Open | P0 | - |
| - Token refresh mechanism | 🔴 Open | P0 | JWT setup |
| User Registration | 🔴 Open | P0 | Database |
| - Registration endpoint | 🔴 Open | P0 | - |
| - Input validation | 🔴 Open | P0 | - |
| - Email uniqueness check | 🔴 Open | P0 | Database |
| User Login/Logout | 🔴 Open | P0 | JWT auth |
| - Login endpoint | 🔴 Open | P0 | - |
| - Logout/Token invalidation | 🔴 Open | P1 | JWT auth |
| Password Security | 🔴 Open | P0 | - |
| - Password hashing | 🔴 Open | P0 | - |
| - Password strength validation | 🔴 Open | P1 | - |
| - Password reset flow | 🔴 Open | P2 | Email service |
| Protected Routes | 🔴 Open | P0 | JWT auth |
| - Route protection middleware | 🔴 Open | P0 | - |
| - Role-based access control | 🔴 Open | P1 | - |
| File upload service | 🔴 Open | P1 | Backend API |

### 📊 Data Processing
| Task | Status | Priority | Dependencies |
|------|--------|----------|--------------|
| Telemetry data parser | 🔴 Open | P1 | File upload |
| Lap detection | 🔴 Open | P1 | Data parser |
| Sector time calculation | 🔴 Open | P2 | Lap detection |
| Basic metrics | 🔴 Open | P2 | Data parser |

### 🖥️ Frontend Development
| Task | Status | Priority | Dependencies |
|------|--------|----------|--------------|
| Session list view | 🟡 In Progress | P1 | API endpoints |
| Telemetry charts | 🔴 Open | P1 | Data processing |
| Track map | 🔴 Open | P2 | Telemetry data |
| Lap comparison | 🔴 Open | P2 | Session view |

---

## 📅 Upcoming Milestones

### 🚀 MVP Release (v0.1.0)
- [ ] Basic telemetry upload and storage
- [ ] Session list and details view
- [ ] Basic telemetry visualization
- [ ] Simple lap comparison
- [ ] User authentication

### 🎯 v0.2.0 - Enhanced Analysis
- [ ] Advanced metrics calculation
- [ ] Setup comparison
- [ ] Export functionality
- [ ] Mobile-responsive UI

### 🧠 v0.3.0 - AI Insights
- [ ] AI-powered lap analysis
- [ ] Driving style classification
- [ ] Setup recommendations
- [ ] Performance predictions

---

## 🔄 Development Workflow

### Priority Levels
- **P0**: Critical for MVP
- **P1**: Important features
- **P2**: Nice to have
- **P3**: Future enhancements

### Status Key
- 🟢 Done
- 🟡 In Progress
- 🔴 Not Started
- ⚠️ Blocked

---

## 🛠️ Technical Dependencies

1. **Frontend**
   - React + TypeScript
   - Vite
   - Tailwind CSS + ShadCN
   - Chart.js / D3.js

2. **Backend**
   - FastAPI
   - SQLAlchemy
   - PostgreSQL
   - Redis (caching)

3. **DevOps**
   - Docker
   - GitHub Actions
   - Sentry (error tracking)

---

## 📈 Progress Tracking

```
[===🟢======] 30% Complete
🟢 5 tasks done
🟡 3 in progress
🔴 12 not started
```

---

## 🤝 Contribution Guidelines

1. Check the current focus area
2. Pick an unassigned task
3. Create a feature branch
4. Submit a PR with tests
5. Get code review
6. Merge to main

## 📄 License

MIT License - See [LICENSE](LICENSE) for details.
