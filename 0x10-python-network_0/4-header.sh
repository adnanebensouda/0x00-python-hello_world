#!/bin/bash
# Send GET request to given URL with a header variable.
curl -sH "X-HolbertonSchool-User-Id: 98" "${1}"
