FROM abiosoft/caddy:0.11.0

COPY ./compose/production/caddy/Caddyfile /etc/Caddyfile
RUN mkdir /etc/ssl/caddy
RUN chown -R ubuntu:root /etc/ssl/caddy
RUN chmod 770 /etc/ssl/caddy
COPY /home/ubuntu/certificados_ssl/linuxito.crt /etc/ssl/caddy
COPY /home/ubuntu/certificados_ssl/linuxito.key /etc/ssl/caddy
