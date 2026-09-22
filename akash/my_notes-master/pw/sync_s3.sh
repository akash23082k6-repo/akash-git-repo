#!/bin/bash

LOG_DIR="/var/log/bastion/"
DATE_FORMAT=$(date +"%Y/%m/%d")
TARGET_S3_DIR="s3://pw-bastion-audit-logs/logs/dev/$DATE_FORMAT"
REGION="ap-south-1"

# Create a directory with the current date
CURRENT_DATE_DIR="/var/log/push_logs"
mkdir -p "$CURRENT_DATE_DIR"

# Move log files to the current date directory
cp "/var/log/bastion/"* "$CURRENT_DATE_DIR"

# Copy log files to S3 with server-side encryption enabled.
/usr/local/bin/aws s3 cp "$CURRENT_DATE_DIR" "$TARGET_S3_DIR" --sse --region "$REGION" --recursive && find /var/log/bastion/ -name '*.*' -mtime +0 -delete > /dev/null

# Delete Current DATE DIR 

rm -rf "$CURRENT_DATE_DIR"