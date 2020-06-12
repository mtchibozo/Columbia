# Publishing Resources {#publish}

![](images/banners/banner_publish.png)

## Vue d'ensemble

Cette section explique comment nous avons construit *edav.info/* et mentionnent des références pour construire vos propres sites et livres en utilisant R. 


## tl;dr

Tu veux commencer à construire un site entier avec Travis CI comme celui-ci? Zach Bogard a créé [un bookdown-template] (https://github.com/zachbogart/bookdown-template){target="_blank"} que tu peux cloner et travailler pour créer ton propre site. Pour plus d'information, lis le README file. 

## Bookdown

*edav.info/* a été construit à l'aide de [Bookdown](https://bookdown.org/){target="_blank"}, un package open-source construit à partir de [R Markdown](https://rmarkdown.rstudio.com/){target="_blank"} afin d'écrire facilement des livres et autres longs articles.

Le plus gros avantage de `bookdown` est qu'il nous premet de créer du contenu à la fois professionel et adaptable. Si on veut éditer un vrai livre, il faut publier une autre édition et c'est la croix et la bannière. With `bookdown`, on peut publier notre travail dans des formats différents (format papier inclus) et faire des moficiations facilement lorsque c'est nécessaire. 

Nous avons choisi `bookdown` pour *edav.info/* parce que cela nous permet de présenter énormément de contenu d'une façon qui facilite la recherche, est compacte et permet aux étudiants de modifier ou ajouter du contenu. A nouveau, `bookdown` est professionel *et* adaptable (la version par défaut est juste un livre en ligne mais nous avons essayé de lui donner plus de vie en ajoutant beaucoup d'icônes, des logos et des bannières pour en améliorer la navigation). 

Ci-dessous sont mentionnées des références utiles qui ont été utilisées lors de la création d' *edav.info/*. Elles peuvent être utiles pour quelqu'un qui souhaite créer son propre site internet ou une ressource en ligne pour R. 


## Les essentiels

- [How to Start a Bookdown Book](http://seankross.com/2016/11/17/How-to-Start-a-Bookdown-Book.html){target="_blank"}: Le plus dur avec `bookdown` est de le mettre en marche. [Sean Kross](http://seankross.com/about/){target="_blank"} propose le meilleur tutoriel que nous avons trouvés jusqu'à présent. Nous avons commencé ce projet en clonant son template repo et en le modifiant. Les descriptions sont excellentes, expliquent le rôle que joue chaque dossier et insistent sur ce qui est essentiel pour commencer un projet. 

- [bookdown: Authoring Books and Technical Documents with R Markdown](https://bookdown.org/yihui/bookdown/){target="_blank"}: Ce livre de [Yihui Xie](https://yihui.name/en/){target="_blank"}, auteur du package `bookdown`, explique tout ce que `bookdown` est capable de faire. Une mine d'informations que nous gardons toujours à portée de main. Ce que l'auteur en dit:

> Un guide pour écrire des livres avec R Markdown qui inclut comment générer des graphiques et tableaux, insérer des citations, HTML widgets et applications Shiny dans R Markdown.
>

- [RStudio Bookdown Talk](https://www.rstudio.com/resources/webinars/introducing-bookdown/){target="_blank"}: Yihui Xie (auteur du package `bookdown`) parle de son package et ce qu'il peut faire en une heure de discussion. Cette ressource est plutôt intéressante pour avoir une idée d'exemples terminées.

- [bookdown.org](https://bookdown.org/home/about.html){target="_blank"}: Site pour le package `bookdown`. Le site présente plusieurs livres populaires qui utilisent `bookdown` et des informations sur comment et par où commencer. 

- [Creating Websites in R](http://www.emilyzabor.com/tutorials/rmarkdown_websites_tutorial.html){target="_blank"}: Ce tutoriel, écrit par [Emily Zabor](http://www.emilyzabor.com/){target="_blank"} (une alumni de Columbia), explique pas-à-pas comment créer un site internet en utilisant différents outils R. L'auteur explique comment construire différents types de sites (personel, package, projet, blog) ainsi que l'intégration GitHub et comment préparer les templates et leur hosting. Cette ressource est très détaillée est vaut la peine d'être parcourue si l'on souhaite créer son propre site.
    
## Ajouter un nom de domaine personnalisé

Ajouter un nom de domaine personnalisé se fait en plusieurs parties:

1. Acheter un nom de domaine et éditer les paramètres DNS

Nous avons utilisés les [domaines Google](https://domains.google.com/){target="_blank"}. Sur la [page du registrar](https://domains.google.com/registrar){target="_blank"}, cliquez sur l'icône DNS et ajoutez ceci aux Custom resource records:

|NAME|TYPE|TTL|DATA|
|----|----|---|----|
|@|A|1h|185.199.108.153|
|www|CNAME|1h|@|

Remarquez que plusieurs tutoriels présentent des adresses IP plus vieilles. Cliquez [ici](https://help.github.com/articles/troubleshooting-custom-domains/#dns-configuration-errors){target="_blank"} pour celles qui sont le plus recommendées.

2. Changer les paramètres de son repo

Dans Settings, ajoutez votre nom de domaine personnalisée dans la section GitHub Pages.

3. Ajoutez un CNAME file à la branche `gh-pages`.

Il s'agit d'un file texte très simple nommé CNAME. Le content doit être une ligne avec le nom du domaine personnalisé.  

Pour plus de détails sur les étapes 2 et 3, voir: [Emily Zabor's Tutorial on Custom Domains](http://www.emilyzabor.com/tutorials/rmarkdown_websites_tutorial.html#custom_domains){target="_blank"}

## Faire une page 404 personnalisée

Votre site peut être très joli mais la page 404 par défaut est toujours une déception. Lorsque quelqu'un écrit une partie de notre url de façon incorrecte ou que le lien casse, on doit s'assurer qu'il y ait quelque chose d'autres qu'une page ennuyeuse qu'on n'a pas su designer. [Cet article](https://mycyberuniverse.com/developing/custom-404-page-for-website-hosted-on-github.html){target="_blank"} explique le procédé en détails mais en réalité, il suffit de créer un fichier intitulé `404.html` dans notre root directory et GitHub l'utilisera plutôt que la version par défaut. Pour cette raison, il n'y a vraiment aucune excuse pour ne pas en avoir un. Jetez un oeil à [notre 404 page](404.html). On espère que vous ne la voyez pas trop souvent. <i class="far fa-smile"></i>

Quelques considérations:

- **Incluez toujours un lien vers votre site**: Aide toujours le user.
- **Expliquez clairement que quelque chose n'a pas bien fonctionné**: Ne cachez pas que le fait de tomber sur cette page est une erreur.
- **Utilisez des absolute paths**: L'URL qui lance l'erreur 404 est peut-être cachée dans des dossiers inattendus. Vérifiez que si vous avez des images ou des liens, ceux-ci fonctionnent indépendemment du file path (utilisez "/images/..." rather than "images/...", liez directement au css/page d'accueil, etc.)
- **Et sinon, amusez-vous!**: Il y a [plein d'exemples](https://www.canva.com/learn/404-page-design/){target="_blank"} de personnes qui réalisent d'[excellentes pages 404](https://www.pagecloud.com/blog/best-404-pages){target="_blank"}. Cela devrait aider à traverser l'expérience frustrante de tomber sur une de ces pages 404.
    
## Choper Travis

Ce tutoriel est désigné pour vous aider à ajouter Travis à votre GitHub Pages créé à l'aide de bookdown. Il suppose que vous avez déjà un site internet qui fonctionne avec des pages stockées dans une branche `gh-pages`.

Nous ne recommendons pas nécessairement la route `gh-pages`; Nous l'avons choisie parce que nous avons trouvé des exemples simples qui fonctionnent avec cette méthode. Comme les dossiers `/docs` sont une nouvelle approche 'plus propre', il existe très certainement une meilleure manière d'organiser le repo.

Ceci dit, il y a beaucoup de tutoriels qui expliquent comment utiliser la branche `gh-pages`; Il s'avère que la meilleure façon de procéder est de créer une branche orpheline, comme expliqué [ici](https://www.bruttin.com/2017/12/22/github-ghpages-worktree.html){target="_blank}.

Notez également que ceci donne l'impression qu'ajouter Travis est très facile, ce qui n'est en réalité pas du tout le cas. Tout a toujours l'air facile avec du recul. Si vous avez du mal, faites-le nous savoir en [loggant un problème](https://github.com/jtr13/edav/issues){target="_blank"} ou en [envoyant une pull request](https://github.com/jtr13/edav/pulls){target="_blank}. PLus d'information sur toutes les contributions communautaires peuvent être trouvées sur notre [page de contribution](contribute.html)

### Ajouter les fichiers de Travis au repo GitHub

**Ajoutez ces fichiers** à votre rep:

1. [https://github.com/rstudio/bookdown-demo/blob/master/.travis.yml](https://github.com/rstudio/bookdown-demo/blob/master/.travis.yml){target="_blank}
    - Pas de changements

2. [https://github.com/rstudio/bookdown-demo/blob/master/_build.sh](https://github.com/rstudio/bookdown-demo/blob/master/_build.sh){target="_blank}
    - Retire les deux dernières lignes si vous n'êtes intéressés par un livre GitHub Pages.

3. [https://github.com/rstudio/bookdown-demo/blob/master/_deploy.sh](https://github.com/rstudio/bookdown-demo/blob/master/_deploy.sh){target="_blank}
    - Les seuls changements que vous devez faire sont les lignes de `git config`. Vous devez utilisé votre adresse mail GitHub, mais le pseudonyme peut être n'importe quoi.

### Ajouter le service de Travis

1. **Créer un compte Travis** sur www.travis-ci.org en cliquant sur "Sign in with GitHub" en haut à droite. Cliquez sur *Authorize* pour permettre à Travis d'avoir son propre accès à GitHub.

2. Retournez sur GitHub et **créez un *personal access token (PAT)*** si vous n'en avez pas encore un. Vous pouvez le faire [ici](https://github.com/settings/tokens){target="_blank"}. Notez que vous devez sauvegarder votre PAT quelque part car vous ne pourrez plus y accéder une fois qu'il est créé. Notez également que le PAT donne un moyen d'accéder votre repo GitHub via une API, ce qui est une autre façon de se connecter que via un pseudonyme/mot de passe. 

3. **Retournez sur votre profil Travis** (travis-ci.org/profile/[GITHUB username]) et cliquez sur le bouton à côté du repo approprié afin de le ***toggle***. Cliquez sur Paramètres à côté du bouton et **ajoutez-le à votre GITHUB_PAT sauvegardé** sous les variables environementale: choisissez un "Nom" pour le "GITHUB_PAT" et une "Valeur" pour la valeur du token.

Si tout s'est bien passé, vous pouvez vous relaxer et regarder Travis faire le travail à votre place.

<center>
<iframe src="https://giphy.com/embed/uLP5x8WzYVzP2" width="480" height="258" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/funny-the-simpsons-uLP5x8WzYVzP2">via GIPHY</a></p>
</center>

## Notes sur notre workflow

### 

## Autres ressources

- [blogdown: Creating Websites with R Markdown](https://bookdown.org/yihui/blogdown/){target="_blank"}: Textbook on the `blogdown`package, another option for generating websites with R.
- [Getting Started with GitHub Pages](https://guides.github.com/features/pages/){target="_blank"}: Short article from [GitHub Guides](https://guides.github.com/){target="_blank"} on creating/hosting a website using [GitHub Pages](https://pages.github.com/){target="_blank"}.
- [A Beginner's Guide to Travis CI for R](https://juliasilge.com/blog/beginners-guide-to-travis/){target="_blank"}: Fantastic blog post by [Julia Silge](https://juliasilge.com/){target="_blank"}, includes debugging advice that helped us solve a problem involving installing packages with system requirements.

