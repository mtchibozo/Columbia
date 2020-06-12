# (PART) Other Topics {-}

# Perception/Couleur {#percept}

![](images/banners/banner_percept.png)

## Vue d'ensemble

Cette section contient des ressources pour en savoir plus sur la perception graphique et sur l’utilisation efficace des couleurs. 

## Perception

Voici quelques liens vers des ouvrages / articles clés sur la perception:

- [Graphical Perception: Theory, Experimentation, and Application to the Development of Graphical Methods](https://www.jstor.org/stable/2288400){target="_blank"}: Article classique de William Cleveland and Robert McGill
- [The Elements of Graphing Data](https://clio.columbia.edu/catalog/SCSB-8519758){target="_blank"}: Textbook by William Cleveland
- [Visualizing Data](https://clio.columbia.edu/catalog/SCSB-1389825){target="_blank"}: Livre écrit par William Cleveland
- [Creating More Effective Graphs](https://clio.columbia.edu/catalog/5291007){target="_blank"}: Livre écrit par by Naomi Robbins

## Couleur

La couleur est très subjective. Il est important de faire les bons choix de couleur pour que votre travail soit facile à comprendre.

- [Color Brewer](http://colorbrewer2.org/){target="_blank"}: Excellente ressource pour obtenir des palettes de couleurs efficaces pour vos différents projets. Son objectif principal est la cartographie, mais il est extrêmement utile pour tout projet impliquant la couleur. Vous pouvez choisir entre différents types de données (sequentielles, divergentes, qualitative). Assurez-vous que la palette choisie est efficace pour les utilisateurs daltoniens (ou bien rendez possible une impression simplifiée ou photocopie adaptée), et exporter facilement la palette de couleurs dans différents formats (Adobe, GIMP / Inkscape, JS, CSS).
- [Color Blindness Simulator](http://colorbrewer2.org/){target="_blank"}: Vous ne savez pas si votre choix de couleur sera adapté pour un utilisateur daltonien ? Cet outil peut aider. Vous pouvez télécharger une image pour voir son apparence avec différents handicaps liés à la vision des couleurs.
- [ColorPick Eyedropper](https://chrome.google.com/webstore/detail/colorpick-eyedropper/ohcpnigalekghcmgcdcenkpelffpdolg?hl=en){target="_blank"}: Cette extension Chrome vous permet de copier les valeurs hexadécimales des couleurs sur une page Web. Simple et intuitif, il sera beaucoup plus facile de créer vous-mêmes vos superbes palettes de couleurs.

## Astuces pour utiliser les couleurs avec `ggplot2`

L'un des problèmes les plus courants est la confusion entre `color` et `fill`. `geom_point()` et `geom_line` utilisent `color`, de nombreux autres geoms utilisent `fill`. Certains utilisent les deux, tels que `geom_tile()`, auquel cas `color` est la couleur de la bordure et `fill` est la couleur de remplissage.

### Données continues

#### ColorBrewer

+ `scale_color_distiller(palette = "PuBu")` or `scale_fill_distiller(palette = "PuBu")`

(What *doesn't* work: `scale_color_brewer(palette = "PuBu")`)

#### Viridis

+ `scale_color_viridis_c()` or `scale_fill...`  (the c stands for continuous)

#### Créer la votre

`+ scale_color_gradient(low = "white", high = "red")` or `+ scale_fill...`

`+ scale_color_gradient2(low = "red", mid = "white", high = "blue", midpoint = 50)` or `+ scale_fill...`

`+ scale_color_gradientn(colours = c("red", "pink", "lightblue", "blue"))` or `scale_fill...`


### Données discrètes

#### ColorBrewer

+ `scale_color_brewer(palette = "PuBu")` or `scale_fill...`

#### Viridis

+ `scale_color_viridis_d()` or `scale_fill...` (the d stands for discrete)

#### Créer la votre

`+ scale_color_manual(values = c("red", "yellow", "blue"))` or `scale_fill...`

`+ scale_fill_manual(values = c("red", "yellow", "blue"))` or `scale_fill...`

