from scrapegraphai.graphs import SmartScraperGraph


graph_config = {
# "llm": {
#     "model": "ollama/gemma2:2b",
#     "temperature": 1,
#     "format": "json",  # Ollama needs the format to be specified explicitly
#     "model_tokens": 2000, #  depending on the model set context length
#     "base_url": "http://localhost:11434",  # set ollama URL of the local host (YOU CAN CHANGE IT, if you have a different endpoint
# }
"llm": {
        "model": "ollama/gemma2",
        "model_tokens": 8192,
        "base_url": "http://localhost:11434"
    },
    "verbose": True,
    "headless": False,

}

# ************************************************
# Create the SmartScraperGraph instance and run it
# ************************************************

smart_scraper_graph = SmartScraperGraph(
prompt="Give me the product price.",
# also accepts a string with the already downloaded HTML code
source="https://www.jimms.fi/fi/Product/Show/187900/fd-c-nor1c-02/fractal-design-north-charcoal-black-tg-dark-ikkunallinen-miditornikotelo-musta",
config=graph_config
)

result = smart_scraper_graph.run()
print(result)