#!/usr/bin/env bash

# A script that return a json file containing all currently running containers and their non truncated ids
# Required by the API script

output_file="containers.json"
containers=()

# Currently running containers
while IFS=$'\t' read -r container_id container_name; do
    # JSON object for each container
    container_json="{ \"container_name\": \"$container_name\", \"container_id\": \"$container_id\" }"

    container_objects=$(
        IFS=,
        echo "${containers[*]}"
    )

    # Append to array
    containers+=("$container_json")
done < <(docker ps --format "{{.ID}}\t{{.Names}}" --no-trunc | sort -k2)

output_json="{ \"container_names\": [${container_objects[*]}] }"

# Write the JSON object to the file
echo "$output_json" >"$output_file"

echo "{ \"container_names\": [${container_objects}] }"
