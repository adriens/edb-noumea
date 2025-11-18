# Comment Publier une Nouvelle Version sur PyPI

Ce guide décrit les étapes nécessaires pour construire et publier le package `edb-noumea` sur [PyPI](https://pypi.org/).

## Prérequis

1.  **Compte PyPI** : Assurez-vous d'avoir un compte sur [PyPI](https://pypi.org/).
2.  **Token d'API PyPI** : Pour une publication sécurisée, il est fortement recommandé d'utiliser un token d'API plutôt que votre nom d'utilisateur et mot de passe. Vous pouvez créer un token dans les paramètres de votre compte PyPI.
3.  **Outils de publication** : Installez les derniers outils nécessaires pour la construction et la publication.

    ```bash
    uv pip install --upgrade build twine
    ```

## Étapes de Publication

### 1. Mettre à jour la version

Avant de publier, incrémentez le numéro de version dans le fichier `pyproject.toml`. Suivez le versionnage sémantique (Semantic Versioning).

Par exemple, passez de `version = "0.1.0"` à `version = "0.1.1"` pour une correction de bug.

```toml
# pyproject.toml
[project]
name = "edb-noumea"
version = "0.1.1" # <-- Mettre à jour ici
# ...
```

### 2. Nettoyer les anciennes constructions (Optionnel)

Pour éviter toute confusion, il est bon de supprimer les distributions des versions précédentes.

```bash
rm -rf dist/
```

### 3. Construire le package

Exécutez la commande suivante à la racine du projet (`noumea_water_quality`) pour créer les fichiers de distribution (source `sdist` et `wheel`).

```bash
python -m build
```

Cette commande créera un répertoire `dist/` contenant les fichiers à publier (par exemple, `edb_noumea-0.1.1-py3-none-any.whl` et `edb-noumea-0.1.1.tar.gz`).

### 4. Publier sur PyPI

Utilisez `twine` pour téléverser les fichiers de distribution sur PyPI.


#### Méthode recommandée : variable d'environnement

Pour automatiser et sécuriser la publication, définissez votre token PyPI dans une variable d'environnement :

```bash
export TWINE_PASSWORD="pypi-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
twine upload -u __token__ dist/*
```

**Ne jamais committer votre token PyPI dans le code ou dans un fichier de configuration !**

Vous pouvez aussi utiliser la méthode interactive :

```bash
twine upload dist/*
```

`twine` vous demandera vos identifiants :
-   **Nom d'utilisateur** : entrez `__token__`.
-   **Mot de passe** : collez votre token d'API PyPI (y compris le préfixe `pypi-`).

---

### Recommandation : Tester sur TestPyPI

Avant de publier sur le vrai PyPI, il est judicieux de tester le processus sur [TestPyPI](https://test.pypi.org/), un environnement de test distinct.

1.  **Créer un compte** sur [TestPyPI](https://test.pypi.org/) et générer un token d'API spécifique à ce site.
2.  **Téléverser sur TestPyPI** en spécifiant le dépôt :
    ```bash
    twine upload --repository testpypi dist/*
    ```
3.  **Vérifier l'installation** depuis TestPyPI :
    ```bash
    uv pip install --index-url https://test.pypi.org/simple/ edb-noumea
    ```

Si tout fonctionne comme prévu, vous pouvez alors procéder à la publication sur le vrai PyPI.
