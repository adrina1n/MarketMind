# MarketMind

Outil d'automatisation d'etudes de marche pour consultants en strategie.

A partir de trois variables — **client**, **secteur** et **geographie** — MarketMind recherche automatiquement des donnees sur le web, les synthetise via un LLM et genere un rapport structure, source et exploitable.

---

## Probleme

Les consultants en strategie passent des heures a preparer des etudes de marche pour leurs propositions commerciales. Le travail est repetitif : chercher des donnees sur la taille du marche, les tendances, les concurrents, le profil du client... a travers des dizaines de sources web, puis synthetiser le tout dans un document structure.

Ce processus manuel est lent, sujet aux oublis, et ne capitalise pas sur les recherches precedentes.

## Solution

MarketMind automatise la generation d'etudes de marche. L'utilisateur saisit trois variables et recoit un rapport complet en 5 sections, chacune accompagnee de ses sources.

### Les 5 sections du rapport

| Section | Contenu |
|---------|---------|
| **Taille de marche** | Valeur et volume du marche, CAGR, segmentation, tendances structurantes |
| **Environnement de marche** | Tendances sectorielles, facteurs macroeconomiques, operations M&A recentes |
| **Paysage concurrentiel** | Acteurs principaux, parts de marche, dynamique concurrentielle, positionnement du client |
| **Profil du client** | Chiffres cles, activites principales, position dans la chaine de valeur |
| **Strategie et enjeux** | Operations strategiques recentes, enjeux futurs du client |

### Principes

- Chaque chiffre est accompagne de sa source
- Les donnees manquantes sont explicitement signalees
- Le format est directement exploitable pour alimenter des slides de presentation
- L'ajout d'une nouvelle section au rapport ne necessite aucune modification du code existant

---

## Architecture

MarketMind fonctionne en trois etapes :

1. **Recherche** — Pour chaque section, plusieurs requetes sont envoyees en parallele a un moteur de recherche web (Tavily). Les resultats sont dedupliques.

2. **Synthese** — Les resultats de recherche sont transmis a un LLM (Gemini 2.5 Flash) avec un prompt expert adapte a la section. Le LLM redige une analyse structuree en Markdown avec des citations.

3. **Affichage** — Le Markdown est converti en HTML cote serveur et affiche dans le navigateur via HTMX, sans rechargement de page.

### Stack technique

- **Backend** : Python 3.13, FastAPI
- **Frontend** : Jinja2, TailwindCSS (CDN), HTMX
- **Recherche web** : Tavily (API REST)
- **LLM** : Google Gemini 2.5 Flash
- **Tests** : pytest, pytest-asyncio

---

## Installation

### Prerequis

- Python 3.13+
- Une cle API Gemini (gratuite sur [Google AI Studio](https://aistudio.google.com/apikey))
- Une cle API Tavily (gratuite sur [tavily.com](https://tavily.com), 1000 recherches/mois)

### Mise en place

```
git clone https://github.com/adrina1n/MarketMind.git
cd MarketMind
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r requirements.txt
```

Creer un fichier `.env` a la racine :

```
DEBUG=true
GEMINI_API_KEY=votre-cle-gemini
TAVILY_API_KEY=votre-cle-tavily
```

### Lancement

```
uvicorn app.main:app --reload
```

Ouvrir http://127.0.0.1:8000 dans le navigateur.

### Tests

```
pytest tests/ -v
```

---

## Roadmap

- [x] Setup projet + interface formulaire
- [x] Pipeline E2E avec premiere section (taille de marche)
- [x] 5 categories de rapport completes
- [ ] Score de confiance et gestion des donnees manquantes
- [ ] Pre-recherche et clarification des ambiguites
- [ ] RAG : base de connaissances avec upload de documents (ChromaDB)
- [ ] Polish : parallelisation, streaming, export PDF

---

## Licence

Projet prive.
