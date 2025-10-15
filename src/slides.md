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

Notes:
* TODO :
  * garder cette section ici ?

-v-

## Tester ?

Notes:
* c'est quoi tester ? c'est quoi tester automatiquement ? (moment chiant avec des définitions)
* action, réaction, stimuli, SUT
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
* quelle valeur à un logiciel qui ne peut pas être testé automatiquement ? uniquement court-terme
* pas d'autom == risque projet
* une certaine forme de spécification (c'est plus simple de savoir ce que le code doit faire, quand c'est littéralement commité dans le repo)
    * et encore mieux, elle se vérifie toute seule !!
* exécution automatique/systématique -> pas besoin de devoir s'en souvenir (CI, make, ...)
* empêche le "Fear driven development"

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

-v-

## Seul moyen de tenir la cadence

-v-

## C'est vachement bien !

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
    * le cours de dernière année
        * @Julien TODO quentin pigné

-v-

## Vocabulaire confusant

Notes:
* personne n'est d'accord sur rien : 47 pyramides différentes, le vocabulaire du test,~~les perspectives tech~~, les rôles, les niveaux de test
* lister et illustrer avec différents types de pyramides
    * blague illuminatis (pyramide)
    * On est des ègyptiens, on a plein plein de pyramides diffèrentes
* Mike cohn pyramide des tests 2009, (martin fowler ??)
* Florilège des autres formes : ice cream, hourglass, diamond, upside-down pyramid, trophy (kent beck) ... --> aucune solution universelle
    * https://claude.ai/chat/3ff66008-4cc7-431e-9657-9f4987e7d86c
* Dimensions de la pyramide : vitesse d'exécution, coût à écrire/maintenir, quantité de code exercée, fidélité utilisateur, ...
* Le test c'est un sujet transverse our chaque dev, qu'importe le langage, la stack, le métier, ... Donc tout le monde parle de quelque chose avec un point de vue et un focus diffèrent, pas toujours mentionné
* prêt-à-penser
    * dans quels contextes-projets travaillent les différentes personnes qui ont proposé ces pyramides ? et en quelle année ?
    * ne suffit pas pour appréhender le test
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
* QA vs QE vs testeur vs "dev" vs IVVQ vs ...
* Test error vs test failure : le test n'a pas abouti pour une raison technique (problème de test), le test a abouti mais n'a pas produit le résultat attendu (problème fonctionnel on espère !)

-v-

## Trop de tests

Notes:
* explosion combinatoire
* cible mouvante et floue

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
* comme beaucoup de sujets, c'est pas un casse-pied de service qu'il faut, mais un changement de culture (beaucoup plus compliqué, cf Agile bullshit)

-v-

## Inutile

Notes:
* convaincre (le management et/ou les devs) que c'est utile, avant de se manger une mise-en-prod foirée
* dépense versus économie

-v-

## Test impossible

Notes:
* imitations techniques, matérielles, de coût, ... variabilité selon les environnements
* exemple board farm Schneider
* exemple Windows 10 LTSC 2019 à Thales

-v-

## Code intestable

Notes:
* Ennemis : side-effects ("spooky action at a distance", "que fait cette méthode ?"), (global/static) state, IO, singletons, time, locale, network, files, env, GPU, unclear pre/post-conditions, non-determinism, (G)UI vs API, concurrency et threading, random (non-deterministic), complex outputs and high dimensionality
* différence entre "c'est compliqué de réaliser le test" (limitations tech) versus "c'est compliqué d'écrire le test" (iceberg, gorille)
* exemple : code des bornes qui échoue le 29 Février
* exemple : code du Edge qui est correct sur la timezone 6 mois par an

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
* exemple de Xavier Nopre (cf post LinkedIn), je lui ai dit qu'il y avait un problème, c'est pas censé être aussi lent
* exemple de Schneider : board farms
* exemple de Schneider : code dont le run dure des centaines jours !! (à travers les timezones :p)

-v-

## Bug ou feature ou code mort ?

Notes:
* descriptivism vs prescriptivism (cf Romeu)
* test de caractérisation OK, mais est-ce que c'est ce que ça devrait vraiment faire ? 🤷
  * bug ou feature ?
* source de vérité = code ou spec Word ?

-v-

## En Bref

