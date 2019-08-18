FROM openfaas/classic-watchdog:0.15.4 as watchdog

FROM xe1gyq/opencv
USER root

COPY --from=watchdog /fwatchdog /usr/bin/fwatchdog
RUN chmod +x /usr/bin/fwatchdog

# Add non root user
RUN groupadd app && \
    useradd -g app -d /home/app -m app && \
    echo "app ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

WORKDIR /home/app

USER app

# Populate example here - i.e. "cat", "sha512sum" or "node index.js"
ENV fprocess="cat"
# Set to true to see request in function logs
ENV write_debug="false"

EXPOSE 8080

HEALTHCHECK --interval=3s CMD [ -e /tmp/.lock ] || exit 1

CMD ["fwatchdog"]
