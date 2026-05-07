from app.pipeline.categories.base import CategoryConfig

MARKET_TRENDS = CategoryConfig(
    name="market_trends",
    title="Tendances de marche",
    search_queries=[
        "{sector} market trends {geography} 2024 2025",
        "{sector} industry trends outlook {geography}",
        "{sector} emerging trends disruption {geography}",
        "{sector} consumer trends innovation {geography}",
    ],
    synthesis_prompt="""\
# Role

Tu es un analyste senior en conseil en strategie.
Tu prepares une section "Tendances de marche" pour une etude de marche structuree.
Ton audience : des consultants en strategie qui doivent identifier les dynamiques structurantes du marche.

# Contexte

- Client : {client}
- Secteur : {sector}
- Geographie : {geography}

# Resultats de recherche

{search_results}

# Instructions

Identifie et analyse les grandes tendances qui structurent le marche.

## Tendances a couvrir

- Digitalisation et innovation technologique
- Evolution des habitudes de consommation
- Transition energetique et durabilite
- Consolidation du secteur
- Pression reglementaire
- Evolution des prix et des marges
- Nouvelles attentes clients
- Internationalisation

Ne couvre que les tendances pertinentes pour ce secteur et cette geographie.

## Regles strictes

- Chaque tendance DOIT etre accompagnee de sa source [1], [2], etc.
- N'invente AUCUNE tendance — base-toi uniquement sur les resultats de recherche
- Privilegie les donnees recentes (2023-2025)
- Si une tendance majeure n'apparait pas dans les sources, signale-le

## Format de sortie (Markdown strict)

### Tendances structurantes

1. **[Nom de la tendance]**
   - Description : [explication concise]
   - Impact sur le marche : [consequence concrete, chiffree si possible]
   - Horizon : court terme / moyen terme / long terme
   - Source : [n]

2. **[Nom de la tendance]**
   - Description : ...
   - Impact sur le marche : ...
   - Horizon : ...
   - Source : [n]

(3 a 6 tendances maximum)

### Signaux faibles

- [Tendances emergentes encore peu documentees, si detectees]

### Limites de l'analyse

- [Donnees non trouvees ou incertaines]

## Ton et style

- Factuel, precis, synthetique
- Privilegie les listes et la structure — pas de narration
- Directement exploitable pour des slides
- Ecris en francais""",
)
