# MarketMind — Product Requirements Document

## Vision

Outil d'automatisation d'études de marché pour consultants en stratégie. À partir de 3 variables (client, secteur, géographie), le système génère un rapport structuré, sourcé et exploitable.

---

## Utilisateurs cibles

Analystes et consultants en stratégie (type KPMG, Deloitte) qui préparent des études de marché pour des propositions commerciales.

---

## Variables d'entrée

| Variable | Description | Exemple |
|----------|-------------|---------|
| Client | Entreprise analysée | L'Oréal, Airbus |
| Secteur | Industrie / marché | Cosmétique, aéronautique |
| Géographie | Zone géographique | France, Europe, Monde |

---

## Catégories d'information générées

1. Taille du marché (valeur + volume)
2. Tendances de marché
3. Facteurs macroéconomiques
4. Entreprises du secteur (concurrents, parts de marché)
5. Segmentation du secteur
6. Acquisitions et cessions récentes (M&A)
7. Chiffres clés du client
8. Activités du client
9. Position du client dans la chaîne de valeur
10. Opérations stratégiques récentes du client
11. Enjeux futurs du client

---

## Décisions techniques

### Stack

| Composant | Choix |
|-----------|-------|
| Backend | Python + FastAPI |
| Frontend | Jinja2 + TailwindCSS + HTMX |
| LLM principal | Gemini 2.5 Flash (free tier) |
| LLM fallback | Mistral Small |
| Recherche web | Tavily (principal) + Serper (complément) |
| Vector store | ChromaDB |
| Embeddings | sentence-transformers ou Mistral embeddings |
| Format sortie | Markdown structuré |

### Architecture

- **Pipeline parallélisé** (asyncio) — les 11 catégories recherchées en parallèle
- **Interfaces profondes** : `search()` et `synthesize()` génériques, chaque catégorie = un fichier de config/prompt
- **Abstraction LLM** : wrapper commun, switch de modèle via config
- **Modulaire** : préparé pour migration multi-agents future

### Données

- **Recherche web temps réel** : templates de requêtes pré-définis par catégorie + passe agentic pour combler les trous
- **Base de connaissances** : ChromaDB, alimentée par upload (PDF/Word/Excel) + copier-coller texte/URLs
- **Score de confiance** : heuristique basé sur la fiabilité du domaine source + convergence multi-sources

### UX

- Pré-recherche de clarification si ambiguïté détectée (avant génération)
- Gestion explicite des informations non disponibles
- Mono-utilisateur, pas d'authentification

### Déploiement

- Développement en local
- Démo via cloud (Render/Railway) + Docker

---

## Interfaces clés (deep modules)

```python
# Point d'entrée principal — high leverage
async def generate_study(client: str, sector: str, geography: str) -> StudyReport

# Recherche unifiée — cache Tavily + Serper + RAG derrière une seule interface
async def search(query: str, category: str) -> list[SourcedResult]

# Synthèse par catégorie — données brutes → section structurée
async def synthesize(results: list[SourcedResult], category: str) -> ReportSection

# Pré-recherche de clarification
async def disambiguate(client: str, sector: str, geography: str) -> Clarification | None
```

---

## Plan de livraison (tranches verticales)

| # | Tranche | Vérifiable par |
|---|---------|----------------|
| 1 | Setup + Hello World | L'app démarre, formulaire affiché |
| 2 | Interfaces profondes + "Taille de marché" E2E | Requête → résultat affiché avec source |
| 3 | Tendances + Facteurs macro | 3 sections dans le rapport |
| 4 | Concurrents + Segmentation + M&A | 6 sections |
| 5 | Catégories client (chiffres, activités, chaîne de valeur, opérations, enjeux) | Rapport complet 11 sections |
| 6 | Score de confiance + gestion données manquantes | Badges de confiance visibles |
| 7 | Pré-recherche + clarification ambiguïtés | "Orange" → demande de précision |
| 8 | RAG : upload docs + utilisation dans pipeline | PDF uploadé apparaît dans résultats |
| 9 | Polish : parallélisation, loading states, export .md | Étude complète < 60s |

---

## Hors scope MVP

- Authentification / multi-utilisateurs
- Export PowerPoint automatique
- Architecture multi-agents
- Export PDF / Word
- SSO / gestion d'équipes
- Historique des recherches
