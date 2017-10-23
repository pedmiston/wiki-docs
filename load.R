stats <- jsonlite::fromJSON(system("python article_stats.py 'Persoonia terminalis'", intern = TRUE))
crotchet::read_graphviz_chunk("totems", "diachronic-collaboration")