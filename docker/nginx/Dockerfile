FROM nginx

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx

COPY nginx_config /etc/nginx/sites-enabled/