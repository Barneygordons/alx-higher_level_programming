#!/bin/bash
# takes a uRL, method POST
curl -sL -X PUT -d "user_id=98" -H "You got me!" 0.0.0.0:5000/catch_me