Notes:
* difficile de savoir quoi faire, Todo : retrouver comment faire, de le faire, à exécuter, à analyser, à maintenir, à faire confiance, pas assez, pas assez bien, pas assez rapide, ...
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

-v-

## Stratégie de test

Notes:
* quoi pourquoi pour quoi comment qui quand ...
* spécifications, Exigences et Requirements, business (value stream) et risques business, quadrants, matrice confiance versus risque, moyens (et toute la suite)
* construisez votre "pyramide" (demander à une IA diK6 typologie : breakpoint, soak, stress, load, ...fférente pyramides, de plein de formes différentes à la Dali), en se basant sur les moyens de test
* à adapter/repenser régulièrement, comme tout le reste
* pourquoi, pour quoi, quoi, où, qui, quand et comment, ...
* trust boundaries (dépendences externes, parties peu fiables, risque métier, responsabilité, vitesse d'évolution, ...)
* Repenser la strat fréquemment, tout comme on le fait pour l'architecture de la solution
* considérer les niveaux de test : Fonctionnalités techniques (endpoint) versus user
* Quadrant des tests !! Axes : business vs tech, pour le produit vs èquipe

-v-

## Moyens de test

Notes:
* humains, techniques, teTodo : retrouver mporels, ...
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

-v-

## Processus

Notes:
* (reprendre des tamis) : tres amigos, example mapping, BDD, prise en compte de la testabilité dès la (pré-)conception, compter le coût du test dans l'estimation de la story, les tests font partie de la dette technique du projet, analyse d'impact lors de nouveaux devs, découpage en équipe Dev versus QA ??
  * identifier les manquements dans son équipe, sur son projet, et trouver comment communiquer dessus avec les autres, avoir des idées à proposer

-v-

## Scénarios

Notes:
* cénarios de test (nominaux, critiques, ...) décidés, "use cases" (orientés "utilisateur" de l'interface)
* TODO retravailler cette section
* typologie de test : "unitaire au niveau technique (méthode/classe)", ou "unitaire d'interface mais profond"
* avoir une spec
  * Exigences et Requirements (cf Schneider, Thales, ...)
* value streams, risques, manque de confiance, ...
* smoke tests (cf origine du mot "smoke test" en logiciel)

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
* pousser les IO à l'extérieur (techniqTodo : retrouver ue du sandwich)
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

-v-

## Feedback

Notes:
* fast feedback + CI/CD + DevOps (monitoring, observability), frequent deployment, Monitoring, debuggability

-v-

## Fluide

Notes:
* ajouter un test doit être simple, s'il y a de la friction alors ça décourage de tester, il faut éliminer la friction
* sentir la douleur : "If it hurts, do it more often" (core XP principle)
* ne pas être capable de réaliser les tests rapidement diminue l'itérativité, la qualité, l'agréabilité, ... la probabilité qu'ils soient écrit tout court
  * comme un évier plein de vaisselle (cercle vicieux)
* Blague du docteur : "j'ai mal quand je suis debout" "alors arrêtez de vous lever"

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

-v-

## Ecriture

Notes:
* méthodologie d'écriture : setup/teardown, Given/When/Then, Assert/Arrange/Act, tester une seule chose plutôt qu'un scénario complet, erreur versus échec
* FIRST : https://stackoverflow.com/questions/18024785/tdd-first-principle Fast Indep Repeat Self-Check Timely (pas écrit dans 1000 ans mais avec le code à tester)
  * double i : isolation ?

-v-

## Techniques

Notes:
* ce qu'on considère le minimum à maîtriser pour tester
* test harness
* TestContainers
* framework
* mocking et fakes versus simulateurs/émulateurs, oracles
  * qu'est-ce je gagne et je perds si je mocke ? gain = vitesse d'exec + facile à mettre en oeuvre (autospec), perte = maintenabilité et réalisme
  * TODO: ne pas mentionner les 2 écoles, mettre en aller en + loin
* DB in-memory

-v-

## techniques avancées

Notes:
* outils et techniques <<avancés>>, pour aller + loin (et qui mérite chacun son 45 minutes ou +) pour développer culture et savoir-faire
* TODO trier/ordonner ces techniques
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
* snapshot/golden-master/approval
  * normatif versus descriptif
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
* full simulation ("Matrix") : cHumilité de devoir testerf conf Devoxx (simulation-driven development)
  * replay du talk CleverCloud au Devoxx sur la simulation du testbench
  * Conf Devoxx 2025 sur le déterminisme CleverCloud
* contract testing
  * Test d'interface d'une third-party (rupture d'API, ...)
* recording/replaying (VCR)
* monkey testing (Doublures de test : des inputs au hasard, le test n'est pas structuré)
* profile your tests ! (éviter les "slips/sleeps sales") cf snakeviz marche aussi pour les tests (cf article de Xavier et son setup de DB), tests en parallèle (cf article du blog de PyPi), être réactif plutôt que passif (cf MQTT tester de Schneider)
* property-based testing + fuzzing
* trunk-based development + feature flags
* monitoring en prod
* Snapshot-testing (approval, golden master)
* Technique de refactoring du sandwich (snowcamp) : push IO to the edge (functional core, imperative shell)
* Mockist vs Behaviorist (detroit vs london)
* Test d'èchafaudage (scaffolding)
* (London versus Chicago, Classicist versus Mockist)
* tests d'architecture (Java = ArchUnit, Python = PyTestArch)
* Security testing : automated tools
* Black box / white /glass
* Baseline perf comparison testing
* time : freezegun en Python, libfaketime avec LD_PRELOAD sinon
  * exemple : tester du code qui doit s'exécuter pendant des mois (harness de test d'endurance)
* rôle de l'IA dans les tests ? (cf Tao blue/red team)
*  property(/fuzzing) (cf article sur la différence)
* advanced features of pytest (or your framework), know your tools
* sans_io
* systrace/ptrace
* HTTPS Man-in-the-Middle (MITM proxy par exemple)
* trucage DNS via `/etc/hosts` ou `/etc/resolv.conf`
* `ssl_verify=False`
* test des logs/metrics (cf mon post LinkedIn)
* test hybride : test auto avec vérif humDéfinition de test unitaire contre-intuitive : ne pas penser microscopique/indivisible, mais cohérence/séparation-frontièreaine, ou test manuel avec assistance autom
* anonymiser des données (de prod)
* générer des donnéesmartin fowler

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
* TODO
* replay vidéo (Youtube) de LyonCraft 2025 : [Jeremy Sorent "j'écris de tests sans pleurer maintenant"](https://www.youtube.com/watch?v=2S9TxoTE8BA)
    * @Julien TODO: revoir
* working effectively with legacy code
* software craft, dunod
* taverne
* https://www.joelonsoftware.com/2001/07/31/hard-assed-bug-fixin/ : est-ce que tous les bugs devraient être corrigés ? ça dépend.
* https://www.mathieueveillard.com/blog/50-shades-of-tests : des définitions plutôt claires pour différents types de test, leur positionnement sur 3 dimensions, au-delà de la pyramide de tests
* https://martinfowler.com/bliki/TestDouble.html : définitions claires de tous les "*test doubles*" (dummy, stub, fake, spy, mock)
* https://latavernedutesteur.fr/2025/09/15/que-doit-on-attendre-dun-testeur/ : les diffèrentes dimensions du métier de testeur
* le DevOps (TODO trouver une bonne référence ? conf Full Cycle d'Alpes Craft)
* [la strat de test de Colin Damon](https://www.linkedin.com/posts/colin-damon_mettre-en-place-une-strat%C3%A9gie-de-tests-qui-activity-7343525861444247552-6BJY)
* [How SQLite Is Tested](https://www.sqlite.org/testing.html)
* http://rednafi.com/go/test-state-not-interactions/
* https://blog.codinghorror.com/falling-into-the-pit-of-success/
* [Tests pragmatiques : comment presque arrêter les tests automatisés ? - La Duck Conf 2025](https://m.youtube.com/watch?v=ohV6GvCIeLY)
* Conf snowcamp 2025, "tester c'est tricher" de JAutomatisé-automatisable-manuelules Poissonnet et Antoine Caron
* [Comment une architecture influence votre stratégie de test ? Par Christophe Bréheret-Girardin - La Duck Conf 2024](https://m.youtube.com/watch?v=IeOa6XWxkxg)

---

# Crédits photos

Notes:
* TODOD

---

# Remerciements

Notes:
* Damien Roulier, Eric Papazian, Mathieu Mattringe, Rachel Da Silva

---

# Questions

Notes:
* TODO image
