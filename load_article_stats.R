# Run the python script with article name as the argument and capture the output.
stdout <- system("python load_article_stats.py 'Persoonia terminalis'", intern = TRUE)
# Convert the output expected in json format to an R list.
stats <- jsonlite::fromJSON(stdout)
