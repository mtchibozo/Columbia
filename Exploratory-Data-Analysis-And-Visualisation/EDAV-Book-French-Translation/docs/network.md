# Interactive Networks {#network}

![](images/banners/banner_network.png)

<!--## ggnetwork (static)-->

## visNetwork (interactive)

`visNetwork` est une puissante implémentation via R de la librairie JavaScript `vis.js`; il utilise `tidyverse`: [Documentation VisNetwork](https://datastorm-open.github.io/visNetwork/){target="_blank"}.

--> Le Vignette a des exemples clairement élaborés disponibles sur : https://cran.r-project.org/web/packages/visNetwork/vignettes/Introduction-to-visNetwork.html


La documentation `visNetwork` ne fournit pas le même niveau d’explication que la documentation original, il est donc intéressant de consulter la documentation de `vis.js` : http://visjs.org/index.html  En particulier, les [exemples interactifs](http://visjs.org/network_examples.html){target="_blank"} sont particulièrement utiles pour essayer différentes options. Par exemple, vous pouvez essayer des options concrètes avec le [network configurator](http://visjs.org/examples/network/physics/physicsConfiguration.html){target="_blank"}. 


### L'exemple service minimum

Créer un [node data frame](https://datastorm-open.github.io/visNetwork/nodes.html){target="_blank"} avec au moins une colonne (appelée `id`) contenant le nom des noeuds :


```r
# nodes
boroughs <- data.frame(id = c("The Bronx", "Manhattan", "Queens", "Brooklyn", "Staten Island"))
```


Créer un autre dataframe contenant les [arêtes](https://datastorm-open.github.io/visNetwork/edges.html){target="_blank"} avec pour colonnes `from` et `to`. 



```r
# edges
connections <- data.frame(from = c("The Bronx", "The Bronx", "Queens", "Queens", "Manhattan", "Brooklyn"), to = c("Manhattan", "Queens", "Brooklyn", "Manhattan", "Brooklyn", "Staten Island"))
```


Dessinons le graphe avec `visNetwork(nodes, edges)`


```r
library(visNetwork)
visNetwork(boroughs, connections)
```

<!--html_preserve--><div id="htmlwidget-2a24b263113f9cdb043f" style="width:672px;height:480px;" class="visNetwork html-widget"></div>
<script type="application/json" data-for="htmlwidget-2a24b263113f9cdb043f">{"x":{"nodes":{"id":["The Bronx","Manhattan","Queens","Brooklyn","Staten Island"]},"edges":{"from":["The Bronx","The Bronx","Queens","Queens","Manhattan","Brooklyn"],"to":["Manhattan","Queens","Brooklyn","Manhattan","Brooklyn","Staten Island"]},"nodesToDataframe":true,"edgesToDataframe":true,"options":{"width":"100%","height":"100%","nodes":{"shape":"dot"},"manipulation":{"enabled":false}},"groups":null,"width":null,"height":null,"idselection":{"enabled":false},"byselection":{"enabled":false},"main":null,"submain":null,"footer":null,"background":"rgba(0, 0, 0, 0)"},"evals":[],"jsHooks":[]}</script><!--/html_preserve-->


Tu peux ajouter des labels en ajoutant l'argument label à la colonne `nodes`:


```r
library(dplyr)
boroughs <- boroughs %>% mutate(label = id)
visNetwork(boroughs, connections)
```

<!--html_preserve--><div id="htmlwidget-70a697dd4b9e55ace25a" style="width:672px;height:480px;" class="visNetwork html-widget"></div>
<script type="application/json" data-for="htmlwidget-70a697dd4b9e55ace25a">{"x":{"nodes":{"id":["The Bronx","Manhattan","Queens","Brooklyn","Staten Island"],"label":["The Bronx","Manhattan","Queens","Brooklyn","Staten Island"]},"edges":{"from":["The Bronx","The Bronx","Queens","Queens","Manhattan","Brooklyn"],"to":["Manhattan","Queens","Brooklyn","Manhattan","Brooklyn","Staten Island"]},"nodesToDataframe":true,"edgesToDataframe":true,"options":{"width":"100%","height":"100%","nodes":{"shape":"dot"},"manipulation":{"enabled":false}},"groups":null,"width":null,"height":null,"idselection":{"enabled":false},"byselection":{"enabled":false},"main":null,"submain":null,"footer":null,"background":"rgba(0, 0, 0, 0)"},"evals":[],"jsHooks":[]}</script><!--/html_preserve-->



### Performance

`visNetwork` peut être très lent. 

`%>% visPhysics(stabilization = FALSE)` commence l'affichage avant que la stabilisation soit complète, ce qui accélère réellement les choses mais vous permet de voir ce qui se passe en temps réel. Cela fait une grande différence dans l'expérience utilisateur. (C’est aussi amusant de regarder la stabilisation du graphe). D'autres astuces de performance sont décrites [ici](https://datastorm-open.github.io/visNetwork/performance.html){target="_blank"}.
  
### Des outils de configuration utiles  
  
`%>% visConfigure(enabled = TRUE)` est un outil utile pour configurer les options de manière interactive. Une fois terminé, cliquez sur "generate options" pour que le code reproduise les paramètres. Plus d'info [ici](https://datastorm-open.github.io/visNetwork/configure.html){target="_blank"} (Notez que changer les options puis les visualiser nécessite beaucoup le défilement vertical dans le navigateur. Je ne suis pas sûr que quelque chose peut être fait à ce sujet. Si vous avez une solution, n'hésitez pas à partager !)
  
### Colorer les noeuds

Ajouter une colonne avec les vrais noms des couleurs dans le dataframe des noeuds :


```r
boroughs <- boroughs %>% mutate(is.island = c(FALSE, TRUE, FALSE, FALSE, TRUE)) %>% mutate(color = ifelse(is.island, "blue", "yellow"))
visNetwork(boroughs, connections)
```

<!--html_preserve--><div id="htmlwidget-abd3abc567fb2e2eec47" style="width:672px;height:480px;" class="visNetwork html-widget"></div>
<script type="application/json" data-for="htmlwidget-abd3abc567fb2e2eec47">{"x":{"nodes":{"id":["The Bronx","Manhattan","Queens","Brooklyn","Staten Island"],"label":["The Bronx","Manhattan","Queens","Brooklyn","Staten Island"],"is.island":[false,true,false,false,true],"color":["yellow","blue","yellow","yellow","blue"]},"edges":{"from":["The Bronx","The Bronx","Queens","Queens","Manhattan","Brooklyn"],"to":["Manhattan","Queens","Brooklyn","Manhattan","Brooklyn","Staten Island"]},"nodesToDataframe":true,"edgesToDataframe":true,"options":{"width":"100%","height":"100%","nodes":{"shape":"dot"},"manipulation":{"enabled":false}},"groups":null,"width":null,"height":null,"idselection":{"enabled":false},"byselection":{"enabled":false},"main":null,"submain":null,"footer":null,"background":"rgba(0, 0, 0, 0)"},"evals":[],"jsHooks":[]}</script><!--/html_preserve-->

### Noeuds orientés (flèches)


```r
visNetwork(boroughs, connections) %>% 
  visEdges(arrows = "to;from", color = "green")
```

<!--html_preserve--><div id="htmlwidget-e4b5113fcea310493fd3" style="width:672px;height:480px;" class="visNetwork html-widget"></div>
<script type="application/json" data-for="htmlwidget-e4b5113fcea310493fd3">{"x":{"nodes":{"id":["The Bronx","Manhattan","Queens","Brooklyn","Staten Island"],"label":["The Bronx","Manhattan","Queens","Brooklyn","Staten Island"],"is.island":[false,true,false,false,true],"color":["yellow","blue","yellow","yellow","blue"]},"edges":{"from":["The Bronx","The Bronx","Queens","Queens","Manhattan","Brooklyn"],"to":["Manhattan","Queens","Brooklyn","Manhattan","Brooklyn","Staten Island"]},"nodesToDataframe":true,"edgesToDataframe":true,"options":{"width":"100%","height":"100%","nodes":{"shape":"dot"},"manipulation":{"enabled":false},"edges":{"arrows":"to;from","color":"green"}},"groups":null,"width":null,"height":null,"idselection":{"enabled":false},"byselection":{"enabled":false},"main":null,"submain":null,"footer":null,"background":"rgba(0, 0, 0, 0)"},"evals":[],"jsHooks":[]}</script><!--/html_preserve-->

### Désactiver le mouvement du graphe

C'est beaucoup plus rapide sans la simulation. Le nodes sont placés au hasard et peuvent être déplacés sans affecter le reste du graphe, au moins dans le cas des petits graphes.


```r
visNetwork(boroughs, connections) %>% 
  visEdges(physics = FALSE)
```

<!--html_preserve--><div id="htmlwidget-0e42fd9c978d71b3893c" style="width:672px;height:480px;" class="visNetwork html-widget"></div>
<script type="application/json" data-for="htmlwidget-0e42fd9c978d71b3893c">{"x":{"nodes":{"id":["The Bronx","Manhattan","Queens","Brooklyn","Staten Island"],"label":["The Bronx","Manhattan","Queens","Brooklyn","Staten Island"],"is.island":[false,true,false,false,true],"color":["yellow","blue","yellow","yellow","blue"]},"edges":{"from":["The Bronx","The Bronx","Queens","Queens","Manhattan","Brooklyn"],"to":["Manhattan","Queens","Brooklyn","Manhattan","Brooklyn","Staten Island"]},"nodesToDataframe":true,"edgesToDataframe":true,"options":{"width":"100%","height":"100%","nodes":{"shape":"dot"},"manipulation":{"enabled":false},"edges":{"physics":false}},"groups":null,"width":null,"height":null,"idselection":{"enabled":false},"byselection":{"enabled":false},"main":null,"submain":null,"footer":null,"background":"rgba(0, 0, 0, 0)"},"evals":[],"jsHooks":[]}</script><!--/html_preserve-->

### Griser les noeuds loins de celui selectionné (par définition du degré)

(Cliquez sur un noeud pour voir l'effet)


```r
# defaults to 1 degree
visNetwork(boroughs, connections) %>% 
  visOptions(highlightNearest = TRUE)
```

<!--html_preserve--><div id="htmlwidget-97147c132764ddef01c2" style="width:672px;height:480px;" class="visNetwork html-widget"></div>
<script type="application/json" data-for="htmlwidget-97147c132764ddef01c2">{"x":{"nodes":{"id":["The Bronx","Manhattan","Queens","Brooklyn","Staten Island"],"label":["The Bronx","Manhattan","Queens","Brooklyn","Staten Island"],"is.island":[false,true,false,false,true],"color":["yellow","blue","yellow","yellow","blue"]},"edges":{"from":["The Bronx","The Bronx","Queens","Queens","Manhattan","Brooklyn"],"to":["Manhattan","Queens","Brooklyn","Manhattan","Brooklyn","Staten Island"]},"nodesToDataframe":true,"edgesToDataframe":true,"options":{"width":"100%","height":"100%","nodes":{"shape":"dot"},"manipulation":{"enabled":false}},"groups":null,"width":null,"height":null,"idselection":{"enabled":false,"style":"width: 150px; height: 26px","useLabels":true,"main":"Select by id"},"byselection":{"enabled":false,"style":"width: 150px; height: 26px","multiple":false,"hideColor":"rgba(200,200,200,0.5)"},"main":null,"submain":null,"footer":null,"background":"rgba(0, 0, 0, 0)","highlight":{"enabled":true,"hoverNearest":false,"degree":1,"algorithm":"all","hideColor":"rgba(200,200,200,0.5)","labelOnly":true},"collapse":{"enabled":false,"fit":false,"resetHighlight":true,"clusterOptions":null,"keepCoord":true,"labelSuffix":"(cluster)"}},"evals":[],"jsHooks":[]}</script><!--/html_preserve-->

```r
# set degree to 2
visNetwork(boroughs, connections) %>% 
  visOptions(highlightNearest = list(enabled = TRUE, 
                                     degree = 2))
```

<!--html_preserve--><div id="htmlwidget-fdcb2bf1b5ce1c2603fe" style="width:672px;height:480px;" class="visNetwork html-widget"></div>
<script type="application/json" data-for="htmlwidget-fdcb2bf1b5ce1c2603fe">{"x":{"nodes":{"id":["The Bronx","Manhattan","Queens","Brooklyn","Staten Island"],"label":["The Bronx","Manhattan","Queens","Brooklyn","Staten Island"],"is.island":[false,true,false,false,true],"color":["yellow","blue","yellow","yellow","blue"]},"edges":{"from":["The Bronx","The Bronx","Queens","Queens","Manhattan","Brooklyn"],"to":["Manhattan","Queens","Brooklyn","Manhattan","Brooklyn","Staten Island"]},"nodesToDataframe":true,"edgesToDataframe":true,"options":{"width":"100%","height":"100%","nodes":{"shape":"dot"},"manipulation":{"enabled":false}},"groups":null,"width":null,"height":null,"idselection":{"enabled":false,"style":"width: 150px; height: 26px","useLabels":true,"main":"Select by id"},"byselection":{"enabled":false,"style":"width: 150px; height: 26px","multiple":false,"hideColor":"rgba(200,200,200,0.5)"},"main":null,"submain":null,"footer":null,"background":"rgba(0, 0, 0, 0)","highlight":{"enabled":true,"hoverNearest":false,"degree":2,"algorithm":"all","hideColor":"rgba(200,200,200,0.5)","labelOnly":true},"collapse":{"enabled":false,"fit":false,"resetHighlight":true,"clusterOptions":null,"keepCoord":true,"labelSuffix":"(cluster)"}},"evals":[],"jsHooks":[]}</script><!--/html_preserve-->

