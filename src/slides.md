# L'enfer des tests autos

Notes:
* TODO :
  * exemples concrets tout du long
  * exemples de code/archi à la fin
  * images
  * FIXME: the slides should be vertical (cf mkslides_config.yml)

---

# 0. Introduction

Notes:
* TODO :
  * illustration de chapitre ?

-v-

## Disclaimer on n'est pas parfaits

Notes:
* on n'est pas parfait, des fois on ne teste pas (assez), ou pas auto

-v-

## Sondage : qui trouve que c'est l'enfer

Notes:
* qui trouve que les tests c'est l'enfer ? Qui trouve que c'est le paradis ? le purgatoire ?

-v-

## Présentation

Julien Lenormand 😇

Jonathan Gaffiot 👹
@ Kaizen Solutions

Notes:
* TODO :
  * garder cette section ici ?

-v-

## Tester ?

Notes:
* c'est quoi tester ? c'est quoi tester automatiquement ? (moment chiant avec des définitions)
* action, réaction, stimuli, SUT
  * définiton test = s'assurer de la réponse attendue de la part du système dans un certain état à un stimuli particulier
* Qualité avec un grand Q : (d'après Rambo Python) fiabilité, maintenabilité, évolutivité, sécurité
    * mentionner ISO-truc pour une autre définition (plus large)

---

# 1. Pourquoi c'est important les tests autos ? (il faut le rappeller !)

Notes:
* TODO :
  * illustration de chapitre ?
  * @Julien refaire une passe sur les répétitions (cf réunion du mercredi 08 octobre)
  * scientific proofs of efficiency ?

-v-

## Confiance

Notes:
* sérénité
* mise en prod le vendredi après-midi
* confiance dans ce qui a changé, confiance dans ce qui n'a pas changé

-v-

## Feedback rapide

Notes:
* ownership de la qualité du code, ce n'est pas juste aux QAs, ou utilisateurs de trouver les bugs, "ça marche sur ma machine"
* la qualité c'est une démarche, un tamis, un empilement (vrai sens de Kanban), une culture (LEAN, Kanban "right the first time")
* facile à exécuter : un clic et c'est bon, ça part en prod

-v-

## Qualité (fiabilité) du code

Notes:
* et les autres ? maintenabilité/évolutivité/sécurité !
* s'autoriser le refactoring, conserver du code maintenable
* stabilité / perennité / scalabilité humaine-temporelle-technique-complexité-busfactor
  * Tests auto = moyen de scaler dans le temps, la taille, les personnes, les techs, ...
* quelle valeur à un logiciel qui ne peut pas être testé automatiquement ? uniquement court-terme
* pas d'autom == risque projet
* une certaine forme de spécification (c'est plus simple de savoir ce que le code doit faire, quand c'est littéralement commité dans le repo)
    * et encore mieux, elle se vérifie toute seule !!
* exécution automatique/systématique -> pas besoin de devoir s'en souvenir (CI, make, ...)
* empêche le "Fear driven development"
  * Comment faire du fearless refactoring sans Rust ni test ?
* évite le "tombé en marche"
* non-reg
* Sens strict de refactoring, pas de refactoring sans garantie que le comportement "observable" (externe) n'a pas évolué
  * nécessaire pour dompter la dette technique

-v-

## Éthique professionnelle

Notes:
* (cf Craft), déontologie
* responsabilité en tant que dev, que Crafteur, que prestataire; que ...
* critère de validité de ce qui est livré ("si c'est pas testé, c'est réputé ne pas marcher")
* pas obligé de faire comme les autres
* livraison, recette
* maturité professionnelle

-v-

## Rentabilité

Notes:
* Accelerate
* TODO autres preuves d'efficacité ? (cf scientific proofs)
* se concentrer sur des activités à forte valeur ajoutée, par rapport à répéter des tests
* Seul moyen de tenir la cadence

-v-

## Le paradis !

Notes:
* une fois qu'on s'est dit ça, ça paraît vachement bien, donc y'a aucune raison de pas en faire
* meme avec l'image recto/verso, ville en feu, bébé zombie
  * "Kid Thrown In The Air Meme: How Dad Sees It Vs How Mom Sees It" cf https://i.imgur.com/qL915f0.jpeg
* Stop au masochisme ! (TODO: autre section ?)
* transition vers la partie suivante

---

# 2. Pourquoi c'est difficile les tests autos ? (il faut bien l'avouer !)

Notes:
* TODO: le formuler de façon à répondre au chemin de crête ?
* TODO: ajouter des exemples concrets à chacun

-v-

## Chemin de crête

Notes:
* métaphore du chemin de crête : facile de tomber

-v-

## Pas appris

Notes:
* sauf pour les testeurs de métier, les moldus s'en passeront bien ?
* pas de formation dans la plupart des cursus master, ou bien théorique ou très court
* assez peu présent dans la littérature généraliste, malgré sa prévalence et importance (cf biblio)
* pas un sujet "sexy" (formation continue, conférences, ...)
* exemple Ensimag, mon cursus versus ce qui est proposé actuellement
    * Mon ècole d'ingé, ni mon DUT ne m'ont enseigné le test
    * Le test ètait une option, une année, d'une filière
    * les cours de Groz sur la vérif statique et la modélisation boite noire
    * Ensimag, examens de SAP en 2014 et 2015 :
      * déterminer les (in)variants de boucle
      * preuve d'arrêt,
      * interprètation abstraite (réduction de machines à états),
      * accès mémoire invalide,
      * valeurs par défaut en Java,
      * détection de la récursion ou de code mort,
      * propagation d'intervalles pour exécution symbolique
      * preuves de comportement de programme
    * https://ensimag.grenoble-inp.fr/fr/formation/analyse-de-code-pour-la-s-ucirc-ret-eacute-et-la-s-eacute-curit-eacute-4mmacss
      * Ce cours est une introduction aux fondements de la sémantique et l’analyse de programmes. Il offre les bases sur lesquelles s’appuyer pour spécifier et développer des applications sûres, construire et se servir d’outils d’analyse et de vérification.
      * Sémantique opérationnelle des langages de programmation.
      * Calcul de plus faible précondition et preuve de programmes.
      * Analyse de flot de données.
      * Analyse statique et interprétation abstraite.
      * Applications à la compilation, à la sûreté et à la sécurité des logiciels.
      * Travaux pratiques à l'aide de 2 outils industriels.
        * (Frama-C et Coq sûrement ?)
    * https://ensimag.grenoble-inp.fr/fr/formation/test-des-syst-egrave-mes-logiciels-5mmtsl6
      * une option parmi 3, pour ceux qui font pas d'Erasmus
      * Présentation des méthodes de test pour assurer la sûreté de fonctionnement des logiciels.
      * Test
      * Vérification et validation
      * Les tests au cours du cycle de vie.
      * Test structurel des logiciels.
      * Test à partir des spécifications: partitionnement, combinatoire.
      * Méthodes de test basées sur des modèles, en particulier automates.
      * Analyse des notions de couverture, test mutationnel.
      * Eclairage sur des domaines de test importants:
        * test de performance et test de charge
        * test d'interface
        * test de sécurité.
      * Cours de génie logiciel abordant notamment les cycles de développement : cela permet de situer correctement le test dans une activité de développement.  
      * Bonnes connaissances en algorithmique et programmation : être capable d'analyser un programme, de l'exécuter symboliquement "à la main", fait partie des activités du testeur et est une compétence indispensable pour comprendre les techniques fondées sur l'analyse du code.  
      * Langages et automates : une partie du cours porte sur de modèles et en particulier des machines d'états finis exploitées pour engendrer des tests de conformité.
      * Bibliographie :
        * Aditya P. Mathur:Foundations of Spftware Testing, Pearson 2008.  
        * J-F. Pradat-Peyre, J. Printz: Pratique des tests logiciels, Dunod 2009.  
        * Myers, G.J. : The Art of Software Testing. Wiley 1979; réédité 2004.
    * le cours de dernière année
      * @Julien TODO zip de quentin pigné
* "missing semester" ?
* Apprentissage théorique (en études ingé) versus apprentissage empirique de l'informatique (sur le terrain), en particulier du test

-v-

## Vocabulaire confusant

Notes:
* personne n'est d'accord sur rien : 47 pyramides différentes, le vocabulaire du test,~~les perspectives tech~~, les rôles, les niveaux de test
* lister et illustrer avec différents types de pyramides
    * blague illuminatis (pyramide)
    * On est des ègyptiens, on a plein plein de pyramides diffèrentes
* Pyramide originale par Mike Cohn dans "Succeeding with Agile" publié en 2009
* Florilège des autres formes : ice cream, hourglass, diamond, upside-down pyramid, trophy (kent beck) ... --> aucune solution universelle
    * https://claude.ai/chat/3ff66008-4cc7-431e-9657-9f4987e7d86c
* Dimensions de la pyramide : vitesse d'exécution, coût à écrire/maintenir, quantité de code exercée, fidélité utilisateur, ...
  * Multiples interprétations des dimensions de la pyramide : quantité, vitesse d'exécution, confiance, spécificité, couverture apportée, coût de production, fréquence de changement / bug, ...
* Le test c'est un sujet transverse our chaque dev, qu'importe le langage, la stack, le métier, ... Donc tout le monde parle de quelque chose avec un point de vue et un focus diffèrent, pas toujours mentionné
* prêt-à-penser
    * dans quels contextes-projets travaillent les différentes personnes qui ont proposé ces pyramides ? et en quelle année ?
    * ne suffit pas pour appréhender le test
    * Testing tools have evolved in 30 years
* jeu des 7314 différences : industrie, technos, maturité du produit, durée de maintenance, culture d'équipe, compétences lacunaires, vitesse, confiance, ...
    * il n'y en a pas qu'une seule, mais une par projet ! chaque projet est différent !
    * chaque projet est (quasi) unique
* anecdote sur le vocabulaire pas unifié : du temps de mon stage en autom de test, j'avais travaillé entre autres sur un glossaire unifié entre ISTQB et CFTL
* meilleure définition des axes : "finalité, granularité, modalité d'assertion" (50 shades ...)
* essayons de poser une définition, dans notre contexte, des mots que nous employons
    * différences entre ISTQB et CFTL, cf mon stage Sogeti
* tous les différents types de test : carac, fonc, integ, unit, acceptance, user-testing, accessibility, composant-unitaire versus composant-UI, e2e-stack ou e2e-scénario...
    * TODO more
    * charge : soak, breakpoint, ... (cf doc de k6 avec de jolis graphiques)
        * K6 typologie : breakpoint, soak, stress, load, ...
    * cf ISO 15010
    * peu de personnes, même dans des livres (exemple Clean Code de Robert C Martin "Uncle Bob"), ne font l'effort de définir
    * Pyramyde inversé de la valeur : le haut niveau est le plus pertinent, mais cher et fragile ?
        * Facilitation des tests web d'ui (selenium, cypress, playwright)
* QA analyst/tester vs quality engineer vs testeur-automaticien vs "dev" vs IVVQ vs QA "quality advisor" vs test manager ...
* Test error vs test failure : le test n'a pas abouti pour une raison technique (problème de test), le test a abouti mais n'a pas produit le résultat attendu (problème fonctionnel on espère !)
  * distinction "test qui plante" versus "test qui échoue"
* Imbrication et interconnexion des systèmes : les tests au même endroit n'ont pas le même nom / fonction.
* politique vs stratégie vs plan de test
* E2e : vertical de la stack ? Ou horizontal du parcours utilisateur ?
* Sanity vs smoke ?
* test fonctionnel + non-fonctionnel : si la perf fait partie des requirements, alors fonctionnel ou pas ?
* [le glossaire ISTQB](https://glossary.istqb.org/en_US/search?term=) donne 601 résultats en anglais, 559 en français

-v-

## Trop de tests

Notes:
* explosion combinatoire
* cible mouvante et floue
* L'explosion combinatoire rend l'exhaustivité impossible

-v-

## Pratique réticente

Notes:
* des tonnes d'outils différents, les différents types de tests évoqués, les différents métiers, l'insertion dans le process de production, ...
* s'organiser, planifier et réaliser sont des tâches complexes

-v-

## Punition

Notes:
* l'absence de testeur/expertise/culture dans les projets (des gens formés, motivés, avec le mindset adéquat)
* > On peut conduire un cheval à l'abreuvoir, mais pas le forcer à boire
* certifications ISTQB par le CFTL
* casse-pied de service

-v-

## Inutile

Notes:
* convaincre (le management et/ou les devs) que c'est utile, avant de se manger une mise-en-prod foirée
* dépense versus économie
* Résultats intangibles

-v-

## Test impossible

Notes:
* imitations techniques, matérielles, de coût, ... variabilité selon les environnements, pas de données de test (réalistes)
* exemple board farm Schneider
* exemple Windows 10 LTSC 2019 à Thales

-v-

## Code intestable

Notes:
* Ennemis : side-effects ("spooky action at a distance", "que fait cette méthode ?"), (global/static) state, IO, singletons, time, locale, network, files, env, GPU, unclear pre/post-conditions, non-determinism, (G)UI vs API, concurrency et threading, random (non-deterministic), complex outputs and high dimensionality
* différence entre "c'est compliqué de réaliser le test" (limitations tech) versus "c'est compliqué d'écrire le test" (iceberg, gorille)
* exemple : code des bornes qui échoue le 29 Février
* exemple : code du Edge qui est correct sur la timezone 6 mois par an
* anecdote schneider :
  * on me demande de rajouter un paramètre booléen à une route HTTP, sur un composant sur lequel je n'ai jamais travaillé
  * je me dis je vais le faire en TDD, commencer par écrire un test
  * mais y'a aucun test sur le projet, donc je dois commencer par écrire un test avant
  * j'écris un test, je le lance un fois il passe, deux fois il échoue
  * car il avait une dépendance sur une base de données, laquelle est gérée par un singleton, qui stocke l'état
  * donc je fixturise le singleton pour le réinitialiser (ou le détruire/reconstruire) afin que mon test soit répétable
  * ensuite j'ajoute mon test et le changement est easy
  * (ah, maintenant faut que j'ajoute une CI !!)

-v-

## Fragile

Notes:
* couplage versus maintenabilité en carton, tests cassés pas réparés ("vitre cassée"), maintenance des tests vécue comme un fardeau
  * le summum : test de mock !
* Tester le mauvais 80% : métaphore du streetlight problem ("plus simple de chercher dans la lumière")
* test flaky
  * l'équivalent de "ptèt bin qu'oui, ptèt bin qu'non"
  * suffit de les relancer plusieurs fois mdr, ~zéro confiance

-v-

## Illisible

Notes:
* exemple d'Eric (Schneider)

-v-

## Lent

Notes:
* lenteur, car tests lents et/ou trop de tests
* exemple de Xavier Nopre (cf [post LinkedIn](https://www.linkedin.com/posts/xnopre_pourquoi-jai-mis-plus-de-3-jours-%C3%A0-trouver-activity-7316027544934191104-Otww)), je lui ai dit qu'il y avait un problème, c'est pas censé être aussi lent
* exemple de Schneider : board farms
* exemple de Schneider : code dont le run dure des centaines jours !! (à travers les timezones :p)

-v-

## Bug ou feature ou code mort ?

Notes:
* descriptivism vs prescriptivism (cf Romeu)
* test de caractérisation OK, mais est-ce que c'est ce que ça devrait vraiment faire ? 🤷
  * bug ou feature ?
  * xkcd workflow https://xkcd.com/1172/
* source de vérité = code ou spec Word ?

-v-

## L'enfer !

Notes:
* difficile de savoir quoi faire, comment faire, de le faire, à exécuter, à analyser, à maintenir, à faire confiance, pas assez, pas assez bien, pas assez rapide, ...
* Facile à dire de faire "le bon test", mais concrètement ?
  * y'a le bon testeur et le mauvais testeur ...
* transition

---

# 3. Comment faire pour bien tester auto ? (il faut s'aider !)

Notes:
* TODO:
  * orienté solution cf partie précédente orienté problème ?
  * le formuler de façon à répondre au chemin de crête
  * mentionner "se rendre dispensable" ? (vis-à-vis du scaling humain)

-v-

## Chemin de crête

Notes:
* comment le naviguer ? comment être/devenir/rester rigoureux ?
  * discipline d'un moine bouddhiste, ou d'un garde de la reine d'Angleterre

-v-

## Culture de la qualité

Notes:
* culture qualité, formation (cours, conférences, livres, exercices, katas, ...)
* cf nos recos à la fin, expérience (empirisme)
* compréhension du business et des stakeholders,
* tournure d'esprit (cf joke "un testeur rentre dans un bar, il commande -1 bière, NaN bière, demande où sont les toilettes ..."), "vicieux" pour "casser le code" et non pas seulement montrer qu'il fonctionne 
* exemple : SQLite testing, test code ratio, test harnesses, ... (+évolution dans le temps)
* le code il faut le malmener
* la qualité c'est un ensemble de tamis successifs : empilement de couches pour attraper les bugs, du besoin, design, archi, implem, test, validation, déploiement
  * processus/démarche au niveau deDéfinition de test unitaire contre-intuitive : ne pas penser microscopique/indivisible, mais cohérence/séparation-frontière l'équipe/projet/entreprise/...
* exemple : NDP Systems
* "Le test n'apporte pas de valeur (argent) par rapport aux fonctionnalités"
* Humilité de devoir tester
* "move fast and break things"
* https://news.ycombinator.com/item?id=13130991 : you get paid for "software", not "maintainable software"
* Avoir un "Patrick" (ou whatever name) dans son équipe, éternellement vigilant, le "relou"
* comme beaucoup de sujets, c'est pas un casse-pied de service qu'il faut, mais un changement de culture (beaucoup plus compliqué, cf Agile bullshit, sécurité, ...)
* Responsabilité individuelle et d'équipe
* Lean, faire bien du premier coup, kanban, "right the first time"

-v-

## Stratégie de test

Notes:
* quoi pourquoi pour quoi comment qui quand ...
* spécifications, Exigences et Requirements, business (value stream) et risques business, quadrants, matrice confiance versus risque, moyens (et toute la suite)
  * cartographier les flux d’information, les cas d’usage, les frontières techniques et les domaines de l’application afin de discerner les frontières des tests
* construisez votre "pyramide" (demander à une IA diK6 typologie : breakpoint, soak, stress, load, ...fférente pyramides, de plein de formes différentes à la Dali), en se basant sur les moyens de test
* à adapter/repenser régulièrement, comme tout le reste
* pourquoi, pour quoi, quoi, où, qui, quand et comment, ...
* trust boundaries (dépendences externes, parties peu fiables, risque métier, responsabilité, vitesse d'évolution, ...)
* Repenser la strat fréquemment, tout comme on le fait pour l'architecture de la solution
* considérer les niveaux de test : Fonctionnalités techniques (endpoint) versus user
* Quadrant des tests !! Axes : business vs tech, pour le produit vs èquipe
* dépendences externes (on ne les controle pas, c'est compliqué, et elles peuvent changer sans qu'on y prête attention) versus dépendances internes (on les controle, mais c'est quand même compliqué, et peuvent changer si on ne fait pas assez gaffe)
* Choisir l'effort de test par périmètre = choisir là où on préfère diminuer la proba d'un bug
* contrats (boundaries)
* Plan de test au format IEEE 29119-3 (ou pas !)
* Le système testé peut faire partie d'un sur-système, et se composer de sous-systèmes, les composants des uns sont les acceptation des autres
  * Ce qui dépend de nous versus ce qui ne dèpend pas (stoïcisme)

-v-

## Moyens de test

Notes:
* humains, techniques, temporels, ...
* outils de test, formations, avoir le temps, déployabilité, disponibilité du hardware, dispo des data, ...
* avoir des specs ! (claires)
* pas de bras, pas de chocolat

-v-

## Renoncer

Notes:
* renoncer à tout automatiser (quadrants, moyens insuffisants, ...), ROI
* tradeof : cout, risque, complexité, ...
* critère qui favorisent l'automatisation : répétition, confiance dans l'autom, pénibilité, longueur, criticité, ...
* il vaut mieux un mix d'autom et de manuel, la force de chacun
* Le coût des tests est parfois supérieur aux benéfices
* exemple : lecteur de fichier à EDF
* Tester le code techniquement complexe, sensible pour le métier, et utile
* loi de pareto 80/20 : toujours fausse, toujours vraie
* hybrid possible aussi (soit manuel assisté par autom, soit autom avec verif manuelle) : continuum Automatisé-automatisable-manuel
* Sans jugement : un pas après l'autre, on hérite de codebases, on essaye de faire mieux
  * incrémental
* tester ne prouve pas l'absence de bugs, mais en élimine certains  
* process avec des rendements décroissants, trouver le bon curseur, le bon équilibre
* garder des tests qu'on apprécie : rapides (ou moins rapides en CI mais + couvrants), fiables, maintenables, estimer le ROI
* OK de supprimer un test inutile
* fatalisme, tout tester en auto est un voeu pieux
* Choisir ses batailles, mettre les efforts au "bon" endroit
* à tester = risque business + risque tech + facilement automatisable >= 1

-v-

## Processus

Notes:
* (reprendre des tamis) : tres amigos, example mapping, BDD, prise en compte de la testabilité dès la (pré-)conception, compter le coût du test dans l'estimation de la story, les tests font partie de la dette technique du projet, analyse d'impact lors de nouveaux devs, découpage en équipe Dev versus QA ??
  * identifier les manquements dans son équipe, sur son projet, et trouver comment communiquer dessus avec les autres, avoir des idées à proposer

-v-

## Scénarios

Notes:
* scénarios de test (nominaux, critiques, ...) décidés, "use cases" (orientés "utilisateur" de l'interface)
* TODO retravailler cette section, semble un peu redite avec la stratégie
* typologie de test : "unitaire au niveau technique (méthode/classe)", ou "unitaire d'interface mais profond"
* avoir une spec
  * Exigences et Requirements (cf Schneider, Thales, ...)
* value streams, risques, manque de confiance, ...
* smoke tests (cf origine du mot "smoke test" en logiciel)
* quoi tester ? critique ou sujet à forte régression, et stable, fréquence d'exécution

-v-

## Architecture testable

Notes:
* sinon architecture intestable ou semi-testable
* seams (cf Michale feathers, Working effectively with legacy code) versus scalpel et pied-de-biche
* dépendances, interfaces, contrats, ... "trust boundaries"
* you can't write good tests for badly written code
* version de dev, suffisament isoprod mais avec des backdoors
* attention au couplage : ni trop peu, ni pas assez (monolithe spaghetti versus micro-services passe-plats)
  * plus simple de tester des fonctions (niveau code) que des programmes
* functionnal core, imperative shell (ou héxagonal, ou onion)
* pousser les IO à l'extérieur (technique du sandwich)
* design goal sinon accidentel
* critère d'acceptabilité
* state is the enemy, prog fonctionnelle
* narrow interfaces for deep modules
* "fracture planes" de Team Topo, selon des "lignes de faille" (user persona, tech, change cadence, regulatory compliance, team location, risk, performance isolation, ...)
  * cf https://teamtopologies.com/key-concepts-content/finding-good-stream-boundaries-with-independent-service-heuristics
  * cf https://yoan-thirion.gitbook.io/knowledge-base/xtrem-reading/resources/book-notes/team-topologies#software-boundaries-or-fracture-planes
* sans architecture testable, la strat s'effondre !

-v-

## Surface d'interface

Notes:
* TODO: sous-partie de l'architecture testable ?
* maîtriser la surface de test du code
* Tester aux frontières d'une interface, que ce soit une méthode privée, publique, classe, module, programme, sous-système, système, sur-systeme
* facile pour des modules narrow-interface mais deep, impossible pour des hubs
* les "unit" tests n'ont pas vocation à tester le moinds de lignes possible, mais à tester des APIs
* Ne pas tester tout le code ? Cf couverture, et faire des tests croisés
* Quantité de test versus qualité
* contravariance, tester l'interface plutôt que l'implémentation, cf Uncle Bob https://blog.cleancoder.com/uncle-bob/2017/10/03/TestContravariance.html
* bon test = SRP + behavior not implementation
* niveau de test :
  * Test u = contrat dev
  * Test inté = contrat intégrateur
  * Test accep = contrat user
* Exercer le système depuis l'extérieur
  * ok pour du e2e
  * un désastre pour en tester des sous-parties (banane, gorille, jungle)
* "mock roles, not objects" - in "Growing Object-Oriented Software, Guided by Tests" by Steve Freeman and Nat Pryce

-v-

## Feedback

Notes:
* fast feedback + CI/CD + DevOps (monitoring, observability), frequent deployment, Monitoring, debuggability
* Feedback lors du dev, test, code review, design, recette, bugs en prod : tout renseigne sur ce qui mérite d'être testé et comment
* tester en prod avec le devops : canary, green-blue, ...
* Les tests doivent planter de temps en temps, pour les bonnes raisons
  * Signal et feedback
  * Doivent ne pas échouer tout le temps (sinon signe de couplage) ni jamais (signe que rien n'est testé). Doivent être un signal, ni zéro ni un. Équilibre difficile.
* Les tests qui pètent (pour une bonne raison) c'est moins de bugs en prod, qui est l'objectif principal.

-v-

## Fluide

Notes:
* ajouter un test doit être simple, s'il y a de la friction alors ça décourage de tester, il faut éliminer la friction
* sentir la douleur : "If it hurts, do it more often" (core XP principle)
* ne pas être capable de réaliser les tests rapidement diminue l'itérativité, la qualité, l'agréabilité, ... la probabilité qu'ils soient écrit tout court
  * comme un évier plein de vaisselle (cercle vicieux)
* Blague du docteur : "j'ai mal quand je suis debout" "alors arrêtez de vous lever"
* éviter les micro-services, les submodules, les tests pas dans le même repo que le code (tant que possible)
* Pente glissante de la qualité:
  * Si les tests sont difficiles à lancer, ils ne le seront pas souvent
  * Si les résultats des tests sont peu fiables/lisibles, il ne seront pas regardés
  * Si les tests sont lents à s'éxécuter, les tests rajoutés seront lents aussi

-v-

## Investissement

Notes:
* investissement dans un second logiciel pour mieux produire le premier
* outils de test
* investir dans le futur
* projet logiciel = le code qui part en prod, mais pas seulement, aussi : la doc, la CI, les specs, et donc aussi les tests, ...
* "Le test n'apporte pas de valeur (argent) par rapport aux fonctionnalités" (et les fonctionnalités non plus d'ailleurs, ça dépend si elles sont connues, utilisées, ...)
* Second-système de stabilisation du premier, par opposition à la flexibilité
* Une sécurité, ou un frein ? les deux ?
* exemple de SQLite (x 590)
* Vraiment à retenir : ne pas penser le test comme un après, mais comme un même temps, voire enabler
* estimer le ROI de l'automatisation : gain versus coût ? matrice
  * c'est un gros sujet pour les Test Managers, et les chefs de projets
* le meilleur moment pour commencer à mettre des tests sur le projet c'était le premier jour, le second meilleur moment c'est aujourd'hui
* https://xkcd.com/974/ "The General problem" (et sa caption : perception de perfectionniste versus maître-artisan)
* https://xkcd.com/1205/ "Is it worth the time?"
* Le code pourrit sans test auto, mais les tests auto eux-mêmes pourrissent, ou peuvent pourrir (vérouiller) le code
* J'avais un problème, maintenant j'en ai deux (un nouveau)
* le test c'est une analyse coût-bénéfice : combien je veux mettre dans mes tests, pour le run de mon dev et de ma prod
* des tests systèmes pas effectués = risque business
  * exemples : 8 bcs biologic, 50 bornes schneider, ...

-v-

## Ecriture

Notes:
* méthodologie d'écriture : setup/teardown, Given/When/Then, Assert/Arrange/Act, tester une seule chose plutôt qu'un scénario complet, erreur versus échec
* FIRST : https://stackoverflow.com/questions/18024785/tdd-first-principle Fast Indep Repeat Self-Check Timely (pas écrit dans 1000 ans mais avec le code à tester)
  * double i : isolation ?
  * test FIRST : Timely ou Thorough ?
* un test sans assert = red flag
* unit test = focus, sinon scénario utilisateur end-to-end
  * sinon "Shotgun unit testing" : le test fait tout et n'importe quoi

-v-

## Techniques

Notes:
* ce qu'on considère le minimum à maîtriser pour tester
* test harness
* TestContainers
* framework
* mocking et fakes versus simulateurs/émulateurs, oracles
  * qu'est-ce je gagne et je perds si je mocke ? gain = vitesse d'exec + facile à mettre en oeuvre (autospec), perte = maintenabilité et réalisme
* DB in-memory

-v-

## techniques avancées

Notes:
* outils et techniques <<avancés>>, pour aller + loin (et qui mérite chacun son 45 minutes ou +) pour développer culture et savoir-faire
* TODO trier/ordonner ces techniques, dégager des catégories ?
  * quelques-unes principales, d'autres justes énoncées ?
* advanced features of pytest (or your framework), know your tools
  * fixture
  * mock
  * plugins
* TU : Définition de test unitaire contre-intuitive : ne pas penser microscopique/indivisible, mais cohérence/séparation-frontière
* TDD (cf on peut pas oublier de les faire à la fin si on les fait au début), différents sens du mot TDD, ...
  * cf slides ABC + Discovery Day
  * Mon tddd : testable design
  * "Tdd malgrè son nom n'est pas une technique de test mais de design"
* mock et doublures : mock fake stub spy
  * Cf martinfowler (en ref à la fin)
* chaos monkey + chaos engineering, cf Netflix + [Chaos Monkey Army](https://github.com/Netflix/SimianArmy/wiki/The-Chaos-Monkey-Army)
* ATDD versus BDD (parcours versus comportement segmenté, cf la Taverne)
  * Bdd mindset versus bdd outil
* snapshot/golden-master/approval
  * normatif versus descriptif
  * Approval Testing == Snapshot Testing == Golden Master ?
* fake time (freezegun en Python, libfaketime + LD_PRELOAD), Reactive instead of passive polling ou sleeping, 
* Ab testing
  * canary release, alpha testing, beta testing, blue-green, ...
  * Field testing (schneider)Dimensions de la pyramide : vitesse d'exécution, coût à écrire/maintenir, quantité de code exercée, fidélité utilisateur, 
  * user acceptance ?
* sans io
* architecture héxagonale
* programmation fonctionnelle
* IA
* mesure de la couverture de test
  * Code coverage : line/branch/cond
  * 80 ? 90 ? 99 ?
  * Ne suffit pas !!!
  * Cf "1 / 0" avec 100% de coverage.
  * Ou "foo.update()" si foo est null
  * Il y a des branches invisibles (exceptions, données mal modelées)
* test guidé par la couverture (sans mention de pourcentage)
  * pour orienter les tests
* surveiller la performance des tests autos
  * ne correspond pas aux tests de performance
* security testing
* load testing (rendu accessible par de l'outillage, mais reste rare et hyper-spécifique en terme de scénario)
* table testing
* full simulation (à la Matrix)
  * [What's the big deal about Deterministic Simulation Testing?](https://notes.eatonphil.com/2024-08-20-deterministic-simulation-testing.html)
  * [Pierre Zemb : Et si on faisait du simulation-driven development ?](https://www.youtube.com/watch?v=12LO_l90vDk)
* contract testing
  * Test d'interface d'une third-party (rupture d'API, ...)
* recording/replaying (VCR)
* monkey testing (Doublures de test : des inputs au hasard, le test n'est pas structuré)
* profile your tests ! (éviter les "slips/sleeps sales") cf snakeviz marche aussi pour les tests (cf article de Xavier et son setup de DB), tests en parallèle (cf article du blog de PyPi), être réactif plutôt que passif (cf MQTT tester de Schneider)
* property-based testing + fuzzing
* trunk-based development + feature flags
* tests de maintenabilité ISO 25010 (tests de modularité, réutilisabilité, analysabilité, modifiabilité, testabilité), cf https://latavernedutesteur.fr/2018/11/19/types-de-tests-iso-25-010-les-tests-de-maintenabilite-7-8/
* coverage-based testing
* mother object, method factories for test objects, data builders, ... https://martinfowler.com/bliki/ObjectMother.html
* parallélisation de tests
* dependency injection (D de SOLID), SRP
* DevOps (cf slide)
* test utilisateurices/accessibilité
* test de sécu (automatisé)
* mutation testing
  * du code de prod, et du code de test
* Snapshot-testing (approval, golden master)
* Formal methods, preuves
* ISO/IEC 25010:2023
  * https://www.iso.org/fr/standard/78176.html
  * https://iso25000.com/images/figures/iso_25010_en.png
  * + critères d'usage ISO 25019
* DDD
* boundary analysis et extreme values
* Page object model (POM)
* gestion des erreurs souvent peu poussée, manque de contexte dans les logs
  * error model
* Technique de refactoring du sandwich (snowcamp) : push IO to the edge (functional core, imperative shell)
* Test d'èchafaudage (scaffolding)
* Mockist vs Behaviorist (detroit vs london)
* (London "Mockist"/"Behaviorist" versus Detroit "Classicist")
  * exemple dans un post Linkedin : https://www.linkedin.com/posts/francois-baveye_met-tes-tests-unitaires-%C3%A0-la-poubelle-activity-7370443832401747968-Uc1O
  * tests unitaires : sociables vs solitaires (est-ce que les objets testés ont leurs dépendances réelles ou mockées) 
* tests d'architecture (Java = ArchUnit, Python = PyTestArch)
* Security testing : automated tools
* Clean Test = 3 things : readability, readability, readability
  * Evolving/surfacing a "testing language" to reveal intent
    * = POM ?
* Black box / white /glass
* Baseline perf comparison testing
* Pairwise pour la couverture, en contrant l'explosion combinatoire (produit cartésien des paramètres)
* risk-based testing
* test data management
* "test impact analysis"
* Linter, typechecker, SonarQube, ... (compilation) des tests qu'il n'y a pas besoin d'écrire (tests statiques)
  * Rust, tooling
* inclure des fonctionnalités requises par les tests dans le code de prod ? non-préférable mais acceptable
* historisation (visuelle) des résultats, pour repérer les tendances, les patterns
* time : freezegun en Python, libfaketime avec LD_PRELOAD sinon
  * exemple : tester du code qui doit s'exécuter pendant des mois (harness de test d'endurance)
* rôle de l'IA dans les tests ? (cf Tao blue/red team)
*  property vs fuzzing (cf [article sur la différence](https://www.tedinski.com/2018/12/11/fuzzing-and-property-testing.html))
  * oracle parfois difficile à obtenir, parfois évident
* advanced features of pytest (or your framework), know your tools
* sans_io
* systrace/ptrace
* LD_PRELOAD
* HTTPS Man-in-the-Middle (MITM proxy par exemple)
* trucage DNS via `/etc/hosts` ou `/etc/resolv.conf`
* `ssl_verify=False`
* test des logs/metrics (cf mon post LinkedIn)
* test hybride : test auto avec vérif humDéfinition de test unitaire contre-intuitive : ne pas penser microscopique/indivisible, mais cohérence/séparation-frontièreaine, ou test manuel avec assistance autom
* anonymiser des données (de prod)
* générer des données

---

# 4. Cas pratique

Notes:
* TODO : 3 exemples de test
  * fonction pure (mais avec de la complexité interne), quelques cas d'erreur prévus -> tests fonc, table, edge cases, fuzz, property-based
  * API WEB : mock, contrat, VCR, fake d'API
  * gros Postgres legacy, nouvelle feature

---

# 5. Conclusion

Notes:
* expertise indispensable, il faut s'y mettre, dans un environnement semi-hostile (vocab, équipe, rythme, outillage, ...) -> CI, run local. C'est une partie de l'ingénierie

---

# 6. Nos recommandations

Notes:
* TODO @jonathan d'autres à rajouter ?
* [Jeremy Sorent "j'écris de tests sans pleurer maintenant" - LyonCraft 2025](https://www.youtube.com/watch?v=2S9TxoTE8BA) : TODO @julien mon avis
* [Michael feathers - Working effectively with legacy code](https://softwareengineering.stackexchange.com/questions/122014/what-are-the-key-points-of-working-effectively-with-legacy-code) : spoiler ça parle énormément de test !
* [Joel "on Software" Spolsky - Hard-assed Bug Fixin’](https://www.joelonsoftware.com/2001/07/31/hard-assed-bug-fixin/) : est-ce que tous les bugs devraient être corrigés ? ça dépend.
* [Mathieu Eveillard - 50 shades of tests](https://www.mathieueveillard.com/blog/50-shades-of-tests) : des définitions plutôt claires pour différents types de test, leur positionnement sur 3 dimensions, au-delà de la pyramide de tests
* [Marc Hage Chahine (La Taverne du Testeur) - Que doit-on attendre d’un testeur ?](https://latavernedutesteur.fr/2025/09/15/que-doit-on-attendre-dun-testeur/) : les différentes dimensions du métier de testeur
* [Arnaud Lemaire - From code to consequences](https://www.youtube.com/watch?v=muRdH9u7gO4) : en quoi les "full cycle engineers" sont importants pour mener à bien des projets
* [Colin Damon - ma typologie de tests et leur équilibrage](https://www.linkedin.com/posts/colin-damon_mettre-en-place-une-strat%C3%A9gie-de-tests-qui-activity-7343525861444247552-6BJY) : un exemple de "pyramide" dans un contexte précis
* [Dwayne Richard Hipp - How SQLite Is Tested](https://www.sqlite.org/testing.html) : un exemple de comment n'avoir quasi aucun bug pour un des logiciels les plus utilisé au monde
* [Redowan Delowar - Test state, not interactions](http://rednafi.com/go/test-state-not-interactions/) : pourquoi les tests proposés par des LLMs ne sont pas nécessairement les bons, et comment faire mieux (par exemple privilégier les fakes aux mocks)
* [Jeff Atwood (CodingHorror) - Falling Into The Pit of Success](https://blog.codinghorror.com/falling-into-the-pit-of-success/) : comment ne plus avoir besoin de se battre pour que la qualité ne dégringole pas ?
* [Antoine Mazure - Tests pragmatiques : comment presque arrêter les tests automatisés ?](https://www.youtube.com/watch?app=desktop&v=ohV6GvCIeLY) : un exemple de tester la mauvaise chose, et de comment mieux tester avec pourtant moins de tests
* [Jules Poissonnet et Antoine Caron - Tester c'est tricher)](https://www.youtube.com/watch?v=I_zNxGqRI3w) : une vision d'ensemble, claire et illustrée, de la démarche de test, du vocabulaire et des difficultés
* [Christophe Bréheret-Girardin - Comment une architecture influence votre stratégie de test ?](https://m.youtube.com/watch?v=IeOa6XWxkxg)
* [Ham Vocke - The Practical Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html) : des exemples concrets dans un contexte clair de différents types de test, et des limitations de la pyramide de Mike Cohn
* [Martin Fowler - Mocks Aren't Stubs](https://martinfowler.com/articles/mocksArentStubs.html) : définitions claires de tous les "*test doubles*" (dummy, stub, fake, spy, mock) par Martin Fowler
  * [Martin Fowler - Test Double](https://martinfowler.com/bliki/TestDouble.html) : en version ultra-abrégée
* [Anaël Lefebvre - Comment en finir avec la fragilité des tests unitaires](https://www.sqli.com/fr-fr/insights/comment-en-finir-avec-la-fragilite-des-tests-unitaires) : un contexte clair, une explication de FIRST, et une méthodo ("ZOMBIES") pour identifier les cas de test
* [Adam Bender - SMURF: Beyond the Test Pyramid](https://testing.googleblog.com/2024/10/smurf-beyond-test-pyramid.html) : un exemple par Google de détricoter la pyramide des tests dans une vision complémentaire des tests selontleurs propriétés techniques
* [Miško Hevery - Writing Testable Code](https://testing.googleblog.com/2008/08/by-miko-hevery-so-you-decided-to.html) : un ensemble de conseils pour rendre son code testable, dont le premier point ("Mixing object graph construction with application logic") est trop méconnu
* [The Grug Brained Developer - Testing](https://grugbrain.dev/#grug-on-testing) : des conseils de programmation pertinents, mais rédigés par "Grug" qui a une capacité limitée, et qui le revendique (!)
* [Qalisty - Comment s’en sortir lorsqu’on est 1 testeuse face à 25 développeurs ? (Anaïs Fournier)](https://open.spotify.com/episode/1nwA9nLdezVk6mzWu39T7a) : des techniques concrètes pour mettre en place une culture qualité et une stratégie
* [Victor Lambret - Le TDD sans commencer par les tests](https://www.youtube.com/watch?v=Ddarw3wUXQY) : TODO @julien mon avis
* [Mike Wacker - Just Say No to More End-to-End Tests](https://testing.googleblog.com/2015/04/just-say-no-to-more-end-to-end-tests.html) : les tests unitaires seraient ceux qui compte le plus, du point de vue des utilisateurs (!)
* [Simon Stewart - Test Sizes](https://testing.googleblog.com/2010/12/test-sizes.html) : caractérisation des tests (en un tableau), non pas en unitaires versus end-to-end, mais en small versus big, en fonction de leurs IO
* [Igor Roztropiński - Unit, Integration, E2E, Contract, X tests: what should we focus on?](https://binaryigor.com/unit-integration-e2e-contract-x-tests-what-should-we-focus-on.html) : de l'intérêt de favoriser les tests d'intégration ("in-between", n'étant pas extrêmes), et les tests de contrat
* [Kent C. Dodds - Write tests. Not too many. Mostly integration.](https://kentcdodds.com/blog/write-tests) : introduit la pyramide "trophy" (en incluant les tests statiques) pour des applis JS, avec surtout des tests d'intégration
* [Seb Rose - Making a meal of architectural alignment and the test-induced-design-damage fallacy](https://claysnow.co.uk/architectural-alignment-and-test-induced-design-damage-fallacy/) : une bonne leçon d'équilibre et de pragmatisme
* [IFTTD #43.src - Test: Tester c'est douter avec Arnaud Lemaire](https://open.spotify.com/episode/2gRex0ajRA1oVc7DZBL0B9) : TODO @julien
* [Cécilia Bossard et Angi Guyard - On n’aurait pas oublié un truc dans le craft !?](https://www.youtube.com/watch?v=yVmKkRH60VI) : spoiler il s'agit des tests utilisateurs
* [BiteCode - Testing with Python (part 4): why and what to test?](https://www.bitecode.dev/p/testing-with-python-part-4-why-and) : toute la série d'articles vaut le détour, mais cet épisode s'attarde sur, sans le nommer ainsi, la stratégie de test

---

# Bibliographie (et quantité pertinente)

* TODO @Julien Abseil
* TODO @Julien Software Craft (Dunod)
* TODO @Julien Clean Code 2008
* TODO @Julien Software Architecture in practice
* TODO @Julien A philosophy of software design
* TODO @Julien Working effectively with legacy code
  * (recommandé auparavant)
* TODO @Julien Test-Driven Development By Example
* TODO @Julien Itérations Product(ives)
* TODO @Julien Pourquoi votre stratégie de tests end-to-end échoue ?
* Refactoring, Martin Fowler, 2ème édition française, 2019 (410 pages)
  * Chapitre 4 "Création des tests" (15 pages)

Manquants :
* TODO @Julien Agile Testing - Lisa Crispin et Janet Gregory
* Growing Object-Oriented Software Guided by Tests - ... TODO @julien
* Unit Testing - Baptiste Lyet TODO @julien
* How to test legacy code - emily bache TODO @julien
* Can we test it? Yes we can - Mitchell Hashimoto TODO @julien

---

# Crédits photos

Notes:
* TODO later

---

# Remerciements

Notes:
* Damien Roulier, Eric Papazian, Mathieu Mattringe, Rachel Da Silva, Francky Flamant, Fanny Velsin, Victor Lambret

---

# Questions

Notes:
* TODO image

---

# Exemple de citation trompeuse

> "I get paid for code that works, not for tests [...]"

- Kent Beck

[...]

> I get paid for code that works, not for tests, so my philosophy is to test as little as possible to reach a given level of confidence (I suspect this level of confidence is high compared to industry standards, but that could just be hubris).
> If I don't typically make a kind of mistake (like setting the wrong variables in a constructor), I don't test for it
> I do tend to make sense of test errors, so I'm extra careful when I have logic with complicated conditionals.
> When coding on a team, I modify my strategy to carefully test code that we, collectively, tend to get wrong.

Source : [Stack Overflow en 2008 : "How deep are your unit tests?"](https://stackoverflow.com/a/153565/11384184)

---

# Abstract

L'enfer des tests auto

Des tests automatiques, on sait qu'il faut en faire. Mais trop souvent c'est une véritable corvée : c'est lent, pas fiable, compliqué à lancer, compliqué à maintenir, voire compliqué à écrire tout court. Pourquoi c'est si dur ? Et comment reprendre le contrôle ?

Il va falloir reprendre depuis le début : pourquoi on teste ? et on teste quoi ? et on teste comment ?
Ensuite, il va falloir revoir un peu les bases du test : un brin de vocabulaire, et surtout de la méthodologie (dépendances, interfaces, contrat, mock, simulateur, fixture, inversion, ...).
On fera un petit détour par l'architecture, parce que la testabilité est une propriété à prendre en compte dès le design, ou bien il faudra jouer du scalpel ou du pied-de-biche par la suite pour les faire rentrer.
Enfin, on passera à l'implémentation, et avec quelques bonnes pratiques et le bon outillage (framework de test, TestContainers, CI, ...), ça se passera plutôt bien.

A travers des cas concrets tirés de nos expériences, suivez-nous sur le chemin pour quitter l'enfer des tests.
