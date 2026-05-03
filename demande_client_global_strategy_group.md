# Compréhension détaillée de la demande client  
## Projet : Automatisation des études de marché pour KPMG Global Strategy Group

---

## 1. Contexte client

**Global Strategy Group (GSG)** est l’entité de KPMG dédiée au conseil en stratégie.

Ses missions incluent notamment :

- la réalisation d’études de marché ;
- l’accompagnement des clients dans leurs décisions d’investissement ;
- la préparation de propositions commerciales ;
- l’analyse des enjeux sectoriels, géographiques et concurrentiels.

Les clients accompagnés peuvent appartenir à **tous types de secteurs** et être présents dans **toutes les géographies**.

Dans le cadre des propositions commerciales, KPMG doit être capable de présenter une **vision d’ensemble du marché du client** afin de démontrer :

- une bonne compréhension du marché ;
- une bonne compréhension des enjeux du client ;
- une capacité à identifier les tendances susceptibles de l’impacter ;
- une capacité à structurer rapidement des informations fiables et exploitables.

---

## 2. Problème identifié

Les études de marché suivent généralement une structure similaire.

Les consultants recherchent souvent les mêmes types d’informations, en les adaptant à trois variables principales :

1. **Le nom du client**
2. **L’industrie / le secteur**
3. **La géographie**

Cette répétitivité rend possible une **automatisation partielle ou quasi complète** de la recherche et de la structuration des informations.

Les informations recherchées sont de deux types :

- **quantitatives** : chiffres, tailles de marché, revenus, volumes, parts de marché, données macroéconomiques, etc.
- **qualitatives** : tendances, analyse sectorielle, positionnement, enjeux stratégiques, segmentation, opérations récentes, etc.

---

## 3. Objectif de la mission

L’objectif est de construire un modèle capable de :

- effectuer automatiquement des recherches sur des éléments pré-définis ;
- adapter ces recherches selon les variables d’entrée ;
- récupérer des informations quantitatives et qualitatives ;
- structurer les résultats de manière claire ;
- fournir des sources fiables, récentes et croisées ;
- alimenter presque automatiquement un support de présentation pré-défini.

Le modèle doit donc agir comme un outil d’aide à la production d’études de marché pour des consultants en stratégie.

---

## 4. Variables d’entrée

Le modèle doit fonctionner à partir de trois variables principales.

| Variable | Description | Exemple |
|---|---|---|
| Nom du client | Entreprise ou cible analysée | L’Oréal, Airbus, Schneider Electric |
| Industrie / secteur | Marché ou secteur d’activité à analyser | Cosmétique, aéronautique, énergie |
| Géographie | Zone géographique pertinente | France, Europe, Amérique du Nord, monde |

Ces variables doivent permettre au modèle d’adapter ses recherches et ses résultats.

---

## 5. Informations à rechercher

Le modèle doit rechercher plusieurs catégories d’informations.

### 5.1 Taille du marché

Le modèle doit identifier la taille du marché concerné.

La taille de marché peut être exprimée :

- en valeur : chiffre d’affaires, revenus, milliards d’euros, dollars, etc.
- en volume : nombre d’unités vendues, tonnes produites, utilisateurs, clients, etc.

Exemple attendu :

> Le marché européen de X est estimé à 20 milliards d’euros en 2024.

---

### 5.2 Tendances de marché

Le modèle doit identifier les grandes tendances qui structurent le marché.

Exemples :

- digitalisation ;
- transition énergétique ;
- consolidation du secteur ;
- évolution des habitudes de consommation ;
- innovation technologique ;
- pression réglementaire ;
- évolution des prix ;
- nouvelles attentes clients.

---

### 5.3 Facteurs macroéconomiques

Le modèle doit identifier les facteurs macroéconomiques susceptibles d’impacter le secteur.

Exemples :

- inflation ;
- taux d’intérêt ;
- croissance du PIB ;
- évolution du pouvoir d’achat ;
- prix des matières premières ;
- taux de change ;
- réglementation ;
- tensions géopolitiques ;
- politiques publiques.

---

### 5.4 Entreprises du secteur

Le modèle doit identifier les principales entreprises présentes sur le marché.

À rechercher :

- leaders du marché ;
- concurrents directs ;
- challengers ;
- nouveaux entrants ;
- acteurs locaux ou internationaux ;
- parts de marché si disponibles.

---

### 5.5 Segmentation du secteur

