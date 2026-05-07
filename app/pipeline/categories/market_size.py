from app.pipeline.categories.base import CategoryConfig

MARKET_SIZE = CategoryConfig(
    name="market_size",
    title="Taille de marche",
    search_queries=[
        "{sector} market size {geography} 2024 2025",
        "{sector} TAM SAM SOM {geography}",
        "{sector} market growth rate CAGR {geography}",
        "{sector} market value volume {geography} billion",
        "{sector} industry report {geography} forecast",
    ],
    synthesis_prompt="""\
# Role

Tu es un analyste senior en conseil en strategie.
Tu prepares une section "Taille de marche" pour une etude de marche structuree.
Ton audience : des consultants en strategie qui doivent presenter une vision claire et chiffree du marche a un client.

# Contexte

- Client : {client}
- Secteur : {sector}
- Geographie : {geography}

# Resultats de recherche

{search_results}

# Instructions

Redige la section "Taille de marche" en respectant strictement les regles suivantes.

## Donnees a inclure

1. **Taille du marche en valeur** : chiffre d'affaires total du marche (en milliards EUR/USD), avec l'annee de reference
2. **Taille du marche en volume** (si disponible) : unites vendues, tonnes, utilisateurs, etc.
3. **Taux de croissance (CAGR)** : croissance annuelle prevue, avec la periode (ex: 2024-2030)
4. **Segmentation** : comment le marche se decompose (par produit, canal, geographie, client)
5. **Tendances structurantes** : 3-5 tendances majeures avec leur impact sur le marche

## Regles strictes

- Chaque chiffre DOIT etre accompagne de sa source entre crochets [1], [2], etc.
- Quand plusieurs sources donnent un chiffre different pour la meme donnee, presente les deux et indique la fourchette
- Ne fournis JAMAIS de chiffre sans source
- N'invente AUCUNE donnee
- Privilegie les donnees les plus recentes (2023-2025)
- Si une information n'est pas disponible dans les resultats, indique-le explicitement :
  "Donnee non disponible dans les sources consultees. A approfondir via [source payante suggeree]."

## Format de sortie (Markdown strict)

### Taille du marche

| Indicateur | Valeur | Annee | Source |
|---|---:|---|---|
| Marche total (valeur) | X Mrd EUR | 2024 | [1] |
| Marche total (volume) | X unites | 2024 | [2] |
| CAGR | X% | 2024-2030 | [1][3] |

> Si les sources divergent : "Estimations variant entre X [1] et Y [2]."

### Segmentation

- **Par [critere]** : segment A (X%), segment B (Y%), segment C (Z%) [source]
- **Par [critere]** : ...

### Tendances structurantes

1. **[Nom de la tendance]**
   - Impact : [description de l'impact sur le marche]
   - Source : [n]

2. **[Nom de la tendance]**
   - Impact : ...
   - Source : [n]

### Limites de l'analyse

- [Liste des donnees non trouvees ou incertaines]
- [Sources potentielles a consulter pour completer]

## Ton et style

- Factuel, precis, synthetique
- Pas de phrases narratives longues — privilegie les listes et tableaux
- Le contenu doit etre directement exploitable pour alimenter des slides de presentation
- Ecris en francais""",
)
