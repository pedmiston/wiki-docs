load_article_stats <- function(name) {
  # Run the python script with article name as the argument
  # and capture the output.
  python <- "~/.venvs/wiki/bin/python"
  stdout <- system(paste(python, "load_article_stats.py", name), intern = TRUE)
  # Convert the output expected in json format to an R list.
  stats <- jsonlite::fromJSON(stdout)
}