Le modèle doit expliquer comment le secteur est structuré.

La segmentation peut être faite selon :

- la taille des clients ;
- les secteurs clients ;
- les besoins clients ;
- les gammes de produits ;
- les canaux de distribution ;
- les zones géographiques ;
- les types d’offres ;
- les profils d’utilisateurs.

---

### 5.6 Acquisitions et cessions récentes

Le modèle doit identifier les opérations récentes réalisées dans le secteur.

À rechercher :

- acquisitions ;
- cessions ;
- fusions ;
- prises de participation ;
- levées de fonds ;
- partenariats stratégiques ;
- opérations de consolidation.

---

### 5.7 Chiffres clés du client

Le modèle doit collecter les chiffres importants concernant l’entreprise analysée.

Exemples :

- chiffre d’affaires total ;
- chiffre d’affaires par géographie ;
- chiffre d’affaires par branche d’activité ;
- croissance récente ;
- marge opérationnelle ;
- effectifs ;
- nombre de clients ;
- implantation géographique ;
- principaux produits ou services.

---

### 5.8 Activités du client

Le modèle doit décrire les activités principales du client.

À préciser :

- ce que fait l’entreprise ;
- ses produits ou services principaux ;
- ses segments de clientèle ;
- ses zones d’activité ;
- son modèle économique ;
- ses principales sources de revenus.

---

### 5.9 Position du client dans la chaîne de valeur

Le modèle doit expliquer où se situe le client dans la chaîne de valeur globale du marché.

Exemples de positionnement :

- fournisseur de matières premières ;
- fabricant ;
- distributeur ;
- plateforme ;
- intégrateur ;
- prestataire de services ;
- client final ;
- intermédiaire.

L’objectif est de comprendre le rôle du client dans l’écosystème global.

---

### 5.10 Opérations stratégiques récentes du client

Le modèle doit identifier les actions stratégiques récentes menées par le client.

Exemples :

- acquisition ;
- partenariat ;
- lancement de produit ;
- ouverture de marché ;
- restructuration ;
- cession d’activité ;
- investissement industriel ;
- innovation technologique ;
- expansion internationale.

---

### 5.11 Enjeux futurs du client

Le modèle doit identifier les principaux enjeux du client pour les années à venir.

Exemples :

- croissance ;
- rentabilité ;
- concurrence ;
- innovation ;
- réglementation ;
- internationalisation ;
- digitalisation ;
- transition environnementale ;
- pression sur les coûts ;
- évolution de la demande ;
- consolidation du marché.

---

## 6. Format attendu des résultats

Les résultats doivent être fournis de manière **structurée**, afin de pouvoir alimenter presque automatiquement un support de présentation prédéfini.

Le format doit donc être :

- clair ;
- hiérarchisé ;
- exploitable par un consultant ;
- facilement transformable en slides ;
- sourcé ;
- synthétique mais suffisamment précis.

Format recommandé :

```markdown
## Synthèse marché

### Taille de marché
- Donnée principale :
- Année :
- Géographie :
- Source :
- Niveau de confiance :

### Tendances clés
1. Tendance 1
   - Explication :
   - Impact :
   - Source :

2. Tendance 2
   - Explication :
   - Impact :
   - Source :

### Facteurs macroéconomiques
- Facteur :
- Impact potentiel :
- Source :

### Principaux acteurs
| Entreprise | Positionnement | Géographie | Source |
|---|---|---|---|

### Segmentation
- Segment 1 :
- Segment 2 :
- Segment 3 :

### M&A / opérations récentes
| Date | Entreprise | Type d’opération | Montant si disponible | Source |
|---|---|---|---|---|

## Analyse client

### Chiffres clés
| Indicateur | Valeur | Année | Source |
|---|---:|---|---|

### Activités
- Description :

### Position dans la chaîne de valeur
- Position :
- Rôle dans l’écosystème :

### Opérations stratégiques récentes
- Opération :
- Date :
- Objectif stratégique :
- Source :

### Enjeux futurs
1. Enjeu 1
2. Enjeu 2
3. Enjeu 3
```

---

## 7. Exigences sur les sources

Les résultats doivent indiquer précisément les sources utilisées.

Les sources doivent être :

- fiables ;
- récentes ;
- croisées ;
- explicitement citées ;
- idéalement publiques ou accessibles.

Le modèle ne doit pas se contenter d’une seule source lorsqu’une information importante est fournie.

