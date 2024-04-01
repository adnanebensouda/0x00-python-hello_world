#!/bin/bash
# Display all HTTP methods the server given URL will accept.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
