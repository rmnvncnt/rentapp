# rentapp

Application web destinée à évaluer la légalité des annonces locatives proposées sur [pap.fr](http://www.pap.fr/) pour la ville de Paris dans le cadre de la [loi d'encadrement des loyers](https://www.service-public.fr/particuliers/vosdroits/F1314).

L'application permet de récupérer les informations présentes dans l'annonce via son URL, recoupe ces informations avec les données publiques du cadastre parisien (quartier, année de construction), puis effectue si nécessaire une prédiction des charges locatives. Lorsque les recoupages ont été effectués, l'application compare le prix proposé dans l'annonce au loyer légal demandé pour un logement de cette surface.

Cette application a été réalisée en collabortion avec les membres de [DataForGood](http://dataforgood.fr/)(d'autres informations sont disponibles sur le [repos du projet](https://github.com/dataforgoodfr/batch2_loyers)).
