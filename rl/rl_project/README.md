# 🚀 Reinforcement Learning Agent - GridWorld Exploration

This project is a step-by-step implementation of a **Reinforcement Learning
(RL) Agent** that learns to navigate a `GridWorld` environment. The agent is
trained using **Q-Learning**, and the entire project is containerized using
**Docker** and orchestrated with **Docker Compose**.

---

## 📌 **Project Structure**

```bash
rl_project/
│
├── environments/                    # Contains the environment logic (GridWorld)
│   ├── __init__.py
│   └── gridworld.py
│
├── agents/                          # Contains the agent logic (Q-Learning Agent)
│   ├── __init__.py
│   └── q_learning_agent.py
│
├── trainers/                        # Reserved for advanced training logic (Future)
│   ├── __init__.py
│   └── trainer.py
│
├── main.py                          # Main application loop for agent training
│
├── Dockerfile                       # Docker configuration for containerization
│
├── docker-compose.yml               # Docker Compose for multi-service orchestration
│
├── .dockerignore                    # Ignore unnecessary files during Docker build
│
└── Makefile                         # Task automation for Docker and execution
```

---

## ✅ **Key Concepts Implemented**

1. **GridWorld Environment (OOP Design):**
   - Agent moves through a grid to find the goal.
   - Actions: `UP`, `DOWN`, `LEFT`, `RIGHT`.
   - Rewards:
     - `+1` for reaching the goal.
     - `-1` for hitting a boundary.
     - `0` for regular movement.

2. **Q-Learning Agent:**
   - Learns state-action values (`Q-values`) through exploration.
   - Explores unknown paths and exploits known good paths.
   - Uses the Q-Learning update formula to adjust its strategy.

3. **Docker & Docker Compose:**
   - Full containerization for isolated, reproducible environments.
   - Docker Compose for easy multi-service orchestration.
   - Mounted volumes for real-time sync of code changes.

4. **Makefile for Easy Management:**
   - `make build` → Build the Docker image.
   - `make docker-run` → Run the agent inside Docker.
   - `make compose-up` → Launch with Docker Compose.
   - `make compose-down` → Stop the Docker Compose service.
   - `make clean` → Remove Python cache files.

---

## 🚀 **Quick Start**

1️⃣ **Build the Docker image:**

```bash
make build
```

2️⃣ **Run the application inside Docker:**

```bash
make docker-run
```

3️⃣ **Orchestrate with Docker Compose:**

```bash
make compose-up
```

4️⃣ **Stop the services:**

```bash
make compose-down
```

---

## 📌 **Next Steps (Planned)**

1. **Unit Testing:** Write tests for agent learning and environment step logic.
2. **Visualization:** Display agent paths and Q-values.
3. **Advanced Training:** Use trainers to enhance agent learning.
4. **Multi-agent support:** Expand to multi-agent systems in the same GridWorld.

---

## 👤 **Author**

- Developed by [SGTMcPass](https://github.com/SGTMcPass)

---

**Happy Reinforcement Learning!**
