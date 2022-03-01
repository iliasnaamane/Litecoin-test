# Litecoin-test

## Question 1

Basic Dockerfile has been taken from this repository:  https://github.com/uphold/docker-litecoin-core/tree/master/0.18

### Checksum verification

Checksum verification has been already setup. Comment has been added for the checksum verification.

### Security Scan ( Reference: https://anchore.com/blog/inline-scanning-with-anchore-engine/ )

As a tool, Anchore has been used for docker image scanning. An inline scanning with anchore has been performed.

After building the Dockerfile using:
```
docker build -t litecoin:0.18.1 .
```

Time for scanning:

curl -s https://ci-tools.anchore.io/inline_scan-v0.6.0 | bash -s -- -f -d Dockerfile -b .anchore-policy.json litecoin:0.18.1


## Question 2

