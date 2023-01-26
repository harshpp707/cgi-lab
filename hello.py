
#!/usr/bin/env python3

import os
import json

# print("Content-Type: text/plain")
# print()
# print(os.environ)

# print("Content-Type: application/json")
# print()
# print(json.dumps(dict(os.environ), indent=2))

print("Content-Type: text/html")
print()
print(f'<p>QUERY_STRING={os.environ.get("QUERY_STRING")}</p>')
print(f'<p>HTTP_USER_AGENT={os.environ.get("HTTP_USER_AGENT")}</p>')
