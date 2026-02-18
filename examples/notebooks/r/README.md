# Rapport R Markdown - Qualité des Eaux de Baignade à Nouméa

Ce répertoire contient un rapport R Markdown permettant de générer des rapports d'analyse de la qualité des eaux de baignade à Nouméa à partir de données DuckDB.

## 📋 Prérequis

### Logiciels requis

1. **R** (version 4.0 ou supérieure)
   ```bash
   # Ubuntu/Debian
   sudo apt-get install r-base r-base-dev
   
   # macOS avec Homebrew
   brew install r
   ```

2. **Task** - Task runner moderne
   ```bash
   # Ubuntu/Debian
   sh -c "$(curl --location https://taskfile.dev/install.sh)" -- -d -b /usr/local/bin
   
   # macOS avec Homebrew
   brew install go-task/tap/go-task
   ```

3. **Pandoc** - Convertisseur de documents universel
   ```bash
   # Ubuntu/Debian
   sudo apt-get install pandoc
   
   # macOS avec Homebrew
   brew install pandoc
   ```

4. **XeLaTeX** - Moteur LaTeX pour génération PDF (via TeX Live)
   ```bash
   # Ubuntu/Debian
   sudo apt-get install texlive-xetex texlive-fonts-recommended texlive-latex-extra
   
   # macOS avec Homebrew
   brew install --cask mactex
   ```

5. **Poppler** - Pour conversion PDF vers JPEG (optionnel)
   ```bash
   # Ubuntu/Debian
   sudo apt-get install poppler-utils
   
   # macOS avec Homebrew
   brew install poppler
   ```

6. **Kaggle CLI** - Pour télécharger les données (optionnel)
   ```bash
   pip install kaggle
   # Configurez ensuite vos credentials Kaggle dans ~/.kaggle/kaggle.json
   ```

### Packages R requis

Installez les packages R nécessaires :

```r
# Dans une console R
install.packages("rmarkdown")
install.packages("knitr")
install.packages("duckdb")
install.packages("DBI")
install.packages("dplyr")
install.packages("ggplot2")
install.packages("kableExtra")
```

Ou en ligne de commande :

```bash
Rscript -e "install.packages(c('rmarkdown', 'knitr', 'duckdb', 'DBI', 'dplyr', 'ggplot2', 'kableExtra'), repos='https://cloud.r-project.org/')"
```

## 🚀 Utilisation

### Télécharger les données depuis Kaggle

Si vous n'avez pas encore la base de données DuckDB :

```bash
task kaggle-download
```

Cela télécharge les données du notebook Kaggle et copie le fichier `edb-noumea.duckdb` dans le répertoire courant.

### Générer le rapport PDF

```bash
task pdf
```

Génère le fichier `rapport_plages_noumea.pdf`.

### Générer le rapport HTML

```bash
task html
```

Génère le fichier `rapport_plages_noumea.html`.

### Générer le rapport Word

```bash
task word
```

Génère le fichier `rapport_plages_noumea.docx`.

### Convertir le PDF en images JPEG

```bash
task jpeg
```

Convertit chaque page du PDF en image JPEG (`rapport_plages_noumea-1.jpg`, `rapport_plages_noumea-2.jpg`, etc.).

### Nettoyer les fichiers générés

```bash
task clean
```

Supprime tous les fichiers générés (PDF, HTML, DOCX, JPEG) ainsi que les données téléchargées.

## 📊 Contenu du rapport

Le rapport généré contient :

1. **Résumé statistique** - Synthèse des statuts de qualité des eaux
2. **Graphique E. coli** - Concentrations d'E. coli par point de prélèvement
3. **Graphique Entérocoques** - Concentrations d'entérocoques par point de prélèvement
4. **Tableau détaillé** - Résultats complets des derniers prélèvements

## 🗂️ Structure des fichiers

```
.
├── README.md                      # Ce fichier
├── Taskfile.yml                   # Tâches d'automatisation
├── rapport_plages_noumea.Rmd      # Source R Markdown
├── edb-noumea.duckdb              # Base de données (après download)
└── rapport_plages_noumea.pdf      # Rapport généré (après génération)
```

## 🔍 Dépannage

### Erreur LaTeX

Si vous rencontrez des erreurs lors de la génération PDF, assurez-vous que XeLaTeX est correctement installé :

```bash
xelatex --version
```

### Erreur Pandoc

Vérifiez que Pandoc est installé et accessible :

```bash
pandoc --version
```

### Packages R manquants

Si des packages R sont manquants, installez-les via :

```r
install.packages("nom_du_package")
```

## 📝 Personnalisation

Pour modifier le rapport, éditez directement le fichier `rapport_plages_noumea.Rmd` et régénérez avec `task pdf`, `task html`, ou `task word`.

## 📚 Ressources

- [R Markdown Documentation](https://rmarkdown.rstudio.com/)
- [DuckDB R Package](https://duckdb.org/docs/api/r)
- [Task Documentation](https://taskfile.dev/)
- [Site officiel Ville de Nouméa](https://www.noumea.nc/noumea-pratique/salubrite-publique/qualite-eaux-baignade)
