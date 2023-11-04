#!/bin/sh

chmod +x final.sh

# Set the container ID (you should replace 'CONTAINER_ID' with your actual container ID)
CONTAINER_ID="vigilant_johnson"

# Define the directory paths for the files to be copied and the destination on your local machine
CONTAINER_DIR="/home/doc-bd-a1/"
LOCAL_DIR="C:/Users/dodor/Documents/bd-a1/service-result"


# Copy the output files from the container to your local machine
docker cp $CONTAINER_ID:$CONTAINER_DIR/eda-in-1.txt $LOCAL_DIR
docker cp $CONTAINER_ID:$CONTAINER_DIR/eda-in-2.txt $LOCAL_DIR
docker cp $CONTAINER_ID:$CONTAINER_DIR/eda-in-3.txt $LOCAL_DIR
docker cp $CONTAINER_ID:$CONTAINER_DIR/eda-in-4.txt $LOCAL_DIR
docker cp $CONTAINER_ID:$CONTAINER_DIR/k.txt $LOCAL_DIR
docker cp $CONTAINER_ID:$CONTAINER_DIR/res_dpre.csv $LOCAL_DIR
docker cp $CONTAINER_ID:$CONTAINER_DIR/vis.png $LOCAL_DIR

# Close the container
docker stop $CONTAINER_ID

