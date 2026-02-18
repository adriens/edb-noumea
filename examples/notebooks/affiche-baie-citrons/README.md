# Affiche Baie des Citrons

Ce projet génère une affiche PDF et JPEG pour la surveillance de la qualité des eaux de baignade de la Baie des Citrons à Nouméa.

## Prérequis

### Outils système

Installez les dépendances système suivantes sur Ubuntu/Debian :

```bash
# Outils de base
sudo apt-get update
sudo apt-get install -y r-base

# Dépendances LaTeX
sudo apt-get install -y texlive-xetex texlive-fonts-recommended texlive-latex-extra

# Bibliothèques de développement pour les packages R
sudo apt-get install -y \
  libfontconfig1-dev \
  libxml2-dev \
  libharfbuzz-dev \
  libfribidi-dev

# ImageMagick pour la conversion PDF vers JPEG
sudo apt-get install -y imagemagick
```

### Task (gestionnaire de tâches)

Installez [Task](https://taskfile.dev/) pour exécuter les tâches de build :

```bash
# Avec Go
go install github.com/go-task/task/v3/cmd/task@latest

# Ou avec Homebrew
brew install go-task/tap/go-task

# Ou téléchargement direct
sh -c "$(curl --location https://taskfile.dev/install.sh)" -- -d -b ~/.local/bin
```

### Packages R

Les packages R suivants sont requis et seront installés automatiquement lors de la première exécution :

- `rmarkdown` - Pour compiler les documents RMarkdown
- `kableExtra` - Pour les tableaux améliorés
- `systemfonts` - Gestion des polices système
- `textshaping` - Mise en forme du texte
- `svglite` - Export SVG
- `xml2` - Parsing XML

**Note :** Les packages R s'installent automatiquement dans `~/R/library` lors de l'exécution du document RMarkdown.

### Configuration R (optionnel)

Si vous rencontrez des problèmes avec les chemins de bibliothèques, vous pouvez créer un fichier `~/.Rprofile` :

```r
.libPaths(c("~/R/library", .libPaths()))
```

## Utilisation

### Générer l'affiche

Pour générer à la fois le PDF et le JPEG :

```bash
task
```

Ou explicitement :

```bash
task build-jpeg
```

### Générer uniquement le PDF

```bash
task build-pdf
```

### Nettoyer les fichiers générés

```bash
task clean
```

## Structure du projet

```
.
├── Taskfile.yml      # Définition des tâches de build
├── affiche.Rmd       # Document RMarkdown source
├── dist/             # Répertoire de sortie
│   ├── affiche.pdf   # PDF généré
│   └── affiche.jpg   # JPEG généré
└── README.md         # Ce fichier
```

## Détails techniques

- **Format de sortie** : A4 paysage
- **Moteur LaTeX** : XeLaTeX
- **Police** : DejaVu Sans
- **Résolution JPEG** : 300 DPI
- **Qualité JPEG** : 90%

## Source des données

Les données sont récupérées depuis :
```
https://raw.githubusercontent.com/adriens/edb-noumea-data/refs/heads/main/data/resume.csv
```

## Dépannage

### Erreur "cannot open shared object"

Si vous obtenez des erreurs de bibliothèques partagées, assurez-vous que toutes les dépendances système sont installées.

### Erreur "Undefined color"

Le document utilise les couleurs standard de xcolor (blue, red, yellow, gray). Assurez-vous que `texlive-latex-extra` est installé.

### Erreur avec convert (ImageMagick)

Si la conversion en JPEG échoue, vérifiez qu'ImageMagick est installé :

```bash
which convert
```
