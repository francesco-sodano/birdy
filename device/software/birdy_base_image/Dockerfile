FROM raspbian/stretch:latest AS raspbian-stretch-upgrade

ENV DEBIAN_FRONTEND noninteractive

RUN true \
	# Do not start daemons after installation.
	&& echo -e '#!/bin/sh\nexit 101' > /usr/sbin/policy-rc.d \
	&& chmod +x /usr/sbin/policy-rc.d \
	# Update all packages.
	&& apt-get update \
	&& apt-get upgrade -y \
	&& apt-get full-upgrade -y \
	&& apt-get autoremove --purge -y \
	&& apt-get clean -y \
	# Switch to Bullseye repository.
	&& sed -i 's/stretch/bullseye/g' /etc/apt/sources.list \
	# Update all packages.
	&& apt-get update \
	&& apt-get upgrade -y \
	&& apt-get full-upgrade -y \
	&& apt-get autoremove --purge -y \
	&& apt-get clean -y \
	# Remove files outside base image.
	&& rm -rf /var/lib/apt/lists/* \
	&& rm -f /usr/sbin/policy-rc.d

# Collapse image to single layer.
FROM scratch

LABEL maintainer="Francesco Ares Sodano <frsodano@github.com>"

COPY --from=raspbian-stretch-upgrade / /