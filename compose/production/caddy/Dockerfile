FROM abiosoft/caddy:0.11.0

RUN mkdir /etc/ssl/caddy
RUN chown -R root:root /etc/ssl/caddy
RUN chmod 770 /etc/ssl/caddy
COPY ./compose/production/caddy/Caddyfile /etc/Caddyfile
