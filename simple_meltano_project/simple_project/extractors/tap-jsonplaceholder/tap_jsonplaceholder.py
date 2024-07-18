import json
import sys
import requests
import singer

def main():
    args = sys.argv[1:]

    if "--config" in args:
        config_path = args[args.index("--config") + 1]
        with open(config_path) as config_file:
            config = json.load(config_file)
    else:
        config = {
            "api_url": "https://jsonplaceholder.typicode.com/posts"
        }

    schema = {
        "type": "object",
        "properties": {
            "userId": {"type": "integer"},
            "id": {"type": "integer"},
            "title": {"type": "string"},
            "body": {"type": "string"}
        }
    }

    if "--discover" in args:
        catalog = {
            "streams": [
                {
                    "stream": "posts",
                    "tap_stream_id": "posts",
                    "schema": schema,
                    "key_properties": ["id"]
                }
            ]
        }
        print(json.dumps(catalog))
    else:
        api_url = config.get("api_url")
        response = requests.get(api_url)
        response.raise_for_status()
        posts = response.json()

        singer.write_schema("posts", schema, "id")
        singer.write_records("posts", posts)

if __name__ == "__main__":
    main()