Il doit idéalement comparer plusieurs sources pour confirmer :

- les chiffres de marché ;
- les tendances ;
- les opérations récentes ;
- les chiffres clés du client ;
- les informations financières ;
- les données macroéconomiques.

---

## 8. Gestion des informations indisponibles

Si certaines informations ne peuvent pas être collectées, le modèle doit le signaler clairement.

Cas possibles :

- information non disponible publiquement ;
- information uniquement disponible dans une base payante ;
- information trop ancienne ;
- sources contradictoires ;
- données partielles ;
- absence de données fiables ;
- marché trop niche ;
- entreprise privée ne publiant pas ses chiffres.

Le modèle doit éviter d’inventer des chiffres ou des analyses non sourcées.

Format recommandé :

```markdown
Information non trouvée / non disponible publiquement.
Sources consultées :
- Source 1
- Source 2
Hypothèse possible :
- ...
Niveau de confiance : faible
```

---

## 9. Gestion des ambiguïtés

Le modèle doit être capable d’identifier les situations ambiguës et de demander des précisions.

Exemples de cas ambigus :

- deux sociétés portent le même nom ;
- le nom du client est incomplet ;
- le secteur n’est pas clairement défini ;
- la géographie est trop large ou imprécise ;
- plusieurs marchés proches peuvent correspondre à la demande ;
- le client appartient à plusieurs secteurs ;
- la cible est une filiale et non un groupe indépendant.

Dans ce cas, le modèle doit demander une clarification avant de produire une analyse complète.

Exemple :

```markdown
Plusieurs entreprises correspondent au nom indiqué :
1. Société A — secteur X — pays Y
2. Société B — secteur Z — pays W

Pouvez-vous préciser laquelle doit être analysée ?
```

---

## 10. Ce que le modèle doit éviter

Le modèle ne doit pas :

- inventer des données ;
- fournir des chiffres sans source ;
- utiliser uniquement des sources anciennes ;
- ignorer les contradictions entre sources ;
- confondre deux entreprises homonymes ;
- confondre le client avec un concurrent ;
- produire une réponse trop narrative et difficile à convertir en slides ;
- fournir une analyse sans distinguer marché, client, concurrence et macroéconomie ;
- oublier d’indiquer les limites de l’analyse.

---

## 11. Résultat final attendu

Le livrable attendu est un outil ou modèle capable de générer automatiquement une première version structurée d’étude de marché à partir de trois variables :

```text
Client + Industrie + Géographie
```

Le résultat doit permettre à un consultant de gagner du temps sur :

- la recherche documentaire ;
- la collecte de données ;
- la structuration de l’analyse ;
- la préparation de slides ;
- l’identification des sources utiles ;
- la mise en évidence des points à approfondir.

L’outil doit produire une base de travail fiable, sourcée et exploitable, mais ne remplace pas nécessairement la validation finale du consultant.

---

## 12. Reformulation synthétique de la demande

KPMG Global Strategy Group souhaite automatiser la production d’études de marché utilisées dans ses propositions commerciales et missions de conseil en stratégie.

Le modèle devra, à partir du nom d’un client, d’un secteur et d’une géographie, rechercher et structurer les informations clés sur :

- le marché ;
- les tendances ;
- la macroéconomie ;
- les concurrents ;
- la segmentation ;
- les opérations récentes ;
- les chiffres clés du client ;
- son positionnement dans la chaîne de valeur ;
- ses initiatives stratégiques ;
- ses enjeux futurs.

Les résultats devront être directement exploitables pour alimenter un support de présentation, avec des sources fiables, récentes et croisées, ainsi qu’une gestion explicite des incertitudes, des données manquantes et des ambiguïtés.

---

## 13. Points clés pour la conception de la solution

Pour répondre correctement à cette demande, la solution devra intégrer :

- un système de recherche multi-sources ;
- une logique de vérification croisée ;
- une structuration automatique des résultats ;
- une extraction de données quantitatives ;
- une synthèse qualitative ;
- une gestion des cas ambigus ;
- une indication du niveau de confiance ;
- une capacité à signaler les informations manquantes ;
- une sortie compatible avec un modèle de slide ou de rapport.

---

## 14. Résumé en une phrase

Construire un outil capable de transformer une demande du type **“analyser tel client, dans tel secteur, sur telle géographie”** en une étude de marché structurée, sourcée, récente et directement exploitable par un consultant en stratégie.
