---
title: Infos zur Nutzung von Markdown
date: 12.02.2023
author: Dr. Bastian Ebeling
---

## Basis

## Editoren und Tipps

## eingebaute Grafiken

Gemäß dem [Link](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams) können in GitHub einige Grafiken inline codiert und in der Anzeige gleich dargestellt werden.

### PlantUML

Viele grafische Darstellung können mit Hilfe von [PlantUML](https://plantuml.com/) erzeugt werden.
Falls es hier klappt, folgen ein paar Tests:

#### Version

```plantuml
@startuml
version
@enduml
```

#### Farben

Mehr Informationen über die Verwendung von Farben ist [hier](https://plantuml.com/de/color) hinterlegt.

##### Palette

Die benannten Palette der Farben kann mit dem Befehl `colors` angezeigt werden.

```plantuml
@startuml
colors
@enduml
```

##### Nachbarfarben

Verträgliche Nachbarfarben können mit dem Befehl `colors #FARBNAME#` angezeigt werden.

```plantuml
@startuml
colors Gainsboro
@enduml
```

### Mermaid

Eine andere Syntax bietet [Mermaid](https://mermaid-js.github.io/mermaid).

```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```

### kroki

### GeoJSON and TopoJSON

[GeoTopo]: https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams#creating-geojson-and-topojson-maps

Folgend der Beschreibung unter dem [Link][GeoTopo] können auch direkt Karten eingebettet werden.
