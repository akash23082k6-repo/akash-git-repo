# Base image
FROM python:3

# Install AWS CLI
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        groff \
        less \
        curl && \
    rm -rf /var/lib/apt/lists/*

RUN curl "https://d1vvhvl2y92vvt.cloudfront.net/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
     ./aws/install && \
    rm -rf awscliv2.zip ./aws

# Install Boto3
RUN pip install boto3

# Set the working directory
WORKDIR /tmp

# Copy your application files
COPY daily_cost.py .
COPY weekly_cost.py .

# Run your application
CMD [ "/bin/bash"]
 