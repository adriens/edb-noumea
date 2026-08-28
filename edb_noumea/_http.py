import time

import requests

DEFAULT_TIMEOUT = 15
DEFAULT_RETRIES = 3
DEFAULT_BACKOFF = 5


def get_with_retry(url, headers=None, timeout=DEFAULT_TIMEOUT, retries=DEFAULT_RETRIES, backoff=DEFAULT_BACKOFF):
    """
    Effectue un GET HTTP avec un timeout explicite et quelques nouvelles tentatives
    en cas d'erreur réseau (le site de la ville de Nouméa est parfois lent/instable
    depuis les runners GitHub Actions).
    """
    last_exc = None
    for attempt in range(1, retries + 1):
        try:
            response = requests.get(url, headers=headers, timeout=timeout)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            last_exc = e
            if attempt < retries:
                print(f"⚠️  Tentative {attempt}/{retries} échouée ({e}), nouvel essai dans {backoff}s...")
                time.sleep(backoff)
    raise last_exc
