# Curso Gen AI — UCEMA 2026

Material práctico del curso de Inteligencia Artificial Generativa. Cada clase tiene sus notebooks y casos de estudio.

## Requisitos

- Python 3.11+
- API key de OpenAI

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install openai ipykernel jupyter
```

Copiá el archivo de variables de entorno y completá tu API key:

```bash
cp .env.sample .env
# editá .env y poné tu OPENAI_API_KEY
```

## Estructura

```
clase_1/
  notebooks/   → Jupyter notebooks
  casos/       → Casos de estudio y datasets
```

## Uso

```bash
source .venv/bin/activate
jupyter notebook
```

## Variables de entorno

| Variable | Descripción |
|---|---|
| `OPENAI_API_KEY` | API key de OpenAI |
