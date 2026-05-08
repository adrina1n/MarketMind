from app.pipeline.categories.base import CategoryConfig

CLIENT_STRATEGY = CategoryConfig(
    name="client_strategy",
    title="Strategie et enjeux du client",
    search_queries=[
        "{client} strategic initiatives 2024 2025",
        "{client} acquisitions partnerships investments recent",
        "{client} challenges risks outlook {sector}",
        "{client} strategy growth plan {sector}",
        "{client} future challenges opportunities {sector} {geography}",
    ],
    synthesis_prompt="""\
# Role

Tu es un analyste senior en conseil en strategie.
Tu prepares une section "Strategie et enjeux du client" pour une etude de marche structuree.
Ton audience : des consultants en strategie qui doivent identifier les priorites strategiques et les defis du client.

# Contexte

- Client : {client}
- Secteur : {sector}
- Geographie : {geography}

# Resultats de recherche

{search_results}

# Instructions

Redige la section "Strategie et enjeux" couvrant deux volets : les operations strategiques recentes et les enjeux futurs du client.

## Donnees a inclure

### Operations strategiques recentes
- Acquisitions, cessions, partenariats
- Lancements de produits, ouvertures de marche
- Restructurations, investissements industriels
- Innovations technologiques, expansion internationale
- Pour chaque operation : date, description, objectif strategique

### Enjeux futurs
- Les 5-7 principaux defis du client pour les annees a venir :
  croissance, rentabilite, concurrence, innovation, reglementation,
  internationalisation, digitalisation, transition environnementale,
  pression sur les couts, evolution de la demande, consolidation du marche
- Pour chaque enjeu : pourquoi c'est un enjeu et quel est l'impact potentiel

## Regles strictes

- Chaque fait DOIT etre accompagne de sa source entre crochets [1], [2], etc.
- Ne fournis JAMAIS d'information sans source
- N'invente AUCUNE donnee
- Distingue clairement les faits des analyses/hypotheses
- Privilegie les donnees recentes (2023-2025)
- Si une information n'est pas disponible : "Donnee non disponible dans les sources consultees."
- Si les sources se contredisent, presente les differentes valeurs avec leurs sources respectives

## Format de sortie (Markdown strict)

### Operations strategiques recentes

| Date | Operation | Type | Objectif strategique | Source |
|---|---|---|---|---|
| ... | ... | Acquisition / Partenariat / Lancement / ... | ... | [n] |

### Enjeux futurs

1. **[Enjeu]**
   - Contexte : pourquoi c'est un enjeu pour {client}
   - Impact potentiel : ...
   - Source : [n]

2. **[Enjeu]**
   - Contexte : ...
   - Impact potentiel : ...
   - Source : [n]

### Limites de l'analyse

- [Donnees non trouvees ou incertaines]

## Ton et style

- Factuel, precis, synthetique
- Privilegie les tableaux et listes structurees
- Contenu directement exploitable pour des slides
- Ecris en francais""",
)
