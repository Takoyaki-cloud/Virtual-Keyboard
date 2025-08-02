# simulation_clavier_a_distance

disposition et organisation des fichiers :

/ (racine du projet sur la clé USB Pico W)
│
├── code.py          # Code principal CircuitPython
│                    # - connexion Wi-Fi
│                    # - serveur HTTP embarqué
│                    # - gestion des requêtes web (exécution, ajout, suppression commandes)
│                    # - interprète les commandes JSON complexes (combinaison touches, délai, texte)
│                    # - sert la page web avec l’interface utilisateur en HTML+JavaScript
│
├── secrets.py       # Fichier contenant les identifiants Wi-Fi
│                    # - dictionnaire 'secrets' avec ssid et password
│
├── commands.py      # Gestion des commandes HID stockées en JSON
│                    # - fonctions pour charger, sauvegarder, ajouter, supprimer commandes
│                    # - fichier JSON : commands.json
│
├── commands.json    # Fichier JSON stockant les commandes HID utilisateur
│                    # - liste d’objets JSON avec le nom et la séquence d’actions
│                    # - exemple : [{"name": "Ouvrir menu", "sequence": ["GUI r", "DELAY 500", "entrez"]}, ...]
│
└── lib/             # Dossier où tu mets toutes les bibliothèques CircuitPython nécessaires
     ├── adafruit_hid/          # Bibliothèque pour émuler clavier USB (Keycode, Keyboard, etc.)
     ├── adafruit_requests/     # Pour faire les requêtes HTTP si besoin
     ├── adafruit_esp32spi/     # Pilotes Wi-Fi (selon matériel)
     ├── ...                   # Autres libs nécessaires selon la plateforme et code
