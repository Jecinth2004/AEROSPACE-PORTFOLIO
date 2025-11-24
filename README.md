# AEROSPACE-PORTFOLIO
Aerospace portfolio projects
```markdown
# aerospace-portfolio

A personal portfolio for aerospace-related projects: simulations, controls, MDAO, flight‑software experiments, and notes. This repository hosts clean, reproducible demonstrations you can share with recruiters or collaborators.

## Contents
- docs/            — design notes, architecture docs, and short reports  
- notebooks/       — Jupyter notebooks demonstrating simulations and analyses  
- projects/        — self-contained project folders (6DOF-sim, MDAO-case, PX4-experiments)  
- docker/          — Dockerfiles and compose files for demos  
- scripts/         — utility scripts for data processing and plotting

## Highlights
- 6-DOF flight dynamics simulator (Python + NumPy/SciPy) with PID and LQR controllers  
- Interactive Jupyter demo to trim and simulate maneuvers (uses ipywidgets or Streamlit)  
- Small MDAO example (OpenMDAO / SciPy optimize) demonstrating a simple wing sizing/weight tradeoff  
- PX4 SITL notes and a minimal change built and run in SITL (for flight-software familiarity)  

## Quick start (clone & run demo)
1. Clone the repo:
   ```bash
   git clone https://github.com/Jecinth2004/aerospace-portfolio.git
   cd aerospace-portfolio
   ```
2. Create and activate a Python venv (recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate    # macOS / Linux
   .venv\Scripts\activate       # Windows (PowerShell)
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Jupyter demo notebook:
   ```bash
   jupyter notebook notebooks/6DOF-sim.ipynb
   ```
   or run the Streamlit demo:
   ```bash
   streamlit run notebooks/6DOF_demo.py
   ```

## Docker (optional)
To run the simulator in Docker (example):
```bash
docker build -t aerospace-sim:0.1 -f docker/Dockerfile .
docker run --rm -p 8501:8501 aerospace-sim:0.1
# then open the demo at http://localhost:8501 (if using Streamlit)
```

## Project structure suggestions
Each project folder should include:
- README.md — short description, tools used, quickstart, and expected outputs
- requirements.txt or environment.yml
- tests/ — pytest tests for core functions
- demo.gif / demo.mp4 — short visual demo

## Development workflow
- Use feature branches: `git checkout -b feat/my-feature`
- Write tests and run `pytest` before creating a PR
- Use GitHub Actions to run tests and linting on push (CI folder contains workflows)

## Contributing
If you'd like to contribute, please:
1. Open an issue describing the change or enhancement.
2. Fork the repo, implement changes, add tests, and submit a PR.
3. Follow the project's code style (PEP8 for Python) and include a short description of what changed.

## License
This repository is intended as a personal portfolio. Add a license if you want others to reuse your code (MIT recommended). Example:
```text
MIT License
```

## Contact
Owner: Jecinth2004 — https://github.com/Jecinth2004  
LinkedIn: (add your LinkedIn URL)

---

Notes & next steps:
- Replace placeholder project folders with your actual notebooks and demos (start by adding `notebooks/6DOF-sim.ipynb`).  
- If you want, I can provide a starter requirements.txt, Dockerfile, and a scaffold notebook for the 6DOF simulator that you can paste into the repo.
```
